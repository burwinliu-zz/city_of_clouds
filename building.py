import pygame
from os.path import join, dirname


class Building:
    def __init__(self):
        script_dir = dirname(__file__)
        self.image1 = pygame.image.load(join(script_dir, 'image_files', 'building1.png'))
        self.image2 = pygame.image.load(join(script_dir, 'image_files', 'building2.png'))
        self.image3 = pygame.image.load(join(script_dir, 'image_files', 'building3.png'))
        self.image4 = pygame.image.load(join(script_dir, 'image_files', 'building4.png'))
        self.image_fire = pygame.image.load(join(script_dir, 'image_files', 'fire.png'))
        self._image = {1: self.image1,
                       2: self.image2,
                       3: self.image3,
                       4: self.image4}

    def get_dict(self):
        return self._image

    def get_fire(self):
        return self.image_fire
