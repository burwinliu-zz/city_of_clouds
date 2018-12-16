import pygame
import game_logic as gl
from lightning import Lightning
import octocat as oc
import building as b

_FRAME_RATE = 30
_INITIAL_WIDTH = 600
_INITIAL_HEIGHT = 600
_BACKGROUND_COLOR = pygame.Color(255, 255, 255)
_PLAYER_COLOR = pygame.Color(0, 0, 128)


class CloudGame:
    def __init__(self):
        self._cloud_game = gl.Game(10, 10, 6, 5)
        self.game_size = 10
        self.screen_width = _INITIAL_WIDTH
        self.screen_height = _INITIAL_HEIGHT
        self.game_size = 10
        self._running = True
        self._surface = None

    def run_game(self):
        pygame.init()
        try:
            while self._running:
                self._create_surface((_INITIAL_WIDTH, _INITIAL_HEIGHT))
                self._handle_events()
                self._draw_frame()
        finally:
            pygame.quit()

    # Left and right movement
    def check_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self._cloud_game.move_right()
        elif event.key == pygame.K_LEFT:
            self._cloud_game.move_left()
                  
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
        if keys[pygame.K_RIGHT]:
            self._cloud_game.move_right()
            oc.moving_right()
        if keys[pygame.K_LEFT]:
            self._cloud_game.move_left()
            oc.moving_left()
        if keys[pygame.K_SPACE]:
            self._cloud_game.catch_lightning()

    def _draw_window(self):
        self._surface.fill(_BACKGROUND_COLOR)
        pygame.display.flip()

    def _draw_frame(self) -> None:
        self._surface.fill(_BACKGROUND_COLOR)
        self._draw_player()
        pygame.display.flip()

    def _draw_player(self):
        player_rect = pygame.Rect(300, 300, .025, .025)
        pygame.draw.rect(self._surface, _PLAYER_COLOR, player_rect)
        pass

    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

    def _stop_program(self) -> None:
        self._running = False


if __name__ == '__main__':
    CloudGame().run_game()