from typing import Tuple
import pygame

try:
    from classes.ui.case import Case
except ModuleNotFoundError:
    from case import Case

pygame.init()
class CaseTunnelBackward(Case):
    """
    Author     : Amine Maourid
    Date       : 16/12/2022
    Version    : 1
    """
    STROKE_COLOR:Tuple[int, int, int] = (144, 90, 90)

    def __init__(self, screen, position:Tuple[int, int], dimension:Tuple[int, int], numero:int, backward_steps:int) -> None:
        super().__init__(screen, position, dimension, numero)
        self.backward_steps:int = backward_steps 
        

    def action_to_take(self) -> int:
        # if we are in a tunnel forward case we must advance by 10 cases 
        return (-1)*self.backward_steps