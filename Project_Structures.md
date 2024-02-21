### Deutsch

# Projekt Cellular Automata und Emergent Structures

## Überblick

Das Projekt Cellular Automata und Emergent Structures ist eine auf Python basierende Software, die darauf abzielt, zelluläre Automaten zu simulieren, emergente Strukturen zu erkunden und speziell Conway's Game of Life zu implementieren. Zelluläre Automaten bestehen aus Zellen, die in zwei Zuständen existieren, 0 (tot) oder 1 (lebendig), und sich über Generationen basierend auf vordefinierten Regeln entwickeln.

## Game of Life

### Regeln

Die Simulation folgt den Regeln von Conway's Game of Life, einem bekannten zellulären Automaten:
1. Jede lebende Zelle mit weniger als zwei lebenden Nachbarn stirbt (Unterbevölkerung).
2. Jede lebende Zelle mit zwei oder drei lebenden Nachbarn überlebt bis zur nächsten Generation.
3. Jede lebende Zelle mit mehr als drei lebenden Nachbarn stirbt (Überbevölkerung).
4. Jede tote Zelle mit genau drei lebenden Nachbarn wird lebendig (Reproduktion).

### Emergente Strukturen

Emergente Strukturen sind Muster, die durch die Anwendung von Regelsätzen in zellulären Automaten-Simulationen entstehen. Conway's Game of Life zeigt faszinierende emergente Strukturen wie Gliders und Glider Guns. Diese Strukturen entwickeln sich dynamisch über Generationen und zeigen die Komplexität, die aus einfachen Regeln entstehen kann.

## Projektbestandteile

### 1. Konsolenanwendung (game_of_life.py)

#### Funktionen:
- Benutzerinteraktion über eine Konsolenschnittstelle.
- Starten und Stoppen von Simulationen, Umschalten von Zellen, Zufällige Initialisierung des Gitters und mehr.
- Visualisierung von Generationen in der Konsole.

#### Ausführung:
1. Führen Sie `main.py` aus, um die Konsolenanwendung zu starten.
2. Befolgen Sie die Bildschirmanweisungen, um mit der Simulation zu interagieren.

### 2. Kivy GUI-Anwendung (kivy_app.py)

#### Funktionen:
- Grafische Benutzeroberfläche (GUI) unter Verwendung des Kivy-Frameworks.
- Starten und Stoppen von Simulationen, Bearbeiten von Zellen, Durchschalten von Generationen, Zufällige Initialisierung des Gitters und Löschen des Gitters.
- Visuelle Darstellung des Gitters mit interaktivem Umschalten der Zellen.

#### Ausführung:
1. Führen Sie `main.py` aus, um die Kivy GUI-Anwendung zu starten.
2. Nutzen Sie die Schaltflächen in der GUI, um die Simulation zu steuern und zu beobachten.

## Projektstruktur

- game_of_life.py: Enthält die Kernlogik für die Game of Life-Simulation.
- kivy_app.py: Implementiert die GUI-Schnittstelle mit Kivy und verbindet sie mit der Simulationslogik.
- main.py: Hauptdatei, die sowohl die Konsolen- als auch GUI-Anwendungen integriert.

## Dank

Dieses Projekt wird durch Beiträge von @juldimag, @sekkurocode, @Sara25s, @redibaj und @fabrice-eberle unterstützt.

Fühlen Sie sich frei, diese Beschreibung basierend auf den spezifischen Details Ihres Projekts oder Ihrer Präsentation anzupassen und zu erweitern.

### Englisch

# Project Cellular Automata and Emergent Structures

## Overview

The Cellular Automata and Emergent Structures project is a Python-based software aiming to simulate cellular automata, explore emergent structures, and specifically implement Conway's Game of Life. Cellular automata consist of cells that exist in two states, 0 (dead) or 1 (alive), evolving over generations based on predefined rules.

## Game of Life

### Rules

The simulation follows the rules of Conway's Game of Life, a well-known cellular automaton:
1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors survives to the next generation.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes alive (reproduction).

### Emergent Structures

Emergent structures are patterns that emerge from applying rule sets in cellular automaton simulations. Conway's Game of Life showcases fascinating emergent structures like gliders and glider guns. These structures dynamically evolve over generations, demonstrating the complexity that can arise

from simple rules.

## Project Components

### 1. Console Application (game_of_life.py)

#### Features:
- User interaction via a console interface.
- Starting and stopping simulations, toggling cells, randomizing the grid, and more.
- Visualization of generations in the console.

#### Execution:
1. Run `main.py` to start the console application.
2. Follow on-screen instructions to interact with the simulation.

### 2. Kivy GUI Application (kivy_app.py)

#### Features:
- Graphical user interface (GUI) using the Kivy framework.
- Starting and stopping simulations, editing cells, stepping through generations, randomizing the grid, and clearing the grid.
- Visual representation of the grid with interactive cell toggling.

#### Execution:
1. Run `main.py` to start the Kivy GUI application.
2. Utilize the buttons in the GUI to control and observe the simulation.

## Project Structure

- game_of_life.py: Contains the core logic for the Game of Life simulation.
- kivy_app.py: Implements the GUI interface with Kivy and connects it to the simulation logic.
- main.py: Main file integrating both console and GUI applications.

## Acknowledgments

This project is supported by contributions from @juldimag, @sekkurocode, @Sara25s, @redibaj, and @fabrice-eberle.

Feel free to adapt and expand this description based on the specific details of your project or presentation.
