import pygame

class Octocat:
    def __init__(self, screen):
        self.image = pygame.image.load('')
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

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 1
        if self.move_left and self.rect.left > 0:
            self.center -= 1

        # update rect object
        self.rect.centerx = self.center

    def blitme(self):
        """draws octocat at current location"""
        self.screen.blit(self.image, self.rect)