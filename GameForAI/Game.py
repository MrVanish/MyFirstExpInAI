import pygame

class GameScreen:

	def update(self):
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
		###################################
		
		###################################
		pygame.display.update()

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		pygame.display.update()
		while True:
			self.clock.tick(120)
			self.update()
			
		

GameScreen()