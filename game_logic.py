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
        self._game_over = False
        self._state = list()
        self._lighting = list()
        self._cat_pos = [0, 0]
        self._building_height = building
        self._column = column
        self._row = row
        self._height = height
        self._column_drop = 0
        self._glossary_of_states = {
                                    EMPTY: [' ', ' '],
                                    FALLING: ['[', ']'],
                                    ON_FIRE: ['|', '|'],
                                    CLOUD: ['*', '*'],
                                    BUILDING: ['~', '~'],
                                    CAT: ['`', '`']
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

    def set_lightning(self, falling_pos: int):
        for element in self._lighting:
            if element[1] == falling_pos:
                return
        self._lighting.append([0, falling_pos])

    def search(self, parameter: int):
        result = list()
        for row in range(self._row):
            for column in range(self._column):
                if self._state[row][column] == parameter:
                    result.append([row, column])
        return result

    def move_left(self):
        self._cat_pos[1] -= 1

    def move_right(self):
        self._cat_pos[1] += 1

    def catch_lightning(self):
        pass

    def update_game(self) -> None:
        """
        :return: None

        Updates the game according to necessary requirements and fulfills all necessary steps to
        move the game forward according to everything that has been changed
        """
        self._update_cat_pos()
        self._update_lightning()
        self._update_building()
        self._print_game()

    def _update_cat_pos(self):
        if self._state[self._cat_pos[0]][self._cat_pos[1]] != CAT:
            todo = self.search(CAT)
            for pos in todo:
                self._state[pos[0]][pos[1]] = EMPTY
        self._state[self._cat_pos[0]][self._cat_pos[1]] = CAT

    def _update_lightning(self):
        pass

    def _update_building(self):
        pass

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

    def _format_element(self, column: int, row: int) -> str:
        """
        :param column: int
        :param row: int
        :return: str

        format the game into their proper string state, and returns that string state
        """
        beginning, end = self._glossary_of_states[self._state[row][column]]
        return beginning + str(self._state[row][column]) + end

    def _print_game(self) -> None:
        """
        :return: None

        prints out the games that are in self._game
        """
        formatted_str = self._format_print_game()[0]
        for i in formatted_str:
            print(i)
        counter_row = self._format_print_game()[1]
        counter_row = counter_row * 3
        under_print = " "
        under_print += '-' * counter_row
        under_print += ' '
        print(under_print)
