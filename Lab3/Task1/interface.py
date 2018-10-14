import pygame
from maze_lib import *

RES = (800, 860)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (128, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 250)
SIZE = 40

class Interface:
	def __init__(self, ai=False):
		pygame.init()
		pygame.font.init()
		self.screen = pygame.display.set_mode(RES)
		pygame.display.set_caption('Labyrinth')
		self.clock = pygame.time.Clock()
		self.FPS = 60
		self.font = pygame.font.Font(None, 30)

		self.start_point = (1, 1)
		self.end_point = (57, 57)

		self.hero_x = 1
		self.hero_y = 1

		self.steps = 0

		self.ai_walk = ai


	def draw(self):

		self.maze = Labyrinth(SIZE)

		while True and not self.ai_walk:
			self.hero_x = random.randint(1, 2*(SIZE - 1))
			self.hero_y = random.randint(1, 2*(SIZE - 1))
			if self.maze.get(self.hero_x, self.hero_y) == CELL:
				self.start_point = (self.hero_x, self.hero_y)
				break

		while True and not self.ai_walk:
			x = random.randint(1, 2*(SIZE - 1))
			y = random.randint(1, 2*(SIZE - 1))
			if self.maze.get(x, y) == CELL:
				self.end_point = (x, y)
				break



		self.screen.fill(WHITE)

		pygame.draw.rect(self.screen, BLUE, (self.end_point[0]*10, self.end_point[1]*10, 10, 10) )

		for i in range(2*SIZE):
			for j in range(2*SIZE):
				if self.maze.get(i, j) == WALL:
					pygame.draw.rect(self.screen, BLACK, (i*10, j*10, 10, 10))


		text = self.font.render('Press R to restart', True, BLACK)
		self.screen.blit(text, (10, 810))

		pygame.display.update()

	def main(self):

		self.start_time = time.time()
		self.draw()

		success = False

		while True:
			self.clock.tick(self.FPS)


			if ( self.hero_x, self.hero_y ) == self.end_point:
					while True:
						for event in pygame.event.get():
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_r:
									self.draw()
									self.start_time = time.time()
									self.hero_x = self.start_point[0]
									self.hero_y = self.start_point[1]
									break

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						quit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_r:
						self.draw()
						self.start_time = time.time()
						while True:
							self.hero_x = random.randint(1, 2*(SIZE - 1))
							self.hero_y = random.randint(1, 2*(SIZE - 1))
							if self.maze.get(self.hero_x, self.hero_y) == CELL:
								break

						while True:
							x = random.randint(1, 2*(SIZE - 1))
							y = random.randint(1, 2*(SIZE - 1))
							if self.maze.get(x, y) == CELL:
								self.end_point = (x, y)
								break

					elif event.key == pygame.K_w or event.key == pygame.K_UP:
						if self.maze.get( self.hero_x, self.hero_y - 1 ) != WALL:
							pygame.draw.rect(self.screen, PINK, (self.hero_x*10, self.hero_y*10, 10, 10) )
							self.hero_y = self.hero_y - 1
							self.steps += 1

					elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
						if self.maze.get( self.hero_x, self.hero_y + 1 ) != WALL:
							pygame.draw.rect(self.screen, PINK, (self.hero_x*10, self.hero_y*10, 10, 10) )
							self.hero_y = self.hero_y + 1
							self.steps += 1

					elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
						if self.maze.get( self.hero_x + 1, self.hero_y ) != WALL:
							pygame.draw.rect(self.screen, PINK, (self.hero_x*10, self.hero_y*10, 10, 10) )
							self.hero_x = self.hero_x + 1
							self.steps += 1

					elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
						if self.maze.get( self.hero_x - 1, self.hero_y ) != WALL:
							pygame.draw.rect(self.screen, PINK, (self.hero_x*10, self.hero_y*10, 10, 10) )
							self.hero_x = self.hero_x - 1
							self.steps += 1


			pygame.draw.rect(self.screen, RED, (self.hero_x*10, self.hero_y*10, 10, 10) )


			elapsed_time = time.time() - self.start_time
			el_time = self.font.render("Elapsed time: {0:.2f} s.".format(elapsed_time), True, BLACK, WHITE)
			self.screen.blit(el_time, (370, 810))

			steps_counter = self.font.render("Steps: {}".format(self.steps), True, BLACK, WHITE)
			self.screen.blit(steps_counter, (370, 830))

			pygame.display.update()



if __name__ == '__main__':
	interface = Interface()
	interface.main()
