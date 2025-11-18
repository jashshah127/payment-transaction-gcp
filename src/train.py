import joblib
import os
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import json
from datetime import datetime
from data import TransactionDataProcessor

class ModelTrainer:
    def __init__(self, model_dir="../model"):
        self.model_dir = model_dir
        os.makedirs(self.model_dir, exist_ok=True)
    
    def train(self):
        print("Training model...")
        processor = TransactionDataProcessor()
        data = processor.prepare_data()
        
        self.model = GradientBoostingClassifier(n_estimators=100, random_state=42)
        self.model.fit(data['X_train'], data['y_train'])
        
        y_pred = self.model.predict(data['X_test'])
        acc = accuracy_score(data['y_test'], y_pred)
        print(f"Accuracy: {acc:.4f}")
        
        joblib.dump(self.model, os.path.join(self.model_dir, "model.pkl"))
        joblib.dump(data['scaler'], os.path.join(self.model_dir, "scaler.pkl"))
        joblib.dump(data['label_encoder'], os.path.join(self.model_dir, "encoder.pkl"))
        
        metrics = {'accuracy': float(acc), 'categories': data['categories'], 'training_date': datetime.now().isoformat()}
        with open(os.path.join(self.model_dir, "metrics.json"), 'w') as f:
            json.dump(metrics, f)
        
        print("Model saved!")

if __name__ == "__main__":
    trainer = ModelTrainer()
    trainer.train()