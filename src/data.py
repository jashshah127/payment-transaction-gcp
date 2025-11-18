import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

class TransactionDataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.feature_names = ['amount', 'hour', 'day_of_week', 'is_weekend', 'merchant_location', 'payment_method', 'distance_from_home']
        self.categories = ['Groceries', 'Dining', 'Transportation', 'Entertainment', 'Shopping', 'Healthcare', 'Utilities']
    
    def create_data(self, n=2000):
        np.random.seed(42)
        data = {
            'amount': np.random.lognormal(3, 1.5, n),
            'hour': np.random.randint(0, 24, n),
            'day_of_week': np.random.randint(0, 7, n),
            'merchant_location': np.random.randint(0, 11, n),
            'payment_method': np.random.randint(0, 3, n),
            'distance_from_home': np.random.exponential(5, n)
        }
        df = pd.DataFrame(data)
        df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
        
        categories = []
        for _, row in df.iterrows():
            if row['amount'] < 20 and row['hour'] in range(6, 10):
                cat = 'Dining'
            elif 50 <= row['amount'] < 150:
                cat = 'Groceries'
            elif row['amount'] < 30:
                cat = 'Transportation'
            else:
                cat = np.random.choice(self.categories)
            categories.append(cat)
        
        df['category'] = categories
        return df
    
    def prepare_data(self):
        df = self.create_data()
        X = df[self.feature_names]
        y = df['category']
        y_encoded = self.label_encoder.fit_transform(y)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)
        
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        return {
            'X_train': X_train_scaled,
            'X_test': X_test_scaled,
            'y_train': y_train,
            'y_test': y_test,
            'scaler': self.scaler,
            'label_encoder': self.label_encoder,
            'categories': self.categories
        }