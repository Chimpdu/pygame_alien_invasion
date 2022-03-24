import pygame
import sys
from settings import Settings
from ship import Ship
class AlienInvasion:
	"""the class which administrates the games' asset and behaviour"""

	def __init__(self):
		"""initiate the game and build the assets"""
		pygame.init()
		self.settings=Settings()
		self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) #surface_1:屏幕。 赋给self.screen的是一个surface，surface是屏幕的一部分，用于显示游戏元素，每个元素如（ship和alien）都是一个surface
		self.ship=Ship(self)
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
			pygame.display.flip()
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

if __name__=="__main__":
	ai=AlienInvasion()
	ai.run_game()
import time
time.sleep(10)