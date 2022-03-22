import pygame
import sys
from settings import Settings
class AlienInvasion:
	"""the class which administrates the games' asset and behaviour"""

	def __init__(self):
		"""initiate the game and build the assets"""
		pygame.init()
		self.settings=Settings()
		self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		pygame.display.flip()
		self.screen.fill(self.settings.bg_color)

if __name__=="__main__":
	ai=AlienInvasion()
	ai.run_game()