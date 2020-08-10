import speech_recognition as sr # recognise speech
import pyttsx3 # python text to speech
import random
import webbrowser 
import datetime
import wikipedia
from googletrans import Translator
import calendar
from tkinter.ttk import *
import os
import winerror
import ctypes
from tkinter import *
from tkinter import filedialog
import requests
import wolframalpha
from PyDictionary import PyDictionary
import urllib3
import psutil
import pywhatkit
urllib3.disable_warnings()
r = sr.Recognizer() # initialize a recogniser
url='Google.com'
class person:
    name = ''
    def setName(self, name):
        self.name = name
def there_exists(terms):

    for term in terms:
        if term in voice_data:
            return True
# get string and make a audio file to be played
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("EDITH: ", audio)
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source:  # microphone as source

        print('speak anything')
        voice_data=''
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        try:
           voice_data = r.recognize_google(audio)    # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down')  # error: recognizer is not connected
        print(f"myself :  {voice_data.lower()}")  # print what user said
        return voice_data.lower()
def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            speak('Good Morning!')
        if currentH >= 12 and currentH < 18:
            speak('Good Afternoon!')
        if currentH >= 18 and currentH != 0:
            speak('Good Evening!')
def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)
    if 'thank you ' in voice_data:
        speak('welcome')
    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is edith sir ")
        else:
            speak("my name is edith sir. what's your name sir?")
    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object
    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")
    if 'introduce yourself'in voice_data:
        speak('hi sir.I am EDITH. full form Even Dead Iam The Hero.I can assistant you in various things.')
        speak('i can translate in 10 languages, show you the calendar ,search the web, open apps, show you movies,news,open email')
        speak('i can also search the wikipedia and I can answer any question you ask.')
        speak('i was created by Shreevatsan.R')
    # 4: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')
    # 5: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')
    #6 : movie
    if 'movie' in voice_data:
        stream= ('https://www.netflix.com/browse','https://www.hotstar.com/in','https://www.primevideo.com/region/eu')
        a=random.choice(stream)
        webbrowser.get().open(a)
    # 7 : send E-mail
    if there_exists(['email']):
        speak('opening')
        mail = 'https://mail.google.com/mail/u/0/#inbox'
        webbrowser.get().open(mail)
        speak('opened')
    # 8 : translate
    if 'translate' in voice_data:
        translator = Translator()
        speak('what language do you want to translate')
        d = record_audio()
        if sr.UnknownValueError:
                speak('say it again')
                d = record_audio()
        speak('say the word which you want to translate')
        if sr.UnknownValueError:
            b = record_audio()
        deste=''
        if d=='tamil':
            deste='ta'
        if d== 'telugu':
            deste='te'
        if d== 'malayalam':
            deste='ml'
        if d== 'hindi':
            deste='hi'
        if  d== 'gujarati':
            deste='gu'
        if d == 'irish':
            deste = 'ga'
        if d == 'italian':
            deste = 'it'
        if d == 'bengali':
            deste = 'bn'
        if d == 'chinese':
            deste = 'zh-cn'
        if d == 'hungarian':
            deste='hu'
        value=translator.translate(b,src='en',dest=deste)
        print(value.text)
    # 9 : lock
    if 'lock my screen' in voice_data:
        speak('ok, sir')

        ctypes.windll.user32.LockWorkStation()
        exit()
    #10 : shut down
    if 'shut down' in voice_data:
        speak('ok sir.')
        speak("Do you wish to shutdown your computer ? (yes / no): ")
        d=record_audio()
        if d=='no':
            speak('ok')
        else:
            os.system("shutdown /s /t 1")
            exit()
    # 11: calendar
    if 'calendar' in voice_data :
        # Function for showing the calendar of the given year
        def showCal():
            new_gui = Tk()
            # Set the background colour of GUI window
            new_gui.config(background="white")
            # set the name of tkinter GUI window
            new_gui.title("CALENDER")
            # Set the configuration of GUI window
            new_gui.geometry("550x600")
            # get method returns current text as string
            fetch_year = int(year_field.get())
            # calendar method of calendar module return
            # the calendar of the given year .
            cal_content = calendar.calendar(fetch_year)
            # Create a label for showing the content of the calender
            cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")
            # grid method is used for placing
            # the widgets at respective positions
            # in table like structure.
            cal_year.grid(row=5, column=1, padx=20)
            # start the GUI
            new_gui.mainloop()
            # Driver Code
        if __name__ == "__main__":
            # Create a GUI window
            gui = Tk()
            # Set the background colour of GUI window
            gui.config(background="white")
            # set the name of tkinter GUI window
            gui.title("CALENDER")
            # Set the configuration of GUI window
            gui.geometry("250x140")
            # Create a CALENDAR : label with specified font and size
            cal = Label(gui, text="CALENDAR", bg="dark gray",
                        font=("times", 28, 'bold'))
            # Create a Enter Year : label
            year = Label(gui, text="Enter Year", bg="light green")
            # Create a text entry box for filling or typing the information.
            year_field = Entry(gui)
            # Create a Show Calendar Button and attached to showCal function
            Show = Button(gui, text="Show Calendar", fg="Black",
                          bg="Red", command=showCal)
            # Create a Exit Button and attached to exit function
            Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)
            # grid method is used for placing
            # the widgets at respective positions
            # in table like structure.
            cal.grid(row=1, column=1)
            year.grid(row=2, column=1)
            year_field.grid(row=3, column=1)
            Show.grid(row=4, column=1)
            Exit.grid(row=6, column=1)
            # start the GUI
            gui.mainloop()
    # 12 : time
    if 'tell me the time' in voice_data :
        now = datetime.datetime.now()  # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        speak("date and time:"+str(date_time))
    # 13 file explorer
    if 'open file explorer' in voice_data :
        speak('sure sir')
        def browseFiles():
            filename = filedialog.askopenfilename(initialdir="/",
                                                  filetypes=(("Text files", "*.txt*"),
                                                             ("all files")))
            # Change label contents
            label_file_explorer.configure(text="File Opened: " + filename)
            # Create the root window
        window = Tk()
        # Set window title
        window.title('File Explorer')
        # Set window size
        window.geometry("1000x1000")
        # Set window background color
        window.config(background="white")
        # Create a File Explorer label
        label_file_explorer = Label(window,
                                    text="File Explorer",
                                    width=100, height=4,
                                    fg="blue")
        button_explore = Button(window,
                                text="Browse Files",
                                command=browseFiles)
        button_exit = Button(window,
                             text="Exit",
                             command=exit)
        label_file_explorer.grid(column=1, row=1)
        button_explore.grid(column=1, row=2)
        button_exit.grid(column=1, row=3)
        # Let the window wait for any events
        window.mainloop()
    # 14 : open google apps
    if 'apps' in voice_data :
        speak('what app do you want')
        app=record_audio()
        if app=='excel':
            webbrowser.get().open('https://docs.google.com/spreadsheets/u/0/')
        if app=='word':
            webbrowser.get().open('https://docs.google.com/document/u/0/')
        if app=='google calendar':
            webbrowser.get().open('https://calendar.google.com/calendar')
        if app=='meet':
            webbrowser.get().open('https://meet.google.com/?hs=197&pli=1&authuser=0')
    # 15 : news
    if 'tell me the news' in voice_data :
        main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"

        # fetching data in json format
        open_bbc_page = requests.get(main_url).json()

        # getting all articles in a string article
        article = open_bbc_page["articles"]

        # empty list which will
        # contain all trending news
        results = []

        for ar in article:
            results.append(ar["title"])

        for i in range(len(results)):
            # printing all trending news
            speak( results[i])
    # 18 dictionary
    if 'say the meaning' in voice_data:
        speak('sure sir')
        dictionary=PyDictionary()
        speak('what is the word')
        a=record_audio()
        print (dictionary.meaning("indentation"))
    #19 charger level
    if 'what is the charger level' in voice_data:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        if plugged == False:
            plugged = "Not Plugged In"
        else:
            plugged = "Plugged In"
        speak(percent + '%' + plugged)
    # 20 bye
    if 'bye' in voice_data:
        speak('bye sir')
        exit()
    # 21 wikipedia
    if 'wikipedia'in voice_data:
        infor = record_audio('tell me your topic')
        speak(wikipedia.summary(infor, sentences=2))

    #music
    if 'play music'in voice_data:
        py
    else:
        try:
            k= record_audio('can you say it again')
            speak('getting the output')
            app_id = "2UPE4R-4YQ876X352"
            client = wolframalpha.Client(app_id)
            res = client.query(k)
            answer = next(res.results).text
            speak(answer)
        except:
            speak('we are facing errors talk again')

person_obj = person()
greeted = False
while(1):
    if greeted == False:
        greetMe()
        greeted = True
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond
