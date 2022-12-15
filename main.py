import math
import sys
from typing import Tuple

import pygame
from pygame.locals import *

from classes.Dice import Dice
from classes.ui.battery import Battery
from classes.ui.button import Button
from classes.ui.case import Case
from classes.ui.dice_rolling import DiceUI
from classes.voiture import Voiture

white:Tuple[int] = (0xFF, 0xFF, 0xFF)
black:Tuple[int] = (0x00, 0x00, 0x00)
screen_size:Tuple[int] = (1500, 600)

pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill(white)

dice_display = DiceUI(screen, (100, 200), (100, 100))
battery_display = Battery(screen, (1100, 0), (200, 512))
player = Voiture()
launch_value = None
dice = Dice()
def launch_dice():
    global launch_value
    launch_value = dice.throw()
    dice_display.set_value(launch_value)

def displacement():
    if player.get_charge_lvl() >= 2:
        player.deplacement(launch_value)
        battery_display.set_battery_lvl(player.get_charge_lvl())
        launch_dice()
    else:
        print("You do not have the battery for this.")

def charge_car():
    player.charge(launch_value)
    battery_display.set_battery_lvl(player.get_charge_lvl())
    launch_dice()


#création du bouton de déplacement
button1 = Button(screen, (200, 40), (150, 30), 'déplacement', 5)
button1.set_on_click(displacement)
#création du bouton de recharge
button2 = Button(screen, (200, 80), (150, 30), 'recharge', 5)
button2.set_on_click(charge_car)

buttons = [button1, button2]
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
    screen.fill(white)
    for case in cases:
        case.draw()
    buttons_draw()
    battery_display.draw()
    dice_display.draw()

    index = player.get_position() + 1
    pawn_pos = cases[-index]
    pawn_pos = (pawn_pos._position[0] + pawn_pos._dimension[0]/2, pawn_pos._position[1] + pawn_pos._dimension[1]/2)
    pygame.draw.circle(screen, black, pawn_pos, 5)

launch_dice()
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    update_plate()
    pygame.display.update()