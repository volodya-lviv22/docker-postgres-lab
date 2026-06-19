# Docker PostgreSQL Lab 🚀

## 📌 Project Overview

This project demonstrates a simple DevOps environment built with Docker Compose.

The application consists of:

- Python Flask web application
- PostgreSQL database
- Docker containers
- Docker network
- Persistent Docker volume

The goal of this project is to understand how multiple services communicate with each other and how data can persist even after containers are recreated.

---

## 🏗️ Architecture

```
              User Browser
                    |
                    |
            localhost:8000
                    |
                    |
              Flask Container
                    |
             Docker Network
                    |
             PostgreSQL Container
                    |
              Docker Volume
                    |
              Persistent Data
```

---

## 📁 Project Structure

```
docker-postgres-lab/
│
├── app/
│   ├── app.py              # Flask application
│   ├── Dockerfile          # Docker image instructions
│   └── requirements.txt    # Python dependencies
│
├── compose.yaml            # Docker Compose configuration
└── README.md               # Project documentation
```

---

## 🛠 Technologies Used

- Python 3.12
- Flask
- Docker
- Docker Compose
- PostgreSQL 15
- Linux Containers

---

## ⚙️ Environment Variables

### Web service

```
DB_HOST=db
DB_USER=admin
DB_PASSWORD=secret
```

### Database service

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
POSTGRES_DB=mydatabase
```

---

## 🚀 Getting Started

### 1. Clone repository

```bash
git clone <repository_url>
cd docker-postgres-lab
```

### 2. Start the project

```bash
docker compose up --build
```

The application will be available at:

```
http://localhost:8000
```

Health check:

```
http://localhost:8000/health
```

---

## 🐳 Useful Docker Commands

### Show running containers

```bash
docker ps
```

### View networks

```bash
docker network ls
```

### View volumes

```bash
docker volume ls
```

### Stop the project

```bash
docker compose down
```

---

## 🗄 PostgreSQL Example

Connect to PostgreSQL container:

```bash
docker exec -it postgres-db sh
```

Open database:

```bash
psql -U admin mydatabase
```

Show tables:

```sql
SELECT * FROM students;
```

Example result:

```
 id | name      | course
----+-----------+--------
 1  | Volodimir | DevOps
 2  | Ivan      | Python
 3  | Anna      | QA
```

---

## 💡 DevOps Concepts Covered

- Containerization with Docker
- Building custom Docker images
- Multi-container applications
- Docker Compose orchestration
- Environment variables
- Docker networking
- Data persistence with Docker Volumes
- Working with PostgreSQL inside containers

---

## 🔮 Future Improvements

- Add Flask connection to PostgreSQL
- Add database migrations
- Create CI/CD pipeline with GitHub Actions
- Push Docker images to Docker Hub
- Deploy application to Kubernetes

---

## 👨‍💻 Author

Created as a DevOps learning project.
