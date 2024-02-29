
## -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
import numpy as np
import random

class Cell(Button):
    def __init__(self, row_idx, col_idx, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.state = 'normal'
        self.alive = False
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.bind(on_press=self.toggle)

    def toggle(self, instance):
        if app.root.modify_mode:
            self.alive = not self.alive
            self.update_color()
            app.root.game.board[self.row_idx, self.col_idx] = int(self.alive)

    def update_color(self):
        if self.alive:
            self.background_color = [1, 1, 1, 1]
        else:
            self.background_color = [0, 0, 0, 1]

class GameOfLifeGUI(BoxLayout):
    def __init__(self, **kwargs):
        super(GameOfLifeGUI, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.grid_layout = GridLayout(cols=50, rows=50, padding=5)
        self.cells = [[Cell(row_idx, col_idx) for col_idx in range(50)] for row_idx in range(50)]
        for row in self.cells:
            for cell in row:
                self.grid_layout.add_widget(cell)
        self.add_widget(self.grid_layout)

        self.control_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.control_button = Button(text='Start', size_hint_x=None, width=100)
        self.control_button.bind(on_press=self.start_stop)
        self.control_layout.add_widget(self.control_button)

        self.menu_button = Button(text='Menu', size_hint_x=None, width=100)
        self.menu_button.bind(on_press=self.open_menu)
        self.control_layout.add_widget(self.menu_button)
        
        self.add_widget(self.control_layout)

        self.running = False
        self.modify_mode = False

        self.modify_indicator = Label(text='', size_hint=(None, None), size=(100, 50), halign='right')
        self.modify_indicator.canvas.before.add(Color(0.8, 0.89, 1, 1))  
        self.modify_indicator.canvas.before.add(Rectangle(size=self.modify_indicator.size, pos=self.modify_indicator.pos))
        self.add_widget(self.modify_indicator)
        
        self.game = Game()

    def open_menu(self, instance):
        self.pause_game()
        content = BoxLayout(orientation='vertical')
        modify_button = Button(text='Modify')
        modify_button.bind(on_press=self.toggle_modify_mode)
        content.add_widget(modify_button)
        random_button = Button(text='Random')
        random_button.bind(on_press=self.set_random_cells)
        content.add_widget(random_button)
        clear_button = Button(text='Clear')
        clear_button.bind(on_press=self.clear_cells)
        content.add_widget(clear_button)
        popup = Popup(title='Menu', content=content, size_hint=(None, None), size=(200, 150))
        popup.open()

    def toggle_modify_mode(self, instance):
        self.modify_mode = not self.modify_mode
        if self.modify_mode:
            self.modify_indicator.text = '          Modify Active'
        else:
            self.modify_indicator.text = ''

    def set_random_cells(self, instance):
        for row_idx, row in enumerate(self.cells):
            for col_idx, cell in enumerate(row):
                cell.alive = bool(random.getrandbits(1))
                self.game.board[row_idx, col_idx] = int(cell.alive)
                cell.update_color()

    def clear_cells(self, instance):
        for row in self.cells:
            for cell in row:
                cell.alive = False
                cell.update_color()
                self.game.board[cell.row_idx, cell.col_idx] = 0

    def update(self, dt):
        if self.running:
            self.game.update_board()
            self.update_grid()

    def update_grid(self):
        for row_idx, row in enumerate(self.cells):
            for col_idx, cell in enumerate(row):
                cell.alive = self.game.board[row_idx, col_idx]
                cell.update_color()
    
    def start_stop(self, instance):
        self.running = not self.running
        if self.running:
            self.control_button.text = 'Stop'
            Clock.schedule_interval(self.update, 1.0 / 2) 
        else:
            self.control_button.text = 'Start'
            Clock.unschedule(self.update)

    def pause_game(self):
        self.running = False
        self.control_button.text = 'Start'
        Clock.unschedule(self.update)

class Game:
    def __init__(self):
        self.numcol = 50
        self.numrow = 50
        self.numNeighbors = 0
        self.board = np.zeros((self.numrow, self.numcol), dtype=int)
        self.temp_board = np.zeros((self.numrow, self.numcol), dtype=int)

    def update_board(self):
        for row in range(self.numrow):
            for col in range(self.numcol):
                if self.board[row, col]:
                    self.numNeighbors = np.sum(self.board[max(0, row - 1):min(row + 2, self.numrow), max(0, col - 1):min(col + 2, self.numcol)]) - 1
                else:
                    self.numNeighbors = np.sum(self.board[max(0, row - 1):min(row + 2, self.numrow), max(0, col - 1):min(col + 2, self.numcol)])

                if self.numNeighbors >= 4:
                    self.temp_board[row, col] = 0
                elif self.numNeighbors == 3:
                    self.temp_board[row, col] = 1
                elif self.numNeighbors <= 2:
                    self.temp_board[row, col] = 0

                self.numNeighbors = 0
                
        self.board = self.temp_board.copy()
        self.temp_board.fill(0)

class GameOfLifeApp(App):
    def build(self):
        self.root = GameOfLifeGUI()
        return self.root

    def on_start(self):
        from kivy.core.window import Window
        Window.clearcolor = (0.8, 0.89, 1, 1)

if __name__ == '__main__':
    app = GameOfLifeApp()
    app.run()
