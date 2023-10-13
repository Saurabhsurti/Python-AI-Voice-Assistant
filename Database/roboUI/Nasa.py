import requests
import cartopy.crs as ccrs 
import matplotlib.pyplot as plt
from PIL import Image
import random
import matplotlib
import pyttsx3
import webbrowser
from geopy.geocoders import Nominatim
import geocoder
from geopy.distance import great_circle
import os
from dotenv import load_dotenv

load_dotenv()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[2].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

Api_Key = os.getenv('Api_Key')

def NasaNews(Date):

    Speak("Extracting Data From Nasa . ")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']
    print("Image URL:", Image_Url)

    Image_r = requests.get(Image_Url)
    # print(Image_r)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\" + str(FileName)

    Path_2 = "C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\NasaDatabase\\" + str(FileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info[:150]}")

# NasaNews("2023-03-10") 
# 9, 2

def MarsImage():

    name = 'curiosity' 

    date = '2020-12-3'

    Api_ = str(Api_Key)

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"

    r = requests.get(url)

    Data = r.json()

    Photos = Data['photos'][:5]

    try:

        for index , photo in enumerate(Photos):

            camera = photo['camera']

            rover = photo['rover']

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img,'wb') as file:
                file.write(p.content)

            Path_1 = "C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\" + str(img)

            Path_2 = "C:\\Users\\saura\\OneDrive\\Documents\\Python-p\\Database\\NasaDatabase\\MarsImage\\" + str(img)

            os.rename(Path_1,Path_2)

            os.startfile(Path_2)

            Speak(f"This Image Was Captured With : {full_camera_name}")

            Speak(f"This Image Was Captured On : {date_of_photo}")

    except Exception as e:
        Speak("Sorry image not available at this time")
        

# MarsImage()


def Astro(start_date,end_date):

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"

    r = requests.get(url)

    Data = r.json()

    Total_Astro = Data['element_count']

    neo = Data['near_earth_objects']

    Speak(f"Total Astroid Between {start_date} and {end_date} Is : {Total_Astro}")

    Speak("Extact Data For Those Astroids Are Listed Below .")

    for body in neo[start_date]:

        id = body['id']

        name = body['name']

        absolute = body['absolute_magnitude_h']

        print(id,name,absolute)

# Astro('2022-09-01','2022-09-02')

def SolarBodies(body):
    url="https://api.le-systeme-solaire.net/rest/bodies/"
    r=requests.get(url)
    Data = r.json()
    bodies = Data['bodies']
    Number = len(bodies)
    for bodyyy in bodies:
        print(bodyyy['id'],end=', ')

    url_2=f"https://api.le-systeme-solaire.net/rest/bodies/{body}"
    rrr=requests.get(url_2)
    data_2=rrr.json()
    mass=data_2['mass']['massValue']
    volume=data_2['vol']['volValue']
    density=data_2['density']
    gravity=data_2['gravity']
    escape=data_2['escape']
    Speak(f"Number of bodies in Solar System are: {Number}")
    Speak(f"Mass of {body} is: {mass} kg")
    Speak(f"Volume of {body} is: {volume}")
    Speak(f"Density of {body} is: {density}")
    Speak(f"Gravity of {body} is: {gravity}")
    Speak(f"Escape Velocity of of {body} is: {escape} metres per second")
# SolarBodies("mars")
