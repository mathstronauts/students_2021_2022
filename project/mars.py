import pygame  # pygame library for graphics
import mathstropy  # mathstropy library
import requests

# Mars Curiosity Rover REMS API URL
mars_URL = "https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json"

# Store weather data in a dictionary
mars_var = {}

#---------------------------------------
def getWeather():
    global mars_var
    print("no data")

#---------------------------------------
def displayPage():
    global mars_var
    print("no image")

    # display function returns True or False
    menu_page = True
    return menu_page