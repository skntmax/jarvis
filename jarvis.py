import pyttsx3
import datetime
from selenium import webdriver
import speech_recognition as sr
import time  
import pyaudio
import wikipedia 
import webbrowser
import os 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')


def command():
    r = sr.Recognizer()        
    with sr.Microphone(device_index=1) as source:
        print("listening...")
        # print(sr.Microphone.list_microphone_names(),"\n\n")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("recognizing...")
        fquery=r.recognize_google(audio,language='en-in')
        query=fquery.lower()
        print(f"user said : {query} \n ")
        file=open("sample.txt",'a')
        file.write(query)
        speak(f"so do you mean that {query} okeyy sir let me check ")

    except Exception as e:
        print(e)
        print("say that again please ")
        return "None"
        file.close()
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning Max !")

    elif hour>12 and hour<=18:
        speak("Good evening Max !")
    
    elif hour>18 and hour<=24:
        speak("Good night Max !")
    
    speak("this is Jarvis Here Nice to see you again Sir ")
    time.sleep(1)
    speak("What can i Do for you ?")

def og():
    if 'google' in query:
        speak("yes you are in the correct loop")                

class G():
    def __init__(self):
        speak("so would you like to open google chrome sir ?")
    def open_google():
        print("please press y for open the google or press N for no")
        res=input("")
        if res=='y':
            speak("Okey Sir ")
            speak("well wait for a second ")
            print("opening...")
            open()
            speak("Enjoy Sir")
        else:
            speak("okey thank you sir no problem at all ")

    def open():
        prog=webdriver.Chrome()
        prog.get("google.com")


if __name__ == "__main__":
    wishme()
    while True:
        query=command()
        print(query,"\n")
        if 'Love you jarvis' in query:
            speak("Love you too sir ")
        elif "facebook" in query:
            webbrowser.open("facebook.com")
        elif "stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "insta" in query:
            webbrowser.open("instagram.com")
        elif "wikipedia" in query:
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("okey sir according to the wikipedia")
            print(result)
            speak(result)
        
        elif "see the problem" in query:
            speak("But what is the problem sir")
        
        elif "jarvis" in query:
            speak("oo love you too sir")
        
