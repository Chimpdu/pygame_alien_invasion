class GameStats:
	"""track the game's statistics"""

	def __init__(self,ai_game):
		"""initialize the statistics attributes"""
		self.settings=ai_game.settings
		self.reset_stats()
		self.game_active=False

	def reset_stats(self):  #之所以特意用一个方法来初始化统计信息，是因为玩家每次开始新游戏时，需要重置一些统计信息，像这样初始化统计信息，在玩家开始新游戏时可直接调用这个方法。
		"""initiate the changable statistic information"""
		self.ships_left=self.settings.ship_limit