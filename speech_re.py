import speech_recognition as st

def command():
    r=st.Recognizer()
    with st.Microphone() as source:
        r.adjust_for_ambient_noise(source ,duration=1)
        print("Listening....")
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            print("Recognizing............")
            text = r.recognize_google(audio,language='en-in')
            print(f"User Said :{text}\n")
        except Exception as e:
            print(e)
            print("Unable To Recognize Your Voice")

while True:
    command()