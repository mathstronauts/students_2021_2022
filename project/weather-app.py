# import libraries
import pygame
import mathstropy
import requests

# Create our textbox
textinput = mathstropy.TextInput(initial_string="Toronto", font_size=30)

#------------------------------------------------------
# Weather API
URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "19375602113c10e69b03a7ecc71e655f"

# Get Weather Data

# Make API Request
# Response [200] is good!
# Response [401] something went wrong, check your parameters

#--------------------------------------------------------
# initialize pygame

#WIDTH = 
#HEIGHT =

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# initialize display text
text = mathstropy.TextDisplay(screen)

# define some colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Import the images
#background_file = "project/images/[file_name].png"
#background = pygame.image.load(background_file)
#backgroundRect = background.get_rect()

#----------------------------------------------------------------
# Call API data functions

#----------------------------------------------------------------
# App loop
running = True
while running:
    # detecting events

    #----------------------------------------
    # draw screen

    #-----------------------------------------
    # text.display(size, text, colour, x, y)

    #-----------------------------------------
    # draw textbox
    #textinput.update(events)
    #textbox = textinput.get_surface()
    #textboxRect = (25, 20) 
    #screen.blit(textbox, textboxRect)
    
    #------------------------------------------
    # update screen
    pygame.display.flip()

# close app window
pygame.quit()
