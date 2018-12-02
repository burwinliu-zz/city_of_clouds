import pygame

class Octocat:
    def __init__(self, screen):
        self.image = pygame.image.load('Octocat.png')
        self.screen = screen

        # get ship rectangle
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect

        # start octocat on clouds
        self.rect.centerx = 4

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # movement flags
        self.move_right = False
        self.move_left = False
    def moving_right(self):
        self.move_right = True

    def moving_left(self):
        self.move_left = True

    def update(self):
        self.rect.centerx = self.center

    def blitme(self):
        """draws octocat at current location"""
        self.screen.blit(self.image, self.rect)