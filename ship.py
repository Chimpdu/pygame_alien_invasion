import pygame
from settings import Settings
class Ship:
	"""a class for administrating the ship"""

	def __init__(self,ai_game):
		"""initialize the ship and set their original position"""
		self.screen=ai_game.screen                  
		self.screen_rect=ai_game.screen.get_rect()  

		self.image=pygame.image.load("images\\ship.bmp") 
		self.rect=self.image.get_rect()                   

		self.rect.midbottom=self.screen_rect.midbottom  

		self.moving_right=False
		self.moving_left=False	
		self.moving_up=False
		self.moving_down=False 

		self.x=float(self.rect.x)     #先把rect.x y转化为浮点型
		self.y=float(self.rect.y)
		self.settings=Settings()                                              

	def blitme(self):        
		self.screen.blit(self.image,self.rect)

	def update(self):
		"""update ship's position when events occurs"""
		if self.moving_right and self.rect.right<self.screen_rect.right:  #这些是为了限制飞船的移动距离，千万要记住pygame的坐标是向右下方增大的，所以一定要小心
			self.x+=self.settings.ship_speed
		if self.moving_left and self.rect.left>self.screen_rect.left:
			self.x-=self.settings.ship_speed
		self.rect.x=self.x              #仔细想，虽然rect.x仍取整数，但self.x仍在增加，小数之间会产生进位，所以rect.x仍然增大
		if self.moving_up and self.rect.top>self.screen_rect.top:
			self.y-=self.settings.ship_speed
		if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
			self.y+=self.settings.ship_speed
		self.rect.y=self.y

	def center_ship(self):
		"""center the ship and reset self.x/y"""
		self.rect.midbottom=self.screen_rect.midbottom
		self.x=float(self.rect.x)
		self.y=float(self.rect.y) #必须重置，不然self.x/y仍在撞击的位置。