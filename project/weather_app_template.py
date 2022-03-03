# import libraries
import pygame
from mathstropy import *

# Create our textbox
# textinput = TextInput(initial_string="", font_size=)

#------------------------------------------------------
# API Data
# Geocoding API
# "http://api.openweathermap.org/geo/1.0/direct?"

# Weather API
# "https://api.openweathermap.org/data/2.5/onecall?"

# API Key
# "bc93af7ec21317a25fa7d755f7391e39"

# Make API Request
# Response [200] is good!
# Response [401] something went wrong, check your parameters

#--------------------------------------------------------
# initialize pygame

# Define WIDTH and HEIGHT

# screen = pygame.display.set_mode(([x,y]))

# define some colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Import the images
# background_file = "app_development/images/[file_name].png"
# background = pygame.image.load([file_here])
# backgroundRect = background.get_rect([rect=(x,y)])

# function to display text on screen
def display_text(size, text, colour, x, y):
   font = pygame.font.Font('freesansbold.ttf', size)  # specify the font and size
   textSurf = font.render(text, True, colour)    # create a surface for the text object
   textRect = textSurf.get_rect()  # get rect position of text on the screen
   textRect.topleft = (x, y)  # specify rect position of text on screen
   screen.blit(textSurf, textRect)  # show the text on the screen

#----------------------------------------------------------------
# App loop
running = True
while running:
    # detecting events

    #----------------------------------------
    # draw screen

    #-----------------------------------------
    # display_text(size, text, colour, x, y)

    #-----------------------------------------
    # draw textbox
    # textinput.update(events)
    # textbox = textinput.get_surface()
    # textboxRect = (25, 20) 
    # screen.blit([image, rect])
    
    #------------------------------------------
    # update screen
    pygame.display.flip()

# close app window
pygame.quit()
