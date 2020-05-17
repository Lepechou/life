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


def next_state(board):
    new_board = np.array([[0] * columns for i in range(rows)])
    for row in range(rows -1):
        if (row - 1) < 0 or (row + 1) > rows:
            continue
        for column in range(columns - 1):
            neighbours = 0
            if (column - 1) < 0 or (column + 1) > columns:
                continue
            else:
                neighbours += board[row - 1][column + 1]
                neighbours += board[row][column + 1]
                neighbours += board[row + 1][column + 1]
                neighbours += board[row - 1][column]
                neighbours += board[row + 1][column]
                neighbours += board[row - 1][column - 1]
                neighbours += board[row][column - 1]
                neighbours += board[row + 1][column - 1]
                if neighbours == 2 :  # Normal :If 2 or 3 neighbours changes state to alive: 1
                    new_board[row][column] = 1
                elif neighbours == 0 :  # Underpopulation: If 0 or 1 neighbours changes state to dead: 0
                    new_board[row][column] = 0
                elif neighbours > 4:  # Overpopulation : change state to dead: 0
                    new_board[row][column] = 0
    return new_board


next_state(Initial_Board)




