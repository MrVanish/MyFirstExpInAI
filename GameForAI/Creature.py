import pygame
import threading
import time

class Creature():

	def Up(self):
		for i in range(10):
			time.sleep(0.1)
			self.posY = self.posY - 2
			self.posX = self.posX + 1
			
	def Left(self):
		for i in range(10):
			self.posX = self.posX - 2
	
	def Right(self):
		for i in range(10):
			self.posX = self.posX + 2
	
	def Down(self):
		for i in range(10):
			self.posY = self.posY + 2
			self.posX = self.posX - 1
			
	def __init__(self,model):
		self.posX = 0
		self.posY = (pygame.display.get_surface()).get_height()-50
		self.creatureModel = model

		
	def update(self,screen):
		screen.blit(self.creatureModel,(self.posX,self.posY)) 
	
	def getLeft(self):
		(threading.Thread(target = self.Left)).start()

	def getRight(self):
		(threading.Thread(target = self.Right)).start()

	def getUp(self):
		(threading.Thread(target = self.Up)).start()

	def getDown(self):
		(threading.Thread(target = self.Down)).start()

