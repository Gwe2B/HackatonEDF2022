from pygame.locals import *
import pygame

try:
	from classes.ui.ui_element import UIElement
except ModuleNotFoundError:
	from ui_element import UIElement

pygame.init()

gui_font = pygame.font.Font(None,30)

class Button(UIElement):
	DEFAULT_TEXT_COLOR:str = '#fff'
	DEFAULT_BG_COLOR:str = '#475F77'
	DEFAULT_HOVER_COLOR:str = '#D74B4B'
	DEFAULT_BOTTOM_COLOR:str = '#354B5E'

	def __init__(self,screen, position, dimension, text,elevation): 
		super().__init__(screen, position, dimension)

		self.reset_colors()

		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elevation = elevation
 
		# top rectangle 
		self.top_rect = pygame.Rect(self._position[0], self._position[1], self._dimension[0], self._dimension[1])
		self.top_color = self.__bg_color
 
		# bottom rectangle 
		self.bottom_rect = pygame.Rect(self._position[0], self._position[1], self._dimension[0], self._dimension[1])
		self.bottom_color = self.__bottom_color
		#text
		self.text = text
		self.text_surf = gui_font.render(text,True,self.__text_color)
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
 
	def reset_color(self):
		self.__text_color = Button.DEFAULT_TEXT_COLOR
		self.__bg_color = Button.DEFAULT_BG_COLOR
		self.__hover_color = Button.DEFAULT_HOVER_COLOR
		self.__bottom_color = Button.DEFAULT_BOTTOM_COLOR

	def set_text_color(self, color:str):
		self.text_surf = gui_font.render(self.text, True, color)
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
		self.__text_color = color

	def set_bg_color(self, color:str):
		self.__bg_color = color

	def set_hover_color(self, color:str):
		self.__hover_color = color

	def set_bottom_color(self, color:str):
		self.__text_color = color

	def change_text(self, newtext):
		self.text_surf = gui_font.render(newtext, True, self.__text_color)
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
 
	def draw(self):
		# elevation logic 
		self.top_rect.y = self._position[1] - self.dynamic_elevation
		self.text_rect.center = self.top_rect.center 
 
		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
 
		pygame.draw.rect(self.screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(self.screen,self.top_color, self.top_rect,border_radius = 12)
		self.screen.blit(self.text_surf, self.text_rect)
		self.check_click()
 
	def set_on_click(self, callback: callable) -> None:
		self._on_click_action = callback

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = self.__hover_color
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elevation = 0
				self.pressed = True
				self.change_text(f"{self.text}")
			else:
				self.dynamic_elevation = self.elevation
				if self.pressed == True:
					self._on_click_action()
					self.pressed = False
					self.change_text(self.text)
		else:
			self.dynamic_elevation = self.elevation
			self.top_color = self.__bg_color
