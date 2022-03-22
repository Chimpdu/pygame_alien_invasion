#创建一个表示游戏的类
import sys            #引用sys模块以退出游戏
import pygame         #pygame模块包含开发游戏所需的功能
class AlienInvasion:
	"""interface and interaction"""

	def __init__(self):
		"""initiate the game and build assets"""
		pygame.init()
		self.screen=pygame.display.set_mode((1200,800))  #pygame.display.set_mode()用于创立一个pygame窗口，输入的是一个tuple（元组）
		pygame.display.set_caption('Alien Invasion')
		self.bg_color=(230,230,230)            			 #pygame用RBG格式表示颜色每种色的取值是（0-255）共1600万种颜色 ，（230，230，230）是一种浅灰色

	def run_game(self):
		"""run the game"""
		while True:										  #这个循环称为event loop
			for event in pygame.event.get():              #event就是用户的输入，如键盘的敲击以及鼠标的点击
				if event.type==pygame.QUIT:                    #退出的条件
					sys.exit()
			pygame.display.flip()
			self.screen.fill(self.bg_color)
			
if __name__=='__main__':
	ai=AlienInvasion()
	ai.run_game()
