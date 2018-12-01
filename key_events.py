import pygame
import octocat as oc
import game_logic as gl

game = gl.Game(10, 8, 6, 3)

def check_keydown_events():
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gl.move_right()
            if event.key == pygame.K_LEFT:
                gl.move_left()
            if event.key == pygame.K_SPACE:
                 gl.catch_lightning()
