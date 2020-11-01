import pyttsx3

def say (text):
    engine=pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)
    engine.say(text)
    engine.runAndWait()

while True:
    text = input(print("Enter Any Text!"))
    say(text)