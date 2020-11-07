import speech_recognition as sr 
import pyttsx3
import pyjokes
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

assis_name="Rocky"
boss_name="Code Thamila"
def say(text):
    engine=pyttsx3.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening.......")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognizing.............")
            text=r.recognize_google(audio,language='en-in')
            print(f"User said : {text}\n")
        except Exception as e :
            print(e)
            print("can not recognize your voice")
            return "None"
        return text

def tell_joke():
    joke=pyjokes.get_joke()
    return joke
    

def respond(text):
    if 'hai' in text:
        say("HI SIR !")
    elif "who are you" in text:
        say("My name is {}".format(assis_name))
    elif "good morning" in text: 
        say("A warm" +text) 
        say("How are you"+boss_name+"?")         
    elif "I am fine" in text:
        say("oh really good")
    elif "who I am" in text: 
        say("If you talk then definately your human.")
    elif 'who are you' in text:
        say("My name is "+assis_name+"!"+"My Boss Name is "+boss_name)
    elif 'where am I' in text:
        say("you are in ")
    elif 'thank you so much' in text:
        say("It's my pleasure Sir!")
    elif 'fine' in text or "good" in text: 
        say("It's good to know that your fine")
    elif 'tell me joke' in text:
        engine2=pyttsx3.init()
        engine2.setProperty('rate',100)
        engine2.say(tell_joke())
        engine2.runAndWait()
    elif 'open my site' in text:
        webbrowser.open('https://thasacodethamizha.blogspot.com/')
    elif 'open' in text:
        text =text.replace("open","")
        if 'Notepad' in text:
            os.startfile('C:\\Program Files (x86)\\Notepad++\\notepad++.exe')
        elif 'Arduino' or 'arduino' in text:
            os.startfile('C:\\Program Files (x86)\\Arduino\\arduino.exe')
    elif 'close' in text:
        text=text.replace("close","")
        if 'Notepad' or 'notepad' in text:
            os.system("TASKKILL /F /IM notepad++.exe")
        elif 'Arduino' or 'arduino' in text:
            os.system("TASKKILL /F /IM arduino.exe")      
    elif 'search YouTube' in text:
        text=text.replace("search YouTube","")
        path="F:\\Projects\\P-Projects\\python projects\\Voice assistant\\chromedriver.exe"
        driver=webdriver.Chrome(path)
        url='https://www.youtube.com/'
        driver.get(url)
        search= driver.find_element_by_name("search_query")
        search.send_keys(text)
        search.send_keys(Keys.RETURN)
        

while True:
    text=takecommand()
    respond(text)
