# A-algorithm
## Problem Definition 
In this project, you are expected to solve a 2-D maze using A*. A maze is path
typically from start node ‘S’ to Goal node ‘E’.

![maze1](https://github.com/KEROLIS/A-algorithm-/blob/master/A*/maze1.png)

**Input :** 2D maze represented as a string.
**Output:** the full path from Start node to End node (Goal Node), direct path to go from Start to End directly and Cost.

**Maze: 'S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,.
#,.,#,E,.,#,.'**

![strmaze](https://github.com/KEROLIS/A-algorithm-/blob/master/A*/string%20maze.png)


* Maze is a string, rows are separated by space and columns are separated by comma ‘,’.
* The board is read row wise, the nodes are numbered 0-based starting the leftmost node.
* You have to create your own board as a 2D array (NO 1D ARRAY ALLOWED) of Nodes.

**EdgeCost: [0, 15, 2, 100, 60, 35,
30, 3, 100, 2, 15, 60,
100, 30, 2, 100, 2, 2,
2, 40, 30, 2, 2, 100,
100, 3, 15, 30, 100, 2,
100, 0, 2, 100, 30]**

* Edge cost is a list, will be passed for A*.
* Each Node has an edge value that represents the cost from any parent node to this node.

## Introduction to the algorthem  
This algorthem is often used for the common pathfinding
problem in applications such as video games, but was originally
designed as a general graph traversal algorithm. It finds
applications in diverse problems, including the problem of
parsing using stochastic grammars in NLP her cases include an
Informational search with online learning.
you can read more [here](https://brilliant.org/wiki/a-star-search/)

![A](https://github.com/KEROLIS/A-algorithm-/blob/master/A*/A.gif)

## Discussion

There are many additions to the code :
1. The Node class :
  Class Node represents a cell in the board of game.
A. I added the position attribute to the node class to make the navigation between the nodes more easier and knowing the actual position of the each node in the 2d grid .
B. the inform function :
  this function is used to fill the values of edge cost and position of each object node .
2. The SearchAlgorithms class :
A. the attributes
  mazeBoard : this attribute holds the 2d maze matrix
  startNode : the first node in the path .
  goalNode : the target node to reach in the grid .
  mazeHight : the length of the hight dimension at the maze matrix .
  MazeWidth : the length of the width dimension at the maze matrix .
B. the constructor :
  I used the list comprehension and the function split to turn the input string into 2 dimension array then get hight and width of the mazethen nested for loop to replace each value of the grid with a node object . Then calculate the heuristic for the first node in the grid .
C. The getNode functions :
  this functions works to return the the surrounded nodes by position and return the (#) if the position is out of the maze instead of padding the grid with (#)value.
D. add_to_open function :
  It checks if the neighbor node is not in open list .
  E. AstarManhattanHeuristic function :
  the main steps of the algorithm as mentioned above .
