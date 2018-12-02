import pygame
from pygame.sprite import Sprite


class Building:
    def __init__(self, screen):
        super(Building, self).__init__()
        self.screen = screen
        self.onFire = False
        self.image = pygame.image.load('building1.png')
        self.image2 = pygame.image.load('building2.png')
        self.image3 = pygame.image.load('building3.png')
        self.image4 = pygame.image.load('building4.png')
        self.fire_image = pygame.image.load('fire.png')
        self.rect = self.image.get_rect()

    def get_rect(self):
        return self.rect

    def set_on_fire(self):
        self.onFire = True
        self.screen.blit(self.fire_image, self.rect)

    def blitme(self): #TODO: Make random choice of images
        self.screen.blit(self.image, self.rect)

