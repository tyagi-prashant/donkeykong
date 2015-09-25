import pygame

def checkCollision(obj, sprite_list, x, y, x_change, y_change): #checks collision of obj with sprite list
	obj.rect.x += x_change
	obj.rect.y += y_change
	obj_collide_something = pygame.sprite.spritecollide(obj,sprite_list,False)
	obj.rect.x -= x_change
	obj.rect.y -= y_change
	if len(obj_collide_something) != 0 : 
		return 1
	else:
		return 0
