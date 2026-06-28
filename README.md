# AI Chat Demo

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI-red)
![Pytest](https://img.shields.io/badge/Pytest-Passing-brightgreen)

# AI Chat Demo

A simple AI chat application built with **FastAPI**, **OpenAI API**, **Docker**, and **Jenkins CI**.

---

## Tech Stack

* Python 3.11
* FastAPI
* OpenAI Python SDK
* Pytest
* Docker
* Docker Compose
* Jenkins Pipeline
* Git & GitHub

---

## Project Structure

```text
.
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── tests/
│   └── test_main.py
│
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

---

## Features

* AI Chat API using FastAPI
* Simple HTML/JavaScript frontend
* Dockerized backend
* Docker Compose support
* Automated testing with Pytest
* Jenkins CI pipeline
* GitHub integration

---

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/alirezarashidipp/ai-chat-demo.git
cd ai-chat-demo
```

### 2. Create environment file

Create:

```text
backend/.env
```

Example:

```text
OPENAI_API_KEY=your_api_key_here
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Start FastAPI

```bash
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Run with Docker

Build:

```bash
docker build -t ai-chat-demo .
```

Run:

```bash
docker run --rm -p 8000:8000 --env-file backend/.env ai-chat-demo
```

---

## Run with Docker Compose

```bash
docker compose up --build
```

---

## Run Tests

```bash
pytest tests/
```

---

## Jenkins CI Pipeline

The project includes a Jenkins Pipeline (`Jenkinsfile`) that performs:

1. Checkout source code from GitHub
2. Build the Docker image
3. Run unit tests inside a Docker container
4. Report build status

Pipeline overview:

```text
GitHub
   │
   ▼
Jenkins
   │
Checkout
   │
Docker Build
   │
Run Pytest Inside Docker
   │
Success
```

---

## Future Improvements

* GitHub Webhooks
* Docker Registry
* Multi-stage Docker builds
* Automated deployment
* Kubernetes support
* GitHub Actions pipeline

---

## Author

**Ali Reza Rashidi**
