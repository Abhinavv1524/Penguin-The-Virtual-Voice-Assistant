# weather_prediction.py

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from penguin_assistant.chatbot_logic import speak

# Load the trained model
clf = joblib.load('data/weather_model.pkl')  # Adjust the path as necessary

# Load the dataset for visualization
csv_file_path = 'data/Weather.csv'
data = pd.read_csv(csv_file_path)
X = data[['Temperature', 'Humidity', 'Wind_Speed']]
y = data['Rain_Tomorrow']

# Function to predict weather
def predict_weather():
    # Get user input for weather features
    print("Enter temperature in Celsius: ")
    speak("Enter temperature in Celsius: ")
    temperature = int(input())
    print("Enter humidity in percentage: ")
    speak("Enter humidity in percentage: ")
    humidity = int(input())
    print("Enter wind speed in km/h: ")
    speak("Enter wind speed in km/h: ")
    wind_speed = int(input())

    prediction = clf.predict([[temperature, humidity, wind_speed]])

    if prediction == 1:
        print("It will likely rain .")
        speak("It will likely rain .")
    else:
        speak("It will likely not rain .")

