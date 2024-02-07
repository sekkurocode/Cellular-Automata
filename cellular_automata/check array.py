import numpy as np
import random

numberOfRows = 10
numberOfColumns = 10

board = np.random.choice([0, 1], size=(10, 10), p=[0.7, 1-0.7])
# board = np.zeros((numberOfRows, numberOfColumns))
offsets = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

# Randomly fill the board with 0's and 1's
# for rows in range(numberOfRows):
#   for columns in range(numberOfColumns):
#     board[rows][columns] = random.randint(0, 1)


#print(board)
# 2D Array for neighborhood
numNeighbors = 0
print(board)
for _ in range(1):
  for rows in range(numberOfRows):
    for columns in range(numberOfColumns):
      # checks all neighboring cells
      if board[rows,columns]:
        numNeighbors = np.sum(board[rows-1:rows+2,columns-1:columns+2])-1
      else:
        numNeighbors = np.sum(board[rows-1:rows+2,columns-1:columns+2])
        
          # Update the status for the next generation
      if numNeighbors >= 4:
        board[rows,columns] = 0
      if numNeighbors == 3:
        board[rows,columns] = 1
      elif numNeighbors <= 2:
        board[rows,columns] = 0
        # Reset the number of neighbors for checking the next array position
          
      numNeighbors = 0
      print(board)





# for offset in offsets:
#         r = rows + int(offset[0]) 
#         c = columns + int(offset[1])
#         if r<numberOfRows and c <numberOfColumns:
#           if board[r][c] != 0:
#               numNeighbors += 1
