class Settings:
	"""store the settings in game Alien invasion"""

	def __init__(self):
		"""initialize the static settings of the game"""
		#screen settings
		self.screen_width=1550
		self.screen_height=800
		self.bg_color=(230,230,230)
		#ship static settings
		self.ship_limit=3
		#bullet static settings
		self.bullet_widths=3
		self.bullet_heights=15
		self.bullet_color=(60,60,60)
		self.bullet_num=3
		#fleet settings
		self.fleet_drop_speed=6
		self.speedup_scale=1.1
		self.score_scale=1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""initialize the dynamic settings of the game"""
		self.ship_speed=1.5 
		self.bullet_speed=1.0
		self.fleet_speed=1.0
		self.fleet_direction=1
		self.alien_points=50

	def increase_speed(self):
		"""increase speed after the whole fleet is eliminated"""
		self.ship_speed*=self.speedup_scale
		self.bullet_speed*=self.speedup_scale
		self.fleet_speed*=self.speedup_scale
		self.alien_points=int(self.score_scale*self.alien_points)		