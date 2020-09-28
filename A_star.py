# -*- coding: utf-8 -*-
from math import sqrt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from random import seed
from random import randrange
from csv import reader
from math import sqrt
import random
r = random.Random()
r.seed("AI")


import math


# region SearchAlgorithms
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False

    def exists(self, value):
        if value not in self.stack:
            return True
        else:
            return False

    def pop(self):
        if len(self.stack) <= 0:
            return ("The Stack == empty")
        else:
            return self.stack.pop()

    def top(self):
        return self.stack[0]


class Node:
    id = None  
    up = None 
    down = None 
    left = None
    right = None 
    previousNode = None 
    edgeCost = None
    gOfN = 0  # total edge cost
    hOfN = None  # heuristic value
    heuristicFn = None
    position = None     

    def __init__(self, value):
        self.value = value
        
    def inform(self,id , position , edgeCost)   :
        self.id = id
        self.edgeCost = edgeCost
        self.position = position


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = 0
    mazeBoard= None
    startNode = None 
    goalNode = None
    mazeHight=None
    mazeWidth=None
    

    def __init__(self, mazeStr,edgeCost = -1):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
        mazeStr=mazeStr.split()
        self.mazeBoard=[s.split(',') for s in mazeStr]   
        self.mazeHight=len(self.mazeBoard)
        self.mazeWidth=len(self.mazeBoard[0])
        
        id = 0
        for i in range(0,len(self.mazeBoard)):
            for j in range (0, len(self.mazeBoard[0])):
                
                if self.mazeBoard[i][j]=='E' : 
                   self.mazeBoard[i][j]= Node (self.mazeBoard[i][j])
                   self.mazeBoard[i][j].inform(id,(i,j),edgeCost[id])
                   self.goalNode=self.mazeBoard[i][j]
                                   
                elif self.mazeBoard[i][j]=='S' :
                   self.mazeBoard[i][j]= Node (self.mazeBoard[i][j])
                   self.mazeBoard[i][j].inform(id,(i,j),edgeCost[id])
                   self.mazeBoard[i][j].gOfN= edgeCost[id]                  
                   self.startNode=self.mazeBoard[i][j]
                   
                                                     
                else : 
                   self.mazeBoard[i][j]= Node (self.mazeBoard[i][j])
                   self.mazeBoard[i][j].inform(id,(i,j),edgeCost[id])
                
                id+=1
        self.startNode.hOfN=abs(self.startNode.position[0] - self.goalNode.position[0]) + abs(self.startNode.position[1] - self.goalNode.position[1])
        self.startNode.heuristicFn=self.startNode.hOfN+self.startNode.gOfN
        pass
    
    def getNode(self,position) :
        
            for i in range(0,len(self.mazeBoard)):
                for j in range (0, len(self.mazeBoard[0])):
                    if position == self.mazeBoard[i][j].position :
                        return self.mazeBoard[i][j]
            return Node('#')
        
    def getUpNode (self,position) :
            x=position[0]-1
            if x<0:
                return Node('#')
            y=position[1]
            return self.getNode((x,y))
        
    def getDownNode (self,position):
            x=position[0]+1
            if x>self.mazeHight-1:
                return Node('#')
            y=position[1]
            return self.getNode((x,y))
        
    def getRightNode(self,position) :
            y=position [1]+1
            if y>self.mazeWidth-1:
                return Node('#')            
            x=position[0]
            return self.getNode((x,y))
        
    def getLeftNode(self,position) :
            y=position[1]-1
            if y<0:
                return Node('#')
            x=position[0]
            return self.getNode((x,y))
    
        
    def AstarManhattanHeuristic(self):
        openList=[self.startNode]
        i=len(openList)
        while i > 0 :
            current_node = openList[0]
            current_index = 0
            for index, item in enumerate(openList):
                if item.heuristicFn < current_node.heuristicFn :
                    current_node = item
                    current_index = index    
            openList.pop(current_index)
            self.fullPath.append(current_node)
            if current_node == self.goalNode:
                    self.path=[]
                    for i in range(0,len(self.fullPath)):
                            self.fullPath[i]=self.fullPath[i].id
                    current = current_node
                    while current is not None:
                        self.path.append(current.id)
                        self.totalCost+=current.gOfN
                        current = current.previousNode
                    self.path=self.path[::-1]    
                    return self.fullPath, self.path, self.totalCost
            current_node.up=self.getUpNode(current_node.position)
            current_node.down=self.getDownNode(current_node.position)
            current_node.right=self.getRightNode(current_node.position)
            current_node.left=self.getLeftNode(current_node.position)
            neighbors = [current_node.up, current_node.down, current_node.right, current_node.left]
            for next in neighbors:
                    # Check if the node is a wall
                    if next in self.fullPath:
                        continue
                    if next.value == '#' :
                        continue                            
                    neighbor = next
                    neighbor.previousNode=current_node
                    # Generate heuristics (Manhattan distance)
                    neighbor.gOfN = neighbor.edgeCost+self.totalCost
                    neighbor.hOfN = abs(neighbor.position[0] - self.goalNode.position[0]) + abs(neighbor.position[1] - self.goalNode.position[1])
                    neighbor.heuristicFn = neighbor.gOfN + neighbor.hOfN
                    # Everything is green, add neighbor to open list
                    if self.add_to_open(openList, neighbor) : openList.append(neighbor)
                        
        
                
    
    def add_to_open(self,openList, neighbor):
        for node in openList:
            if (neighbor == node and neighbor.heuristicFn >= node.heuristicFn):
                return False
        return True
    
# region Search_Algorithms_Main_Fn
def SearchAlgorithm_Main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.',
                                  [0, 15, 2, 100, 60, 35, 30, 3
                                          , 100, 2, 15, 60, 100, 30, 2
                                          , 100, 2, 2, 2, 40, 30, 2, 2
                                          , 100, 100, 3, 15, 30, 100, 2
                                          , 100, 0, 2, 100, 30])
    fullPath, path, TotalCost = searchAlgo.AstarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic ** Full Path:' + str(fullPath) + '\nPath is: ' + str(path)
          + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

# endregion

if __name__ == '__main__':

    SearchAlgorithm_Main()
    