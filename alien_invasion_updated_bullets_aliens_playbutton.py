import sys #sys module is used to exit the game when a player quits

import pygame #contains the functionality needed to make a game

from pygame.sprite import Group
from settings_updated import Settings
from ship_updated import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():

    # Initializes game and creates the screen object
    pygame.init()

    ai_settings=Settings()
    
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship=Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    # Make a group of aliens
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make the play button
    play_button = Button(ai_settings, screen, "Play")
    
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets) # Ship parameter goes to the func. which moves ship right

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, ship, aliens,
               bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)
        
run_game()
            
    
