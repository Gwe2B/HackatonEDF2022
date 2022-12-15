from typing import Tuple
import pygame

class Battery:
    BATTERY_MAX_LVL:int = 6
    MARGIN:int = 6
    FILL_COLOR:Tuple[int] = (0x00, 0xFF, 0x00)

    # TODO: Make sure the path is still correct
    battery_outline = pygame.image.load('assets/battery_outline.png')

    def __init__(self, position:Tuple[int], dimension:Tuple[int], screen) -> None:
        self.screen = screen
        self.__battery_lvl = 6
        self.__position = position
        self.__dimension = dimension
        self.__outline = pygame.transform.scale(Battery.battery_outline, dimension)
    
    def draw(self) -> None:
        battery_lvl_height:int = (self.__dimension[1]/Battery.BATTERY_MAX_LVL)
        battery_lvl_width:int = (self.__dimension[0] - 2*Battery.MARGIN)
        x = self.__position[0] + Battery.MARGIN

        for i in range(1, self.__battery_lvl):
            y = (self.__position[1] + self.__dimension[1]) - (i*battery_lvl_height) - (i*Battery.MARGIN)
            pygame.draw.rect(
                self.screen,
                (0,255,0),
                (x, y, battery_lvl_width, battery_lvl_height)
            )

        self.screen.blit(self.__outline, self.__position)

    def set_battery_lvl(self, lvl:int) -> None:
        self.__battery_lvl = lvl