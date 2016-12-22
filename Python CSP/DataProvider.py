import numpy as np
from random import randint


sudoku6x6 = np.matrix([[1, 5, 6, 3, 4, 2]
                          , [2, 4, 3, 1, 5, 6]
                          , [4, 1, 2, 5, 6, 3]
                          , [3, 6, 5, 2, 1, 4]
                          , [6, 3, 1, 4, 2, 5]
                          , [5, 2, 4, 6, 3, 1]])

sudoku9x9 = np.matrix([[3, 1, 6, 5, 7, 8, 4, 9, 2]
                          , [5, 2, 9, 1, 3, 4, 7, 6, 8]
                          , [4, 8, 7, 6, 2, 9, 5, 3, 1]
                          , [2, 6, 3, 4, 1, 5, 9, 8, 7]
                          , [9, 7, 4, 8, 6, 3, 1, 2, 5]
                          , [8, 5, 1, 7, 9, 2, 6, 4, 3]
                          , [1, 3, 8, 9, 4, 7, 2, 5, 6]
                          , [6, 9, 2, 3, 5, 1, 8, 7, 4]
                          , [7, 4, 5, 2, 8, 6, 3, 1, 9]])

sudoku9x9Normal = np.array([[0, 0, 0, 0, 0, 8, 4, 9, 2]
                               , [5, 2, 0, 1, 3, 4, 7, 6, 8]
                               , [4, 0, 0, 0, 0, 9, 5, 3, 1]
                               , [2, 0, 3, 4, 1, 0, 0, 8, 7]
                               , [0, 0, 4, 0, 0, 0, 1, 2, 5]
                               , [8, 5, 1, 7, 9, 2, 6, 4, 3]
                               , [0, 3, 0, 0, 4, 0, 2, 5, 6]
                               , [6, 9, 0, 0, 0, 0, 8, 7, 4]
                               , [7, 4, 5, 2, 8, 6, 0, 0, 0]])

sudoku9x9Hard = np.array([[4,0,0,0,0,0,8,0,5],
                          [0,3,0,0,0,0,0,0,0],
                          [0,0,0,7,0,0,0,0,0],
                          [0,2,0,0,0,0,0,6,0],
                          [0,0,0,0,8,0,4,0,0],
                          [0,0,0,0,1,0,0,0,0],
                          [0,0,0,6,0,3,0,7,0],
                          [5,0,0,2,0,0,0,0,0],
                          [1,0,4,0,0,0,0,0,0]])

sudoku16x16 = np.array([[8, 15, 11, 1,  6, 2, 10, 14 , 12, 7, 13, 3,  16, 9, 4, 5],
                        [10 ,6 ,3 ,16 ,12 ,5 ,8 ,4  ,14 ,15 ,1 ,9 ,2 ,11 ,7 ,13 ],
                        [14, 5, 9, 7, 11, 3, 15, 13, 8, 2, 16, 4, 12, 10, 1, 6],
                        [4 ,13 ,2 ,12 ,1 ,9 ,7 ,16 ,6 ,10 ,5 ,11 ,3 ,15 ,8 ,14 ],
                        [9, 2, 6, 15 , 14, 1, 11, 7,  3, 5, 10, 16,  4, 8, 13, 12],
                        [3, 16, 12, 8,  2, 4, 6, 9 , 11, 14, 7, 13,10, 1, 5, 15 ],
                        [11 ,10 ,5 ,13 ,8 ,12, 3 ,15, 1 ,9 ,4 ,2, 7 ,6 ,14 ,16 ],
                        [1, 4, 7, 14, 13, 10, 16, 5, 15, 6, 8, 12, 9, 2, 3, 11 ],
                        [13, 7 ,16 ,5,9 ,6 ,1 ,12, 2 ,8 ,3 ,10, 11 ,14 ,15, 4 ],
                        [2 ,12, 8, 11, 7, 16, 14, 3, 5, 4, 6, 15, 1, 13, 9, 10 ],
                        [6, 3 ,14 ,4,10, 15, 13, 8, 7, 11, 9 ,1, 5, 12 ,16, 2 ],
                        [15, 1, 10, 9 ,4, 11, 5 ,2, 13, 16, 12, 14, 8, 3, 6, 7 ],
                        [12 ,8 ,4 ,3 ,16 ,7 ,2 ,10, 9 ,13, 14,6,15, 5, 11, 1 ],
                        [5 ,11, 13, 2 ,3, 8, 4, 6, 10, 1, 15, 7, 14, 16, 12, 9 ],
                        [7 ,9 ,1 ,6,15, 14 ,12, 11,16, 3, 2, 5,13, 4, 10, 8 ],
                        [16 ,14, 15, 10, 5, 13, 9, 1, 4, 12, 11, 8, 6, 7, 2, 3 ]])

global lastGenerateGrid
lastGenerateGrid = []

def generateSudoku6x6(numberOfFields):
    grid = np.zeros(shape = (6,6), dtype=int)
    for iter in range(0,numberOfFields):
        row = randint(0,5)
        col = randint(0,5)
        while grid[row,col] != 0:
            row = randint(0,5)
            col = randint(0,5)
        grid[row, col] = sudoku6x6[row,col]
    return grid

def generateSudoku9x9(numberOfFields):
    grid = np.zeros(shape = (9,9), dtype=int)
    for iter in range(0,numberOfFields):
        row = randint(0,8)
        col = randint(0,8)
        while grid[row,col] != 0:
            row = randint(0,8)
            col = randint(0,8)
        grid[row, col] = sudoku9x9[row,col]
    return grid

def generateSudoku16x16(numberOfFields):
    grid = np.zeros(shape = (16,16), dtype=int)
    for iter in range(0,numberOfFields):
        row = randint(0,15)
        col = randint(0,15)
        while grid[row,col] != 0:
            row = randint(0,15)
            col = randint(0,15)
        grid[row, col] = sudoku16x16[row,col]
    return grid


def getNQueensGrid(N):
    return np.array(np.zeros(shape = (N,N), dtype=int))