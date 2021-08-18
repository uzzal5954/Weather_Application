  
# Weather API
import requests

def format_response(weather_data):
    try:
        city_name   = weather_data['name']
        country_name= weather_data['sys']['country'] # ***
        condition   = weather_data['weather'][0]['description']
        temperature = weather_data["main"]["temp"]
        icon_name   = weather_data["weather"][0]["icon"]

        weather_report = "City: %s \nCountry: %s \nCondition: %s \nTemperature(°F): %s" % (city_name, country_name, condition, temperature) # **
    except:
        weather_report = "server error 500"
        icon_name = ""
    return (weather_report, icon_name)

def weather_information(city_name):
    # get weather Information by calling openweather api
    weather_key = "e1b9e0b7aee9851b9984a26f3675878e"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q" : city_name, "units" : "imperial"}
    response = requests.get(url, params)
    weather_data = response.json()
    # print(weather_data)

    weather_report = format_response(weather_data)
    return weather_report
print("Wellcome To My Weather Application. This Application Designe and Developed By Uzzal Chandra Boissha.")
from os import terminal_size
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
from tkinter.constants import ANCHOR
from typing import Text
from weather_api import weather_information



"""
|---------------------------------------|
|__Weather app__________|____search_____|
|                                       |
|  Weather Data                         |
|                                       |
|                                       |
|                                       |
|                                       |
|_______________________________________|
"""
def open_weather_icon(icon):
    # set weather icon
    size = int(information_frame.winfo_height()*0.30)
    
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


def get_weather_info(city_name):
    # set weather  Information
    weather_report = weather_information(city_name)

    results["text"] = weather_report[0]
    weather_icon_name = weather_report[1]
    open_weather_icon(weather_icon_name)
    return None





# basic setting for app window
app = tk.Tk() # Create a Graphical Window
canvas = tk.Canvas(app, height=600, width=700) # set window height and width

canvas.pack()
app.resizable(False, False)
app.title("Weather App")

# set background image
background_image = tk.PhotoImage(file='background-image_000.png')
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

# set heading for the app
heading = tk.Label(app, text="Weather Information", font=("Righteous", 25, "bold"), bg="#000000", bd=5, fg="#ffffff", cursor=["heart"])
heading.place(relwidth=1)

frame = tk.Frame(app, bg="#313B3B", bd=5)
frame.place(x=100, y=80,relwidth=0.75, relheight=0.1)

# input text-Box
textbox = tk.Entry(frame, font=("Alegreya", 16, "bold"), fg="#000000", cursor=["plus"])
textbox.place(relwidth=0.65, relheight=1)

# submit button
submit_button = tk.Button(frame, text="Serch Weather", font=("Alegreya", 15, "bold"), fg="#000", cursor=["mouse"], command=lambda: get_weather_info(textbox.get()))
submit_button.place(x=360, relwidth=0.3, relheight=1)

# Information frame
information_frame = tk.Frame(app, bg="#313B3B", bd=6, cursor=["sizing"])
information_frame.place(x=100, y=200, relwidth=0.75, relheight=0.55)

results = tk.Label(information_frame, font=("Merienda", 14), anchor="nw", justify="left", bg="#fff", bd=4)
results.place(relwidth=1, relheight=1)

# canvas for weather icon
weather_icon = tk.Canvas(results, bg="#fff", bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

app.mainloop() # for show the window

