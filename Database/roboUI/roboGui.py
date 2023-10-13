import time
import pyttsx3
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import wikipedia
from translate import Translator
import pywhatkit
import pyautogui
import requests
from bs4 import BeautifulSoup
import math
import pyjokes
import PyPDF2
from pytube import YouTube
import keyboard
from PyDictionary import PyDictionary as Diction
import os
from datetime import datetime
from pywikihow import search_wikihow
import webbrowser 
import sys
from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
from time import sleep
import wolframalpha
from notifypy import Notify
import bs4
import requests
from Body.Speak import Speak
from Robo import MainExecution
from roboUI import Ui_RoboUI
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import subprocess
import speedtest
import os
from dotenv import load_dotenv

load_dotenv()

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        self.Pass()
    #    self.TaskExe()


    def TakeCommand(self):
        command=sr.Recognizer()
        print(command)

        with sr.Microphone() as source:
            print(": Listening....")
            command.pause_threshold = 1
            audio=command.listen(source, 0, 6)

        try:
            print(": Recongnizing...")
            self.query = command.recognize_google(audio, language="en-in")
            print(f": You Said: {self.query}")
        except Exception as Error:
            print(Error)
            return ""

        return self.query.lower()
    
    def Pass(self):
        Speak("This File is Password protected please tell password to open the file!!!")
        pass_inp = input("Enter your password: ")
        password = "saurabh"
        passw = str(password)
        if passw == str(pass_inp):
            Speak("Access Granted")
            self.TaskExe()
        else:
            Speak("Access Not Granted")

    def TaskExe(self):

        Speak("Hello Sir, I am Robo . ")
        Speak("How Can I Help You ?")

        def CoronaVirus(country):
            countries = str(country).replace(" ","")
            url = f"https://www.worldometers.info/coronavirus/country/{countries}/"
            result = requests.get(url)
            soups = bs4.BeautifulSoup(result.text,'lxml')
            corona = soups.find_all('div',class_='maincounter-number')
            Data = []
            for case in corona:
                sp=case.find('span')
                Data.append(sp.string)
            cases, death, recovered = Data
            return cases, death, recovered

        def TimeTable1():
            Speak("Checking....")

            from TimeTable.TimeTable import Time

            value = Time()

            Noti = Notify()

            Noti.title = "TimeTable"

            Noti.message = str(value)

            Noti.send()

            Speak("AnyThing Else Sir ??")

        def Notepad():
            Speak("Tell Me The Query .")
            Speak("I Am Ready To Write .")

            writes = self.TakeCommand()

            time = datetime.now().strftime("%H:%M")

            filename = str(time).replace(":","-") + "-note.txt"

            with open(filename,"w") as file:

                file.write(writes)

            path_1 = "C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\" + str(filename)

            path_2 = "C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\Notepad\\" + str(filename)

            os.rename(path_1,path_2)

            os.startfile(path_2)

        def OnlinClass(Subject):

            Speak("Joining The Class Sir .")

            if 'science' in Subject:

                from OnlineClasses.Links import Science

                Link = Science()

                webbrowser.open(Link)

                sleep(10)

                click(x=629, y=788)

                sleep(1)

                click(x=1354, y=598)

                Speak("Class Joined Sir .")

            elif 'mathematics' in Subject:

                from OnlineClasses.Links import Maths

                Link = Maths()

                webbrowser.open(Link)

                sleep(10)

                click(x=629, y=788)

                sleep(1)

                click(x=1354, y=598)

                Speak("Class Joined Sir .")

            elif 'social' in Subject:

                from OnlineClasses.Links import sst

                Link = sst()

                webbrowser.open(Link)

                sleep(10)

                click(x=629, y=788)

                sleep(1)

                click(x=1354, y=598)

                Speak("Class Joined Sir .")

            elif 'hindi' in Subject:

                from OnlineClasses.Links import Hindi

                Link = Hindi()

                webbrowser.open(Link)

                sleep(10)

                click(x=629, y=788)

                sleep(1)

                click(x=1354, y=598)

                Speak("Class Joined Sir .")

            elif 'english' in Subject:

                from OnlineClasses.Links import English

                Link = English()

                webbrowser.open(Link)

                sleep(10)

                click(x=629, y=788)

                sleep(1)

                click(x=1354, y=598)

                Speak("Class Joined Sir .")

        def WolfRam(q):
            api_key = os.getenv('API')
            requester = wolframalpha.Client(api_key)
            requested = requester.query(q)
            try:
                Answer = next(requested.results).text 
                return Answer
            except:
                Speak("An String Value is Not Answerable!!")

        def Temperature(q):
            temp = str(q)
            temp = temp.replace("robo","")
            temp = temp.replace("in","")
            temp = temp.replace("what is the","")
            temp = temp.replace("temperature","")

            temp_query = str(temp)

            if 'outside' in temp_query:
                var1="Temperature in Ahmedabad"
                answer = WolfRam(var1)
                Speak(f"The Temperature Outside is {answer}")
            else:
                var2 = "Temperature in " + temp_query
                answer = WolfRam(var2)
                Speak(f"{var2} is {answer}")

        def Alarm(query):
            Speak("Ok Sir !")
            TimeHere=  open('C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Data.txt','a')
            TimeHere.write(query)
            TimeHere.close()
            os.startfile("C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\ExtraPro\\Alarm.py")

        def YouTubeSearch(term):
            result = "https://www.youtube.com/results?search_query=" + term
            print(result)
            webbrowser.open(result)
            Speak("This Is What I Found For Your Search .")
            pywhatkit.playonyt(term)
            Speak("This May Also Help You Sir .")

        def Music():
            Speak("Tell Me the name of the Song!")
            musicName=self.TakeCommand().lower()     

            if 'chale aana' in musicName:
                os.startfile("C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\Sound\\chale aana.mp3")
            elif 'humnava mere' in musicName:
                os.startfile("C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\Sound\\Humnava Mere.mp3")
            elif 'bulleya' in musicName:
                os.startfile("C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\Sound\\Bulleya.mp3")
            else:
                pywhatkit.playonyt(musicName)
            
            Speak("Your Song has been started!, Enjoy Sir!")

        def OpenApps():
            Speak("OK Sir, Wait A Second") 
            
            if 'code' in self.query:
                os.startfile("C:\\Users\\saura\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif 'telegram' in self.query:
                os.startfile("C:\\Users\\saura\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Telegram Desktop\\Telegram")
            elif 'edge' in self.query:
                os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
            elif 'facebook' in self.query:
                webbrowser.open("https://www.facebook.com/")
            elif 'instagram' in self.query:
                webbrowser.open("https://www.instagram.com/")
            elif 'maps' in self.query:
                webbrowser.open("https://www.google.com/maps/place/%E0%AA%87%E0%AA%B6%E0%AB%8D%E0%AA%B5%E0%AA%B0+%E0%AA%AA%E0%AA%BE%E0%AA%B0%E0%AB%8D%E0%AA%95+%E0%AA%B8%E0%AB%8B%E0%AA%B8%E0%AA%BE%E0%AA%87%E0%AA%9F%E0%AB%80,+P+%26+T+%E0%AA%95%E0%AB%8B%E0%AA%B2%E0%AB%8B%E0%AA%A8%E0%AB%80,+%E0%AA%AE%E0%AA%A3%E0%AB%80%E0%AA%A8%E0%AA%97%E0%AA%B0,+%E0%AA%85%E0%AA%AE%E0%AA%A6%E0%AA%BE%E0%AA%B5%E0%AA%BE%E0%AA%A6,+%E0%AA%97%E0%AB%81%E0%AA%9C%E0%AA%B0%E0%AA%BE%E0%AA%A4+380028/@22.9953297,72.5852493,15z/data=!3m1!4b1!4m6!3m5!1s0x395e85ea6de12e9d:0x8bcdb7f6d59dc0ef!8m2!3d22.9953107!4d72.5955491!16s%2Fg%2F11ghpm4wmf?entry=ttu")

            elif 'chrome' in self.query:
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome")
            else:
                Speak("Your Command has been Successfully Completed!!")
        
        def CloseApps():
            Speak("OK Sir, Wait A Second!")

            
            if 'edge' in self.query:
                os.system("TASKKILL /F /im msedge.exe")
                
            elif 'youtube' in self.query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'telegram' in self.query:
                os.system("TASKKILL /F /im Telegram.exe")

            elif 'code' in self.query:
                os.system("TASKKILL /F /im code.exe")

            elif 'instagram' in self.query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'maps' in self.query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'facebook' in self.query:
                os.system("TASKKILL /F /im chrome.exe")

            elif 'chrome' in self.query:
                os.system("TASKKILL /F /im chrome.exe")
            else:
                Speak("Your Command has been Successfully Completed!!")
        
        def YoutubeAuto():
            Speak("What's Your Command?")
            comm = self.TakeCommand()
            if 'restart' in comm:
                keyboard.press('0')
            elif 'mute' in comm:
                keyboard.press('m')
            elif 'skip' in comm:
                keyboard.press('l')
            elif 'back' in comm:
                keyboard.press('j')
            elif 'full screen' in comm:
                keyboard.press('f')
            elif 'film mode' in comm:
                keyboard.press('t')
            elif 'pause' in comm:
                keyboard.press('k')
            elif 'speed up' in comm:
                keyboard.press('>')
            elif 'speed down' in comm:
                keyboard.press('<')
            elif 'search bar' in comm:
                keyboard.press('/')

            Speak('Done Sir')
        
        def TakeHindi():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold=1
                audio = r.listen(source, 0, 5)

            try:
                print("Recognizing...")
                query=r.recognize_google(audio, language="hi")

            except:
                return ""

            query=str(query).lower()
            return query
        
        def Tran():
            Speak("Tell Me the Line!")
            line=TakeHindi()
            line=str(line)
            from googletrans import Translator as googletrans
            translate = googletrans()
            result = translate.translate(line)
            data=result.text
            Speak(f"The translation is: {data}")
        
        def ChromeAuto():
            Speak("Chrome Automation started!")
            command = self.TakeCommand()

            if 'close this tab' in command:
                keyboard.press_and_release('ctrl + w')
            elif 'open new tab' in command:
                keyboard.press_and_release('ctrl + t')
            elif 'open new window' in command:
                keyboard.press_and_release('ctrl + n')
            elif 'history' in command:
                keyboard.press_and_release('ctrl + h')
            elif 'download' in command:
                keyboard.press_and_release('ctrl + j')
            elif 'incognito mode' in command:
                keyboard.press_and_release('ctrl + shift + n')
            elif 'scroll down' in command:
                keyboard.press_and_release('space bar')
            elif 'full screen' in command:
                keyboard.press_and_release('F11')

            Speak('Done sir!')

        def Dict():
            Speak("Activated Dictionary!")
            Speak("Tell Me the Problem!")
            probl = self.TakeCommand()

            if 'meaning' in probl:
                probl=probl.replace("What is the","")
                probl=probl.replace("robo","")
                probl=probl.replace("meaning of","")
                probl=probl.replace(" of ","")
                result=Diction.meaning(probl)
                Speak(f"The Meaning of {probl} is {result}")

            elif 'synonym' in probl:
                probl=probl.replace("What is the","")
                probl=probl.replace("robo","")
                probl=probl.replace("synonym of","")
                probl=probl.replace(" of ","")
                result=Diction.synonym(probl)
                Speak(f"The Synonym of {probl} is {result}")
            
            elif 'antonym' in probl:
                probl=probl.replace("What is the","")
                probl=probl.replace("robo","")
                probl=probl.replace("antonym of","")
                probl=probl.replace(" of ","")
                result=Diction.antonym(probl)
                Speak(f"The Antonym of {probl} is {result}")

            Speak("Exited Dictionary Sir")

        def Reader():
            Speak("Tell Me the Name of the Book")

            name=self.TakeCommand()

            if 'india' in name:
                os.startfile("C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\Books\\ch1.pdf")
                book=open("C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\Books\\ch1.pdf", 'rb')
                pdfreader1 = PyPDF2.PdfReader(book)
                # pages=pdfreader1.getNumPages()
                pages = len(pdfreader1.pages)
                Speak(f"Number of Pages in This Books Are {pages}")
                Speak("From which Page I Have to Start Reading?")
                numPage=int(input("Enter the page Number: "))
                page = pdfreader1.pages[numPage]
                text=page.extract_text()
                Speak("In Which language, I Have To Read?")
                lang = self.TakeCommand()

                if 'hindi' in lang:
                    trans1 = Translator(to_lang='hi')  # Pass the target language 'hi' here
                    chunk_size = 400  # Adjust the chunk size as needed
                    num_chunks = math.ceil(len(text) / chunk_size)
                    
                    for i in range(num_chunks):
                        chunk = text[i * chunk_size: (i + 1) * chunk_size]
                        textHin = trans1.translate(chunk)
                        textm = textHin

                        try:
                            speech = gTTS(text=textm, lang="hi")
                            chunk_path = f"C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\Books\\chunk_{i}.mp3"
                            speech.save(chunk_path)
                            playsound(chunk_path)
                            os.remove(chunk_path)  # Delete the chunk file after playing
                        except Exception as e:
                            print("Error playing audio:", str(e))

                if 'english' in lang:
                    trans1 = Translator(to_lang='en')  # Pass the target language 'hi' here
                    chunk_size = 400  # Adjust the chunk size as needed
                    num_chunks = math.ceil(len(text) / chunk_size)
                    
                    for i in range(num_chunks):
                        chunk = text[i * chunk_size: (i + 1) * chunk_size]
                        textHin = trans1.translate(chunk)
                        textm = textHin

                        try:
                            speech = gTTS(text=textm, lang="en")
                            chunk_path = f"C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\Books\\chunk_{i}.mp3"
                            speech.save(chunk_path)
                            playsound(chunk_path)
                            os.remove(chunk_path)  # Delete the chunk file after playing
                        except Exception as e:
                            print("Error playing audio:", str(e))

        while True:
            self.query=self.TakeCommand()

            if 'hello' in self.query.lower():
                Speak("Hello Sir, I am robo. Your Personal Voice Assistant!")
                Speak("How May I help You?")

            elif 'how are you' in self.query.lower():
                Speak("I am Fine Sir!")
                Speak('Whats About You?')

            elif 'I am also fine' in self.query.lower():
                Speak("Ok Sir, Anything else you want!!")

            elif 'you need a break' in self.query.lower():
                Speak("Ok Sir, You can Call me Anytime!")
                Speak("Just Say Wake Up robo!")
                break

            elif 'thank you' in self.query.lower():
                Speak("Welcome Sir, I am here to help you anytime.")
                
            elif 'thank u' in self.query.lower():
                Speak("Welcome Sir, I am here to help you anytime.")

            elif 'thankyou' in self.query.lower():
                Speak("Welcome Sir, I am here to help you anytime.")

            # corona
            elif 'corona' in self.query.lower():
                Speak("Please tell the country: ")
                inp=input("Enter country name: ")
                kk1,kk2,kk3=CoronaVirus(inp)
                Speak(f"Cases:{kk1}")
                Speak(f"Deaths:{kk2}")
                Speak(f"Recovered:{kk3}")

            elif 'time table' in self.query.lower():
                Speak("Showing TimeTable Sir")
                TimeTable1()

            elif 'write file' in self.query.lower() or 'right file' in self.query.lower():
                Speak("Ok sir")
                Notepad()
                Speak("Done sir!") 

            elif 'close notepad' in self.query.lower():
                Speak("Ok Sir closing")
                os.system("TASKKILL /F /im Notepad.exe")
                Speak("Done sir!")

            elif 'online class' in self.query.lower():
                Speak("Tell me the name of the class")
                classs= self.TakeCommand()
                OnlinClass(classs)                 

            elif 'solar system' in self.query.lower():
                Speak("Tell me the name of body")
                body_name = self.TakeCommand()
                body_name = body_name.replace(" ", "")
                from Nasa import SolarBodies
                SolarBodies(str(body_name))
                # mars, saturen, venus, etc.
            
            elif 'asteroids' in self.query.lower():
                Speak("Please enter start date and end date")
                start = input("Enter start date in year-month-date format: ")
                end = input("Enter end date in year-month-date format: ")
                from Nasa import Astro
                Astro(start, end)
                # Astro('2022-09-01','2022-09-02')


            elif 'mars images' in self.query.lower():
                from Nasa import MarsImage
                MarsImage()
            
            elif 'space news' in self.query.lower():
                Speak("Tell Me the Date for news Extracting Process .")
                value=input("Enter Date in Year-Month-Date format: ")
                from Nasa import NasaNews
                NasaNews(value)
                # NasaNews("2023-03-10") 
            
            elif 'youtube search' in self.query:
                self.query = self.query.replace("robo","")
                self.query = self.query.replace("youtube search","")
                YouTubeSearch(self.query)

            elif 'website' in  self.query.lower():
                # Speak("Tell Me The Name of the Website!")
                self.query=self.query.replace("robo","")
                self.query=self.query.replace("website","")
                self.query=self.query.replace(" ","")
                web1=self.query.replace("open","")
                web2="https://www."+web1+".com"
                webbrowser.open(web2)
                Speak("Launched Sir!")

            elif 'wikipedia' in self.query.lower():
                Speak("Searching wikipedia...")
                self.query=self.query.replace("robo","")
                self.query=self.query.replace("wikipedia","")
                self.query=self.query.replace("search","")
                self.query=self.query.replace(" ","")
                wiki=wikipedia.summary(self.query, 2)
                Speak(f"According to WikiPedia : {wiki}")

            elif "whatsapp message" in self.query.lower():
                self.query=self.query.replace("robo","")
                self.query=self.query.replace("send","")
                self.query=self.query.replace("whatsapp message","")
                self.query=self.query.replace("to","")
                self.query=self.query.replace("please","")
                name=str(input("Enter name of the person: "))
                Speak(f"What's the Message for {name}") 
                MSG = input("Write message here: ")
                from Automations import WhatsappMsg
                WhatsappMsg(name, MSG)
        
            elif "show chat" in self.query.lower():
                Speak("With Whom?")
                name=input("Enter name: ")
                from Automations import WhatsappChat
                WhatsappChat(name)

            elif 'music' in self.query:
                Music()

            elif 'screenshot' in self.query:
                Speak("OK Boss, What Should I Name That File?? ")
                path=self.TakeCommand()
                pathname=path+".png"
                kk=pyautogui.screenshot()
                saved_path=f'C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\saved_screenshots\\{pathname}'
                kk.save(saved_path)
                Speak("Here's your Screenshot sir.")
                os.startfile(saved_path)

            elif 'bye' in self.query:
                Speak("Ok Sir, Bye")
                break

            elif not self.query.strip():
                pass

            elif 'open facebook' in self.query:
                OpenApps()

            elif 'open instagram' in self.query:
                OpenApps()

            elif 'open maps' in self.query:
                OpenApps()

            elif 'open code' in self.query:
                OpenApps()

            elif 'open telegram' in self.query:
                OpenApps()

            elif 'open edge' in self.query:
                OpenApps()
            
            elif 'open chrome' in self.query:
                OpenApps()

            elif 'open youtube' in self.query:
                OpenApps()

            elif 'close facebook' in self.query:
                CloseApps()

            elif 'close instagram' in self.query:
                CloseApps()
                
            elif 'close maps' in self.query:
                CloseApps()
                
            elif 'close code' in self.query:
                CloseApps()
                
            elif 'close telegram' in self.query:
                CloseApps()
                
            elif 'close edge' in self.query:
                CloseApps()
            
            elif 'close chrome' in self.query:
                CloseApps()
                
            elif 'close youtube' in self.query:
                CloseApps()

            elif 'restart' in self.query:
                keyboard.press('0')
            elif 'mute' in self.query:
                keyboard.press('m')
            elif 'skip' in self.query:
                keyboard.press('l')
            elif 'back' in self.query:
                keyboard.press('j')
            elif 'full screen' in self.query:
                keyboard.press('f')
            elif 'film mode' in self.query:
                keyboard.press('t')
            elif 'pause' in self.query:
                keyboard.press('k')
            elif 'speed up' in self.query:
                keyboard.press('>')
            elif 'speed down' in self.query:
                keyboard.press('<')
            elif 'search bar' in self.query:
                keyboard.press('/')
            elif 'youtube tools' in self.query:
                YoutubeAuto()
            
            elif 'close this tab' in self.query:
                keyboard.press_and_release('ctrl + w')
            elif 'open new tab' in self.query:
                keyboard.press_and_release('ctrl + t')
            elif 'open new window' in self.query:
                keyboard.press_and_release('ctrl + n')
            elif 'history' in self.query:
                keyboard.press_and_release('ctrl + h')
            elif 'incognito mode' in self.query:
                keyboard.press_and_release('ctrl + shift + n')
            elif 'scroll down' in self.query:
                keyboard.press_and_release('space bar')
            elif 'full screen' in self.query:
                keyboard.press_and_release('F11')
            elif 'chrome tools' in self.query:
                ChromeAuto()

            elif 'joke' in self.query:
                get = pyjokes.get_joke()
                Speak(get)
            
            elif 'repeat my words' in self.query:
                Speak("Speak Sir!")
                jj=self.TakeCommand()
                Speak(f"You Said: {jj}")

            elif 'dictionary' in self.query:
                # Enter in dictionary
                Dict()

            elif 'alarm' in self.query:
                Alarm(self.query)

            elif 'translate' in self.query:
                Tran()

            elif 'remember that' in self.query:
                rememberMsg = self.query.replace("remember that","")
                rememberMsg = rememberMsg.replace("robo","")
                Speak("You Tell Me to Remind You that: "+rememberMsg)
                remember = open("Data.txt",'w')
                remember.write(rememberMsg)
                remember.close()

            elif 'what do you remember' in self.query:
                remember = open("Data.txt","r").read()
                Speak("You tell me that "+ remember)

            elif 'google search' in self.query:
                import wikipedia as googleScrap
                self.query=self.query.replace("robo","")
                self.query=self.query.replace("google search","")
                self.query=self.query.replace("google","")
                Speak("This is what o found for your search! ")
                pywhatkit.search(self.query)
                try:
                    result=googleScrap.summary(self.query, 2)
                    Speak(result)
                except:
                    Speak("No speakable data available")

            elif "temperature" in self.query.lower():
                Temperature(self.query)

            elif "read book" in self.query.lower():
                Reader()
            
            elif "speed test" in self.query.lower():
                script_path = "C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\Gui_Program\\SpeedTestGui.py"
                subprocess.Popen(["python", script_path], shell=True)

            elif "how to" in self.query.lower():
                Speak("Getting Data From The Internet: ")
                op = self.query.replace("robo","")
                max_result=1
                howt_to_func = search_wikihow(op, max_result)
                assert len(howt_to_func) == 1
                howt_to_func[0].print()
                Speak(howt_to_func[0].summary)

            elif "wolfram" in self.query.lower():
                self.query=self.query.replace("robo","")
                self.query=self.query.replace("wolfram","")
                self.query=self.query.replace("search in","")
                result = WolfRam(self.query)
                if result:
                    Speak(result)

            elif "ai brain" in self.query.lower():
                Speak("Going to AI Brain")
                MainExecution()
                
            else:
                Speak("Sorry i can't do that. You can call ai brain for that")


startFunctions = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.robo_ui = Ui_RoboUI()
        self.robo_ui.setupUi(self)

        self.robo_ui.pushButton.clicked.connect(self.startFunc)
        self.robo_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.robo_ui.movies_2 = QtGui.QMovie(os.path.join(script_dir,"Iron_Template_1.gif"))
        self.robo_ui.label_2.setMovie(self.robo_ui.movies_2)
        self.robo_ui.movies_2.start()

        self.robo_ui.movies_3 = QtGui.QMovie(os.path.join(script_dir,"__1.gif"))
        self.robo_ui.label_3.setMovie(self.robo_ui.movies_3)
        self.robo_ui.movies_3.start()

        self.robo_ui.movies_4 = QtGui.QMovie(os.path.join(script_dir,"initial.gif"))
        self.robo_ui.label_4.setMovie(self.robo_ui.movies_4)
        self.robo_ui.movies_4.start()

        self.robo_ui.movies_5 = QtGui.QMovie(os.path.join(script_dir,"Health_Template.gif"))
        self.robo_ui.label_5.setMovie(self.robo_ui.movies_5)
        self.robo_ui.movies_5.start()

        self.robo_ui.movies_6 = QtGui.QMovie(os.path.join(script_dir,"B.G_Template_1.gif"))
        self.robo_ui.label_6.setMovie(self.robo_ui.movies_6)
        self.robo_ui.movies_6.start()

        startFunctions.start()

Gui_App = QApplication(sys.argv)
Gui_robo = Gui_Start()
Gui_robo.show()
sys.exit(Gui_App.exec_())