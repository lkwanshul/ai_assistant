import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import time
import ai_avatar
import ai_variables

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("command = ", Query)
        except Exception as e:
            return "None"

        return Query

def speak(audio):
    ai_avatar.lbl.load('talking-avatar.gif')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    ai_avatar.lbl.load('looking-avatar.gif')


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():
    time = datetime.datetime.now().strftime("%H:%M %p")
    speak("The time is sir" + time)

def Hello():
    speak("hello I am "+ai_variables.ai_avatar_name+" your AI assistant. How are you ?")


def Take_query():
    while (True):
        time.sleep(.5)
        emotion = ""
        if(ai_variables.emotionsQ.empty() != True and ai_variables.emotionsQ.qsize() > 10) :
            emotion = max(list(ai_variables.emotionsQ.queue))

        #if "sad" in emotion:
        #    speak("Hello sir are you feeling sad today ")
        #    continue

        query = takeCommand().lower()

        if "open" in query and "google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif ("what" in query or  "which" in query) and "day" in query:
            tellDay()
            continue

        elif "what" in query and "time" in query:
            tellTime()
            continue

        elif "bye" in query:
            speak("Bye. Check Out GFG for more exciting things")
            exit()

        elif "find" in query and "wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
            continue

        elif "what" in query and "your" in query and "name" in query:
            speak("My name is "+ai_variables.ai_avatar_name)
            continue

        elif "start" in query and ai_variables.ai_avatar_name in query :
            Hello()
            continue
