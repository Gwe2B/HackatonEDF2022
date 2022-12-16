from typing import Tuple
import pygame

try:
    from classes.ui.ui_element import UIElement
except ModuleNotFoundError:
    from ui_element import UIElement


class Battery(UIElement):
    """
    Author     : Marion Calpena
    Date       : 15/12/2022
    Version    : 2
    """
    
    BATTERY_MAX_LVL:int = 6
    MARGIN:int = 6
    FILL_COLOR:Tuple[int, int, int] = (0x00, 0xFF, 0x00)

    # TODO: Make sure the path is still correct
    battery_outline = pygame.image.load('assets/battery_outline.png')

    def __init__(self, screen:pygame.Surface, position:Tuple[int, int], dimension:Tuple[int, int]) -> None:
        super().__init__(screen, position, dimension)

        self.__battery_lvl = 6
        self.__outline = pygame.transform.scale(Battery.battery_outline, dimension)
    
    #Overriding
    def draw(self) -> None:
        battery_lvl_height:int = (self._dimension[1]-50)/(Battery.BATTERY_MAX_LVL+1)
        battery_lvl_width:int = (self._dimension[0] - 2*Battery.MARGIN)
        x = self._position[0] + Battery.MARGIN

        for i in range(0, self.__battery_lvl):
            index = i + 1
            y = (self._position[1] + self._dimension[1]) - (index*battery_lvl_height) - ((index)*Battery.MARGIN)
            pygame.draw.rect(
                self.screen,
                (7,56,122),
                (x, y, battery_lvl_width, battery_lvl_height)
            )

        self.screen.blit(self.__outline, self._position)

    def set_battery_lvl(self, lvl:int) -> None:
        self.__battery_lvl = lvl