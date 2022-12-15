from classes.ui.ui_element import UIElement
from typing import Tuple
import pygame

pygame.init()
class Text(UIElement):
    DEFAULT_TEXT_COLOR = (0x00, 0x00, 0x00)
    DEFAULT_FONT_FAMILY = pygame.font.Font(None, 30)

    def __init__(self, screen, position: Tuple[int], dimension: Tuple[int], text:str) -> None:
        super().__init__(screen, position, dimension)
        self.__font_family = Text.DEFAULT_FONT_FAMILY
        self.__text_color = Text.DEFAULT_TEXT_COLOR
        self.__text = text
        self.__text_surface = pygame.Rect(self._position[0], self._position[1], self._dimension[0], self._dimension[1])
    
    def set_font_family(self, font):
        self.__font_family = font
    
    def set_text_color(self, color:Tuple[int]):
        self.__text_color = color
    
    def set_text(self, text:str) -> None:
        self.__text = text

    def draw(self):
        buf = self.__font_family.render(self.__text, True, self.__text_color)
        self.screen.blit(buf, self.__text_surface)
        
