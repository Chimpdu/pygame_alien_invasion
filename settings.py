class Settings:
	"""store the settings in game Alien invasion"""

	def __init__(self):
		"""initiate the settings of the game"""
		#screen settings
		self.screen_width=1550
		self.screen_height=800
		self.bg_color=(230,230,230)
		#ship settings
		self.ship_speed=1.5 #设置一个速度，但是注意在rect属性中，rect.x不接受浮点数，所以要在ship.py 中处理
		#bullet settings
		self.bullet_speed=1.0
		self.bullet_widths=3
		self.bullet_heights=15
		self.bullet_color=(60,60,60)