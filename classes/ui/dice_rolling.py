from typing import Tuple
from math import floor 
import numpy as np 
import pygame

try:
    from classes.ui.ui_element import UIElement
except ModuleNotFoundError:
    from ui_element import UIElement

class DiceUI(UIElement):
    """
    Author : Amine
    date : 15/12/2022
    """
    FILL_COLOR:Tuple[int] = (255,94,17)
    POINT_COLOR :Tuple[int]= (0,0,0)
    def __init__(self, screen, position:Tuple[int], dimension:Tuple[int]) -> None:
        super().__init__(screen, position, dimension)
        self.__value = 0
    
    def draw(self) -> None:
        points_coordinates = []
        pygame.draw.rect(self.screen,DiceUI.FILL_COLOR,self._position + self._dimension)
        width = self._dimension[0]
        height = self._dimension[1]
    
        if self.__value == 1 :
            points_coordinates.append((self._position[0] + (width/2), self._position[1]+(height/2)))
        elif self.__value == 2 :
            x = np.linspace(0, width, self.__value+2)
            step = floor(x[1])
            x1 = (step,floor(height/2))
            points_coordinates.append((x1[0] + self._position[0], x1[1] + self._position[1]))
            x2 = (width - step, floor(height/2))
            points_coordinates.append((x2[0] + self._position[0], x2[1] + self._position[1]))
        elif self.__value == 3 :
            x = np.linspace(0, width, self.__value+2)
            step = floor(x[1])
            x1 = (step,floor(height/2))
            points_coordinates.append((x1[0] + self._position[0], x1[1] + self._position[1]))
            x2 = (2*step, floor(height/2))
            points_coordinates.append((x2[0] + self._position[0], x2[1] + self._position[1]))
            x3 = (width-step,floor(height/2))
            points_coordinates.append((x3[0] + self._position[0], x3[1] + self._position[1]))

        elif self.__value == 4 :
            x = np.linspace(0, width, self.__value)
            step = floor(x[1])
            x1 = (step,step)
            points_coordinates.append((x1[0] + self._position[0], x1[1] + self._position[1]))
            x2 = (width-step, step)
            points_coordinates.append((x2[0] + self._position[0], x2[1] + self._position[1]))
            x3 = (step, height-step)
            points_coordinates.append((x3[0] + self._position[0], x3[1] + self._position[1]))
            x4 = (width-step,height-step)
            points_coordinates.append((x4[0] + self._position[0], x4[1] + self._position[1]))
        elif self.__value == 5 :
            x = np.linspace(0, width, self.__value-1)
            step = floor(x[1])
            x1 = (step,step)
            points_coordinates.append((x1[0] + self._position[0], x1[1] + self._position[1]))
            x2 = (width-step, step)
            points_coordinates.append((x2[0] + self._position[0], x2[1] + self._position[1]))
            x3 = (step, height-step)
            points_coordinates.append((x3[0] + self._position[0], x3[1] + self._position[1]))
            x4 = (width-step,height-step)
            points_coordinates.append((x4[0] + self._position[0], x4[1] + self._position[1]))
            x5 = (floor(width/2), floor(height/2))
            points_coordinates.append((x5[0] + self._position[0], x5[1] + self._position[1]))
            
        elif self.__value == 6 :
            x = np.linspace(0, width, self.__value-1)
            y = np.linspace(0, height, 4)
            step_vertical = floor(y[1])
            step = floor(x[1])
            x1 = (step, step_vertical)
            points_coordinates.append((x1[0] + self._position[0], x1[1] + self._position[1]))
            x2 = (2*step, step_vertical)
            points_coordinates.append((x2[0] + self._position[0], x2[1] + self._position[1]))
            x3 = (width-step, step_vertical)
            points_coordinates.append((x3[0] + self._position[0], x3[1] + self._position[1]))
            x4 = (step, height-step_vertical)
            points_coordinates.append((x4[0] + self._position[0], x4[1] + self._position[1]))
            x5 = (2*step, height-step_vertical)
            points_coordinates.append((x5[0] + self._position[0], x5[1] + self._position[1]))
            x6 = (width-step, height-step_vertical)
            points_coordinates.append((x6[0] + self._position[0], x6[1] + self._position[1]))

        # now that we have our points coordinates we can draw them 
        for coordinate in points_coordinates:
            pygame.draw.circle(self.screen, self.POINT_COLOR, coordinate,5)

    
    def set_value(self, value:int) -> None:
        self.__value = value
