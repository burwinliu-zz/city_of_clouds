import game_logic


def run_commands():
    """
    :return: None

    Runs the game in a UI version
    """
    game = game_logic.Game(10, 10, 9, 3)
    game.create_clear_board()
    while not game.get_game_over():
        command_two = input().rstrip()
        if command_two is "":
            game.update_lightning()
            game._print_game()
            continue
        if command_two[0] == 'L':
            game.set_lightning(command_two[2])
            game.update_cat_pos()
            game.update_lightning()
            continue
        if command_two == 'R':
            game.catch_lightning()
            continue
        if command_two == '<':
            game.move_left()
            game.update_cat_pos()
            continue
        if command_two == '>':
            game.move_right()
            game.update_cat_pos()
            continue
        if command_two == "Q":
            return
        else:
            print("INVALID INPUT PLEASE SPECIFY")
            pass


if __name__ == '__main__':
    run_commands()
