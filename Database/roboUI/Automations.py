from datetime import datetime
from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import pyttsx3
import webbrowser
import speech_recognition as sr
import webbrowser as web
from notifypy import Notify

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def WhatsappMsg(name,message):
    webbrowser.open("https://web.whatsapp.com")

    sleep(10)

    # click(x=195, y=115)
    click(x=147, y=250)

    sleep(1)

    write(name)

    sleep(1)

    click(x=270, y=410)

    sleep(1)

    click(x=877, y=954)

    sleep(1)

    write(message)

    press('enter')

def WhatsappChat(name):

    webbrowser.open("https://web.whatsapp.com")

    sleep(10)

    click(x=147, y=250)

    sleep(1)

    write(name)

    sleep(1)

    click(x=270, y=410)

    sleep(1)

    click(x=877, y=954)

    sleep(1)
# WhatsappChat("Devesh")
