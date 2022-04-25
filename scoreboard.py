import pygame.font
class Scoreboard:
	"""shpw score information"""

	def __init__(self,ai_game):
		"""initialize the attributes of scoreboard"""
		self.screen=ai_game.screen
		self.screen_rect=self.screen.get_rect()
		self.settings=ai_game.settings
		self.stats=ai_game.stats
		#initialize font
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,48)
		#prepare the image
		self.prep_score()

	def prep_score(self):
		"""turn the text into image"""
		self.content=str(self.stats.score)
		self.font_image=self.font.render(self.content,True,self.text_color,self.settings.bg_color)
		self.rect=self.font_image.get_rect()
		self.rect.right=self.screen_rect.right-20
		self.rect.top=20

	def show_score(self):
		"""print the scoreboard on the screen"""
		self.screen.blit(self.font_image,self.rect)