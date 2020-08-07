import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:

        speak("Good Morning!.")

    elif hour >= 12 and hour < 18:

        speak("Good Afternoon!.")

    else:

        speak("Good Evening!.")

    speak("I am Jarvae assistant. sabbbhhh badiya hey. Mein, Paaghal hoon. Tu chootiyaa hey")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        # r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        # print(r.energy_threshold)
        # print("Chucking rate: ", source.CHUNK)
        # print("format rate :", source.format)
        # print("Say something!...")
        # print(r.energy_threshold)
        # r.energy_threshold += 280
        audio = r.listen(source)
        # print(audio)

    try:

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said ", query, '\n')
        speak(query)

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('myline.dicksjohn@gmail.com', 'johndicks1992')
    server.sendmail('myline.dicksjohn@gmail.com', to, content)
    server.close()

if __name__ == '__main__':

    # speak("Good morning")
    # wishMe()
    while True:
        query = takeCommand().lower()

        # LOGIC FOR EXECUTING TASK
        if 'wikipedia' in query:
            speak('Searching Wikipedia....!')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        if query == "bye":
            exit()
        
        if "youtube" in query:
            webbrowser.open('https://www.youtube.com/watch?v=Lp9Ftuq2sVI')

        if "open google" in query:
            webbrowser.open("google.com")

        if "play music" in query:
            speak("Playing Music")
            music_dir = 'C:\\Users\\MUJ\\Desktop\\New folder (4)\\Baar-Baar-Dekho-320Kbps-2016[Songspk.LIVE]'
            songs = os.listdir(music_dir)
            print(songs)
            a = random.randint(0, 5)
            os.startfile(os.path.join(music_dir, songs[a]))
            

        if "the time" in query:
            starttime = datetime.datetime.now().strftime("%H hours. %M minutes. and %S seconds.")
            strin = "The time is! " + starttime + "."
            speak(strin)

        if "email to jay" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rishabhgupta.nmims@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                exit()
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 