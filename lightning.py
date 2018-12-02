import pygame
import random

class Lightning:
    def __init__(self, screen):
        self.screen = screen

        #load the lightning  image
        self.image = pygame.image.load('city_of_clouds/bolt-clipart-transparent-background-6.png')

        #get the lightning rectangle
        self.lightning = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #randomizes x position of

        #creates lightning and sets to correct position
        self.lightning.bottom = 0
        self.lightning.centerx = random.randint(0, 600)

    def update(self):
        """updates position of lightning"""
        self.lightning.y += 1

    def blitme(self):
        """draws the lightning on the screen"""
        self.screen.blit(self.image, self.lightning)


