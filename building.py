import pygame
from pygame.sprite import Sprite

class Building(Sprite):
"""Will choose randomly between a set of building images, will have"""

    def __init__(self, screen):
      super(Building, self).__init__()
      self.screen = screen
      self.onFire = False
   
    def set_on_fire(self):
      self.onFire = True


    def blitme(self):
        """draws octocat at current location"""
        self.screen.blit(self.image, self.rect)