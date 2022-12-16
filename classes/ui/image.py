from typing import Tuple
import pygame

try:
    from classes.ui.ui_element import UIElement
except ModuleNotFoundError:
    from ui_element import UIElement

class Image(UIElement):
    """
    Author     : Marion Calpena
    Date       : 16/12/2022
    Version    : 1
    """
    
    def __init__(self, screen:pygame.Surface, position: Tuple[int, int], dimension: Tuple[int, int], img_path:str) -> None:
        super().__init__(screen, position, dimension)
        self.__img = pygame.image.load(img_path)
        self.__img = pygame.transform.scale(self.__img, self._dimension)

    def draw(self) -> None:
        self.screen.blit(self.__img, self._position)