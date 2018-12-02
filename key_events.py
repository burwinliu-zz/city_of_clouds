import pygame
import octocat as oc
import game_logic as gl
import user_interface as ui
screen = pygame.display.set_mode((600,600))
game = gl.Game(10, 8, 6, 3)
cat = oc.Octocat(screen)

def check_keydown_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gl.move_right()
                oc.moving_right()
            if event.key == pygame.K_LEFT:
                gl.move_left()
                oc.moving_left()
            if event.key == pygame.K_SPACE:
                 gl.catch_lightning()
