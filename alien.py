import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	"""administrate the alien"""

	def __init__(self,ai_game):
		super().__init__()
		self.screen=ai_game.screen
		self.image=pygame.image.load("images/alien.bmp")
		self.rect=self.image.get_rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		#此处之所以不用blite是因为可以在主程序中对编组调用draw(surface)直接将每个元素都绘制到指定区域。(绘制编组的简洁方法)
		self.x=float(self.rect.x)