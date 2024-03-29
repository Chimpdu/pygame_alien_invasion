import pygame
import sys
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
class AlienInvasion:
	"""the class which administrates the games' asset and behaviour"""

	def __init__(self):
		"""initialize the game and build the assets"""
		pygame.init()
		self.settings=Settings()
		self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)  
		self.settings.screen_width=self.screen.get_rect().width       
		self.settings.screen_height=self.screen.get_rect().height
		self.ship=Ship(self)
		self.bullets=pygame.sprite.Group()   #创建用于存储子弹的编组
		self.aliens=pygame.sprite.Group()
		self.play_button=Button(self,"Play")
		self._create_fleet() #千万别写在while里面，不然无限循环，会卡住
		pygame.display.set_caption("Alien Invasion")
		self.stats=GameStats(self)
		self.sb=Scoreboard(self)


	def run_game(self):
		"""start the main loop"""
		while True:
			self._check_events()
			self._update_screen()
			if self.stats.game_active:
				self._update_bullets()	
				self._update_fleet()
			

	def _check_events(self):
		"""response to the events"""
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
				
			elif event.type==pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type==pygame.KEYUP:
				self._check_keyup_events(event)

			elif event.type==pygame.MOUSEBUTTONDOWN:
				if event.button==1:       #pygame中鼠标按键用event.button==n,n=1,2,3分别是左键，滑轮，右键
					mouse_pos=pygame.mouse.get_pos() #返回一个Tuple，包含单击鼠标时的x,y坐标
					self._check_play_button(mouse_pos)

	def _check_play_button(self,mouse_pos):
		"""Start the game when clicking the play button"""
		button_clicked=self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:#避免在游戏进行时点击按钮区域也重置
			self.stats.reset_stats()
			self.stats.game_active=True
			self.bullets.empty()
			self.aliens.empty()
			self._create_fleet()
			self.ship.center_ship()
			pygame.mouse.set_visible(False)
			self.settings.initialize_dynamic_settings()
			self.sb.prep_score()
					
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

	def _update_screen(self):  
		"""update the images on the screen and switch to new screens"""
		pygame.display.flip()
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()   
		self.ship.update() 
		self.aliens.draw(self.screen)
		self.sb.show_score() 
		if not self.stats.game_active:
			self.play_button.draw_button()
	
	def _fire_bullet(self):
		"""create a bullet and add it into the group"""
		if len(self.bullets)<self.settings.bullet_num:
			new_bullet=Bullet(self)
			self.bullets.add(new_bullet)  

	def _update_bullets(self):
		"""update the bullets"""
		self.bullets.update()
		for bullet in self.bullets.sprites():  
			bullet.draw_bullet()

		for bullet in self.bullets.copy():    
			if bullet.rect.bottom<0:
				self.bullets.remove(bullet)
		self._check_bullet_alien_collisions()

	def _create_fleet(self):
		"""creat the alien fleet"""
		alien=Alien(self)
		alien_width,alien_height=alien.rect.size        #size提供一个元组   
		available_space_x=(self.settings.screen_width-(alien_width))
		num_alien_x=available_space_x//(2*alien_width) 

		ship_height=self.ship.rect.height
		available_space_y=(self.settings.screen_height-(3*alien_height)-ship_height)
		num_rows=available_space_y//(2*alien_height)                         
		
		for row_number in range(num_rows):         
			for alien_number in range(num_alien_x):
				self._create_alien(alien_number,row_number)

	def _create_alien(self,alien_num,num_row):
		"""creat a single alien and add into the group"""
		alien=Alien(self)
		alien_width,alien_height=alien.rect.size
		alien.x=alien_width+2*alien_width*alien_num
		alien.rect.x=alien.x
		alien.y=alien_height+2*alien_height*num_row
		alien.rect.y=alien.y
		self.aliens.add(alien)    

	def _check_fleet_edges(self):
		"""check the fleet's edges and change fleet_direction"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""change the route of the aliens"""
		for alien in self.aliens.sprites():
			alien.rect.y+=self.settings.fleet_drop_speed
			alien.fleet_direction*=-1

	def _update_fleet(self):
		"""update fleet's position"""
		self._check_fleet_edges()
		self.aliens.update()

		if pygame.sprite.spritecollideany(self.ship,self.aliens):
			print("Ship hit!!!")
			self._ship_hit()
		self._check_aliens_bottom()

	def _check_bullet_alien_collisions(self):
			"""respond to collisions and rebuild fleet"""
			collisions=pygame.sprite.groupcollide(
			self.bullets,self.aliens,True,True)  
			if collisions:
				for aliens in collisions.values():
					self.stats.score+=len(aliens)*self.settings.alien_points
					self.sb.prep_score()
					self._check_highest_score()
			if not self.aliens:
				self.bullets.empty()
				self._create_fleet() 
				self.settings.increase_speed()
				self.stats.level+=1
				self.sb.prep_level( )

	def _ship_hit(self):
		"""respond to ship hit"""
		if self.stats.ships_left>1:
			self.stats.ships_left-=1 
			self.sb.prep_ship()
			self.bullets.empty()
			self.aliens.empty()
			self._create_fleet()
			self.ship.center_ship()
			sleep(0.5)
		else:
			self.stats.game_active=False
			pygame.mouse.set_visible(True)

	def _check_aliens_bottom(self):
		"""respond when aliens exceed the bottom of the screen"""
		screen_rect=self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom>=screen_rect.bottom:
				self._ship_hit()
				break

	def _check_highest_score(self):
		"""update the highest score"""
		if self.stats.score>self.stats.highest_score:
			self.stats.highest_score=self.stats.score
			self.sb.prep_highest_score()


if __name__=="__main__":
	ai=AlienInvasion()
	ai.run_game()
