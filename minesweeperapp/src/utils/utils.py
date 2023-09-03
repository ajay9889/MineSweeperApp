import random
from constants.constant import *


class Utils:
    def __init__(self, num_mines, grid_size, grid):
        self.num_mines = num_mines
        self.mines = set()
        self.grid_size = grid_size
        # -1  because the first one always gets uncover first
        self.uncovercell = int(grid_size) * int(grid_size) - 1
        self.grid = grid
        self.game_over = False
        self.game_result = ""

    # this is static function I have created for the validating the enter number
    @staticmethod
    def check_user_input(enter_value):
        # checking the number of grid or validation to check the number of mines
        if enter_value:
            try:
                enter_value = int(enter_value)
            except ValueError:
                print(INPUT_ERROR)
                enter_value = None
        else:
            enter_value = None
        return enter_value

    # This function, generate the grid and randomly place the specified number of mines on the grid.

    def place_mine(self, row, col):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                self.grid[r][c] += 1

    def generate_mines(self):
        while len(self.mines) < self.num_mines:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            self.mines.add((row, col))

    # This function, will give the count of how many of its adjacent squares contain mines
    # it will look for there possible adjancent up to 8 times minimum 3

    def calculate_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.grid_size, row + 2)):
            for c in range(max(0, col - 1), min(self.grid_size, col + 2)):
                # all 8 valid adjancent
                if (r, c) in self.mines:
                    count += 1
        return count

    # If an uncovered square has no adjacent mines, the program should automatically uncover
    # all adjacent squares until it reaches squares that do have adjacent mines

    def reveal_cell(self, row, col):
        # print(row, col, "reveal_cell: ", self.mines)
        if (row, col) in self.mines:
            self.grid[row][col] = 'X'
            self.game_result = LOSE_MSG
            self.game_over = True
        else:
            # if self.grid[row][col] != ' ':
            #     return
            # stored opened cell into the grid matrix
            # num_adjacent_mines = self.calculate_adjacent_mines(
            #     row, col)
            num_adjacent_mines = self.grid[row][col]

            self.grid[row][col] = str(num_adjacent_mines)
            # when uncovecell matches to the number of mines for "The game is won when all non-mine squares have been uncovered"
            if(self.uncovercell == self.num_mines):
                self.game_over = True
                self.game_result = WON_MSG
                return
            # here we are checking number of remaining cell which is uncover in order match the number of mines to declare whether the user won or lose.
            self.uncovercell -= 1
            # num_adjacent_mines== 0 means there is no mines at that vertices for r, c in adjacent:
            if num_adjacent_mines == 0:
                for r in range(max(0, row - 1), min(self.grid_size, row + 2)):
                    for c in range(max(0, col - 1), min(self.grid_size, col + 2)):
                        # if the adjacent is ' ' that mean no mines there.. it will call recusrively call function reveal_cell for adjacent row and col
                        if self.grid[r][c] == ' ':
                            self.reveal_cell(r, c)
