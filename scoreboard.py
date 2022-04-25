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
		rounded_score=round(self.stats.score,-1)     #通常街机游戏积分都是10的整数倍，round()是常用的精确小数点位数的函数，round()自定义是精确到小数点后一位，round（XXX,n）代表精确到小数点后第n位，-1则是精确到小数点前一位。（10的整数倍）
		self.content="{:,}".format(self.stats.score)     #"{:,}".format()是字符串的格式设置指令，将数字中插入逗号,使用"{:,}".format()后就不用再str()了
		self.font_image=self.font.render(self.content,True,self.text_color,self.settings.bg_color)
		self.rect=self.font_image.get_rect()
		self.rect.right=self.screen_rect.right-20
		self.rect.top=20

	def show_score(self):
		"""print the scoreboard on the screen"""
		self.screen.blit(self.font_image,self.rect)