from typing import Tuple
import pygame

try:
    from classes.ui.ui_element import UIElement
    from classes.ui.case import Case
except ModuleNotFoundError:
    from ui_element import UIElement

pygame.init()
class CaseTunnelBackward(Case):
    STROKE_COLOR:Tuple[int] = (0x45, 0x4B, 0x1B)

    def __init__(self, screen, position:Tuple[int], dimension:Tuple[int], numero:int,backward_steps:int) -> None:
        super().__init__(screen, position, dimension, numero)
        self.backward_steps = backward_steps 
        

    def action_to_take(self):
        # if we are in a tunnel forward case we must advance by 10 cases 
        return (-1)*self.backward_steps