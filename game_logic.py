FALLING = 0
ON_FIRE = 1
EMPTY = 2
BUILDING = 3
CLOUD = 4
CAT = 5


class Game:
    def __init__(self, column: int, row: int, building: int, height: int)\
            -> None:
        """
        :param column: int
        :param row: int

        Initializes a game object
        """
        self._freeze_state = False
        self._game_over = False
        self._landed = False
        self._state = list()
        self._lighting = list()
        self._building_height = building
        self._column = column
        self._row = row
        self._height = height
        self._column_drop = 0
        self._glossary_of_states = {
                                    EMPTY: [' ', ' '],
                                    FALLING: ['[', ']'],
                                    ON_FIRE: ['|', '|'],
                                    CLOUD: ['*', '*']
                                    }

    def create_clear_board(self) -> None:
        """
        :return: None

        creates a game state for the self._state and self._game attributes
        """
        state = []
        i = 0
        while i < self._row:
            j = 0
            state.append([EMPTY])
            while j < self._column - 1:
                state[i].append(EMPTY)
                j += 1
            i += 1
        self._state = state

    def get_game_over(self) -> bool:
        """
        :return: self._game_over: boolean

        returns a boolean that represents the state of the game
        """
        return self._game_over

    def get_game(self) -> [[str]]:
        """
        :return: self._game: [[str]]

        returns list that represents game
        """
        result = list()
        for i in range(len(self._state)):
            result.append([])
            for element in self._state[i]:
                result[i].append(element)
        return result

    def get_independent_copies(self) -> [[[str]],[[int]]]:
        """
        :return: [game_copy, state_copy]

        creates a back up copy of the game and state states in an independent list
        """
        game_copy = list()
        state_copy = list()
        for row in range(self._row):
            game_copy.append([])
            state_copy.append([])
            for column in range(self._column):
                state_copy[row].append(self._state[row][column])
        return state_copy

    def get_state(self) -> [[int]]:
        """
        :return: self._state: [[int]]

        returns list that represents game state
        """
        result = list()
        for i in range(len(self._state)):
            result.append([])
            for element in self._state[i]:
                result[i].append(element)
        return result

    def get_formatted_game(self) -> [str]:
        """
        :return: the formatted game

        meant to retrieve data from method self._format_print_game()
        """
        return self._format_print_game()[0]

    def update_game(self) -> None:
        """
        :return: None

        Updates the game according to necessary requirements and fulfills all necessary steps to
        move the game forward according to everything that has been changed
        """
        self._check_fallers_and_landed()
        if self._game_over:
            print("GAME OVER")
            return
        to_change = self._detect_change()
        if self._has_bottom():
            if self._landed:
                for temp in to_change:
                    self._state[temp[0]][temp[1]] = FALLING
                self.print_game()
                if self._game_over:
                    print("GAME OVER")
                self._landed = False
                return
        for temp in to_change:
            self._game[temp[0] + 1][temp[1]] = temp[2]
            self._state[temp[0] + 1][temp[1]] = FALLING
        if self._test_bottom(0, self._column_drop):
            self.print_game()
            self._game_over = True
            print("GAME OVER")
            return
        self._state[0][self._column_drop] = FALLING
        self._board_fall()
        if not self._landed:
            self._check_bottom_and_set_to_landed()
        self.print_game()
        self._check_fallers_and_landed()

    def print_game(self) -> None:
        """
        :return: None

        prints out the games that are in self._game
        """
        formatted_str = self._format_print_game()[0]
        for i in formatted_str:
            print(i)
        counter_row = self._format_print_game()[1]
        counter_row = counter_row * 2
        under_print = " "
        under_print += '-' * counter_row
        under_print += ' '
        print(under_print)

    def _board_fall(self) -> None:
        """
        :return: None

        sets the boards item to falling
        """
        self._has_faller = True
        self._landed = False
        for row in range(self._row):
            for column in range(self._column):
                if self._state[row][column] != EMPTY:
                    self._state[row][column] = FALLING

    def _board_landed(self) -> None:
        """
        :return: None

        sets the board's item to landed
        """
        self._has_faller = False
        self._landed = True
        for row in range(self._row):
            for column in range(self._column):
                if self._state[row][column] != EMPTY:
                    self._state[row][column] = ON_FIRE

    def _test_bottom(self, target_row: int, column: int) -> bool:
        """
        :param target_row: int
        :param column: int
        :return: bool

        tests if at the targetrow and column if there is an item frozen with something
        other then a blank space
        """
        if target_row >= self._row:
            return True
        if self._state[target_row][column] == EMPTY:
            return True
        return False

    def _has_bottom(self) -> bool:
        """
        :return: bool

        check if it in the faller has a bottom underneath it
        """
        self._check_fallers_and_landed()
        if self._has_faller or self._landed:
            item = self._find_item(None)
        else:
            return False
        if len(item) != 0:
            interesting_item = item[-1]
            return self._test_bottom(interesting_item[0] + 1, interesting_item[1])

    def _format_element(self, column: int, row: int) -> str:
        """
        :param column: int
        :param row: int
        :return: str

        format the game into their proper string state, and returns that string state
        """
        beginning, end = self._glossary_of_states[self._state[row][column]]
        return beginning + end

    def _detect_change(self) -> [[int, int, str]]:
        """
        :return: [[int, int, str]]

        returns what is falling and their values in the self._game
        """
        row = 0
        to_change = []
        while row < self._row:
            column = 0
            while column < self._column:
                if self._state[row][column] == FALLING:
                    to_change.append([row, column, self._state[row][column]])
                column += 1
            row += 1
        return to_change

    def _format_print_game(self) -> [[[str]], int]:
        """
        :return: [[[str]], int]

        formats the game so that it may print out
        """
        state = self._state
        result = []
        counter_column = 0
        counter_row = 0
        while counter_column < len(state):
            result_temp = "|"
            counter_row = 0
            while counter_row < len(state[counter_column]):
                formatted_element = self._format_element(counter_row, counter_column)
                result_temp += formatted_element
                counter_row += 1
            result_temp += "|"
            result.append(result_temp)
            counter_column += 1
        return [result, counter_row]

    def _format_game_state(self, state: [[str]]) -> [[str]]:
        """
        :param state: [[str]]
        :return: [[str]]

        formats the game so the items move down to bottom
        """
        for iter_count in range(len(state)):
            for row in range(self._row - 1):
                for column in range(self._column):
                    if state[row][column] != ' ' and state[row + 1][column] == ' ':
                            state[row + 1][column] = state[row][column]
                            state[row][column] = ' '
        return state

    def _find_item(self, item_to_look_for: int or None) -> [[int, int, str]]:
        """
        :param item_to_look_for: int or None
        :return: [[int, int, str]]

        return a list with all items that are being searched for or those that are not frozen
        """
        result = list()
        for column in range(self._column):
            for row in range(self._row):
                if item_to_look_for is None:
                    if self._state[row][column] != EMPTY:
                        result.append([row, column, self._state[row][column]])
                        continue
                if self._state[row][column] == item_to_look_for:
                    result.append([row, column, self._state[row][column]])
        return result

    def _check_fallers_and_landed(self) -> None:
        """
        :return: None

        check if the items are falling or landed or matched or frozen and adjusts
        the states accordingly
        """
        for rows in self._state:
            for elements in rows:
                if elements == FALLING:
                    self._has_faller = True
                    self._landed = False
                    self._board_fall()
                    return
                elif elements == ON_FIRE:
                    self._landed = True
                    self._has_faller = False
                    self._board_landed()
                    return
        self._has_faller = False
        self._landed = False
        self._match = False

    def _check_bottom_and_set_to_landed(self):
        """
        :return: None

        makes sure that as they land they are set to frozen
        """
        item = self._find_item(FALLING)
        change_items = False
        for element in item:
            if element[0] + 1 == self._row:
                change_items = True
            elif self._state[element[0] + 1][element[1]] == EMPTY:
                change_items = True
        if change_items:
            self._landed = True
            self._has_faller = False
            for element in item:
                self._state[element[0]][element[1]] = ON_FIRE

