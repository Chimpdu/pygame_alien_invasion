#python的优点是可以像处理矩形（rect对象）那样处理一切游戏元素，这样可很快判断他们之间是否发生了碰撞，将屏幕与飞船全作为矩形处理
import pygame
class Ship:
	"""a class for administrating the ship"""

	def __init__(self,ai_game):
		"""initiate the ship and set their original position"""
		self.screen=ai_game.screen                  #将屏幕赋给Ship里的一个属性
		self.screen_rect=ai_game.screen.get_rect()  #用.get_rect()来访问屏幕的rect属性

		self.image=pygame.image.load("images\\ship.bmp")  #使用pygame.image.load()载入图片
		self.rect=self.image.get_rect()                   #.get_rect()访问ship的rect属性

		self.rect.midbottom=self.screen_rect.midbottom    #原点在（0，0）在最左上角。使用rect处理数据，通过调整矩形中心和四角的坐标指定其所在位置。使元素居中用center，centerx,centery,与边缘平齐：top，bottom，left，right，其他组合：midbottom,midtop,midleft,midright

	def blitme(self):        #定义方法blitme()将图片打印到瑟利夫。rect指定的位置
		"""print the ship at the designated position"""
		self.screen.blit(self.image,self.rect)