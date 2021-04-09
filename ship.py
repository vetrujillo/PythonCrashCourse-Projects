import pygame

class Ship():
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize ship and set starting position"""
        #Assign screen as attr of Ship
        self.screen = ai_game.screen
        #Access screen rect attr and assign it to variable
        self.screen_rect = ai_game.screen.get_rect()
        #Load ship and get its rect
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        #Start each ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    #Draws image to screen at position specified by self.rect
    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)