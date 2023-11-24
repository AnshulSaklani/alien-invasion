import sys #sys module is used to exit the game when a player quits

import pygame #contains the functionality needed to make a game

from settings import Settings

def run_game():

    #initializes game and creates the screen object
    pygame.init()

    ai_settings=Settings()
    
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

        #Start the main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
              sys.exit()

        #redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        
        #makes the most recently drawn screen visible
        pygame.display.flip()

run_game()
            
    
