\ Payment Transaction API - Google Cloud Run



Flask ML API deployed on Google Cloud Run for payment transaction classification.



\ Local Setup

```

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

cd src

python train.py

cd ..

python src/app.py

```



\ Deploy to GCP

```

gcloud run deploy payment-api --source . --region us-central1 --allow-unauthenticated

```



\ Endpoints



\- GET / - API info

\- GET /health - Health check  

\- POST /predict - Classify transaction

\- GET /info - Model info



\ Author



Jash Shah - MLOps Lab 5 - Northeastern University

