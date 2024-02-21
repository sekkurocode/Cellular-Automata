#game_of_life.py
import numpy as np
import os
import time

class CellularAutomata:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = np.zeros((rows, columns), dtype=int)
        self.running = False

    def update(self):
        new_grid = np.copy(self.grid)
        for i in range(self.rows):
            for j in range(self.columns):
                neighbors = self.count_neighbors(i, j)
                if self.grid[i, j] == 0 and neighbors == 3:
                    new_grid[i, j] = 1  # Zelle wird geboren
                elif self.grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[i, j] = 0  # Zelle stirbt
        self.grid = new_grid

    def count_neighbors(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    count += self.grid[(row + i) % self.rows, (col + j) % self.columns]
        return count

    def toggle_cell(self, row, col):
        self.grid[row, col] = 1 - self.grid[row, col]

    def randomize_grid(self, probability):
        for i in range(self.rows):
            for j in range(self.columns):
                if np.random.rand() < probability:
                    self.grid[i, j] = 1

    def display_grid(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        for row in self.grid:
            print(' '.join('■' if cell == 1 else ' ' for cell in row))
        print()

    def start_simulation(self, generations=50, interval=0.2):
        self.running = True
        for _ in range(generations):
            if not self.running:
                break
            self.display_grid()
            self.update()
            time.sleep(interval)
        self.running = False

def main():
    rows, columns = 20, 40
    cellular_automata = CellularAutomata(rows, columns)

    # Zufällige Initialisierung des Gitters
    cellular_automata.randomize_grid(probability=0.3)

    while True:
        cellular_automata.display_grid()
        print("Options:")
        print("1. Start Simulation")
        print("2. Stop Simulation")
        print("3. Toggle Cell")
        print("4. Randomize Grid")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            cellular_automata.start_simulation()
        elif choice == "2":
            cellular_automata.running = False
        elif choice == "3":
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            cellular_automata.toggle_cell(row, col)
        elif choice == "4":
            cellular_automata.randomize_grid(probability=0.3)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()

