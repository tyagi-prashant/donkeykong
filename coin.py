import pygame
import block

coinImage = pygame.image.load('coin.jpg')

class Coin():
	def __init__(self,coin_sprite):
		self.coin = []
		for i in range(24):
			nextcoin = block.Block(coinImage,10,10)
			self.coin.append( nextcoin )
			coin_sprite.add(self.coin[i])
		
		import random
		x_1 = random.sample (range(10,780),4)
		for i in range(0,4) :
			self.coin[i].rect.x = x_1[i]
			self.coin[i].rect.y = 480
		
		x_1 = random.sample (range(10,540),4)
		for i in range(4,8) :
			self.coin[i].rect.x = x_1[i-4]
			self.coin[i].rect.y = 410
	
		x_1 = random.sample (range(250,780),4)
		for i in range(8,12) :
			self.coin[i].rect.x = x_1[i-8]
			self.coin[i].rect.y = 330
		
		x_1 = random.sample (range(10,640),4)
		for i in range(12,16) :
			self.coin[i].rect.x = x_1[i-12]
			self.coin[i].rect.y = 250
		

		x_1 = random.sample (range(200,780),4)
		for i in range(16,20) :
			self.coin[i].rect.x = x_1[i-16]
			self.coin[i].rect.y = 170

		x_1 = random.sample (range(10,640),4)
		for i in range(20,24) :
			self.coin[i].rect.x = x_1[i-20]
			self.coin[i].rect.y = 90
