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


lol = creation(a)

print(lol)

