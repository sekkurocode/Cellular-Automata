# kivy_app.py
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from game_of_life import CellularAutomata
from random import random

class Cell(Button):
    def __init__(self, row, col, automata, app, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.state = 'normal'
        self.alive = False  # Zustand der Zelle (lebendig oder tot)
        self.row = row
        self.col = col
        self.automata = automata
        self.app = app
        self.bind(on_press=self.toggle)  # Verknuepfe das Druecken des Buttons mit der toggle-Methode

    def toggle(self, instance):
        if self.app.root.modify_mode:  # ueberpruefe, ob der Modify-Modus aktiviert ist
            self.alive = not self.alive  # aendere den Zustand der Zelle
            self.update_color()  # Aktualisiere die Farbe der Zelle basierend auf ihrem Zustand
            self.automata.grid[self.row, self.col] = 1 if self.alive else 0

    def update_color(self):
        if self.alive:
            self.background_color = [1, 1, 1, 1]  # Wenn die Zelle lebendig ist, setze die Hintergrundfarbe auf Weiss
        else:
            self.background_color = [0, 0, 0, 1]  # Wenn die Zelle tot ist, setze die Hintergrundfarbe auf Schwarz

class GameOfLifeGUI(BoxLayout):
    def __init__(self, automata, app, **kwargs):
        super(GameOfLifeGUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.automata = automata
        self.app = app

        self.grid_layout = GridLayout(cols=self.automata.columns, rows=self.automata.rows, padding=5, spacing=5)
        self.cells = [[Cell(row, col, self.automata, self.app) for col in range(self.automata.columns)] for row in range(self.automata.rows)]
        for row in self.cells:
            for cell in row:
                self.grid_layout.add_widget(cell)
        self.add_widget(self.grid_layout)

        self.control_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
        self.control_button = Button(text='Start', size_hint_x=None, width=100)
        self.control_button.bind(on_press=self.start_stop)
        self.modify_button = Button(text='Modify', size_hint_x=None, width=100, background_color=[0, 0.5, 1, 1])
        self.modify_button.bind(on_press=self.toggle_modify_mode)
        self.step_button = Button(text='Step', size_hint_x=None, width=100)
        self.step_button.bind(on_press=self.step)
        self.randomize_button = Button(text='Randomize', size_hint_x=None, width=200)
        self.randomize_button.bind(on_press=self.randomize)
        self.clear_button = Button(text='Clear', size_hint_x=None, width=100)
        self.clear_button.bind(on_press=self.clear_grid)

        self.control_layout.add_widget(self.control_button)
        self.control_layout.add_widget(self.modify_button)
        self.control_layout.add_widget(self.step_button)
        self.control_layout.add_widget(self.randomize_button)
        self.control_layout.add_widget(self.clear_button)
        self.add_widget(self.control_layout)

        self.info_label = Label(text='', size_hint_y=None, height=50)
        self.add_widget(self.info_label)

        self.running = False
        self.modify_mode = False
        
        # Hinzufügen des Info-Textes am unteren Rand
        self.info_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        self.info_layout.add_widget(Label(text='Powered by @Sara25s @sekkurocode @fabrice-eberle @juldimag @redibaj'))
        self.add_widget(self.info_layout)

    def toggle_modify_mode(self, instance):
        self.modify_mode = not self.modify_mode
        if self.modify_mode:
            instance.background_color = [0, 0.8, 1, 1]  # Hellblaue Hintergrundfarbe, um anzuzeigen, dass Modify-Modus aktiviert ist
        else:
            instance.background_color = [0, 0.5, 1, 1]  # Normale Hintergrundfarbe

    def update(self, dt):
        if self.running:
            self.automata.update()
            self.display_grid()

    def start_stop(self, instance):
        self.running = not self.running
        if self.running:
            self.control_button.text = 'Stop'
            self.initialize_grid()  # Rufe initialize_grid auf, wenn die Simulation gestartet wird
            Clock.schedule_interval(self.update, 1.0 / 2)  # Update-Frequenz
        else:
            self.control_button.text = 'Start'
            Clock.unschedule(self.update)

    def step(self, instance):
        if not self.running:
            self.automata.update()
            self.display_grid()

    def randomize(self, instance):
        if not self.running:
            self.automata.randomize_grid(probability=0.3)
            self.display_grid()

    def clear_grid(self, instance):
        if not self.running:
            self.automata.grid = self.automata.grid * 0  # Setze alle Zellen auf tot
            self.display_grid()

    def initialize_grid(self):
        for row in self.cells:
            for cell in row:
                cell.alive = bool(round(random()))  # Zufällige Initialisierung der Zellen
                cell.update_color()
                self.automata.grid[cell.row, cell.col] = 1 if cell.alive else 0

    def display_grid(self):
        for row, cells_row in enumerate(self.cells):
            for col, cell in enumerate(cells_row):
                cell.alive = bool(self.automata.grid[row, col])
                cell.update_color()

class GameOfLifeApp(App):
    def build(self):
        automata = CellularAutomata(rows=20, columns=40)
        return GameOfLifeGUI(automata, self)
