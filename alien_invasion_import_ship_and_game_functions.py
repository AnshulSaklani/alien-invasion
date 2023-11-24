import sys #sys module is used to exit the game when a player quits

import pygame #contains the functionality needed to make a game

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    #initializes game and creates the screen object
    pygame.init()

    ai_settings=Settings()
    
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship=Ship(screen)
    
    #Start the main loop for the game
    while True:
        gf.check_events(ship)#ship parameter goes to the func. which moves ship right
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()
            
    
