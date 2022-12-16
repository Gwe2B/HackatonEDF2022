from typing import Tuple
import pygame

try:
    from classes.ui.ui_element import UIElement
    from classes.ui.case import Case
except ModuleNotFoundError:
    from ui_element import UIElement

pygame.init()
class CaseTunnelForward(Case):
    STROKE_COLOR:Tuple[int] = (0xAA, 0xFF, 0x00)
    
    def __init__(self, screen, position:Tuple[int], dimension:Tuple[int], numero:int,forward_steps:int) -> None:
        super().__init__(screen, position, dimension, numero)
        self.forward_steps = forward_steps
        

    def action_to_take(self):
        # if we are in a tunnel forward case we must advance by 10 cases 
        return self.forward_steps 