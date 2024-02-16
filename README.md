# Cellular-Automata and Emergent Structures
The goal of this github project is the development of a python software, simulating "Cellular Automata".<br/><br/>
Cellular Automata are cells, which usually are in one of two **states**, 0 or 1. If a cell is in the state "0" it is in the dead state, meaning it won't have any influence on the cells around it. In the "1" state cells count as alive and take effect on their environment. The state of a cell is in constant flux with every new generation of the simulated environment. This of course depends on the rules imposed on the cells for survival.<br/>
One of the simplest rules for the cells' survival is the state shifting depending on it's current state. So "if state = 0: state = 1" and "if state = 1: state = 0".
This is what one generation on a randomly generated ten by ten board would look like:<br/>
![Cell state change](https://github.com/sekkurocode/Cellular-Automata/assets/119047235/bc2db8f4-dd17-4b28-bae5-cf3a1b29dcb1)


# Conway's Game of Life
We begin with this set of rules, because it is well studied and has known patterns like gliders, which we are able to replicate in our simulation.
The rules are still relatively simple. Any cell with less than two neighbors dies of underpopulation. Any cell with two or three live neighbors lives on to the next generation. Any cell with more than three neighbors dies of overpopulation. Any dead cell with three live neighbors becomes a live cell.<br/>
Below you can see a known pattern, described as Gosper's glider gun, that creates gliders in a regular pattern:<br/>
![Gospers_glider_gun](https://github.com/sekkurocode/Cellular-Automata/assets/119047235/81cd2731-14f0-4f80-906c-382c1ce6aa6b)
