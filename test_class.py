import game_logic


if __name__ == '__main__':
    cloud_game = game_logic.Game(10, 10, 7, 2)
    cloud_game.create_clear_board()
    cloud_game.update_game()
    cloud_game.move_right()
    cloud_game.update_game()
