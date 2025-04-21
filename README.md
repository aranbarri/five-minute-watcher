# 🖥️ 10 Minute Checker

**10 Minute Checker** is a lightweight, self-hosted system monitoring tool built with Python, Flask, WebSockets, and Chart.js.  
It provides real-time system metrics in a clean web dashboard, updating every second and retaining up to the **last 10 minutes** of data.

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
