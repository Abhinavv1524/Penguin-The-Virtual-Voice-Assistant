# chatbot_logic.py
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cv2
import openai

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Please tell me how may I help you")


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Error:", e)
        return "None"


def send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject
    email_message.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, email_message.as_string())

    print("Email sent successfully!")
    speak("Email sent successfully!")


def capture_image(output_path):
    print("Capturing image...")
    speak("Capturing image...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        speak("Error: Could not open webcam")
        return
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_path, frame)
        print("Image captured successfully!")
        speak("Image captured successfully!")
    else:
        print("Error: Could not capture image")
        speak("Error: Could not capture image")
    cap.release()

def get_chatgpt_response(prompt, api_key):
    client = openai.OpenAI(api_key=api_key)
    chat_completion = client.chat_completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-3.5-turbo"
    )
    return chat_completion.choices[0].message.content
