"""
This is the game of life creating by Ricky Mace, following the famous conway game

The game field will be a 100*100 grid
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
import random



columns = 10
rows = 10
Board_Base = np.array([[0] * columns for i in range(rows)])


def creation(board):
    for row in range(rows):
        for column in range(columns):
            board[row][column] = random.randrange(2)
    return board


Initial_Board = creation(Board_Base)


def cell_state(board):
    while True:
        new_board = []
        for row in range(n):
            for column in range(n):
                neighbours = 0
                neighbours += board[row - 1][column + 1]
                neighbours += board[row][column + 1]
                neighbours += board[row + 1][column + 1]
                neighbours += board[row - 1][column]
                neighbours += board[row + 1][column]
                neighbours += board[row - 1][column - 1]
                neighbours += board[row][column - 1]
                neighbours += board[row + 1][column - 1]
                if neighbours == 2 or 3:                      # Normal :If 2 or 3 neighbours changes state to alive: 1
                    new_board[row][column] = 1
                elif neighbours == 0 or 1:                    # Underpopulation: If 0 or 1 neighbours changes state to dead: 0
                    new_board[row][column] = 0
                else:                                         # Overpopulation : change state to dead: 0
                    new_board[row][column] = 0
        yield new_board


cell_state(Initial_Board)




