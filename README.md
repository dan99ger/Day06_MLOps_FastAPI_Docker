# 🐳 Day 06: MLOps, Model Serving & Docker Containerization

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688)
![Docker](https://img.shields.io/badge/Docker-Container-2496ed)
![License](https://img.shields.io/badge/License-MIT-green)

A production-oriented MLOps repository demonstrating how to wrap a trained machine learning model into a high-performance RESTful API using FastAPI and package it inside an isolated Docker container.

---

## 🛠️ Key Features

* **FastAPI Endpoint Service:** High-performance prediction endpoints with automated OpenAPI (Swagger UI) documentation.
* **Input Validation:** Strict payload typing and schema verification using **Pydantic** models.
* **Containerized Deployment:** Multi-stage `Dockerfile` ensuring full dependency isolation and platform reproducibility.
* **Health Monitoring:** Dedicated status routes to verify model loading states and API stability.

---

## 📂 Repository Structure

```text
Day06_MLOps_FastAPI_Docker/
├── Dockerfile          # Docker container configuration script
├── main.py              # FastAPI app definition & model endpoints
├── requirements.txt    # Production Python dependencies
├── .gitignore
└── README.md

🚀 How to Run
Option 1: Running Locally
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Access Swagger UI at http://127.0.0.1:8000/docs

Option 2: Running with Docker
Bash
docker build -t ml-service:v1 .
docker run -p 8000:8000 ml-service:v1
Access containerized API at http://localhost:8000/docs

Part of the 7-Day Machine Learning Engineering Challenge.
