from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
import json

app = Flask(__name__)

# Load model
MODEL_DIR = "model"
model = joblib.load(os.path.join(MODEL_DIR, "model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
encoder = joblib.load(os.path.join(MODEL_DIR, "encoder.pkl"))

with open(os.path.join(MODEL_DIR, "metrics.json")) as f:
    metrics = json.load(f)

@app.route('/')
def home():
    return jsonify({
        'message': 'Payment API - GCP Cloud Run',
        'endpoints': ['/health', '/predict', '/info']
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = [
            data['amount'], data['hour'], data['day_of_week'],
            data['is_weekend'], data['merchant_location'],
            data['payment_method'], data['distance_from_home']
        ]
        
        X = np.array([features])
        X_scaled = scaler.transform(X)
        pred = model.predict(X_scaled)[0]
        proba = model.predict_proba(X_scaled)[0]
        category = encoder.inverse_transform([pred])[0]
        
        return jsonify({
            'category': category,
            'confidence': float(max(proba))
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/info')
def info():
    return jsonify(metrics)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)