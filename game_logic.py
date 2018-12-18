LIGHTNING = 0
ON_FIRE = 1
EMPTY = 2
BUILDING = 3
CLOUD = 4
CAT = 5
ELECTROCUTED_CAT = 6


class Game:
    def __init__(self, column: int, row: int, building: int, height: int)\
            -> None:
        """
        :param column: int
        :param row: int

        Initializes a game object
        """
        self._game_over = False
        self._first_time = False
        self._state = list()
        self._lightning = list()
        self._fire = list()
        self._times_fire_happened = 0
        self._cat_pos = [height, 0]
        self._building_height = building
        self._column = column
        self._row = row
        self._height = height
        self._glossary_of_states = {
                                    EMPTY: [' ', ' '],
                                    LIGHTNING: ['/', '/'],
                                    ON_FIRE: ['|', '|'],
                                    CLOUD: ['*', '*'],
                                    BUILDING: ['~', '~'],
                                    CAT: ['`', '`'],
                                    ELECTROCUTED_CAT: ['\\', '\\']
                                    }
        self.create_clear_board()

    def create_clear_board(self) -> None:
        """
        :return: None

        creates a game state for the self._state and self._game attributes
        """
        state = []
        i = 0
        while i < self._row:
            j = 0
            state.append([])
            while j < self._column:
                if i >= self._building_height:
                    state[i].append(BUILDING)
                    j += 1
                    continue
                if self._height + 1 == i:
                    state[i].append(CLOUD)
                    j += 1
                    continue
                state[i].append(EMPTY)
                j += 1
            i += 1
        self._state = state
        self.update_cat_pos()

    def get_cat_pos(self):
        return self._cat_pos

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
        print(falling_pos)
        for element in self._lightning:
            if element[1] == falling_pos:
                return
        self._lightning.append([0, int(falling_pos)])
        self.update_lightning()

    def search(self, parameter: int):
        result = list()
        for row in range(self._row):
            for column in range(self._column):
                if self._state[row][column] == parameter:
                    result.append([row, column])
        return result

    def move_left(self):
        self._cat_pos[1] -= 1
        if self._cat_pos[1] < 0:
            self._cat_pos[1] += 1
        self.update_cat_pos()

    def move_right(self):
        self._cat_pos[1] += 1
        if self._cat_pos[1] >= self._column:
            self._cat_pos[1] -= 1
        self.update_cat_pos()

    def catch_lightning(self):
        electrocuted = self.search(ELECTROCUTED_CAT)
        if len(electrocuted) == 1:
            try:
                self._lightning.remove(electrocuted[0])
                self._remove_lightning(electrocuted[0])
            except ValueError:
                return

    def update_cat_pos(self):
        if self._state[self._cat_pos[0]][self._cat_pos[1]] != CAT:
            todo = self.search(CAT)
            for pos in todo:
                self._state[pos[0]][pos[1]] = EMPTY
            todo = self.search(ELECTROCUTED_CAT)
            for pos in todo:
                self._state[pos[0]][pos[1]] = EMPTY
        self._state[self._cat_pos[0]][self._cat_pos[1]] = CAT

    def update_lightning(self):
        added_fire = False
        for element in self._lightning:
            self._remove_lightning(element)
            if element[1] < 0:
                self._lightning.remove(element)
                continue
            if self._state[element[0]][element[1]] == ON_FIRE:
                continue
            if self._state[element[0]][element[1]] == BUILDING:
                if added_fire is False:
                    self._times_fire_happened += 1
                    added_fire = True
                items = self.search(BUILDING)
                for item in items:
                    if item[1] == element[1]:
                        self._state[item[0]][item[1]] = ON_FIRE
                self._fire.append(element[1])
                self._lightning.remove(element)
                self._remove_lightning(element)
                self._first_time = True
                continue
            element[0] += 1
            if element[1] < 0 or element[0] >= self._row:
                continue
            for row in range(element[0]):
                self._state[row][element[1]] = LIGHTNING
        if self._cat_pos in self._lightning:
            self._state[element[0]][element[1]] = ELECTROCUTED_CAT

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

    def _remove_lightning(self, element: [int, int]):
        for row in range(element[0]):
            if self._cat_pos[0] == row and element[1] == self._cat_pos[1]:
                self._state[self._cat_pos[0]][self._cat_pos[1]] = CAT
                continue
            if row >= self._building_height:
                self._state[row][element[1]] = BUILDING
                continue
            if self._height + 1 == row:
                self._state[row][element[1]] = CLOUD
                continue
            self._state[row][element[1]] = EMPTY

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
