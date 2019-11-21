import pygame
from Creature import Creature
import keyboard
import concurrent.futures

class GameScreen:

	def update(self):
		for i in pygame.event.get():
			if keyboard.is_pressed('q'):
				exit()
			if keyboard.is_pressed('w'):
				self.creature.getUp()
			if keyboard.is_pressed('s'):
				self.creature.getDown()
			if keyboard.is_pressed('a'):
				self.creature.getLeft()
			if keyboard.is_pressed('d'):
				self.creature.getRight()
			
		###################################
		self.screen.blit(self.background,(0,0))
		pygame.draw.rect(self.screen, (255, 0, 0),
						(pygame.display.get_surface().get_width()/2-50, 20,100, 100)
						,1)
		self.creature.update(self.screen)
		###################################
		pygame.display.update()

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		pygame.display.update()
		pygame.draw.rect(self.screen, (255, 0, 0),
						(pygame.display.get_surface().get_width()/2-50, 20,100, 100)
						,1)
		self.background = pygame.transform.scale(pygame.image.load("CreatureModel/back.png").convert(),
                                                 ((pygame.display.get_surface()).get_width(), (pygame.display.get_surface()).get_height()))
		self.creature = Creature(pygame.image.load("CreatureModel/modelOne.png").convert_alpha())
		while True:
			self.clock.tick(120)
			self.update()
			
		

GameScreen()