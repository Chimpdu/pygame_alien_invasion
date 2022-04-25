import pygame.font
from pygame.sprite import Group #因为只用Group所以不用把pygame全引过来。
from ship import Ship
class Scoreboard:
	"""shpw score information"""

	def __init__(self,ai_game):
		"""initialize the attributes of scoreboard"""
		self.screen=ai_game.screen
		self.screen_rect=self.screen.get_rect()
		self.settings=ai_game.settings	
		self.stats=ai_game.stats
		self.ai_game=ai_game
		
		#initialize font
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,48)
		#prepare the image
		self.prep_score()
		self.prep_highest_score()
		self.prep_level()
		self.prep_ship()


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

	def prep_ship(self):
		""""""
		self.ships=Group() #Group可千万别放在外面，因为防止prep_ship里面时，每次调用prep_ship恰好重置一次Group(),不然Group（）内sprite数量一直增加。
		for ship_num in range(self.stats.ships_left): #重要思想，不要想着删掉图像，而是减少绘制飞船的数量，用for loop就可以做到
			ship=Ship(self.ai_game)
			ship.rect.x=10+ship_num*ship.rect.width   #别忘了for loop 是从0开始遍历到n-1,range(n)
			ship.rect.y=10
			self.ships.add(ship)


	def show_score(self):
		"""print the scoreboard on the screen"""
		self.screen.blit(self.font_image,self.rect)
		self.screen.blit(self.highest_score_image,self.highest_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.ships.draw(self.screen)  #draw的好处是可以一下把sprites全画上