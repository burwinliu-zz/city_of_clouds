import pygame
from pygame.sprite import Sprite

class Building(Sprite):
"""Will choose randomly between a set of building images, will have two modes - either fire or building"""

  def __init__(self, screen):
    super(Building, self).__init__()
    self.screen = screen
    self.onFire = False
    
    self.image = pygame.image.load('')
    self.image2 = pygame.image.load('')
    self.image3 = pygame.image.load('')
    self.image4 = pygame.image.load('')
    self.fire_image = pygame.image.load('')
    
    self.rect = self.image.get_rect()
   
  def set_on_fire(self):
    self.onFire = True
    self.screen.blit(self.fire_image, self.rect)
    
  def blitme(self): #TODO: Make random choice of images
    self.screen.blit(self.image, self.rect)
    
  
