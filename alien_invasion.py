#rebuild _check_events_()
#As this program is growing increasingly complex, the method: _check_event_()would be longer and longer, so rebuild is desperatedly needed.
import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
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
		self.bullets=pygame.sprite.Group()   #创建用于存储子弹的编组
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""start the main loop"""
		while True:
			self._check_events()
			self._update_screen()
			self._update_bullets()
			
			 

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

		elif event.key==pygame.K_SPACE:
			self._fire_bullet()

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
	
	def _fire_bullet(self):
		"""create a bullet and add it into the group"""
		if len(self.bullets)<self.settings.bullet_num:
			new_bullet=Bullet(self)
			self.bullets.add(new_bullet)  

	def _update_screen(self):  
		"""update the images on the screen and switch to new screens"""
		pygame.display.flip()#3
		self.screen.fill(self.settings.bg_color)#1
		self.ship.blitme() #2  
		self.ship.update()      
	
	def _update_bullets(self):
		self.bullets.update()
		for bullet in self.bullets.sprites():  
			bullet.draw_bullet()

		for bullet in self.bullets.copy():      #用for循环删除列表或编组中的元素，必须要用副本，因为for必须遍历长度不变的列表或编组，除了pygame以外，通常用while来删除列表的元素，而不是for
			if bullet.rect.bottom<0:            #循环用的列表是副本但是删除的是真的
				self.bullets.remove(bullet)

if __name__=="__main__":
	ai=AlienInvasion()
	ai.run_game()