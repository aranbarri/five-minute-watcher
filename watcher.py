from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import psutil
import eventlet
import os

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("dashboard.html")

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            return float(f.read().strip()) / 1000.0
    except:
        return None

def collect_metrics():
    while True:
        data = {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "swap": psutil.swap_memory().percent,
            "disk": psutil.disk_usage('/').percent,
            "net_sent": psutil.net_io_counters().bytes_sent,
            "net_recv": psutil.net_io_counters().bytes_recv,
            "uptime": int(time.time() - psutil.boot_time()),
            "load1": os.getloadavg()[0],
            "load5": os.getloadavg()[1],
            "load15": os.getloadavg()[2],
            "processes": len(psutil.pids()),
            "cpu_temp": get_cpu_temp() or 0.0
        }
        socketio.emit("metrics", data)
        socketio.sleep(1)

# Lanzamos la tarea en segundo plano desde el arranque del servidor
def start_background():
    socketio.start_background_task(target=collect_metrics)

if __name__ == "__main__":
    start_background()
    socketio.run(app, host="0.0.0.0", port=5000)
