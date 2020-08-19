import pyttsx3
import datetime
from selenium import webdriver
import speech_recognition as sr
import time  
import pyaudio
import wikipedia 
import webbrowser
import os
import chat
from chat import chat_bot 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')


def command():
    r = sr.Recognizer()        
    with sr.Microphone(device_index=1) as source:
        # fpath=c_drive.replace("c_drive","c:\\")
        print("listening...")
        # print(sr.Microphone.list_microphone_names(),"\n\n")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("recognizing...")
        fquery=r.recognize_google(audio,language='en-in')
        query=fquery.lower()
        print(f"Max said : {query} \n ")
        file=open("sample.txt",'a')
        file.write(query)
        file.write("\n")


    except Exception as e:
        print(e)
        print("Please say that again Max ")
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
        print(query,": \n")
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
        
        elif "whats up jarvis" in query:
            speak("I am good sir good what about you ")
        elif "love you baccha" in query:
            speak("love you baabu ")
        elif "play music" in query:
            music_dir="E:\\all types of songs\\es video\\"
            songs=os.listdir(music_dir)
            # print(songs)
            for i in songs:
                print(f"{i} \n")
                speak(f"do you want to listen {i} songs")
                chat_obj=chat_bot()
                final_query=chat_obj.take_command()
                print(f"max said : {final_query}")
                if "play" in final_query :
                    os.startfile(os.path.join(music_dir,i))
                    break
                else:
                    speak("okey sir no problem at all")

        elif "so jao " in query:
            speak("Okey sir as you wish till then jarvis take care , see you soon sir ")
            exit
        elif "who loves aditi" in query:
            speak("sir you love aditi and you said it to me thousand of time ")
        elif "who is aditi" in query:
            speak("okeyy max let me show you again")
            speak("wanna see some slides sir or videos ")
            chat_obj=chat_bot()
            final_query=chat_obj.take_command()
            if "slides" in final_query:
                os.startfile(os.path.join("C:\\xampp\\htdocs\\php_proj\\glry\\images\\gallery","17.jpg"))
            
            elif "video" in final_query:
                os.startfile(os.path.join("C:\\Users\\sknt\\Documents\\Wondershare Filmora 9\\Output","bd 2.mp4"))
                speak("here is you aditi sir enojy the video")
            else:
                speak("sorry sir we couldn't find anything ")

        elif "ok" in query:
            speak("sure sir")
        elif " aur jarvis kya chal rha hai  " in query:
            speak("mmm i am okey sir what about you ")
        elif "i am good good jarvis" in query:
            speak("O well that's is okeyy sir  ")
            time.sleep(1)
            speak("so what is your today")
        elif "kuchh khaas nahi " in query:
            speak("O But why sir ??")

        elif "hmm good baccha" in query:
            speak("ha ha ha o well thank you sir for calling me baccha")
        elif "take command " in query:
            obj=chat_bot()
            obj.take_command()
        elif "kya kar rahe ho" in query:
            speak("talking to you max , so how was you day today")
        elif "it was good" in query:
            speak("O great sir")
        elif "my drives" in  query:
            speak("I got it Sir please tell me the drive names \n ")
            obj2=chat_bot()
            f_query=obj2.take_command()
            
            drive_letter=f_query.replace(" drive","")
            if len(drive_letter)==1:
            # print(drive_letter)
                print(f"max said{drive_letter} drive ")
                print(f"sir you said {f_query}")
                
                drives=['c','d','e','f','g']
                if drive_letter in drive_letter:
                    final_path=drive_letter+":\\"
                    print(final_path)
                    files_folders=os.listdir(final_path)
                    print("C: drive \n")
                    speak("here are the list of total files and folder sir ")
                    for all_fnf in files_folders:
                        
                        print(f"{all_fnf} \n")
                    # print(final_path)

                else:
                    speak("sorry sir drive not found ")
            else:
                speak("please tell me the drive name sgain sir")            
        
        elif "so jarvis how was your day today" in query:
            speak("O it was good sir tell me about you") 
        
        
        else:
            speak("Please say that again Sir  ")
