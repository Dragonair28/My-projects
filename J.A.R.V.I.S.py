import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Intializing Jarvis......")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Wishing function as per the time
def wishMe():
    hour = (datetime.datetime.now().hour)

    if hour >= 0 and hour <12:
        speak("Good Morning Mr.nair..")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mr.nair..")

    else:
        speak("Good Evening Mr.nair..")
    speak("At you service sir..")

# Sending email function
def sendEmail(to, content):
    server =  smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your passoword')
    server.sendmail('recievers email', to , content)
    server.close()


# takes command according to the audio
#def takecommand():
   # r = sr.Recognizer()
    #with sr.Microphone() as source:
    #    print("Listening....")
     #   audio = r.listen(source)

    #try:
    #    print("Recognizing......")
    #    query = r.recognize_google(audio, language = 'en-in')
    #    print(f"user said{query}\n")

    #except Exception as e:
    #    print("sorry sir can you repeat it...")
    #    query = None

    #return query

speak("Intializing Jarvis......")
wishMe()
query = input("enter:")

# Logic for excecuting the tasks as per the query
if 'wikipedia' in query.lower():
    query = query.replace("wikipedia", "")
    results  = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    url = "youtube.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    url = "google.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'anime' in query.lower():
    url = "gogoanime.com"
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir = "C:/Users/Tenac/Music/tkinter music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f'mr.nair the time is {strTime}')



