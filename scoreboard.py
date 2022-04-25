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
		self.prep_highest_score()
		self.prep_level()

	def prep_score(self):
		"""turn the text into image"""
		rounded_score=round(self.stats.score,-1)     #通常街机游戏积分都是10的整数倍，round()是常用的精确小数点位数的函数，round()自定义是精确到小数点后一位，round（XXX,n）代表精确到小数点后第n位，-1则是精确到小数点前一位。（10的整数倍）
		self.content="{:,}".format(self.stats.score)     #"{:,}".format()是字符串的格式设置指令，将数字中插入逗号,使用"{:,}".format()后就不用再str()了
		self.font_image=self.font.render(self.content,True,self.text_color,self.settings.bg_color)
		self.rect=self.font_image.get_rect()
		self.rect.right=self.screen_rect.right-20
		self.rect.top=20

	def prep_highest_score(self):
		"""the the text of highest score into image"""
		rounded_highest_score=round(self.stats.highest_score,-1)
		content_highest_score="{:,}".format(rounded_highest_score)
		self.highest_score_image=self.font.render(content_highest_score,True,self.text_color,self.settings.bg_color)
		self.highest_score_rect=self.highest_score_image.get_rect()
		self.highest_score_rect.centerx=self.screen_rect.centerx
		self.highest_score_rect.top=self.rect.top

	def prep_level(self):
		"""turn level into image"""
		content_level="Level:"+str(self.stats.level)
		self.level_image=self.font.render(content_level,True,self.text_color,self.settings.bg_color)
		self.level_rect=self.level_image.get_rect()
		self.level_rect.right=self.rect.right
		self.level_rect.top=self.rect.bottom+20

	def show_score(self):
		"""print the scoreboard on the screen"""
		self.screen.blit(self.font_image,self.rect)
		self.screen.blit(self.highest_score_image,self.highest_score_rect)
		self.screen.blit(self.level_image,self.level_rect)