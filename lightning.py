import pygame
from os.path import join, dirname

class Lightning:
    def __init__(self):
        script_dir = dirname(__file__)
        self.image = pygame.image.load(join(script_dir, 'image_files', 'lightning.png'))

    def get_lightning(self):
        return self.image


