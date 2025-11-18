# Payment Transaction Classification API - Google Cloud Run

Production ML API deployed on Google Cloud Platform for real-time payment transaction categorization.

**Live Demo:** https://payment-api-367759665790.us-central1.run.app

Enterprise-grade Flask API that classifies financial transactions into merchant categories, deployed on Google Cloud Run for scalable, serverless ML inference.

**Key Features:**
- Real-time transaction classification (7 categories)
- Deployed on GCP Cloud Run (serverless, auto-scaling)
- Production-ready with health checks
- Gradient Boosting model (80.75% accuracy)
- Containerized with Docker
- Public API endpoint

**Live API Endpoints**

Base URL: https://payment-api-367759665790.us-central1.run.app

- GET / - API information
- GET /health - Health check
- POST /predict - Classify transaction
- GET /info - Model metrics

**Quick Test**

Health check:
```
curl https://payment-api-367759665790.us-central1.run.app/health
```

Classify a transaction:
```
curl -X POST https://payment-api-367759665790.us-central1.run.app/predict -H "Content-Type: application/json" -d '{"amount": 45.50, "hour": 19, "day_of_week": 5, "is_weekend": 1, "merchant_location": 4, "payment_method": 0, "distance_from_home": 3.5}'
```

Response: `{"category": "Dining", "confidence": 0.85}`

**Transaction Categories**

Groceries • Dining • Transportation • Entertainment • Shopping • Healthcare • Utilities

**Local Development**
```
git clone https://github.com/jashshah127/payment-transaction-gcp.git
cd payment-transaction-gcp
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd src
python train.py
cd ..
python src/app.py
```

**Deploy to GCP**
```
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud auth configure-docker
docker build -t gcr.io/YOUR_PROJECT_ID/payment-api .
docker push gcr.io/YOUR_PROJECT_ID/payment-api
gcloud run deploy payment-api --image gcr.io/YOUR_PROJECT_ID/payment-api --region us-central1 --allow-unauthenticated --port 8080
```

**Technology Stack**

Python 3.9 • Flask • scikit-learn • Docker • Google Cloud Run • Gunicorn

**Model Performance**

Gradient Boosting Classifier with 80.75% accuracy on 7-class transaction classification.

**Architecture**

Serverless deployment on Google Cloud Run with automatic scaling, built-in HTTPS, and pay-per-request pricing. Containerized with Docker for consistent deployment.

**Author**

Jash Shah • MLOps - Northeastern University • 17 November 2025

✅ Cloud deployment 
✅ Production architecture  
✅ Serverless ML serving  
✅ Public internet-accessible API

**Links:** [Live API](https://payment-api-367759665790.us-central1.run.app) • [GitHub](https://github.com/jashshah127/payment-transaction-gcp)
