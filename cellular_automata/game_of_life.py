import numpy as np

class Player(self):
    pass


class Game(self,numberOfColumns=10,numberOfRows=10):
    def __init__(self):
        self.rules 
        self.numcol = numberOfColumns
        self.numrow = numberOfRows
        self.numNeighbors = 0
        pass
    
    def start(self):
        
# Randomly fill the board with 0's and 1's
# for rows in range(numberOfRows):
#   for columns in range(numberOfColumns):
#     board[rows][columns] = random.randint(0, 1)

        board = np.random.choice([0, 1], size=(10, 10), p=[0.7, 1-0.7]) 
        for rows in range(self.numrow):
            for columns in range(self.numcol):
                # checks all neighboring cells
                if board[rows,columns]:
                    numNeighbors = np.sum(board[rows-1:rows+2,columns-1:columns+2])-1
                else:
                    numNeighbors = np.sum(board[rows-1:rows+2,columns-1:columns+2])
                
                    # Update the status for the next generation, following the rules 
                if numNeighbors >= 4:
                    board[rows,columns] = 0
                if numNeighbors == 3:
                    board[rows,columns] = 1
                elif numNeighbors <= 2:
                    board[rows,columns] = 0
                # Reset the number of neighbors for checking the next array position
                    
                numNeighbors = 0

        print(board)
 

class Board(self, rows, cols):
    def create():
        board = np.zeros(self.rows, self.cols)
        pass
    
    def next_generation():
        pass
    