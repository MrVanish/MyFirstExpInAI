import pygame

class GameScreen:

	def update(self):
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
		

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		while True:
			self.update()

GameScreen()