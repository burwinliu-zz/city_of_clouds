import pygame
import game_logic as gl

class Octocat:
    def __init__(self, screen):
        self.image = pygame.image.load('octocat.png')
        self.screen = screen
        game = gl.Game(10, 10, 7, 3)

        # get ship rectangle
        temp = game.get_cat_pos()
        self.rect = pygame.Rect((temp[1]/10, temp[0]/8),((200, 200)))
        self.screen_rect = screen.get_rect()


        # start octocat on clouds
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the cat's center
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