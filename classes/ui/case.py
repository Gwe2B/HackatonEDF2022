from typing import Tuple
import pygame
from classes.ui.ui_element import UIElement

pygame.init()

class Case(UIElement):
    STROKE_COLOR:Tuple[int] = (0x00, 0x00, 0x00)
    FONT_FAMILY = pygame.font.SysFont("Forte", 25)

    def __init__(self, screen, position:Tuple[int], dimension:Tuple[int], numero:int) -> None:
        super().__init__(screen, position, dimension)
        self.__numero = numero
        self.screen = screen
    
    def draw(self) -> None:
        pygame.draw.rect(self.screen, Case.STROKE_COLOR, self._position + self._dimension, 2)
        self.screen.blit(Case.FONT_FAMILY.render(str(self.__numero), True, Case.STROKE_COLOR), self._position)  