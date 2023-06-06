# Path-finding-A-star
### Artificial Intelligence Project
path planning problem using A-star algorithm 

## Project description 
the environment of the robot is represented by a grid map in which the initial and goal states are clearly localized on the map.
Part of the cells in the map contain obstacles in which the robot cannot traverse over them to reach the goal.
The robot can move one step horizontally, vertically, or diagonally from a cell to another neighbor free cell (i.e., the maximum number of reachable neighbor cells with one transition is 8). The actual cost is one for each horizontal or vertical move and
√2 for the diagonal one.

## Project Aim 
The aim of this project is to design and implement the A* searching technique for solving the 
path planning problem. 

## Heuristic function
In this project, the L∞ (L-infinity) heuristic function ia used, also known as the Chebyshev distance or maximum heuristic, is a distance metric that calculates the maximum difference between the coordinates of two points in a grid. In the context of pathfinding algorithms, it is used to estimate the minimum number of moves required to reach the goal state from a given state.
In a grid, where diagonal movement is allowed with a cost of 1 or √2, the L∞ heuristic calculates the maximum of the absolute.
This heuristic function provides a more accurate estimate of the actual cost required to reach the goal state when diagonal movements are allowed.

## Visualization 
For the search visualization, we used tkinter , which is a standard GUI library in Python that provides a set of tools for creating windows, buttons, canvas, and other graphical elements. In the code tkinter ,is used to create a window and a canvas widget to draw the maze. The Canvas widget is used to display rectangles representing the maze cells, with different colors for obstacles, start state, goal state, and the path.



![image](https://github.com/Raghad-Aldakhil/Path-finding-A-star/assets/121506944/b8fd43a8-f78d-4fa8-a031-6ce8bf130d24)


## Limitations 
<ul>
<li> the goal and initial states are fixed </li>.
<li> this code will randomly generate test problems on grids of size 100 and varying the percentage of obstacles from 10 to 90.</li>
<li> the gui somtimes becomes irresponsive, if the the algorithms is searching for a path, or if the input was from 70 and above obstacles </li>
<li> obsatcles are generated randomly based on the input percentage</li>

  
  


</ul>
