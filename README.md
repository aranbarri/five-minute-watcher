# 🖥️ 10 Minute Linux Live Checker

**10 Minute Checker** is a lightweight, self-hosted system monitoring tool built with Python, Flask, WebSockets, and Chart.js.  

It provides real-time system metrics in a clean web dashboard, updating every second and retaining up to the **last 10 minutes** of data.

![image](https://github.com/user-attachments/assets/1860ac0f-7c83-497c-8de7-46a8df2e08ea)


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
- 🕒 Retains the **last 10 minutes** of history (600 data points)
- 🖼️ Live values displayed alongside each chart
- 📊 Modern UI with sidebar navigation
- 🐳 Fully containerized with Docker & Docker Compose

---

## 📦 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/your-user/10-minute-checker.git
   cd 10-minute-checker
   ```

2. Start the app:
   ```bash
   docker compose up -d --build
   ```

3. Open your browser at:
   ```
   http://localhost:5000
   ```

---

## 🛠 Requirements

- Docker
- Docker Compose

_No other system configuration is required._

---

## 📁 Project Structure

```
10-minute-checker/
├── app.py                  # Flask + SocketIO backend
├── templates/
│   └── dashboard.html      # Frontend UI (Chart.js)
├── requirements.txt        # Python dependencies
├── Dockerfile              # App image definition
├── docker-compose.yml      # Full stack setup
```

---

## 💡 Customization

- Add or remove metrics in `app.py`
- Modify graph behavior/style in `dashboard.html`
- Adjust retention time by changing the `maxPoints` value

---

## Screenshots

![image](https://github.com/user-attachments/assets/04c0428c-b2b3-42f3-b3ef-b2c62360ce64)

