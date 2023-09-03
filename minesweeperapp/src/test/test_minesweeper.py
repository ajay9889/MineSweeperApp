import unittest
from constants.constant import *
from minesweeper import MinesweeperGame
import pytest

# run the command on terminal using pytest
# using command "pytest "/MineSweeperApp/src/test/test_minesweeper.py"

@pytest.fixture
def game():
    game = MinesweeperGame(5, 5)
    game.utils.mines = FIXED_MIN_LOC_5
    return game


@pytest.fixture
def game_5x2():
    game = MinesweeperGame(5, 2)
    game.utils.mines = FIXED_MIN_LOC_2
    return game


def test_generate_mines(game):
    game.utils.generate_mines()
    assert (len(game.utils.mines) == 5)


def test_calculate_adjacent_mines(game):
    assert game.utils.calculate_adjacent_mines(1, 2) == 2
    assert game.utils.calculate_adjacent_mines(0, 0) == 1


def test_reveal_cell_mine(game):
    game.utils.reveal_cell(2, 2)
    assert (game.utils.game_over == False)
    assert (game.grid[2][2] == '2')


def test_reveal_cell(game):
    game.utils.reveal_cell(0, 0)
    assert (game.grid[0][0] == '1')
    assert(game.grid[1][1] == ' ')
    assert(game.grid[2][2] == ' ')


def test_reveal_cell_empty(game):
    game.utils.reveal_cell(0, 4)
    assert (game.grid[0][0] == ' ')
    assert(game.grid[1][1] == ' ')
    assert(game.grid[2][2] == ' ')


def test_reveal_cell_forwin(game_5x2):
    game = game_5x2
    list_node_to_reveal = [(0, 4), (0, 0), (0, 1), (0, 2), (1, 0)]
    for row, col in list_node_to_reveal:
        game.utils.reveal_cell(row, col)
    assert (game.utils.game_over == True)
    assert (game.utils.game_result == WON_MSG)
