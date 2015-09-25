import block
import pygame
import freefall
import checkwall
import checkcollision
import random

fireballImage = pygame.image.load('fireball.jpg')

class fireBall(): 
	def __init__(self,fire_sprite):
		self.countstart = 0
		self.countend = 1
		self.fire = []
		self.fire.append( block.Block (fireballImage,10,10) )
		self.fire[0].rect.x = 10
		self.fire[0].rect.y = 90
		
		self.fire_p = []
		self.fire_p.append(0)
		
		fire_sprite.add(self.fire[0])
		
	def addFireball(self,fire_sprite):
		self.fire.append( block.Block (fireballImage,10,10) )
		self.fire[self.countend].rect.x = 10
		self.fire[self.countend].rect.y = 90
		
		fire_sprite.add(self.fire[self.countend])
		
		self.countend += 1
		self.fire_p.append(0)
		
	def move(self,ladder_list, block_list,fire_sprite,screen):
		for i in range(self.countstart,self.countend):
			if self.fire[i].rect.x == 10 and self.fire[i].rect.y == 480:
				fire_sprite.remove(self.fire[i])
				
			freefall.freeFall(self.fire[i],ladder_list, block_list)
			
			fire_sprite.draw(screen)
			if self.fire_p[i] == 0:
				check = checkwall.checkWall(self.fire[i] , self.fire[i].rect.x , self.fire[i].rect.y , 10 , 0, block_list)
				if check == 0 :		
					check = checkcollision.checkCollision(self.fire[i] , ladder_list, self.fire[i].rect.x , self.fire[i].rect.y , 0 , 10)

					if check == 0 : 
						self.fire[i].rect.x += 10
						fire_sprite.draw(screen)
					else :
						a = random.randint(1,3)
						if a == 1 : 
							self.fire[i].rect.x += 10				
							self.fire_p[i] = 1					
						else:
							self.fire[i].rect.y += 10
							self.fire_p[i] = 2
				else :
					self.fire[i].rect.x -= 10
					self.fire_p[i] = 3
				
			elif self.fire_p[i] == 1 :
				check = checkwall.checkWall(self.fire[i] , self.fire[i].rect.x , self.fire[i].rect.y , 10 , 0, block_list)
				if check == 0 :
					check = checkwall.checkWall(self.fire[i] , self.fire[i].rect.x , self.fire[i].rect.y , 10 , 10, block_list)
					if check != 0 :
						self.fire[i].rect.x += 10
					
					else :
						self.fire[i].rect.x += 10
						self.fire_p[i] = 4
				else:
					self.fire_p[i] = 3
					
			elif self.fire_p[i] == 2 : 
				check = checkcollision.checkCollision(self.fire[i], ladder_list , self.fire[i].rect.x , self.fire[i].rect.y , 0 , 10)
				if check != 0 :
					self.fire[i].rect.y += 10
				else :
					a = random.randint(1,3)
					if a == 1 : 
						self.fire_p[i] = 0					
					else:
						self.fire_p[i] = 1
			
			elif self.fire_p[i] == 4:
				freefall.freeFall(self.fire[i],ladder_list, block_list)
				a=random.randint(1,3)
				if a==1:
					self.fire_p[i] = 0
				else:
					self.fire_p[i] = 3
					
			if self.fire_p[i] == 3 :
				check = checkwall.checkWall(self.fire[i] , self.fire[i].rect.x , self.fire[i].rect.y , -10 , 0, block_list)
				if check == 0 :
					check = checkcollision.checkCollision(self.fire[i],ladder_list , self.fire[i].rect.x , self.fire[i].rect.y , 0 , 10)
					if check == 0 : 
						self.fire[i].rect.x -= 10
						fire_sprite.draw(screen)
					else :
						a = random.randint(1,3)
						if a == 1 : 
							self.fire[i].rect.x -= 10				
							self.fire_p[i] = 5					
						else:
							self.fire[i].rect.y += 10
							self.fire_p[i] = 2
				
				else:
					self.fire_p[i] = 0
	
			if self.fire_p[i] == 5 :
				check = checkwall.checkWall(self.fire[i] , self.fire[i].rect.x , self.fire[i].rect.y , -10 , 0, block_list)
				if check == 0 :
					check = checkwall.checkWall(self.fire[i] , self.fire[i].rect.x , self.fire[i].rect.y , 10 , 10, block_list)
					
					if check != 0 :
						self.fire[i].rect.x -= 10
					else :
						self.fire[i].rect.x -= 10
						self.fire_p[i] = 4
				else:
					self.fire_p[i] = 0
