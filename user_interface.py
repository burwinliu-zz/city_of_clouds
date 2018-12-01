import pygame
import game_logic.py
from lightning import Lightning
from octocat import Octocat

_FRAME_RATE = 30
_INITIAL_WIDTH = 600
_INITIAL_HEIGHT = 600
_BACKGROUND_COLOR = pygame.Color(255, 255, 255)
_PLAYER_COLOR = pygame.Color(0, 0, 128)


class CloudGame:
    def __init__(self):
        cloud_game = game_logic.Game(10, 8, 6, 5)
        self._running = True
        self._surface = None

    def run_game(self):
        pygame.init()
        try:
            while self._running:
                self._create_surface((_INITIAL_WIDTH, _INITIAL_HEIGHT))
                self._draw_window()
                self._handle_events()
        finally:
            pygame.quit()

    # Left and right movement
    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            cloud_game.move_right()
        elif event.key == pygame.K_LEFT:
            cloud_game.move_left()
                  
    def _handle_events(self) -> None:
        for event in pygame.event.get():
            self._handle_event(event)
        self._handle_keys()

    def _handle_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._stop_program()
        elif event.type == pygame.VIDEORESIZE:
            self._create_surface(event.size)

    def _handle_keys(self):
        keys = pygame.key.get_pressed()

    def _draw_window(self):
        self._surface.fill(_BACKGROUND_COLOR)
        pygame.display.flip()

    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

    def _stop_program(self) -> None:
        self._running = False


if __name__ == '__main__':
    CloudGame().run_game()
