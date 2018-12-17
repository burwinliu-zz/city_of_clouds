import pygame
import game_logic as gl
import octocat, building, lightning
import random

_FRAME_RATE = 30
_INITIAL_WIDTH = 600
_INITIAL_HEIGHT = 600
_BACKGROUND_COLOR = pygame.Color(255, 255, 255)
_PLAYER_COLOR = pygame.Color(0, 0, 128)


class CloudGame:
    def __init__(self):
        self._cloud_game = gl.Game(10, 10, 9, 5)
        self.screen_width = _INITIAL_WIDTH
        self.screen_height = _INITIAL_HEIGHT
        self._block_width = _INITIAL_WIDTH/10
        self._block_height = _INITIAL_HEIGHT/10
        self._game_size = 10
        self._running = True
        self._surface = None
        self._cat = octocat.Octocat()
        self._lightning = lightning.Lightning()
        self._building = building.Building()
        self._building_images = list()
        self.setup_building()
        self._block_dictionary = {gl.LIGHTNING: self._lightning.get_lightning(),
                                  gl.ON_FIRE: self._building.get_fire(),
                                  gl.EMPTY: None,
                                  gl.BUILDING: self._building.get_dict(),
                                  gl.CLOUD: self._cat.get_cloud(),
                                  gl.CAT: self._cat.get_cat(),
                                  gl.ELECTROCUTED_CAT: self._cat.get_electrocuted_cat()}
    def setup_building(self):
        i = 0
        while i < self._game_size:
            rand_int = random.randint(1, 4)
            self._building_images.append(rand_int)
            i += 1
        print(self._building_images)

    def run_game(self):
        pygame.init()
        try:
            clock = pygame.time.Clock()
            while self._running:
                clock.tick(_FRAME_RATE)
                self._create_surface((_INITIAL_WIDTH, _INITIAL_HEIGHT))
                self._handle_events()
                self._draw_window()
        finally:
            pygame.quit()

    # Left and right movement
    def check_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self._cloud_game.move_right()
        elif event.key == pygame.K_LEFT:
            self._cloud_game.move_left()
        if event.key == pygame.K_SPACE:
            self._cloud_game.catch_lightning()
                  
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
            print(self._cloud_game.get_cat_pos())
            self._cloud_game.move_right()
        if keys[pygame.K_LEFT]:
            self._cloud_game.move_left()
        if keys[pygame.K_SPACE]:
            self._cloud_game.catch_lightning()

    def _draw_window(self):
        self._surface.fill(_BACKGROUND_COLOR)
        self._draw_board()
        pygame.display.flip()

    def _draw_board(self):
        for row in range(self._game_size):
            for column in range(self._game_size):
                rect = self._draw_rect(row, column)
                game_block = self._cloud_game.get_game()[row][column]
                self._draw_block(rect, game_block, row)

    def _draw_rect(self, x: int, y: int):
        return pygame.Rect(y * self._block_width, x * self._block_height,
                           self._block_width, self._block_height)

    def _draw_block(self, rect: pygame.Rect, game_block: int, row_number):
        if game_block == gl.BUILDING:
            key = self._building_images[row_number]
            image = self._block_dictionary[game_block][key]
        elif game_block == gl.EMPTY:
            return
        else:
            image = self._block_dictionary[game_block]
        self._surface.blit(image, rect)


    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

    def _stop_program(self) -> None:
        self._running = False


if __name__ == '__main__':
    CloudGame().run_game()