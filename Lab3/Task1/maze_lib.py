import pygame
import numpy as np


class Cell:
    def __init__(self, x=0, y=0, wall=False):
        self.x = x
        self.y = y
        self.wall = wall
    def get_coord(self):
        return (self.x, self.y)



class Labyrinth:
    def __init__(self, dim):
        self.dim = dim
        self.maze = []
        for i in range(dim*2):
            self.maze.append([])
            for j in range(dim*2):
                if ((i % 2 != 0) and (j % 2 != 0)) and ((i < (self.dim - 1)*2) and (j < (self.dim - 1)*2)):    
                    self.maze[i].append(Cell(x=i, y=j, wall=False))
                else:
                    self.maze[i].append(Cell(x=i, y=j, wall=True))


        for i in range(2*self.dim):
            for j in range(2*self.dim):
                if self.maze[i][j].wall:
                    print(" - ", end='')
                else:
                    print(" + ", end='')
                #print( self.maze[i][j].wall, end="; " )
            print()

        #self.generate()

    def generate(self):
        stack = []
        visited = []
        not_visited = []

        for i in range(self.dim):
            for j in range(self.dim):
                if (i, j) != (0, 0):
                    not_visited.append((i, j))
                else:
                    visited.append((i, j))

    #while not not_visited:


l = Labyrinth(6)