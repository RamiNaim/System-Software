import pygame
from maze_lib import *

RES = (900, 900)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SIZE = 5

class Interface:
	def __init__(self):
		self.screen = pygame.display.set_mode(RES)
		self.clock = pygame.time.Clock()
		self.FPS = 60

	def draw(self):

		self.screen.fill(WHITE)
		self.maze = Labyrinth(30)

		for i in range(60):
			for j in range(60):
				if self.maze.get(i, j) == WALL:
					pygame.draw.rect(self.screen, BLACK, (i*10, j*10, 10, 10))

		pygame.display.update()

	def main(self):

		self.draw()

		while True:
			self.clock.tick(self.FPS)


			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.draw()

			pygame.display.update()


if __name__ == '__main__':
	interface = Interface()
	interface.main()