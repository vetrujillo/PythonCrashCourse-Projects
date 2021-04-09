import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviors"""

    def __init__(self):
        """Initialize game, create game resources"""
        #Initializes background seetings required by Pygame
        pygame.init()
        self.settings = Settings()

        #This object is called a surface, and is where the game element
        #will be displayed 
        #Each element in the game, like alien or ship, is its own surface
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                        self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        #Create instance of Ship after screen is created
        self.ship = Ship(self)

    def run_game(self):
        """Start main loop for game"""

        while True:
            #Watch for keyboard and mouse events
            #Event is an action the user performs while playing
            #Following function returns a list of events that occurred since
            #last time game was run. 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Fill method takes one argument, a color
            self.screen.fill(self.settings.bg_color)
            
            #After background is filled, ship is drawn by calling
            #blitme(), placing it on top of background
            self.ship.blitme()        
            
            #Make most recently drawn screen visible
            #Continually updates display to show new positions of elements
            pygame.display.flip()

if __name__ == '__main__':
    #Make game instance and run game
    ai = AlienInvasion()
    ai.run_game()