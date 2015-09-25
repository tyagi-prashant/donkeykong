import pygame
class Block(pygame.sprite.Sprite):
	def __init__(self,objImage,width,height):
		pygame.sprite.Sprite.__init__(self)		
		objImage = pygame.transform.scale(objImage, (width, height))
		self.image = objImage
		self.rect=self.image.get_rect()
