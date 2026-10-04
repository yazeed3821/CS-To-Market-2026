# Week 4: Cloud & DevOps (Containerization)

This project demonstrates the containerization of an AI text classification API(I did in week2) using Docker, preparing it for cloud deployment and CI/CD pipelines.

## Architecture
1. **Application:** FastAPI backend serving a scikit-learn text classification model.
2. **Containerization:** Dockerized the application using a `python:3.12-slim` base image to ensure cross-platform compatibility and environmental consistency.
3. **Port Mapping:** Exposed internal port 8000 to the host environment.

## Commands Used
* `docker build -t text-classifier-api .`
* `docker run -p 8000:8000 text-classifier-api`