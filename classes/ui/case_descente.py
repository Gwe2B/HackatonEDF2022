from typing import Tuple
import pygame

try:
    from classes.ui.ui_element import UIElement
    from classes.ui.case import Case
except ModuleNotFoundError:
    from ui_element import UIElement

pygame.init()
class CaseDescente(Case):
    STROKE_COLOR:Tuple[int] = (0xC9, 0xCC, 0x3F)

    needed_battery:int= 1

    def action_to_take(self):
        pass 