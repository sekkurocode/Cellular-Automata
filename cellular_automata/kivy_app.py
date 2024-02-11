from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

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
            instance.background_color = [0, 0.8, 1, 1]  # Hellblaue Hintergrundfarbe, um anzuzeigen, dass Modify-Modus aktiviert ist
        else:
            instance.background_color = [0, 0.5, 1, 1]  # Normale Hintergrundfarbe

    def update(self, dt):
        if self.running:
            # Hier koennen Sie die Logik fuer die Aktualisierung der Zellen im Game of Life einfuegen
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
