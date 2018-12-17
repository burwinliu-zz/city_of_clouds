import pygame
from os.path import join


class Building:
    def __init__(self, screen):
        super(Building, self).__init__()
        self.screen = screen
        self.onFire = False
        self.image1 = pygame.image.load('building1.png')
        self.image2 = pygame.image.load('building2.png')
        self.image3 = pygame.image.load('building3.png')
        self.image4 = pygame.image.load('building4.png')
        self._image = {1: self.image1,
                       2: self.image2,
                       3: self.image3,
                       4: self.image4}

    def get_rect(self, number: int):
        return self._image[number]

