import pygame


class Lightning:
    def __init__(self, screen):
        self.screen = screen

        # load the lightning  image
        self.image = pygame.image.load('')

        # get the lightning rectangle
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

