import pyttsx3
import datetime
from selenium import webdriver
import speech_recognition as sr
import time  
import pyaudio
 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

def command():
    r = sr.Recognizer() 
    sample=sr.Audio.file("C:\\FFOutput\\Khairiyat _ Remix _ R Factor _ Chhichhore _ Arijit Singh _ BASS CRACKERS(360P).wav")       
    with sample as source:
        print("listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("recognizing...")
        type(audio)
        query=r.recognize_google(audio)
    
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning Max !")

    elif hour>=12 and hour<=18:
        speak("Good evening Max !")
    
    elif hour>=18 and hour<=24:
        speak("Good night Max !")
    
    speak("this is Jarvis Here Nice to see you again Sir ")
    time.sleep(1)
    speak("What can i Do for you ")

if __name__ == "__main__":
    wishme()
    command()
    
    

# def open_google():
#     print("Say...")
#     res=input("")
#     if res=='y':
#         speak("Okey Sir ")
#         speak("well wait for a second ")
#         print("opening...")
#         open()
#         speak("Enjoy Sir")
#     else:
#         speak("okey thank you sir no problem at all  ")

# def open():
#     prog=webdriver.Chrome()
#     prog.get("google.com")

