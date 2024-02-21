from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class Cell(Button):
    def __init__(self, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.state = 'normal'
        self.alive = False  # State of the cell (alive or dead)
        self.bind(on_press=self.toggle)  # Link the pressing of the button with the toggle method

    def toggle(self, instance):
        if app.root.modify_mode:  # check whether the Modify mode is activated
            self.alive = not self.alive  # change the state of the cell
            self.update_color()  # Update the color of the cell based on its state

    def update_color(self):
        if self.alive:
            self.background_color = [1, 1, 1, 1]  # If the cell is alive, set the background color to white
        else:
            self.background_color = [0, 0, 0, 1]  # If the cell is dead, set the background color to black

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
        self.modify_button = Button(text='Modify', size_hint_x=None, width=100, background_color=[0, 0.5, 1, 1])
        self.modify_button.bind(on_press=self.toggle_modify_mode)
        self.control_layout.add_widget(self.control_button)
        self.control_layout.add_widget(self.modify_button)
        self.add_widget(self.control_layout)

        self.running = False
        self.modify_mode = False

    def toggle_modify_mode(self, instance):
        self.modify_mode = not self.modify_mode
        if self.modify_mode:
            instance.background_color = [0, 0.8, 1, 1]  # Light blue background color to indicate that Modify mode is activated
        else:
            instance.background_color = [0, 0.5, 1, 1]  # Normal background color

    def update(self, dt):
        if self.running:
            # Here you can insert the logic for updating the cells in the Game of Life
            pass

    def start_stop(self, instance):
        self.running = not self.running
        if self.running:
            self.control_button.text = 'Stop'
            Clock.schedule_interval(self.update, 1.0 / 2)  # Update-Frequenz
        else:
            self.control_button.text = 'Start'
            Clock.unschedule(self.update)

class GameOfLifeApp(App):
    def build(self):
        return GameOfLifeGUI()

if __name__ == '__main__':
    app = GameOfLifeApp()
    app.run()
