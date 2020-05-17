"""
This is the game of life creating by Ricky Mace, following the famous conway game

The game field will be a 100*100 grid
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
import random



n = 10  # number of rows and columns we want
a = np.array([[0]* n for i in range (n)])


def creation(board):
    for row in range(n):
        for column in range(n):
            board[row][column] = random.randrange(2)
    return board


Initial_Board = creation(a)


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
                if neighbours == 2 or 3:
                    new_board[row][column] = 1
                elif neighbours == 0 or 1:
                    new_board[row][column] = 0
                else:
                    new_board[row][column] = 0
        yield new_board

