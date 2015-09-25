import checkcollision
import checkwall
import pygame

def freeFall(obj,ladder_list, block_list):
	check = checkcollision.checkCollision(obj, ladder_list , obj.rect.x , obj.rect.y , 0 , 0)
	if check == 0:
		check = checkwall.checkWall(obj , obj.rect.x , obj.rect.y , 0 , 10, block_list)
		while check == 0:
			obj.rect.y += 10
			check = checkwall.checkWall(obj , obj.rect.x , obj.rect.y , 0 , 10, block_list)
