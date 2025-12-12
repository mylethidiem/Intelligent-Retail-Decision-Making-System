<div align="center">

<img src="https://raw.githubusercontent.com/mylethidiem/Intelligent-Retail-Decision-Making-System/refs/heads/main/static/assets/intelligent_retail.png" alt="Intelligent-Retail-Decision-Making-System Banner" width="100%">

### **Unified Platform for Forecasting • Segmentation • Inventory Optimization**

A modular AI system designed to support **data-driven retail operations** powered by
**Machine Learning • XAI • Multimodal Intelligence**.

</div>

---

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Gradio-FF4B4B?style=for-the-badge&logo=gradio&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white" />
</div>

<div align="center">

[✨ Features](#-features) • [📁 Project Structure](#-project-structure) • [🚀 Quick Start](#-quick-start) • [🔌 API Endpoints](#-api-endpoints) • [🤖 Model](#-model-information) • [🛠️ Troubleshooting](#-troubleshooting) • [🐳 Docker](#-docker-deployment) • [🗺️ Roadmap](#-roadmap)

</div>

---

## 📋 Overview
**Intelligent Retail Decision Making System** is a multi-module AI platform designed to enhance
**retail operations, analytics, and automation**.

This system evolves from foundational modules such as:

- **Inventory Transfer Optimization**
- **Customer Segmentation**
- **Sales Forecasting with Explainable AI (SHAP/XAI)**

The current public release focuses on **Fashion Object Detection** as the first deployed module, serving as the core backbone for multimodal retail intelligence (image → insight).

Future modules (Forecasting, Segmentation, Recommendation, RAG Chatbot, etc.) are planned in the [🗺️ Roadmap](#-roadmap).

### 🎬 Demo
- [You can run the Hugging Face demo here](https://elizabethmyn-intelligent-retail-decision-making-system.hf.space/)

---


## ✨ Features

### 🧠 Core Intelligence
- **Multimodal Object Detection** (images → bounding boxes + labels)
- **Support for future Retail ML models**:
  - Sales Forecasting
  - XAI-enhanced predictions
  - Customer Segmentation
  - Inventory Transfer Optimization

### 🖥️ Frontend (Gradio / Web UI)
- Single & batch image uploads
- Adjustable confidence threshold
- Real-time visualization and inference
- Built-in example images

### ⚙️ Backend (FastAPI)
- High-performance API
- Auto-generated **OpenAPI docs** at `/api/docs`
- Structured logging + configuration through `.env`
- Ready for **Docker deployment**

### 🔐 Operational Features
- Token-based authentication (JWT)
- Environment-based settings
- Modular service & routing design

### ⚙️ Ops
- **.env** driven config (name/port/model/threshold/token…).
- **🐳 Dockerized** build & run.


## 📁 Project Structure

```txt
intelligent-retail-system/
├── app/
│   ├── api/                # FastAPI API endpoints
│   ├── core/               # Config, security, environment settings
│   ├── models/             # Pydantic schemas
│   ├── services/           # Business logic & ML pipelines
│   ├── utils/              # Helper utilities
│   ├── frontend/           # Gradio interface
│   └── main.py             # Entry point for FastAPI
├── requirements.txt
├── Dockerfile
└── README.md
````

## 🔌 API Endpoints

| Method | Path                   | Auth     | Description                     |
| -----: | ---------------------- | -------- | ------------------------------- |
|    GET | `/api/v1/health`       | X-Token  | 🔐 API health status (requires authentication).|
|   POST | `/api/v1/detect/image` | optional | 🖼️ Detect fashion items in 1 image |
|   POST | `/api/v1/detect/batch` | optional | 🖼️ Detect fashion items in batch   |


## 🤖 Model Information

### 📚 Model Details

- **Model**: [`yainage90/fashion-object-detection`](https://huggingface.co/yainage90/fashion-object-detection)
- **Type**: Object Detection

### 👗 Detection Classes

The model identifies a wide range of fashion items, including:

- **👕 Clothing** (e.g., dresses, shirts, pants)
- **👜 Accessories** (e.g., bags, shoes, glasses)
- **👠 Fashion-specific objects**
- **👖 Various apparel categories**

## 🚀 Quick Start

Follow these steps to set up and run the application locally.

### ✨ Check code
For my learning AIO2025: FastAPI
#### Refactor code
- Using `isort`, `black`
```bash
pip install pytest pytest-cov black isort ruff mypy
```

### 1. 📥 Clone the Repository

```bash
git clone <your-repository-url>
cd intelligent-retail-system
```

### 2. 🐍 Create a Virtual Environment

Using Conda:

```bash
# Conda (recommended)
conda create -n retailsys python=3.11 -y
conda activate retailsys

# or venv
python -m venv .venv
# Linux/Mac:
source .venv/bin/activate   # Windows: .\.venv\Scripts\activate

```

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. ⚙️ Configuration

Create a `.env` file in the project root:

```
# .env
APP_NAME=Intelligent Retail Decision Making System
VERSION=1.0.0
DEBUG=False
HOST=0.0.0.0
PORT=5050
API_PREFIX=/api/v1

MODEL_CHECKPOINT=yainage90/fashion-object-detection
DETECTION_THRESHOLD=0.4

# JWT (demo)
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
API_TOKEN=
```

### 5. 🔄 Launch the Backend Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 5050
# Default: http://localhost:5050
# Docs:    http://localhost:5050/api/docs
```

The API is accessible at: 🌐 `http://localhost:5050`

### 6. 🔑 Obtain a JWT Token

Retrieve the test token from the server logs:

```
INFO:app.utils.logger: Generated test token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### 7. ⚙️ Configure the Frontend

Update the `API_TOKEN` in `app/frontend/gradio_ui.py`:

```python
API_TOKEN = "your-actual-jwt-token-here"  # Replace with the token from step 5
```

### 8. 🎨 Launch the Frontend

Set the `PYTHONPATH`:

```bash
# Linux/Mac:
export PYTHONPATH=$PYTHONPATH:$(pwd)
# Windows CMD:
set PYTHONPATH=%PYTHONPATH%;%CD%
# Windows PowerShell:
$env:PYTHONPATH = "$env:PYTHONPATH;$pwd"
```

Run the Gradio frontend:

```bash
python -m app.frontend.gradio_ui
# Gradio: http://localhost:7860
```

Access the Gradio UI at: 🌐 `http://localhost:7860`

### 9. ✅ Verify API Health

```bash
curl -X GET "http://localhost:5050/api/v1/health" -H "X-Token: your-jwt-token"
curl -X GET "http://localhost:5050/api/v1/health" -H "X-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0X3VzZXIiLCJleHAiOjE3NjE1NDI3MjB9.8f4Omm0kBFWDUUd4SBKwYS72mHEOIgWEGRp8zwmywR0"
```

## 🛠️ Troubleshooting

### 🔍 Common Issues

- **ModuleNotFoundError**:
  Ensure the project root is in `PYTHONPATH`:

  ```bash
  # Linux/Mac:
  export PYTHONPATH=$PYTHONPATH:$(pwd)
  # Windows CMD:
  set PYTHONPATH=%PYTHONPATH%;%CD%
  # Windows PowerShell:
  $env:PYTHONPATH = "$env:PYTHONPATH;$pwd"
  ```

- **🖥️ CUDA/MPS Not Available**: The application automatically falls back to CPU if GPU/MPS is unavailable.
- **🌐 Model Download Issues**: Verify internet connectivity and access to Hugging Face.
- **🔐 Authentication Errors 401/403**: Ensure the JWT token is correctly set in the frontend configuration.

## 🐳 Docker Deployment

### 🏗️ Build and Run

```bash
# Build
docker build -t retailsys .

# Run (reads .env; maps the same port)
docker run --env-file .env -p 5050:5050 retailsys
# → API: http://localhost:5050

```

### 🐳 Docker Compose

```bash
docker-compose up -d
```

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgments

- **🤖 Model**: `yainage90/fashion-object-detection`
- **🚀 Framework**: FastAPI
- **🎨 UI**: Gradio
- **🧠 Machine Learning**: Hugging Face Transformers

## 📞 Support

For assistance:

- 🛠️ Review the [Troubleshooting](#troubleshooting) section.
- 📖 Explore the API documentation at `http://localhost:5050/api/docs`.
- 🐛 Submit issues or questions on the project's GitHub repository.

## 🗺️ Roadmap

_(Current features: Fashion object detection from images, videos, simple Web app)_

* [ ] Sales Forecasting with XAI (SHAP)
* [ ] Customer Segmentation Dashboard
* [ ] Inventory Optimization Engine
* [ ] RAG Chatbot for Retail Handbook
* [ ] Product Similarity Search (CLIP)
* [ ] Multimodal Retrieval (image + text)
* [ ] Improve Dockerfile & CI/CD
* [ ] DVC integration

# 📃 **Relate work**
- [My HuggingFace Space for Intelligent Retail Decision Making System](https://huggingface.co/spaces/elizabethmyn/Intelligent-Retail-Decision-Making-System)
- [My Note for this project](https://www.notion.so/Intelligent-Retail-Decision-Making-System-2c30730a967380bd9139fd540ffb50f8)

______________________________________________________________________

## 📬 Contact
**👩‍💻 Author:** [Lê Thị Diễm My](https://github.com/mylethidiem)
📧 **Email:** lethidiemmy961996@gmail.com
🔗 **LinkedIn:** [Thi-Diem-My Le](https://www.linkedin.com/in/mylethidiem/)

______________________________________________________________________

> _"Learning, Building, and Growing in Data & AI."_ 🌍
