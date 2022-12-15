import math
from pygame.locals import *
import pygame, sys
from typing import Tuple
from classes.ui.case import Case
from classes.ui.button import Button

white:Tuple[int] = (0xFF, 0xFF, 0xFF)
black:Tuple[int] = (0x00, 0x00, 0x00)
screen_size:Tuple[int] = (1500, 600)

pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill(white)

#création du bouton de déplacement
button1 = Button('déplacement',200,40,(30,100),5)
#création du bouton de recharge
button2 = Button('recharge',200,40,(30,150),5)
#création du bouton de lancer de dé
button3 = Button('lancer de dé',200,40,(30,200),5)

buttons = [button1, button2, button3]
def buttons_draw():
	for b in buttons:
		b.draw()

cases:list = []

#variable de grandeur d'une case
case_size = (50,50)
screen_ctr  = (math.floor(screen_size[0] / 2), math.floor(screen_size[1] / 2))

#initialisation des variable du plateau
pos_next = (screen_ctr[0] - case_size[0], screen_ctr[1] - case_size[1])
line_case_count = 3
placed = 0
row = True
reverse = False

#Fonction du plateau à 60 case
for i in range(60, 0, -1):
    cases.append(Case(screen, pos_next, case_size, i))
    placed = placed + 1

    if placed >= line_case_count:
        if(not row):
            reverse = not reverse

        row = not row
        line_case_count = line_case_count + 1
        placed = 1

    if reverse:
        buf = case_size[0] * (-1)
    else:
        buf = case_size[0]

    if row:
        pos_next = (pos_next[0] + buf, pos_next[1])
    else:
        pos_next = (pos_next[0], pos_next[1] + buf)
    
pygame.display.flip() #update de l'affichage

def update_plate():
    for case in cases:
        case.draw()
        buttons_draw()

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    update_plate()
    pygame.display.update()