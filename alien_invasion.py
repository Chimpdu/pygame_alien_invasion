#rebuild _check_events_()
#As this program is growing increasingly complex, the method: _check_event_()would be longer and longer, so rebuild is desperatedly needed.
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
		self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)  #使用(0,0),pygame.FULLSCREEN将游戏全屏播放
		self.settings.screen_width=self.screen.get_rect().width       #更新Setting在主程序里使用的数据避免在直接引用setting.screen_XXX时出现错误
		self.settings.screen_height=self.screen.get_rect().height
		self.ship=Ship(self)
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""start the main loop"""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()

	def _check_events(self):
		"""response to the events"""
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
				
			elif event.type==pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type==pygame.KEYUP:
				self._check_keyup_events(event)
					
	def _check_keydown_events(self,event):
		"""respond to the keydown events"""
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right=True
		elif event.key==pygame.K_LEFT:
			self.ship.moving_left=True
		elif event.key==pygame.K_UP:
			self.ship.moving_up=True
		elif event.key==pygame.K_DOWN:
			self.ship.moving_down=True
		elif event.key==pygame.K_q:
			sys.exit()


	def _check_keyup_events(self,event):
		"""respond to the keyup events"""
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right=False
		if event.key==pygame.K_LEFT:
			self.ship.moving_left=False
		if event.key==pygame.K_UP:
			self.ship.moving_up=False
		if event.key==pygame.K_DOWN:
			self.ship.moving_down=False

	def _update_screen(self):
		"""update the images on the screen and switch to new screens"""
		pygame.display.flip()
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

if __name__=="__main__":
	ai=AlienInvasion()
	ai.run_game()