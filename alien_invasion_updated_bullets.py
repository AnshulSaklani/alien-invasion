import sys #sys module is used to exit the game when a player quits

import pygame #contains the functionality needed to make a game

from pygame.sprite import Group
from settings_updated import Settings
from ship_updated import Ship
from alien import Alien
import game_functions as gf

def run_game():

    #Initializes game and creates the screen object
    pygame.init()

    ai_settings=Settings()
    
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship=Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Make an alien
    alien = Alien(ai_settings, screen)
    
    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)#ship parameter goes to the func. which moves ship right
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()
            
    
