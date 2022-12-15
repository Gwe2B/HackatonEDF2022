from typing import Tuple
import pygame

pygame.init()


class Case:
    STROKE_COLOR:Tuple[int] = (0x00, 0x00, 0x00)
    FONT_FAMILY = pygame.font.SysFont("Forte", 25)

    def __init__(self, position:Tuple[int], dimension:int, numero:int, screen) -> None:
        self.__position = position
        self.__dimension = dimension
        self.__numero = numero
        self.screen = screen
    
    def draw(self) -> None:
        pygame.draw.rect(self.screen, Case.STROKE_COLOR, self.__position + (self.__dimension, self.__dimension), 2)
        self.screen.blit(Case.FONT_FAMILY.render(str(self.__numero), True, Case.STROKE_COLOR), self.__position)  