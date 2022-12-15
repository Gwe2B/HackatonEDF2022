from pygame.locals import *
import pygame, sys
from typing import Tuple
from classes.ui.dice_rolling import Dice


white:Tuple[int] = (0xFF, 0xFF, 0xFF)
black:Tuple[int] = (0x00, 0x00, 0x00)
screen_size:Tuple[int] = (1500, 600)

pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill(white)

hDice = Dice(screen, (0,0), (100,100))
hDice.draw()
while True: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()