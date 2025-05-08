import speech_recognition as sr 
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def automated_response(user_query):
    if "account" in user_query.lower():
        return "I can help you with your account details."
    elif "support" in user_query.lower():
        return "Our support team is here to help you."
    elif "payment" in user_query.lower():
        return "I can assist you with payment-related queries."
    else:
        return "I'm here to help with any other questions."

print("Real-time SRT System for Customer Support Automation")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

        try:
            user_input = recognizer.recognize_google(audio)
            print("User: " + user_input)

            response = automated_response(user_input)
            print("Bot: " + response)

            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Bot: Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print("Bot: Could not request results; check your connection.")