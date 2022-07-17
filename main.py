import time
import pyttsx3
import speech_recognition as sr
import pyaudio
import os
import datetime
import pywhatkit
import subprocess

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 145)

def speak(text):
    engine.say(text)
    engine.runAndWait()
def dateandtime():
    today = datetime.date.today()
    now = datetime.datetime.now()
    speak(f'Todays Date is {today.strftime("%B %d, %Y")}')
    speak(f'and present time is {now.strftime("%H:%M:%S")}')
    print(now.strftime("%H:%M:%S"))

def wishMe():
    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak("Hello sir,Good Morning, i am you personal assistant, friday")
        dateandtime()
        print("Hello sir,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello sir,Good Afternoon, i am you personal assistant, friday" )
        dateandtime()
        print("Hello sir,Good Afternoon")
        takeCommand()
    else:
        speak("Hello sir,Good Evening, i am you personal assistant, Friday" )
        dateandtime()
        print("Hello sir,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"Shiva said:{statement}\n")
        except Exception as e:
            # speak("sorry sir, can you  please say that again")
            return "None"
        return statement







if __name__=='__main__':
    print("friday in Online")
    speak("friday in Online")
    wishMe()
    while True:
        # speak("Tell me sir, how can I help you now?")
        hour=datetime.datetime.now().hour
        mint=datetime.datetime.now().minute
        # print(hour)
        if hour==13 and (mint==20 or mint==25 or mint==30):
            while True:
                speak("This your Lunch Time, put your work a side, and have  a lunch sir")
                speak("Are you going for Lunch or Not?")
                # time.sleep(2)
                statement=takeCommand().lower()
                if "yes" in statement :
                    print("Yes Lunch")
                    speak("Thanks sir, so am going sleep for 20 mins")
                    time.sleep(60*20)
                    break
                else:
                    pass

        elif hour==16 and (mint==20 or mint==15 or mint==25):
            while True:
                speak("sir, it is time to pick up your Father")
                statement = takeCommand().lower()
                if "yes" in statement:
                    print("Yes for pickup father")
                    speak("Thanks sir, so am going sleep for 30 mins")
                    time.sleep(60 * 30)
                    break
                else:
                    pass

        elif hour==20 and (mint==10 or mint==15 or mint==20):
            while True:
                speak("This your Dinner Time, put your work a side, and have  a lunch sir")
                speak("Are you going for Lunch or Not?")
                statement = takeCommand().lower()
                if "yes" in statement:
                    print("Yes for Dinner")
                    speak("Thanks sir, so am going sleep for 20 mins")
                    time.sleep(60 * 20)
                    break
                else:
                    pass
        elif hour==21 and (mint==30 or mint==35 or mint==40):
            while True:
                speak("sir, you are working too much for DXC, please take rest.")
                statement = takeCommand().lower()
                if "yes" in statement:
                    speak("sir, your laptop is going to shutdown in t mins 10 seconds")
                    os.system("shutdown /s /t 10")
                    break
                else:
                    pass

        statement = takeCommand().lower()
        if statement==0:
            continue
        elif "sleep" in statement:
            speak("going to sleep for 3 min")
            time.sleep(60*3)
            speak('sir, i am  back')
        elif "friday" in statement and "offline" in statement:
            speak("Going to offline, love you sir...!")
            break
        elif ("time" in statement or "date" in statement) and "now" in statement:
            dateandtime()
        elif "shutdown" in statement:
            speak("sir, your laptop is going to shutdown in t mins 10 seconds")
            os.system("shutdown /s /t 25")
            for i in range(10):
                speak(i)
            speak("Friday is going to offline sir, good day")
            break
        elif ("open" in statement or "search" in statement) and "google" in statement:
            if 'search' in statement:
                statement=statement.replace("friday","")
                statement=statement.replace("search","")
            else:
                statement = statement.replace("friday", "")
                statement=statement.replace("open","")
            statement=statement.replace("google","")
            speak(f"Searching {statement} in Google")
            pywhatkit.search(statement)
            pass
        elif "youtube" in statement and "play" in statement:
            statement = statement.replace("youtube", "")
            statement = statement.replace("play", "")
            speak(f"Playing {statement} in youtube")
            print(statement)
            pywhatkit.playonyt(statement)
        elif "friday" in statement and "there" in statement:
            speak('yes sir, i am in online')
        elif "lunch" in statement and "time" in statement:
            speak("lunch time is 1 clock 30 min between 2 clock 30 min")
        elif "dinner" in statement and "time" in statement:
            speak("lunch time is 8 clock 0 min between 8 clock 30 min")
        elif "hi" in statement or "hello" in statement or "hai" in statement:
            speak("Hi sir, how can i help you.")
        elif "thanks" in statement and "helping me" in statement:
            speak("it is honour to help you, sir")
        elif "open" in statement:
            if "outlook" in statement:
                speak("Opening Outlook")
                os.startfile("outlook")
            elif "file " in statement and "explorer" in statement:
                speak("Opening file explorer")
                subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
        elif 'close' in statement:
            if "outlook" in statement :
                speak("Closing Outlook")
                os.system('taskkill /im outlook.exe /f')
            elif "google" in statement:
                speak("Closing google")
                os.system("taskkill /im chrome.exe /f")
            elif "file " in statement and "explorer" in statement:
                speak("Closing file explorer")
                os.system("taskkill /f /im explorer.exe")
        else:
            pass
            # speak(f"{statement}  not in my database, sir")

