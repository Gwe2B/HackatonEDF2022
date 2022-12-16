from abc import ABC, abstractmethod
from typing import Tuple
from pygame.surface import Surface


class UIElement(ABC):
    """
    Author     : Gwenaël Guiraud
    Date       : 15/12/2022
    Version    : 1
    Description: Super class of all the UI elements. 
    """
    
    def __init__(self, screen:Surface, position:Tuple[int, int], dimension:Tuple[int, int]) -> None:
        super().__init__()
        self.screen = screen
        self._position = position
        self._dimension = dimension

    def get_position(self) -> Tuple[int, int]:
        return self._position

    def get_dimension(self) -> Tuple[int, int]:
        return self._dimension
    
    @abstractmethod
    def draw(self) -> None:
        pass

