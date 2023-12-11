import numpy as np
import time

class Player:
    def __init__(self, name):
        # Constructor for the Player class.
        # Initializes a player with a given name.
        self.name = name

class Board:
    def __init__(self, rows, cols):
        # Constructor for the Board class.
        # Initializes a game board with a given number of rows and columns.
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)

    def create(self):
        # Method to initialize the game board.
        # Logic should be inserted here to create the initial state of the board.
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i, j] = np.random.choice([0, 1])

    def next_generation(self):
        # Method to calculate the next generation of the game.
        # Logic should be inserted here to calculate the next state of the board.
        new_board = np.copy(self.board)
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors_sum = np.sum(self.board[max(0, i-1):min(self.rows, i+2), max(0, j-1):min(self.cols, j+2)]) - self.board[i, j]
                if self.board[i, j] == 1:
                    if neighbors_sum < 2 or neighbors_sum > 3:
                        new_board[i, j] = 0
                else:
                    if neighbors_sum == 3:
                        new_board[i, j] = 1
        self.board = new_board

class Game:
    def __init__(self):
        # Constructor for the Game class.
        # Initializes a game with placeholders for rules, players, the current player, and the game board.
        self.rules = None  # Placeholder for game rules
        self.players = []  # List to store players
        self.current_player = None  # Variable to keep track of the current player
        self.board = None  # Placeholder for the game board

    def add_player(self, player):
        # Method to add a player to the game.
        # Adds the player to the list of players and sets them as the current player if none is set.
        self.players.append(player)
        if not self.current_player:
            self.current_player = player

    def start(self, rows, cols, generations=10):
        # Method to start the game.
        # Initializes a game board and starts the game for a specified number of generations.
        self.board = Board(rows, cols)
        self.board.create()

        for generation in range(generations):
            print(f"Generation {generation + 1}")
            self.print_board()
            time.sleep(1)  # Optional: Delay between generations
            self.board.next_generation()

        print("Game ended!")

    def print_board(self):
        # Method to print the current game board.
        for i in range(self.board.rows):
            for j in range(self.board.cols):
                print("■" if self.board.board[i, j] == 1 else "□", end=" ")
            print()

if __name__ == "__main__":
    # Example usage
    game = Game()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    game.add_player(player1)
    game.add_player(player2)

    game.start(5, 5, generations=5)
