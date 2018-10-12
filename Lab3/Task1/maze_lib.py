import random, time
from math import copysign

random.seed(time.time())

WALL = True
CELL = False


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
                    self.maze[i].append(CELL)
                else:
                    self.maze[i].append(WALL)


        self.generate()


    def get(self, i, j):
        return self.maze[i][j]


    def print_maze(self):
        for i in range(2*self.dim):
            for j in range(2*self.dim):
                if self.maze[i][j] == WALL:
                    print(" - ", end='')
                else:
                    print(" + ", end='')
            print()
        print()

    def generate(self):

        stack = []
        visited = [ (1, 1) ]

        not_visited = self.getUnvisited(visited)

        start_cell = (1, 1)
        currentCell  = start_cell


        while len(not_visited) != 0:
            neighbours = self.getNeighbours(currentCell, visited)
            if neighbours:
                neighbourCell = random.choice( neighbours )
                stack.append( currentCell )
                visited, not_visited = self.removeWall(currentCell, neighbourCell, visited, not_visited)
                currentCell = neighbourCell
                visited.append( currentCell )
                not_visited.remove( currentCell )
                neighbours = 0
            elif stack:
                currentCell = stack.pop()
            else:
                currentCell = random.choice( not_visited )
                visited.append( currentCell )
                not_visited.remove( currentCell )


    def removeWall(self, first, second, v, nv):
        dx = second[0] - first[0]
        dy = second[1] - first[1]

        if dx == 0:
            addx = 0
        else:
            addx = copysign(1, dx)

        if dy == 0:
            addy = 0
        else:
            addy = copysign(1, dy)

        x = int(first[0] + addx)
        y = int(first[1] + addy)

        self.maze[x][y] = CELL
        v.append( (x, y) )
        nv.remove( (x, y) )

        return v, nv


    def getNeighbours(self, cell, v):
        up = (cell[0], cell[1]+2)
        down = (cell[0], cell[1]-2)
        right = (cell[0]+2, cell[1])
        left = (cell[0]-2, cell[1])
        neighbours = [up, down, right, left]
        cells = []

        for n in neighbours:
            if ( n[0] > 0 and n[0] < self.dim*2 ) and ( n[1] > 0 and n[1] < self.dim*2  ):

                if ( not self.maze[n[0]][n[1]] == WALL ) and not ( n in v ):
                    cells.append(n)

        return cells
 


    def getUnvisited(self, v):
        unvisited = []
        for i in range(1, 2*self.dim):
            for j in range(1, 2*self.dim):
                if not (i, j) in v:
                    unvisited.append( (i, j) )

        return unvisited