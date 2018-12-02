import pygame


_PLAYER_SPEED = 0.01


class Octocat:
    def __init__(self):
        self.image = pygame.image.load('octocat.png')
        # get ship rectangle
        top_left_x = 0.5 - .05 / 2
        top_left_y = 0.5 - .05 / 2
        self.top_left = (top_left_x, top_left_y)

    def declare_top_left(self, top_left_x, top_left_y):
        self.top_left = (top_left_x, top_left_y)

    def get_top_left(self) -> (float, float):
        return self._top_left

    def move_left(self) -> None:
        self._move(-_PLAYER_SPEED, 0)

    def move_right(self) -> None:
        self._move(_PLAYER_SPEED, 0)

    def _move(self, delta_x: float, delta_y: float) -> None:
        tl_x, tl_y = self._top_left
        new_x = tl_x + delta_x
        new_y = tl_y + delta_y
        half_width = self.width() / 2
        half_height = self.height() / 2
        if new_x + half_width < 0.0:
            new_x += 1.0
        elif new_x + half_width > 1.0:
            new_x -= 1.0
        if new_y + half_height < 0.0:
            new_y += 1.0
        elif new_y + half_height > 1.0:
            new_y -= 1.0
        self._top_left = (new_x, new_y)

    def blitme(self, screen, rect):
        """draws octocat at current location"""
        screen.blit(self.image, rect)
