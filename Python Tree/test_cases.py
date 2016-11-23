from BFS_Sudoku import solve_bfs
from DFS_Sudoku import solve_dfs
from BDFS_Sudoku import solve_bt

# Thanks to http://sudopedia.enjoysudoku.com/Test_Cases.html

print ("\n\nTesting on 6x6 board...")
board = [[1,5,0,0,4,0],
      [2,4,0,0,5,6],
      [4,0,0,0,0,3],
      [0,0,0,0,0,4],
      [6,3,0,0,2,0],
      [0,2,0,0,3,1]]

print ("Problem:")
for row in board:
      print (row)

solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting on 6x6 board...")
board = [[0,0,0,0,4,0],
      [5,6,0,0,0,0],
      [3,0,2,6,5,4],
      [0,4,0,2,0,3],
      [4,0,0,0,6,5],
      [1,5,6,0,0,0]]

print ("Problem:")
for row in board:
      print (row)

solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting on invalid 9x9 board...")
board = [[0,0,9,0,7,0,0,0,5],
      [0,0,2,1,0,0,9,0,0],
      [1,0,0,0,2,8,0,0,0],
      [0,7,0,0,0,5,0,0,1],
      [0,0,8,5,1,0,0,0,0],
      [0,5,0,0,0,0,3,0,0],
      [0,0,0,0,0,3,0,0,6],
      [8,0,0,0,0,0,0,0,0],
      [2,1,0,0,0,0,0,8,7]]

print ("Problem:")
for row in board:
      print (row)

solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting on 9x9 board...")
board = [[0,0,0,8,4,0,6,5,0],
      [0,8,0,0,0,0,0,0,9],
      [0,0,0,0,0,5,2,0,1],
      [0,3,4,0,7,0,5,0,6],
      [0,6,0,2,5,1,0,3,0],
      [5,0,9,0,6,0,7,2,0],
      [1,0,8,5,0,0,0,0,0],
      [6,0,0,0,0,0,0,4,0],
      [0,5,2,0,8,6,0,0,0]]

print ("Problem:")
for row in board:
      print (row)
      
solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting on filled valid 9x9 board...")
board = [[9,7,4,2,3,6,1,5,8],
      [6,3,8,5,9,1,7,4,2],
      [1,2,5,4,8,7,9,3,6],
      [3,1,6,7,5,4,2,8,9],
      [7,4,2,9,1,8,5,6,3],
      [5,8,9,3,6,2,4,1,7],
      [8,6,7,1,2,5,3,9,4],
      [2,5,3,6,4,9,8,7,1],
      [4,9,1,8,7,3,6,2,5]]

print ("Problem:")
for row in board:
      print (row)

solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting on 9x9 board...")
board = [[3,0,5,4,2,0,8,1,0],
      [4,8,7,9,0,1,5,0,6],
      [0,2,9,0,5,6,3,7,4],
      [8,5,0,7,9,3,0,4,1],
      [6,1,3,2,0,8,9,5,7],
      [0,7,4,0,6,5,2,8,0],
      [2,4,1,3,0,9,0,6,5],
      [5,0,8,6,7,0,1,9,2],
      [0,9,6,5,1,2,4,0,8]]

print ("Problem:")
for row in board:
      print (row)

solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting on 9x9 board...")
board = [[0,0,2,0,3,0,0,0,8],
      [0,0,0,0,0,8,0,0,0],
      [0,3,1,0,2,0,0,0,0],
      [0,6,0,0,5,0,2,7,0],
      [0,1,0,0,0,0,0,5,0],
      [2,0,4,0,6,0,0,3,1],
      [0,0,0,0,8,0,6,0,5],
      [0,0,0,0,0,0,0,1,3],
      [0,0,5,3,1,0,4,0,0]]

print ("Problem:")
for row in board:
      print (row)

solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting unsolvable quadrant on a 9x9 board...")
board = [[0,9,0,3,0,0,0,0,1],
      [0,0,0,0,8,0,0,4,6],
      [0,0,0,0,0,0,8,0,0],
      [4,0,5,0,6,0,0,3,0],
      [0,0,3,2,7,5,6,0,0],
      [0,6,0,0,1,0,9,0,4],
      [0,0,1,0,0,0,0,0,0],
      [5,8,0,0,2,0,0,0,0],
      [2,0,0,0,0,7,0,6,0]]

print ("Problem:")
for row in board:
      print (row)

solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting on 9x9 board...")
board = [[0,3,9,0,0,0,1,2,0],
      [0,0,0,9,0,7,0,0,0],
      [8,0,0,4,0,1,0,0,6],
      [0,4,2,0,0,0,7,9,0],
      [0,0,0,0,0,0,0,0,0],
      [0,9,1,0,0,0,5,4,0],
      [5,0,0,1,0,9,0,0,3],
      [0,0,0,8,0,5,0,0,0],
      [0,1,4,0,0,0,8,7,0]]
 
print ("Problem:")
for row in board:
      print (row)

solve_bfs(board)
solve_dfs(board)
solve_bt(board)

print ("\n\nTesting on 16x16 board...")
board=[[0,15,11,1,6,2,10,14,12,0,13,3,16,0,4,5],
[10,6,3,16,12,5,0,4,14,15,1,0,2,11,0,13],
[14,5,0,0,11,3,15,13,0,2,16,4,12,10,1,6],
[4,13,2,12,1,0,0,16,6,10,5,11,3,15,0,14],
[0,2,6,15,14,1,11,0,3,5,10,16,4,0,13,12],
[3,16,12,0,2,4,6,0,11,14,0,13,10,1,5,15],
[11,10,5,13,0,12,3,15,1,0,4,2,0,6,14,16],
[1,4,0,14,13,10,16,5,15,6,0,12,0,2,3,11],
[13,0,16,5,0,6,1,12,2,0,3,10,11,14,15,4],
[2,12,0,11,0,16,14,3,5,4,6,15,1,13,0,10],
[6,3,14,4,10,15,13,0,0,11,0,1,5,12,16,2],
[15,1,10,0,4,11,5,2,13,16,12,14,0,3,6,0],
[12,0,4,3,16,0,2,10,0,13,14,6,15,5,11,1],
[5,11,13,2,3,0,4,6,10,1,15,0,14,16,12,0],
[0,0,1,6,15,14,12,11,16,3,2,5,13,4,10,0],
[16,14,15,10,5,13,0,1,4,12,11,0,6,0,2,3]]

print ("Problem:")
for row in board:
      print (row)

solve_bfs(board)
solve_dfs(board)
solve_bt(board)