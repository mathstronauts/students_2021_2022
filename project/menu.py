import pygame  # pygame library for graphics
import earth   # import functions from earth file
import mars    # import functions from mars file

# initialize pygame
pygame.init()

# screen setup
WIDTH = 800
HEIGHT = 600

# create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mars Earth Weather App")

# define some colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# load background images to pygame
bkgd_menu = pygame.image.load("project/images/bkgd_menu.png")  # update with Canva file name
bkgd_menuRect = bkgd_menu.get_rect()

# CREATE PAGES
def menu_display():
    # draw backgrounds
    screen.fill(BLACK)
    screen.blit(bkgd_menu, bkgd_menuRect)

# App Display Loop Conditions
running = True
menu_page = True

# APP DISPLAY Loop
while running:
    # process user input
    events = pygame.event.get()  # creates a list of events
    for event in events:
        # close app window
        if event.type == pygame.QUIT:
            running = False  # stop game and quit
        
        # detect mouse clicks
        mouse = pygame.mouse.get_pos()  # get mouse position (x, y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Earth Button
            if 0 <= mouse[0] <= 225 and 77 <= mouse[1] <= 523: # update with Canva coordinates
                print("EARTH WEATHER")
                menu_page = False
                # get Earth API Data
                earth.getWeather()
                # draw Earth weather page
                menu_page = earth.displayPage()

            # Mars Button
            elif 668 <= mouse[0] <= 800 and 169 <= mouse[1] <= 431:  # update with Canva coordinates
                print("MARS WEATHER")
                menu_page = False
                # get Mars API Data
                mars.getWeather()
                # draw Mars weather page
                menu_page = mars.displayPage()

    # draw the main menu
    if menu_page:
        menu_display()

    # update display
    pygame.display.flip()

# quite pygame screen when we exit the app Loop
pygame.quit()
