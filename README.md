# 🖥️ 5 Minute Linux Live Watcher

**5 Minute Watcher** is a lightweight, self-hosted system monitoring tool built with Python, Flask, WebSockets, and Chart.js.  

It provides real-time system metrics (*CPU, memory, disk, etc.*) in a clean web dashboard, updating every second and retaining up to the **last 5 minutes** of data.

![image](https://github.com/user-attachments/assets/722c6b1f-66d3-42bc-b562-bdd31cd1af07)
*http://localhost:5000* || 
*http://machine-ip:5000*

---

## 🚀 Features

- 🔄 Real-time graphs of:
  - CPU usage & temperature
  - Memory & swap
  - Disk usage
  - Network I/O
  - Uptime
  - System load (1m, 5m, 15m)
  - Total running processes
    
- 🕒 Retains the **last 5 minutes** of history (300 data points)
- 🖼️ Live values displayed alongside each chart
- 📊 Easy to use UI 
- 🐳 Fully containerized 

---

## 📦 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/aranbarri/five-minute-watcher.git
   cd five-minute-watcher
   ```

2. Start the app:
   ```bash
   docker compose up -d 
   ```

3. Open your browser at:
   ```
   http://localhost:5000
   ```
   or
   ```
   http://<machine-ip>:5000
   ```


---

## 🛠 Requirements

- Docker
- Docker Compose

_No other system configuration is required._

---

## 📁 Project Structure

```
five-minute-checker/
├── watcher.py              # Flask + SocketIO backend
├── templates/
│   └── dashboard.html      # Frontend UI (Chart.js)
├── requirements.txt        # Python dependencies
├── Dockerfile              # App image definition
├── docker-compose.yml      # Full stack setup
```

---

## 💡 Customization

- Add or remove metrics in `watcher.py`
- Modify graph behavior/style in `dashboard.html`
- Adjust retention time by changing the `maxPoints` value

---

## Screenshots
![image](https://github.com/user-attachments/assets/940b0212-fe43-43b7-b471-6e5657d16593)

![image](https://github.com/user-attachments/assets/04c0428c-b2b3-42f3-b3ef-b2c62360ce64)

![image](https://github.com/user-attachments/assets/4a0cfdb3-dd7f-4204-89a6-ababe27dfbc5)

