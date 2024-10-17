# assistant_logic.py
from .chatbot_logic import wishMe, takeCommand, speak, send_email, capture_image, get_chatgpt_response
from .weather_prediction import predict_weather
from .image_classifier import capture_and_classify_image
from .labels.class_labels import class_labels
from .config import SENDER_EMAIL, RECEIVER_EMAIL, SMTP_USERNAME, SMTP_PASSWORD
import os
from AppOpener import *
import datetime
import webbrowser
import wikipedia
from dotenv import load_dotenv

def activate_assistant():
    wishMe()
    while True:
        query = takeCommand().lower()
        print("Recognized Query:", query)  # Debug print

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who built you' in query:
            print('I am built by Ms. Diksha Narula and Mr. Abhinav Choudhary')
            speak('I am built by Diksha Narula and Abhinav Choudhary')

        elif 'who are you' in query:
            print('Hey, I am Penguin. Your personal voice assistant. '
                  'I am designed to perform various actions like telling time and jokes, '
                  'running device applications, predicting rainfall, '
                  'capturing pictures, playing songs and many more.')
            speak('Hey, I am Penguin. Your personal voice assistant. '
                  'I am designed to perform various actions like telling time and jokes, '
                  'running device applications, predicting rainfall, '
                  'capturing pictures, playing songs and many more.')

        elif 'hu r u' in query:
            print('Hey, I am Penguin. Your personal virtual assistant. '
                  'I am designed to perform various actions like telling time and jokes, '
                  'running applications, predicting rainfall, '
                  'capturing pictures, playing songs and many more.')
            speak('Hey, I am Penguin. Your personal virtual assistant. '
                  'I am designed to perform various actions like telling time and jokes, '
                  'running applications, predicting rainfall, '
                  'capturing pictures, playing songs and many more.')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'how are you' in query:
            print("I'm doing fine. How about you?")
            speak("I'm doing fine. How about you?")

        elif 'i am good too' in query:
            print("Good. So how may i serve you today?")
            speak("Good. So how may i serve you today?")

        elif 'in which language are you built' in query:
            print("I am built by using Python and Machine learning")
            speak("I am built by using Python and Machine learning")

        elif 'open notes' in query:
            open("notepad")
        elif 'close notes' in query:
            close("notepad")

        elif 'open pinterest' in query:
            open("pinterest")
        elif 'close pinterest' in query:
            close("pinterest")

        elif 'open whatsapp' in query:
            open("whatsapp")
        elif 'close whatsapp' in query:
            close("whatsapp")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\LENOVO\\Documents\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open instagram' in query:
            webbrowser.open("https://instagram.com")

        elif 'tell joke' in query:
            print("Ok, so here's one!")
            speak("Ok, so here's one!")
            print("What did one ocean say to another ocean?")
            speak("What did one ocean say to another ocean?")
            print("Nothing, it just waved.")
            speak("Nothing, it just waved.")

        elif 'another one' in query:
            print("Why did the bicycle fall over?")
            speak("Why did the bicycle fall over?")
            print("Because it was too tired")
            speak("Because it was too tired")

        elif 'email' in query:
            try:
                sender_email = SENDER_EMAIL
                receiver_email = RECEIVER_EMAIL
                speak("Tell the subject of email")
                print("Tell the subject of email")
                subject = takeCommand()
                speak("Tell the message that you want to send")
                print("Tell the message that you want to send")
                message = takeCommand()
                smtp_server = "smtp.gmail.com"
                smtp_port = 465
                smtp_username = SMTP_USERNAME
                smtp_password = SMTP_PASSWORD

                send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, smtp_username,
                           smtp_password)
            except Exception as e:
                print(e)
                speak("Sorry my friend. Iam not  able to send this email")

        elif "goodbye" in query:
            speak("OK TATA BYE BYE sayonarahhh")
            break

        elif "rainfall" in query:
            predict_weather()
            speak("do you wanna know another day data?")
            inpt = takeCommand().lower()

            if inpt == "yes":
                predict_weather()
            else:
                print("Please tell me how may I help you")
                speak(" Please tell me how may I help you")

        elif "chatbot" in query:
            print("yes why not")
            speak("yes why not")
            print("Ask me any problem or anything")
            speak("Ask me any problem or anything")
            while True:
                prompt = takeCommand().lower()
                if prompt == "exit" or prompt == 'isko band karo':
                    print("Okay See ya")
                    speak('Okay See ya')
                    break
                else:
                    api_key = os.getenv('API_KEY')
                    response = get_chatgpt_response(prompt, api_key)
                    print("Penguin Response:", response)
                    speak(response)
                    speak("To stop using my chatbot version say exit")


        elif "click" in query:
            output_path = "captured_image.jpg"
            capture_image(output_path)

        elif "ok leave" in query:
            speak("Okayyy leaving tataa")
            break

        elif "in my hand" in query:
            print("Okay wait a minute!")
            speak("Okay wait a minute!")
            predicted_label = capture_and_classify_image(class_labels)
            speak("Predicted value: " + predicted_label)

        else:
            speak("try again")


