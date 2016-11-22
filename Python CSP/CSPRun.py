import DataProvider
import SudokuSolver
import NQueensSolver
import time
import csv

import numpy as np


def runTestsNQueens(N):
    timeResults = []
    for n in range(8,N):
        start = time.time()
        solved = NQueensSolver.solveNQueensForwardChecking(DataProvider.getNQueensGrid(n), 0)
        end = time.time()
        timeResults.append(end-start)
        print "iteration number", n
    f = open("--.csv", 'wb')
    try:
        # plt.plot(timeResults, range(8,N))
        # plt.axis([0,30,8,25])
        # plt.show()
        writer = csv.writer(f)
        writer.writerow( ('size', 'time') )
        for n in range(1,N-7):
            writer.writerow( (n+7, timeResults[n-1]) )
    finally:
        f.close()
    print "finished"

def runTestSudoku(N):
    timeResults = []
    for n in range(1,N):
        if n%8 == 0:
            print "iter ", n
            start = time.time()
            solved = SudokuSolver.solveBacktracking(DataProvider.generateSudoku16x16(n))
            end = time.time()
            timeResults.append(end-start)
    f = open("--.csv", 'wb')
    try:
        writer = csv.writer(f)
        writer.writerow( ('number of elements', 'time') )
        for n in range(32):
            writer.writerow( (n+1, timeResults[n]) )
    finally:
        f.close()
    print "finished"


start=time.time()
#input = DataProvider.generateSudoku9x9(10)
input = np.array([[0,0,9,0,7,0,0,0,5],
      [0,0,2,1,0,0,9,0,0],
      [1,0,0,0,2,8,0,0,0],
      [0,7,0,0,0,5,0,0,1],
      [0,0,8,5,1,0,0,0,0],
      [0,5,0,0,0,0,3,0,0],
      [0,0,0,0,0,3,0,0,6],
      [8,0,0,0,0,0,0,0,0],
      [2,1,0,0,0,0,0,8,7]])
solved = SudokuSolver.solveForwardCheckingCLI(input)
end=time.time()
print "time = ", end-start
