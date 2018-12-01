import game_logic


if __name__ == '__main__':
    cloud_game = game_logic.Game(10, 8, 6, 3)
    cloud_game.create_clear_board()
    cloud_game.update_game()
    print(cloud_game.get_state())