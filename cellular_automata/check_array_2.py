import numpy as np
import random

np.set_printoptions(threshold=10000)
numberOfRows = 10
numberOfColumns = 10
numberOfIterations = 10

board = np.random.choice([0, 1], size=(numberOfRows, numberOfColumns), p=[0.7, 0.3])
temp_board = np.zeros([numberOfRows, numberOfColumns]).astype(int)

# Randomly fill the board with 0's and 1's
# for rows in range(numberOfRows):
#   for columns in range(numberOfColumns):
#     board[rows][columns] = random.randint(0, 1)


#print(board)
# 2D Array for neighborhood
numNeighbors = 0
print(board)
for _ in range(numberOfIterations):
    for rows in range(numberOfRows):
        for columns in range(numberOfColumns):
        # checks all neighboring cells
            if board[rows,columns]:
                numNeighbors = np.sum(board[rows-1:rows+2,columns-1:columns+2])-1
            else:
                numNeighbors = np.sum(board[rows-1:rows+2,columns-1:columns+2])
                
                # Update the status for the next generation
            # if numNeighbors >= 4:
            #     temp_board[rows,columns] = 0
            if numNeighbors == 3:
                temp_board[rows,columns] = 1
            elif numNeighbors <= 2:
                temp_board[rows,columns] = 0
                # Reset the number of neighbors for checking the next array position
                
            numNeighbors = 0
    board = temp_board
    temp_board = np.zeros([numberOfRows, numberOfColumns]).astype(int)
    print(board)


