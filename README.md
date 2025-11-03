# FlaskCacheOps 🐳⚙️

A lightweight **Flask + Redis** application demonstrating **containerized caching**, **Docker orchestration**, **logging**, and **health monitoring** for DevOps projects.

---

## 🧠 Project Overview

FlaskCacheOps is a small-scale DevOps project designed to showcase how **caching, logging, and container orchestration** work together in a microservice environment.

It’s perfect for demonstrating your DevOps, Docker, and Cloud skills in interviews or portfolios.

---

## ⚙️ Tech Stack

* **Flask (Python)** – Web framework
* **Redis** – In-memory cache store
* **Docker & Docker Compose** – Container orchestration
* **Nginx (optional)** – Reverse proxy for scalability
* **Logging + Health Checks** – For monitoring and uptime validation

---

## 🏗️ Architecture

```
📦 FlaskCacheOps
├── app/
│   ├── app.py            # Flask application
│   ├── templates/
│   │   └── dashboard.html
│   ├── requirements.txt  # Python dependencies
├── docker-compose.yml     # Multi-container setup
├── Dockerfile             # App image build file
├── .env                   # Environment variables
└── README.md              # Documentation
```

---

## 🚀 Features

✅ Containerized Flask API with Redis caching
✅ Real-time request logging
✅ Docker health checks for uptime monitoring
✅ Persistent visit counter using Redis
✅ Simple `/dashboard` UI to visualize container info and cache status
✅ Ready for deployment or CI/CD pipelines

---

## 🐋 Docker Setup

### 1️⃣ Build and Run

```bash
docker-compose up --build -d
```

### 2️⃣ Verify Containers

```bash
docker ps
```

You should see two containers:

* `flaskcacheops_web`
* `flaskcacheops_redis`

### 3️⃣ Access the App

* **API:** [http://localhost:5000/](http://localhost:5000/)
* **Dashboard:** [http://localhost:5000/dashboard](http://localhost:5000/dashboard)
* **Health Check:** [http://localhost:5000/health](http://localhost:5000/health)

---

## 📊 Health Monitoring

The `/health` endpoint returns a live JSON health status:

```json
{
  "service": "FlaskCacheOps API",
  "status": "healthy ✅",
  "timestamp": "2025-11-03T10:45:00Z"
}
```

---

## 📜 Logs & Observability

Flask automatically logs incoming requests:

```
2025-11-03 08:20:01 [INFO] Request received on / from 172.18.0.1
```

You can check container logs anytime:

```bash
docker logs flaskcacheops_web
```

---

## 🧩 Environment Variables

| Variable     | Description       | Default    |
| ------------ | ----------------- | ---------- |
| `REDIS_HOST` | Redis hostname    | redis      |
| `REDIS_PORT` | Redis port        | 6379       |
| `FLASK_ENV`  | Flask environment | production |

---

## 🧠 Learning Highlights

* Docker Compose multi-container setup
* Redis caching and persistence
* Flask route monitoring and health checks
* Real-time container name + uptime tracking
* Logging and observability integration

---

## 🧰 Future Enhancements

* Add Prometheus + Grafana dashboards 📈
* Include Nginx reverse proxy 🧱
* Deploy on AWS ECS / GCP Cloud Run ☁️
* Integrate GitHub Actions CI/CD 🔄

---

## 👨‍💻 Author

**Gaurav Chile**
DevOps Enthusiast
🚀 *Building projects that bridge Development & Operations.*

---

## 🏁 License

This project is licensed under the MIT License – feel free to modify and build upon it.

