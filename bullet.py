import pygame 
from pygame.sprite import Sprite
#class Sprite（精灵）可将相关的元素编组，同时操作编组中的所有元素
class Bullet(Sprite):          #class Bullet是Sprite的子类，不熟悉的话可以复习一下class_3.py
	"""a child class of Sprite which administrates the bullets"""
	
	def __init__(self,ai_game):
		super().__init__()
		self.settings=ai_game.settings
		self.screen=ai_game.screen
		self.color=self.settings.bullet_color

		self.rect=pygame.Rect(0,0,self.settings.bullet_widths,self.settings.bullet_heights) #与screen和ship不同，screen和ship是已经有图形了，用pygame的get_rect()函数使用矩形属性而bullet是直接用pygame的Rect（）在原点绘制矩形
		self.rect.midtop=ai_game.ship.rect.midtop #Don't import Ship from ship because the image in ship.py is static(always at the midbottom of the screen),so the bullets are always shot from the midbottom of the screen, rather than from the midtop of the ship.)
												#besides that, "setting the self.rect.midtop" must follow "setting the self.rect" closely.
		self.y=float(self.rect.y)
	
	def update(self):
		"""move the bullets upward"""
		self.y-=self.settings.bullet_speed
		self.rect.y=self.y

	def draw_bullet(self):    #与ship不同，ship中创建方法blitme(),self.screen.blit(self.image,self,rect)将已有的ship图像在指定区域打印出来
		"""draw the bullets on the screen"""           #此处用pygame.draw.rect()将bullet画出来 
		pygame.draw.rect(self.screen,self.color,self.rect)	