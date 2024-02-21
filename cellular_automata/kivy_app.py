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
    def __init__(self, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.state = 'normal'
        self.alive = False  # Zustand der Zelle (lebendig oder tot)
        self.bind(on_press=self.toggle)  # Verknuepfe das Druecken des Buttons mit der toggle-Methode

    def toggle(self, instance):
        if app.root.modify_mode:  # ueberpruefe, ob der Modify-Modus aktiviert ist
            self.alive = not self.alive  # aendere den Zustand der Zelle
            self.update_color()  # Aktualisiere die Farbe der Zelle basierend auf ihrem Zustand

    def update_color(self):
        if self.alive:
            self.background_color = [1, 1, 1, 1]  # Wenn die Zelle lebendig ist, setze die Hintergrundfarbe auf Weiss
        else:
            self.background_color = [0, 0, 0, 1]  # Wenn die Zelle tot ist, setze die Hintergrundfarbe auf Schwarz

class GameOfLifeGUI(BoxLayout):
    def __init__(self, **kwargs):
        super(GameOfLifeGUI, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.grid_layout = GridLayout(cols=50, rows=50, padding=5)
        self.cells = [[Cell() for _ in range(50)] for _ in range(50)]
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
        self.modify_indicator.canvas.before.add(Color(0.8, 0.89, 1, 1))  # Hellblaue Hintergrundfarbe
        self.modify_indicator.canvas.before.add(Rectangle(size=self.modify_indicator.size, pos=self.modify_indicator.pos))
        self.add_widget(self.modify_indicator)
        
        self.game = Game() # Instanzierung Game 

    def open_menu(self, instance):
        self.pause_game()  # Spiel pausieren und stoppen
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
        for row in self.cells:
            for cell in row:
                cell.alive = bool(random.getrandbits(1))
                cell.update_color()

    def clear_cells(self, instance):
        for row in self.cells:
            for cell in row:
                cell.alive = False
                cell.update_color()

    def update(self, dt):
        if self.running:
            self.game.update_board()
            self.update_grid()

    def update_grid(self):
        # Überprüft den Status jeder Zelle und updated den alive - Parameter mit dem Game.board Parameter (0 oder 1, beim ersten Durchlauf mit gg. Verteilung)
        # Update der Zellfarbe, je nach Zusatnd.
        # HIER FARBE MIT ALTER VERKNÜPFEN!!!
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                cell.alive = self.game.board[row, col]
                cell.update_color()
    
    def start_stop(self, instance):
        self.running = not self.running
        if self.running:
            self.control_button.text = 'Stop'
            Clock.schedule_interval(self.update, 1.0 / 2)  # Update-Frequenz
        else:
            self.control_button.text = 'Start'
            Clock.unschedule(self.update)

    def pause_game(self):
        self.running = False
        self.control_button.text = 'Start'
        Clock.unschedule(self.update)
class Game():
    def __init__(self):
        self.numcol = 50
        self.numrow = 50
        self.numNeighbors = 0
        self.board = np.random.choice([0, 1], size=(self.numrow, self.numcol), p=[0.7, 0.3])
        self.temp_board = np.zeros([self.numrow, self.numcol]).astype(int)

    def update_board(self):
        # Wird von Update gecallt. Passt den Zustand für die nächste Generation an, speichert ein temporäres Board
        # Regeln für Generationenübergang unten. board wird zur Kopie des temp Boards bevor dieses aauf 0 gesetzt wird.
        for row in range(self.numrow):
            for col in range(self.numcol):
                if self.board[row, col]:
                    self.numNeighbors = np.sum(self.board[max(0, row - 1):min(row + 2, self.numrow), max(0, col - 1):min(col + 2, self.numcol)]) - 1
                else:
                    self.numNeighbors = np.sum(self.board[max(0, row - 1):min(row + 2, self.numrow), max(0, col - 1):min(col + 2, self.numcol)])

                # Hier die Regeln
                # Ab 4 lebenden Nachbarn stirbt die Zelle an Nahrungsmangel
                # Bei 3 Lebenden Nachbarn erwacht die zelle zum Leben
                # Bei 2 oder weniger Nachbarn stirbt die Zelle
                # REGEL PARAMETER IN GUI IMPLEMENTIEREN
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
        # Hintergrundfarbe der GUI ändern
        self.root = GameOfLifeGUI()
        return self.root

    def on_start(self):
        from kivy.core.window import Window
        # Setze die Hintergrundfarbe des Fensters auf Hellblau
        Window.clearcolor = (0.8, 0.89, 1, 1)

if __name__ == '__main__':
    app = GameOfLifeApp()
    app.run()
