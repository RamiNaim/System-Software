import pygame
import random, time
from math import copysign

random.seed(time.time())


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

        self.generate()
        print()
        print()
        print()

        for i in range(2*self.dim):
            for j in range(2*self.dim):
                if self.maze[i][j].wall:
                    print(" - ", end='')
                else:
                    print(" + ", end='')
            #print( self.maze[i][j].wall, end="; " )
            print()
        print()

    def generate(self):
        stack = []
        visited = [self.maze[1][1]]

        not_visited = self.getUnvisited(visited)

        start_cell = self.maze[1][1]
        currentCell = start_cell

        while not_visited:
            print(len(not_visited))
            neighbours = self.getNeighbours(start_cell, visited)
            if neighbours:
                neighbourCell = random.choice( neighbours )
                stack.append( neighbourCell )
                visited = self.removeWall(currentCell, neighbourCell, visited)
                currentCell = neighbourCell
                visited.append( currentCell )
            elif stack:
                start_cell.pop()
            else:
                not_visited = self.getUnvisited( visited )
                currentCell = random.choice( not_visited )

    def removeWall(self, first, second, v):
        dx = second.x - first.x
        dy = second.y - first.y

        if dx == 0:
            addx = 0
        else:
            addx = copysign(1, dx)

        if dy == 0:
            addy = 0
        else:
            addy = copysign(1, dy)

        #print("Im breaking walls")

        x = int(first.x + addx)
        y = int(first.y + addy)

        self.maze[x][y].wall = False
        v.append( self.maze[x][y] )
        return v


    def getNeighbours(self, cell, v):
        up = (cell.x, cell.y+2)
        down = (cell.x, cell.y-2)
        right = (cell.x+2, cell.y)
        left = (cell.x-2, cell.y)
        neighbours = [up, down, right, left]
        cells = []

        for n in neighbours:
            if ( self.maze[n[0]][n[1]].x > 0 and self.maze[n[0]][n[1]].x < self.dim*2 ) and ( self.maze[n[0]][n[1]].y > 0 and self.maze[n[0]][n[1]].y < self.dim*2 ):
                currentCell = self.maze[n[0]][n[1]]
                #print(currentCell.wall, self.cellInList(currentCell, v), sep="; ")

                if not currentCell.wall and not self.cellInList(currentCell, v):
                    cells.append(currentCell)

        return cells
 

    def cellInList(self, cell, l):
        for c in l:
            if (cell.x == c.x) and (cell.y == c.y):
                return (c.x, c.y)
            else:
                return False


    def getUnvisited(self, v):
        unvisited = []
        for i in range(2*self.dim):
            for j in range(2*self.dim):
                if not self.cellInList(self.maze[i][j], v):
                    unvisited.append( self.maze[i][j] )

        return unvisited



l = Labyrinth(6)