import speech_recognition as sr
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print("Sorry, there was an error with the request. {0}".format(e))
