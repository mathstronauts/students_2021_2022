import pygame  # pygame library for graphics
import mathstropy
import requests

# user input city location
textinput = mathstropy.TextInput(initial_string="Toronto", font_size=30)

# Weather API Data
weather_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "19375602113c10e69b03a7ecc71e655f"

# Store weather data in a dictionary
earth_var = {}

#---------------------------------------
def getWeather():
    global earth_var
    print("no data")

#---------------------------------------
def displayPage():
    global earth_var
    print("no image")
    
    # display function returns True or False
    menu_page = True
    return menu_page