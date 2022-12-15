from abc import ABC, abstractmethod
from typing import Tuple

class UIElement(ABC):
    def __init__(self, screen, position:Tuple[int], dimension:Tuple[int]) -> None:
        super().__init__()
        self.screen = screen
        self._position = position
        self._dimension = dimension
    
    @abstractmethod
    def draw(self) -> None:
        pass