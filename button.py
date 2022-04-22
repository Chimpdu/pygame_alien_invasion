import pygame.font  #pygame.font是一个可以将文本渲染在屏幕上的模块
class Button:
	"""a class used to administrate the buttons in the game"""
	def __init__(self,ai_game,msg):       #msg是message，既按钮中要显示的文本
		"""initialize the attributes of the button"""
		self.screen=ai_game.screen
		self.screen_rect=ai_game.screen.get_rect()

		#设置按钮的尺寸及其他属性
		self.width,self.height=200,50
		self.button_color=(0,255,0)
		self.text_color=(255,255,255)
		self.font=pygame.font.SysFont(None,48) #None 让其使用默认字体，fontsize=48
		#创建self.rect
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center

		#pygame处理文本的方式是将string渲染为图像
		#按钮的标签只创建一次
		self._prep_msg(msg)

	def _prep_msg(self,msg):
		"""make the text into an image and blit it into the center of the button"""
		self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
		#True开启反锯齿功能，使文本边缘平滑
		#先设置文本的颜色再设置背景色，不指定则透明
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center

	def draw_button(self):
		#先绘制一个颜色填充的按钮，再绘制文本
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)