import numpy as np

class Player():
    pass

class Board():
    def create():
        board = np.zeros(self.rows, self.cols)
        pass
    
    def next_generation():
        pass


class Game():
    def __init__(self):
        self.numcol = 10
        self.numrow = 10
        self.numNeighbors = 0
        self.numiter = 10
        self.board = np.random.choice([0, 1], size=(self.numrow, self.numcol), p=[0.7, 0.3])
        self.temp_board = np.zeros([self.numrow, self.numcol]).astype(int)
    
    def start(self):
        print(self.board)
        for _ in range(self.numiter):
            for rows in range(self.numrow):
                for columns in range(self.numcol):
                    if self.board[rows,columns]:
                        self.numNeighbors = np.sum(self.board[rows-1:rows+2,columns-1:columns+2])-1
                    else:
                        self.numNeighbors = np.sum(self.board[rows-1:rows+2,columns-1:columns+2])
                        
                        # Update the status for the next generation
                    if self.numNeighbors >= 4:
                        self.temp_board[rows,columns] = 0
                    if self.numNeighbors == 3:
                        self.temp_board[rows,columns] = 1
                    elif self.numNeighbors <= 2:
                        self.temp_board[rows,columns] = 0
                        # Reset the number of neighbors for checking the next array position
                        
                    self.numNeighbors = 0
            self.board = self.temp_board
            self.temp_board = np.zeros([self.numrow, self.numcol]).astype(int)
            print(self.board)
      
new_game=Game()

new_game.start()