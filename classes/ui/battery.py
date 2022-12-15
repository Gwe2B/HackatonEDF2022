from typing import Tuple
import pygame
from classes.ui.ui_element import UIElement


class Battery(UIElement):
    BATTERY_MAX_LVL:int = 6
    MARGIN:int = 6
    FILL_COLOR:Tuple[int] = (0x00, 0xFF, 0x00)

    # TODO: Make sure the path is still correct
    battery_outline = pygame.image.load('assets/battery_outline.png')

    def __init__(self, screen, position:Tuple[int], dimension:Tuple[int]) -> None:
        super().__init__(screen, position, dimension)

        self.__battery_lvl = 6
        self.__outline = pygame.transform.scale(Battery.battery_outline, dimension)
    
    #Overriding
    def draw(self) -> None:
        battery_lvl_height:int = (self._dimension[1]/Battery.BATTERY_MAX_LVL)
        battery_lvl_width:int = (self._dimension[0] - 2*Battery.MARGIN)
        x = self._position[0] + Battery.MARGIN

        for i in range(0, self.__battery_lvl - 1):
            index = i + 1
            y = (self._position[1] + self._dimension[1]) - (index*battery_lvl_height) - (index*Battery.MARGIN)
            pygame.draw.rect(
                self.screen,
                (0,255,0),
                (x, y, battery_lvl_width, battery_lvl_height)
            )

        self.screen.blit(self.__outline, self._position)

    def set_battery_lvl(self, lvl:int) -> None:
        self.__battery_lvl = lvl