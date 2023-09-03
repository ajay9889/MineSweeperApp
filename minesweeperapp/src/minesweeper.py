import random
from constants.constant import *
from utils.utils import Utils


class MinesweeperGame:
    def __init__(self, grid_size, num_mines):
        self.grid_size = grid_size
        self.num_mines = num_mines
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.utils = Utils(num_mines, self.grid_size, self.grid)

    # display grid on console
    def display_grid(self):
        print("   " + " ".join(str(i) for i in range(1, self.grid_size + 1)))
        for i, row in enumerate(self.grid):
            print(chr(65 + i) + "  " + " ".join(cell for cell in row))
        print()

    def play(self):
        # firstly placed on the grid random mines
        self.utils.generate_mines()

        # game_over is boolean which manage the end results for Game Over or You Won!.
        while not self.utils.game_over:
            self.display_grid()
            choice = input(SELECT_CELL).strip().upper()
            if len(choice) != 2:
                print(INVALID_ENTRY)
                continue
            # Getting the row index of from Alphabet input and and column from the enter substring.
            row, col = ord(choice[0]) - 65, int(choice[1]) - 1
            if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
                print(ERROR_MESSAGE)
                continue
            self.utils.reveal_cell(row, col)

        # Draw final uncovered Grid to visualise next cell to uncover
        self.display_grid()
        print(self.utils.game_result)


if __name__ == "__main__":

    # The game should begin by prompting the user for the grid size and the number of mines to be randomly placed on the grid.

    # check the input numbers
    grid_size = Utils.check_user_input(input(NUM_GRID))
    while(grid_size is None):
        grid_size = Utils.check_user_input(input(NUM_GRID))

    # start prompting for number of Mines
    num_mines = Utils.check_user_input(input(NUM_MINES))
    # checking the number of grid or  validation to check the number of mines
    while((num_mines is None) or (num_mines > grid_size*grid_size)):
        num_mines = Utils.check_user_input(input(NUM_MINES))

    # initialize MinesweeperGame object to start play
    game = MinesweeperGame(int(grid_size), int(num_mines))

    # init minesweeper game to start play
    game.play()
