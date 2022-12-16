from typing import Tuple
import pygame

try:
    from classes.ui.ui_element import UIElement
    from classes.ui.case import Case
except ModuleNotFoundError:
    from ui_element import UIElement

pygame.init()
class CaseDescente(Case):
    """
    Author     : Amine Maourid
    Date       : 16/12/2022
    Version    : 1
    """
    STROKE_COLOR:Tuple[int, int, int] = (199, 0, 57)

    needed_battery:int= 1

    def action_to_take(self) -> int:
        return super().action_to_take() 