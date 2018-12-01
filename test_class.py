import game_logic
import pygame
import sys
from octocat import Octocat
from lightning import Lightning


if __name__ == '__main__':
    cloud_game = game_logic.Game(10, 8, 6, 5)
    cloud_game.create_clear_board()
    cloud_game.update_game()
