from typing import Tuple
import pygame

try:
    from classes.ui.case import Case
except ModuleNotFoundError:
    from case import Case

pygame.init()
class CaseTunnelForward(Case):
    """
    Author     : Amine Maourid
    Date       : 16/12/2022
    Version    : 1
    """

    STROKE_COLOR:Tuple[int, int, int] = (0, 255, 0)
    
    def __init__(self, screen, position:Tuple[int], dimension:Tuple[int], numero:int,forward_steps:int) -> None:
        super().__init__(screen, position, dimension, numero)
        self.forward_steps:int = forward_steps
        

    def action_to_take(self) -> int:
        # if we are in a tunnel forward case we must advance by 10 cases 
        return self.forward_steps 