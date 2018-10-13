import pygame
import sys
sys.path.append('../')
from Task1.maze_lib import *


WALL = True
CELL = False
SIZE = 40

RES = (800, 860)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 250)
SIZE = 40

class MazeWalker:
	def __init__(self):
		self.visited = []
		self.labyrinth = Labyrinth(SIZE)
		self.steps = 0

		self.success = False

		self.prior = [ 0 for i in range(2*SIZE*2*SIZE) ]

		while True:
			self.x = random.randint(1, 2*(SIZE - 1))
			self.y = random.randint(1, 2*(SIZE - 1))
			if self.labyrinth.get(self.x, self.y) == CELL:
				self.start_point = (self.x, self.y)
				break

		while True:
			x_goal = random.randint(1, 2*(SIZE - 1))
			y_goal = random.randint(1, 2*(SIZE - 1))
			if self.labyrinth.get(x_goal, y_goal) == CELL:
				self.end_point = (x_goal, y_goal)
				break



		self.walk(self.start_point)

	def walk(self, start, prev=None):

		if prev:
			print(start)
			self.prior[ start[0]*40 + start[1] ] = prev


		if start == self.end_point or self.success:
			self.success = True
			return

		self.visited.append(start)

		neighbours = self.getNeighbours(start)
		num_of_neighbours = len(neighbours)
		
		while num_of_neighbours == 1:
			self.steps += 1
			self.prior[ start[0]*40 + start[1] ] = neighbours[0]
			start = neighbours[0]
			self.visited.append(start)
			if start == self.end_point or self.success:
				self.success = True
				return
			neighbours = self.getNeighbours(start)
			num_of_neighbours = len(neighbours)
			#print(len(neighbours))

		for n in neighbours:
			self.steps += 1
			self.walk(n, start)
			if self.success:
				return
			self.steps += 1

		if start == self.end_point:
			print(self.steps)


	def get_path(self):
		current_cell = self.end_point
		self.path = [current_cell]
		while current_cell != self.start_point:
			print(current_cell)
			prev_step = self.prior[current_cell]
			self.path.append( prev_step )
			current_cell = prev_step

		self.path.reverse()





	def draw_path(self):
		#self.get_path()
		pygame.init()
		pygame.font.init()
		self.font = pygame.font.Font(None, 30)
		self.screen = pygame.display.set_mode(RES)

		self.screen.fill(WHITE)

		for i in range(2*SIZE):
			for j in range(2*SIZE):
				if self.labyrinth.get(i, j) == WALL:
					pygame.draw.rect(self.screen, BLACK, (i*10, j*10, 10, 10))


		for i in range(2*SIZE):
			for j in range(2*SIZE):
				if (i, j) in self.visited:
					pygame.draw.rect(self.screen, GREEN, (i*10, j*10, 10, 10))


		pygame.draw.rect(self.screen, BLUE, (self.end_point[0]*10, self.end_point[1]*10, 10, 10) )
		pygame.draw.rect(self.screen, RED, (self.start_point[0]*10, self.end_point[1]*10, 10, 10) )

		#for cell in self.path:
		#	pygame.draw.rect(self.screen, PINK, (cell[0]*10, cell[1]*10, 10, 10) )


		text = self.font.render('Steps: {}'.format(self.steps), True, BLACK)
		self.screen.blit(text, (10, 810))

		pygame.display.update()


		while True:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						quit()




	def getNeighbours(self, cell):
		up = (cell[0], cell[1]+1)
		down = (cell[0], cell[1]-1)
		right = (cell[0]+1, cell[1])
		left = (cell[0]-1, cell[1])
		neighbours = [up, down, right, left]
		cells = []

		for n in neighbours:
			if ( n[0] > 0 and n[0] < self.labyrinth.dim*2 ) and ( n[1] > 0 and n[1] < self.labyrinth.dim*2  ):

				if ( not self.labyrinth.get(n[0], n[1]) == WALL ) and not ( n in self.visited ):
					cells.append(n)

		return cells


if __name__ == '__main__':
	ai = MazeWalker()
	ai.draw_path()