from History.pro4 import logic
import pygame


_FRAME_RATE = 30
_INITIAL_WIDTH = 600
_INITIAL_HEIGHT = 600
_BACKGROUND_COLOR = pygame.Color(255, 255, 255)
_PLAYER_COLOR = pygame.Color(0, 0, 128)


class ColumnsGame:
    def __init__(self):
        self._game = logic.Game(6, 13)
        self._game.create_clear_board()
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
        if keys[pygame.K_LEFT]

    def _draw_window(self):
        self._surface.fill(_BACKGROUND_COLOR)
        pygame.display.flip()

    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

    def _stop_program(self) -> None:
        self._running = False


if __name__ == '__main__':
    ColumnsGame().run_game()