import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os



print('Initializing Jarvis')

MASTER = "sir"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# this function pronunce the string given to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


# this function wish u as per the time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    #print(hour)

    if(hour>=0 and hour<=12):
        speak("good morning" + MASTER)
    elif(hour>12 and hour<=18):
        speak("good afternoon" + MASTER)
    else:
        speak("good evening" + MASTER)

    #speak("i am jarvis .  How may i help u")

# this function will take command from microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")
    except Exception as e:
        print("Say that again please")
        query=None
    return query

# main function starting here
speak("This is jarvis")
wishMe()
query=takeCommand()

if 'wikipedia' in query.lower():
    speak("Searching wikipedia...")
    query=query.replace("wikipedia", "")
    result=wikipedia.summary(query,sentences=2)
    print(result)
    speak(result)
elif 'open youtube' in query.lower():
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open google' in query.lower():
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open music' in query.lower():
    songs_dir="C:\\Users\\Ankit\\Music"
    songs=os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir,songs[0]))
