import pygame
from os.path import join, dirname

_PLAYER_SPEED = 0.01


class Octocat:
    def __init__(self):
        script_dir = dirname(__file__)
        self.image = pygame.image.load(join(script_dir, 'image_files', 'octocat.png'))
        self.image2 = pygame.image.load(join(script_dir, 'image_files', 'electrocuted_cat.png'))
        self.image_cloud = pygame.image.load(join(script_dir, 'image_files', 'cloud.png'))

    def get_cat(self):
        return self.image

    def get_electrocuted_cat(self):
        return self.image2

    def get_cloud(self):
        return self.image_cloud
