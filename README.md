# Cellular-Automata and Emergent Structures
The goal of this githun project is the development of a python software, simulating "Cellular Automata".
Cellular Automata are cells, which usually are in one of two **states**, 0 or 1. If a cell is in the state "0" it is in the dead state, meaning it won't have any influence on the cells around it. In the "1" state cells count as alive and take effect on their environment. The state of a cell is in constant flux with every new generation of the simulated environment. This of course depends on the rules imposed on the cells for survival. The simplest rule for the cells' survival is that the state shifts depending on the cell's current state. So "if state = 0: state = 1" and "if state = 1: state = 0".

# Conway's Game of Life
We begin with this form of Cellular Automata, because it is well understood and has fun patterns like gliders
![Gospers_glider_gun](https://github.com/sekkurocode/Cellular-Automata/assets/119047235/81cd2731-14f0-4f80-906c-382c1ce6aa6b)
