import pygame

def checkWall(obj, x, y, x_change, y_change, block_list): # checks collision of obj with wall
	obj.rect.x += x_change
	obj.rect.y += y_change
	obj_collide_wall = pygame.sprite.spritecollide(obj,block_list,False)
	obj.rect.x -= x_change
	obj.rect.y -= y_change
	if len(obj_collide_wall) != 0 : 
		return 1
	else:
		return 0
