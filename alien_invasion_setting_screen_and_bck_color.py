import sys #sys module is used to exit the game when a player quits

import pygame #contains the functionality needed to make a game

def run_game():

    #initializes game and creates the screen object
    pygame.init()
    
    screen=pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Alien Invasion")

    #set the background colour
    bg_color=(230,230,230) #rgb values

        #Start the main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
              sys.exit()

        #redraw the screen during each pass through the loop
        screen.fill(bg_color)
        
        #makes the most recently drawn screen visible
        pygame.display.flip()

run_game()
            
    
