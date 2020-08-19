import pyttsx3
import datetime
from selenium import webdriver
import speech_recognition as sr
import time  
import pyaudio
import wikipedia 
import webbrowser
import os
# import test_jarvis

engine2=pyttsx3.init('sapi5')
voices=engine2.getProperty('voices')

class chat_bot:
    # def formal_conv(self):
    #     if "aur jarvis kya ho rha hai " in final_query:
    #         speak("kuchh khaas nhi sir what about you ")
    #     elif "kuchh khaas nhi " in final_query:
    #         speak("okeyy no problem sir evrything will be okey")
    #     else:
    #         speak("sorry max i couldn't find anything ")        
    def speak_command(self,audio2):
        engine2.say(audio2)
        engine2.runAndWait()



    def take_command(self):
        print("in the chat_bot")
        tk_cm = sr.Recognizer()        
        with sr.Microphone(device_index=1) as source2:
            print("listening...")
            # print(sr.Microphone.list_microphone_names(),"\n\n")
            tk_cm.pause_threshold = 0.5
            audio2=tk_cm.listen(source2)
        try:
            print("recognizing...")
            cm_query=tk_cm.recognize_google(audio2,language='en-in')
            cm_query_lower=cm_query.lower()
            print(f"user said : {cm_query_lower} \n ")
            file2=open("command.txt",'a')
            file2.write(cm_query_lower)
            o.speak_command(f"so do you mean that {cm_query_lower} okeyy Max let me check ")

        except Exception as e:
            print(e)
            print("Please say that again Max ")
            return "None"
            file2.close()
        return cm_query_lower

o=chat_bot()