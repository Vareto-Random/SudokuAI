from BFS_Sudoku import solve_bfs
from DFS_Sudoku import solve_dfs
from BDFS_Sudoku import solve_bt

# Thanks to http://sudopedia.enjoysudoku.com/Test_Cases.html

print ("\n\nTesting on invalid 9x9 board...0 blanks")
board = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
         [5, 2, 9, 1, 3, 4, 7, 6, 8],
         [4, 8, 7, 6, 2, 9, 5, 3, 1],
         [2, 6, 3, 4, 1, 5, 9, 8, 7],
         [9, 7, 4, 8, 6, 3, 1, 2, 5],
         [8, 5, 1, 7, 9, 2, 6, 4, 3],
         [1, 3, 8, 9, 4, 7, 2, 5, 6],
         [6, 9, 2, 3, 5, 1, 8, 7, 4],
         [7, 4, 5, 2, 8, 6, 3, 1, 9]]
print ("Problem:")
for row in board:
    print (row)
solve_bfs(board)
solve_dfs(board)
solve_bt(board)


print ("\n\nTesting on invalid 9x9 board...9 blanks")
board = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
         [5, 0, 9, 1, 3, 0, 7, 6, 8],
         [4, 8, 7, 6, 2, 0, 5, 3, 1],
         [2, 6, 0, 4, 1, 5, 9, 8, 7],
         [9, 7, 4, 8, 6, 3, 1, 2, 5],
         [8, 5, 1, 7, 9, 0, 6, 4, 3],
         [1, 3, 8, 9, 4, 7, 2, 5, 6],
         [6, 0, 2, 3, 5, 0, 8, 7, 4],
         [7, 4, 5, 0, 8, 6, 3, 0, 9]]
print ("Problem:")
for row in board:
    print (row)
solve_bfs(board)
solve_dfs(board)
solve_bt(board)


print ("\n\nTesting on invalid 9x9 board...18 blanks")
board = [[3, 1, 6, 0, 7, 0, 0, 9, 2],
         [5, 2, 9, 1, 0, 4, 0, 6, 0],
         [0, 0, 7, 6, 2, 9, 5, 3, 0],
         [2, 6, 3, 4, 1, 5, 9, 0, 7],
         [9, 0, 4, 8, 6, 3, 1, 2, 5],
         [8, 0, 1, 7, 9, 2, 0, 4, 3],
         [1, 3, 0, 9, 4, 0, 2, 5, 6],
         [0, 9, 2, 3, 5, 1, 8, 7, 0],
         [7, 4, 5, 2, 8, 6, 3, 1, 0]]
print ("Problem:")
for row in board:
    print (row)
solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting on invalid 9x9 board...27 blanks")
board = [[3, 1, 6, 5, 0, 0, 4, 0, 0],
         [5, 2, 9, 1, 3, 4, 7, 0, 8],
         [4, 8, 7, 6, 0, 9, 0, 3, 1],
         [2, 6, 0, 0, 1, 5, 9, 0, 0],
         [9, 0, 4, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 2, 6, 4, 3],
         [1, 3, 8, 0, 0, 7, 0, 0, 6],
         [6, 0, 0, 3, 5, 1, 0, 7, 4],
         [7, 0, 5, 0, 8, 6, 0, 1, 9]]
print ("Problem:")
for row in board:
    print (row)
solve_bfs(board)
solve_dfs(board)
solve_bt(board)


print ("\n\nTesting on invalid 9x9 board...36 blanks")
board = [[0, 0, 6, 5, 7, 0, 4, 9, 2],
         [0, 0, 0, 1, 3, 4, 7, 6, 0],
         [0, 0, 0, 6, 0, 9, 0, 3, 1],
         [0, 0, 3, 4, 1, 5, 0, 0, 0],
         [9, 7, 0, 8, 0, 3, 1, 2, 5],
         [8, 5, 0, 7, 0, 0, 0, 4, 0],
         [0, 0, 8, 0, 0, 7, 0, 5, 0],
         [6, 9, 2, 0, 5, 1, 8, 0, 0],
         [7, 0, 0, 2, 0, 6, 3, 1, 9]]
print ("Problem:")
for row in board:
    print (row)
solve_bfs(board)
solve_dfs(board)
solve_bt(board)


print ("\n\nTesting on invalid 9x9 board...45 blanks")
board = [[0, 0, 6, 0, 7, 8, 0, 9, 2],
         [0, 0, 9, 1, 0, 4, 7, 0, 8],
         [0, 8, 0, 0, 2, 0, 0, 3, 1],
         [2, 0, 0, 4, 1, 0, 0, 0, 0],
         [9, 7, 0, 8, 0, 0, 1, 0, 0],
         [0, 5, 0, 7, 9, 0, 0, 0, 3],
         [0, 0, 0, 9, 0, 0, 2, 0, 0],
         [6, 9, 2, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 0, 8, 0, 3, 1, 0]]
print ("Problem:")
for row in board:
    print (row)
solve_bfs(board)
solve_dfs(board)
solve_bt(board)


print ("\n\nTesting on invalid 9x9 board...54 blanks")
board = [[0, 0, 6, 0, 0, 0, 0, 0, 0],
         [5, 2, 9, 0, 0, 0, 7, 0, 0],
         [0, 0, 7, 6, 0, 9, 0, 0, 0],
         [2, 0, 3, 0, 0, 0, 9, 0, 0],
         [9, 0, 4, 0, 0, 0, 1, 2, 5],
         [0, 0, 0, 7, 0, 0, 6, 0, 0],
         [0, 0, 0, 9, 0, 0, 2, 0, 0],
         [0, 0, 2, 3, 0, 1, 0, 7, 4],
         [0, 0, 0, 0, 8, 0, 0, 0, 9]]
print ("Problem:")
for row in board:
    print (row)
solve_bfs(board)
solve_dfs(board)
solve_bt(board)


print ("\n\nTesting on invalid 9x9 board...63 blanks")
board = [[3, 1, 0, 5, 0, 8, 0, 0, 0],
         [5, 2, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 0, 0, 0, 0],
         [0, 7, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 7, 0, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 2, 0, 0, 0, 0, 0, 4],
         [0, 0, 0, 2, 8, 0, 0, 1, 0]]
print ("Problem:")
for row in board:
    print (row)
solve_bfs(board)
solve_dfs(board)
solve_bt(board)


# print ("\n\nTesting on invalid 9x9 board...72 blanks")
# board = [[0, 0, 6, 5, 0, 0, 4, 0, 2],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 3, 0, 0, 0],
#          [8, 5, 0, 7, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 3, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# print ("Problem:")
# for row in board:
#     print (row)
# solve_bfs(board)
# solve_dfs(board)
# solve_bt(board)