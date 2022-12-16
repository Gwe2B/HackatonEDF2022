from typing import Tuple
import pygame

try:
    from classes.ui.ui_element import UIElement
except ModuleNotFoundError:
    from ui_element import UIElement

pygame.init()

class Case(UIElement):
    """
    Author     : Gwenaël Guiraud & Amine Maourid
    Date       : 15/12/2022
    Version    : 4
    """
    
    STROKE_COLOR:Tuple[int, int, int] = (0x00, 0x00, 0x00)
    FONT_FAMILY:pygame.font.Font = pygame.font.SysFont("Forte", 25)

    needed_battery:int = 2

    def __init__(self, screen, position:Tuple[int], dimension:Tuple[int], numero:int) -> None:
        super().__init__(screen, position, dimension)
        self.__numero:int = numero
    
    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.STROKE_COLOR, self._position + self._dimension, 2)
        self.screen.blit(Case.FONT_FAMILY.render(str(self.__numero), True, Case.STROKE_COLOR), self._position)  

    def action_to_take(self) -> int:
        return 0

    @classmethod 
    def get_needed_battery(cls) -> int:
        return cls.needed_battery 
    