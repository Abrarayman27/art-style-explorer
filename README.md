# Iris Decision Tree Model Deployment

This project trains a scikit-learn decision tree model on the Iris dataset and deploys it as a REST API using Flask, with prediction logging in SQLite, orchestrated by Docker Compose.

## Prerequisites
- Python 3.10
- Docker and Docker Compose

## Setup
1. **Train the Model**:
   - Activate virtual environment: `.\venv\Scripts\activate`
   - Install dependencies: `pip install scikit-learn joblib`
   - Run `python train_model.py` to create `model/iris_decision_tree.joblib`
2. **Build and Run**:
   - Run `docker-compose up --build`
3. **Access the API**:
   - API runs at `http://localhost:5000`
   - Test the `/predict` endpoint:
     ```powershell
     curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
