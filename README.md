# 🚀 Flask CI/CD with Docker, Kubernetes (K3s), and GitHub Actions

This project demonstrates an **end-to-end CI/CD pipeline** for a simple Flask application.  
It uses **Docker** for containerization, **Kubernetes (K3s)** for deployment, and **GitHub Actions** for automation.

---

## 📂 Project Structure
flask-cicd-app/
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image build instructions
├── k8s/
│ ├── deployment.yml # Kubernetes Deployment
│ ├── service.yml # Kubernetes Service
└── .github/
└── workflows/
└── cicd.yml # GitHub Actions pipeline

yaml
Copy code

---

## ⚙️ Tech Stack
- **Flask** – Python web framework  
- **Docker** – Containerization  
- **K3s (Lightweight Kubernetes)** – Orchestration (running on EC2)  
- **GitHub Actions** – CI/CD automation  
- **DockerHub** – Container registry  

---

## 🐳 Docker Setup

### Build the Docker image
```bash
docker build -t flask-cicd .
Run the container locally
bash
Copy code
docker run -p 5000:5000 flask-cicd
Visit: http://localhost:5000

☸️ Kubernetes Setup (K3s on EC2)
Apply Deployment & Service
bash
Copy code
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
Check resources
bash
Copy code
kubectl get pods
kubectl get svc
🔄 CI/CD Pipeline (GitHub Actions)
The pipeline has 3 stages:

Build & Test

Runs on every push to main

Installs dependencies

Runs tests (if any)

Docker Build & Push

Builds the Docker image

Pushes it to DockerHub

Deploy to EC2 (K3s)

SSH into EC2

Applies Kubernetes manifests (deployment.yml, service.yml)

Rolls out the new version

🔑 GitHub Secrets Configuration
Set the following secrets in your repository:

DOCKER_USERNAME → Your DockerHub username

DOCKER_PASSWORD → Your DockerHub password/token

EC2_HOST → Your EC2 public IP

EC2_SSH_KEY → Contents of your .pem private key

✅ Deployment Verification
Get the service details:

bash
Copy code
kubectl get svc flask-service
Example:

pgsql
Copy code
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
flask-service   LoadBalancer   10.43.142.206   3.113.45.89     5000:32020/TCP   10m
Visit in browser:

cpp
Copy code
http://<EC2_PUBLIC_IP>:5000
