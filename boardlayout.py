import block
import random
import pygame

BLACK = (0,0,0)

wallImage = pygame.image.load('wall.jpg')
ladderImage = pygame.image.load('ladder1.jpg')

class boardLayout:
	def __init__(self,ladder_list,block_list):
		
		#walls
		block_1 = block.Block(wallImage,800,10)
		block_2 = block.Block(wallImage,800,10)
		block_2.rect.y=490
		block_3 = block.Block(wallImage,10,600)
		block_4 = block.Block(wallImage,10,600)
		block_4.rect.x=790
		block_5 = block.Block(wallImage,450 + random.randint(0,100),10)
		block_5.rect.y=420
		block_5.rect.x=10
		block_6 = block.Block(wallImage,900,10)
		block_6.rect.y=340
		block_6.rect.x=170 + random.randint(0,60)
		block_7 = block.Block(wallImage,600 + random.randint(0,70),10)
		block_7.rect.y=260
		block_7.rect.x=10
		block_8 = block.Block(wallImage,900,10)
		block_8.rect.y=180
		block_8.rect.x=170 + random.randint(0,60)
		block_9 = block.Block(wallImage,600 + random.randint(20,70),10)
		block_9.rect.y=100
		block_9.rect.x=10
		block_10 = block.Block(wallImage,160,10)
		block_10.rect.y=50
		block_10.rect.x=200
		block_11 = block.Block(wallImage,10,50)
		block_11.rect.y=0
		block_11.rect.x=200
		block_12 = block.Block(wallImage,10,50)
		block_12.rect.y=0
		block_12.rect.x=350
		block_13 = block.Block(wallImage,800,10)
		block_13.rect.y=590

		block_list.add(block_1,block_2,block_3,block_4,block_5,block_6,block_7,block_8,block_9,block_10,block_11,block_12,block_13)
		
		#ladders
		ladder_1=block.Block(ladderImage,20,70)
		ladder_1.rect.x=random.randint(200,400)
		ladder_1.rect.y=420
		
		ladder_2=block.Block(ladderImage,20,80)
		ladder_2.rect.x=random.randint(330,400)
		ladder_2.rect.y=340

		ladder_3 = block.Block(ladderImage,20,80)
		ladder_3.rect.x=random.randint(330,550)
		ladder_3.rect.y=260
		
		ladder_4 = block.Block(ladderImage,20,80)
		ladder_4.rect.x=random.randint(250,570)
		ladder_4.rect.y=180
		
		ladder_5 = block.Block(ladderImage,20,80)
		ladder_5.rect.x=450
		ladder_5.rect.y=100

		ladder_6 = block.Block(ladderImage,20,50)
		ladder_6.rect.x=300
		ladder_6.rect.y=50
				
		ladder_7 = block.Block(ladderImage,20,70)
		ladder_7.rect.x=150
		ladder_7.rect.y=260
		
		ladder_8 = block.Block(ladderImage,20,70)
		ladder_8.rect.x=150
		ladder_8.rect.y=350
		
		ladder_list.add(ladder_1,ladder_2,ladder_3,ladder_4,ladder_5,ladder_6,ladder_7,ladder_8)

	def printLayout(self,block_list,ladder_list,fire_sprite,donkey_sprite,queen_sprite,coin_sprite,player_sprite,screen):		
		screen.fill(BLACK)
		block_list.draw(screen)
		ladder_list.draw(screen)
		fire_sprite.draw(screen)
		donkey_sprite.draw(screen)
		queen_sprite.draw(screen)
		coin_sprite.draw(screen)
		player_sprite.draw(screen)
