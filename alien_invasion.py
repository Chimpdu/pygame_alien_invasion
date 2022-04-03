import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class AlienInvasion:
	"""the class which administrates the games' asset and behaviour"""

	def __init__(self):
		"""initiate the game and build the assets"""
		pygame.init()
		self.settings=Settings()
		self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)  
		self.settings.screen_width=self.screen.get_rect().width       
		self.settings.screen_height=self.screen.get_rect().height
		self.ship=Ship(self)
		self.bullets=pygame.sprite.Group()   #创建用于存储子弹的编组
		self.aliens=pygame.sprite.Group()
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""start the main loop"""
		while True:
			self._check_events()
			self._update_screen()
			self._update_bullets()	
			self._create_fleet()		 

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

	def _update_screen(self):  
		"""update the images on the screen and switch to new screens"""
		pygame.display.flip()#3
		self.screen.fill(self.settings.bg_color)#1
		self.ship.blitme() #2  
		self.ship.update() 
		self.aliens.draw(self.screen)     
	
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

	def _create_fleet(self):
		"""creat the alien fleet"""
		alien=Alien(self)
		alien_width,alien_height=alien.rect.size        #size提供一个元组   
		available_space_x=(self.settings.screen_width-(alien_width))
		num_alien_x=available_space_x//(2*alien_width) 

		ship_height=self.ship.rect.height
		available_space_y=(self.settings.screen_height-(3*alien_height)-ship_height)
		num_rows=available_space_y//(2*alien_height)                         
		
		for row_number in range(num_rows):          #这个太巧妙了
			for alien_number in range(num_alien_x):
				self._create_alien(alien_number,row_number)


	def _create_alien(self,alien_num,num_row):
		"""creat a single alien and add into the group"""
		alien=Alien(self)
		alien_width,alien_height=alien.rect.size
		alien.rect.x=alien_width+2*alien_width*alien_num
		alien.rect.y=alien_height+2*alien_height*num_row
		self.aliens.add(alien)                   

if __name__=="__main__":
	ai=AlienInvasion()
	ai.run_game()
