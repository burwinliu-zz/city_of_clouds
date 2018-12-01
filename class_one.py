import game_logic


def run_commands():
    """
    :return: None

    Runs the game in a UI version
    """
    rows = int(input())
    column = int(input())
    game = game_logic.Game(column, rows, 6, 3)
    game.create_clear_board()
    command_one = input()
    if command_one == "EMPTY":
        pass
    while not game.get_game_over():
        command_two = input().rstrip()
        if command_two is "":
            game.update_game()
            continue
        if command_two[0] == 'L':
            game.set_lightning(command_two[2])
            game._print_game()
            continue
        if command_two == '<':
            game.move_left()
            game._print_game()
            continue
        if command_two == '>':
            game.move_right()
            game._print_game()
            continue
        if command_two == "Q":
            return
        else:
            print("INVALID INPUT PLEASE SPECIFY")
            pass


if __name__ == '__main__':
    run_commands()
