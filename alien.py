import pygame
from pygame.sprite import Sprite
from settings import Settings
class Alien(Sprite):
	"""administrate the alien"""

	def __init__(self,ai_game):
		"""initialise the alien"""
		super().__init__()
		self.screen=ai_game.screen
		self.screen_rect=ai_game.screen.get_rect()
		self.settings=Settings()
		self.image=pygame.image.load("images/alien.bmp")
		self.rect=self.image.get_rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		self.fleet_direction=1
		#此处之所以不用blite是因为可以在主程序中对编组调用draw(surface)直接将每个元素都绘制到指定区域。(绘制编组的简洁方法)
		self.x=float(self.rect.x)

	def check_edges(self):
		"""check whether the aliens have exceeded the boundary"""
		if self.rect.left<=self.screen_rect.left or self.rect.right>=self.screen_rect.right:
			return True

	def update(self):
		"""update position of the fleet"""
		self.x+=(self.settings.fleet_speed*self.fleet_direction)
		self.rect.x=self.x