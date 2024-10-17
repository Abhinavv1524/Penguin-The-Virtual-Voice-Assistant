# ml_models.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
csv_file_path = '../data/Weather.csv'
data = pd.read_csv(csv_file_path)

# Define features and target variable
X = data[['Temperature', 'Humidity', 'Wind_Speed']]
y = data['Rain_Tomorrow']

# Create a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Save the trained model
joblib.dump(clf, '../data/weather_model.pkl')  # Adjust path as needed
