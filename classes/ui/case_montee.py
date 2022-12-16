from typing import Tuple
import pygame

try:
    from classes.ui.ui_element import UIElement
    from classes.ui.case import Case
except ModuleNotFoundError:
    from ui_element import UIElement

pygame.init()
class CaseMontee(Case):
    STROKE_COLOR:Tuple[int] = (0xFF, 0x00, 0x00)

    needed_battery:int= 4

    def action_to_take(self):
        pass 


        


