import pygame
import random

import coin
import block
import boardlayout
import fireball
import checkcollision
import freefall
import checkwall

BLACK = (0,0,0)
BLUE=(0,0,255)
RED=(255,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
COIN=(10,124,50)

screen_width=800
screen_height=600

block_list = pygame.sprite.Group()  #sprite groups
ladder_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
fire_sprite = pygame.sprite.Group()
donkey_sprite = pygame.sprite.Group()
queen_sprite = pygame.sprite.Group()
coin_sprite = pygame.sprite.Group()
 
screen=pygame.display.set_mode((screen_width,screen_height))

donkeyImage= pygame.image.load('dragon.jpg')
playerImage = pygame.image.load('player.jpg')
queenImage = pygame.image.load('queen.jpg')

clock=pygame.time.Clock()

queen = block.Block(queenImage,20,20)
queen.rect.x=250
queen.rect.y=30
queen_sprite.add(queen)


class Person():
	def __init__(self):
		self.donkey = block.Block(donkeyImage, 20 ,20)
		self.donkey.rect.x = 10
		self.donkey.rect.y = 80
		
		self.player = block.Block(playerImage,15,15)  
		self.score = 0
		self.player.rect.x = 15
		self.player.rect.y = 475	
					
class Donkey(Person):
	def returndonkey(self):
		return self.donkey
		
	def moveRandom(self):
		import random
		a = random.randint(1,2)
		if a==2 :
			check = checkwall.checkWall(self.donkey , self.donkey.rect.x , self.donkey.rect.y , 20, 10, block_list)
			if check != 0 :
				self.donkey.rect.x += 20
		else :
			check = checkwall.checkWall (self.donkey, self.donkey.rect.x, self.donkey.rect.y , -20 , 0 , block_list)
			if check== 0 :
				self.donkey.rect.x -= 20
		

class Player(Person):
	def returnplayer(self):
		return self.player

	def jump(self):
		return self.player
		
	def playerScore(self):
		player_score = pygame.sprite.spritecollide(self.player,coin_sprite,True)
	
		if len(player_score)>0:
			return 1
		else:
			return 0
		
		
	def moveRight(self):
		__check = checkwall.checkWall(self.player , self.player.rect.x , self.player.rect.y , 10 , 0, block_list)
		if __check == 0 :
			self.player.rect.x += 10	
			freefall.freeFall(self.player,ladder_list, block_list)
					
	def moveLeft(self):
		__check = checkwall.checkWall(self.player , self.player.rect.x , self.player.rect.y , -10 , 0, block_list)
		if __check == 0 :	
			self.player.rect.x -= 10
			freefall.freeFall(self.player,ladder_list, block_list)
						
	def moveDown(self):		
		__check = checkcollision.checkCollision(self.player , ladder_list , self.player.rect.x , self.player.rect.y , 0 , 15)
		if __check > 0 :
			self.player.rect.y  += 10				
			boardObj.printLayout(block_list,ladder_list,fire_sprite,donkey_sprite,queen_sprite,coin_sprite,player_sprite,screen)

	def moveUp(self):
		__check = checkcollision.checkCollision(self.player ,ladder_list, self.player.rect.x , self.player.rect.y , 0 , 0)
		if __check > 0 :
			self.player.rect.y -= 10
			boardObj.printLayout(block_list,ladder_list,fire_sprite,donkey_sprite,queen_sprite,coin_sprite,player_sprite,screen)

	def gameover(self):
		__check = checkcollision.checkCollision(self.player ,donkey_sprite, self.player.rect.x , self.player.rect.y , 0 , 0)
		if __check > 0 :
			return 1
		else:
			return 0
	
	def levelcomplete(self):
		check = checkcollision.checkCollision(self.player ,queen_sprite, self.player.rect.x , self.player.rect.y , 0 , 0)
		if check > 0 :
			return 1
		else:
			return 0

	def playerHitFire(self):
		player_collide_fire = pygame.sprite.spritecollide(self.player,fire_sprite,True)
		if len (player_collide_fire) > 0 :
			self.player.rect.x=15
			self.player.rect.y=475 
			return 1
		else:
			return 0

pygame.init()
pygame.display.set_caption("Donkey Kong")

gamestart = 0
gamelevel = 1
score = 0
player_life = 3
firespeed = 50

gameExit=False


while not gameExit:
	if gamestart == 0:
		block_list.empty()
		ladder_list.empty()
		all_sprite_list.empty()
		player_sprite.empty()
		fire_sprite.empty()
		donkey_sprite.empty()
		queen_sprite.empty()
		coin_sprite.empty()
		
		screen.fill(BLACK)
		queen_sprite.add(queen)
		
		#Objects
		coinObj = coin.Coin(coin_sprite)
		boardObj=boardlayout.boardLayout(ladder_list,block_list)
		
		donkeyObj=Donkey()
		donkey=donkeyObj.returndonkey()
		donkey_sprite.add(donkey)
		donkey_sprite.draw(screen)
		
		playerObj=Player()
		player=playerObj.returnplayer()
		player_sprite.add(player)
		
		fireballObj = fireball.fireBall(fire_sprite)
		fireCreator = 1
		jumping = 0
		boardObj.printLayout(block_list,ladder_list,fire_sprite,donkey_sprite,queen_sprite,coin_sprite,player_sprite,screen)


	gamestart =1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit=True
			
		if playerObj.gameover() == 1:
			gamestart = 1
			player_life = 0
				
		if gamestart !=0 and player_life == 0 and event.type == pygame.KEYDOWN:
			if event.key != pygame.K_RETURN:
				gamestart = 1
			else:
				gamestart = 0
				gamelevel = 1
				score = 0
				player_life = 3
				firespeed -= 3

		if event.type == pygame.KEYDOWN and jumping ==0:			
			if event.key == pygame.K_SPACE :
				player=playerObj.jump()
				player.rect.y -= 20
				boardObj.printLayout(block_list,ladder_list,fire_sprite,donkey_sprite,queen_sprite,coin_sprite,player_sprite,screen)
				pygame.display.update()
				jumping=1
		
	keydown = pygame.key.get_pressed()		
	if keydown[pygame.K_q]:
		gameExit=True
		
	if playerObj.gameover() == 1:
		gamestart = 1
		player_life = 0
	
	if gamestart !=0 and player_life == 0 :
		myfont = pygame.font.SysFont("monospace", 15)
		# render text	
		label = myfont.render("Game Over   Press Enter to Restart or q to Exit" , 2, WHITE)
		screen.blit( label, (300 , 550 ))
		pygame.display.update()
		
	else:
		keydown = pygame.key.get_pressed()			
		
		if keydown[pygame.K_d]:
			playerObj.moveRight()	
					
		if keydown[pygame.K_a]:
			playerObj.moveLeft()	
					
		if keydown[pygame.K_w]:
			playerObj.moveUp()	
					
		if keydown[pygame.K_s]:
			playerObj.moveDown()
				
		if jumping == 1 :
			player=playerObj.jump()
			player.rect.y -= 15
			boardObj.printLayout(block_list,ladder_list,fire_sprite,donkey_sprite,queen_sprite,coin_sprite,player_sprite,screen)
			pygame.display.update()	
			jumping=0 
			
			if keydown[pygame.K_d]:
				playerObj.moveRight()	
						
			if keydown[pygame.K_a]:
				playerObj.moveLeft()	
						
			if keydown[pygame.K_w]:
				playerObj.moveUp()	
						
			if keydown[pygame.K_s]:
				playerObj.moveDown()
			
			freefall.freeFall(player,ladder_list, block_list)
			
		if playerObj.playerScore() == 1:
			score += 5
			
		if playerObj.playerHitFire() == 1:
			player_life -=1
			score -= 25
			if score<0:
				score =0
			
		if playerObj.levelcomplete() == 1: 
			gamelevel += 1
			gamestart = 0
			player_life = 3
			
		fireCreator+=1
		if fireCreator % firespeed == 0 :
			fireballObj.addFireball(fire_sprite)
	
	
			
	myfont = pygame.font.SysFont("monospace", 15)
	# render text	
	label = myfont.render("Score : " + str(score), 1, (255,255,255))
	screen.blit(label, (30 , 540 ))
	label = myfont.render("Life : " + str(player_life), 2, (255,255,255))
	screen.blit(label, (180 , 540 ))
	label = myfont.render("Level : " + str(gamelevel), 2, (255,255,255))
	screen.blit(label, (100 , 560 ))

	pygame.display.update()
		
			
	fireballObj.move(ladder_list, block_list,fire_sprite,screen)
	donkeyObj.moveRandom()	
	boardObj.printLayout(block_list,ladder_list,fire_sprite,donkey_sprite,queen_sprite,coin_sprite,player_sprite,screen)

	clock.tick(10)
	pygame.display.update()
		
		
pygame.quit()
quit()
