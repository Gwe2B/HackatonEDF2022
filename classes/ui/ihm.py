import math
import sys
from typing import Tuple

import pygame
from pygame.locals import *

from classes.dice import Dice
from classes.game import Game
from classes.ui.battery import Battery
from classes.ui.button import Button
from classes.ui.case import Case
from classes.ui.dice_rolling import DiceUI
from classes.voiture import Voiture

pygame.init()

class IHM:
    WHITE:Tuple[int] = (0xFF, 0xFF, 0xFF)
    BLACK:Tuple[int] = (0x00, 0x00, 0x00)

    def __init__(self, size:Tuple[int]) -> None:
        self.screen_size = size
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(IHM.WHITE)

        # Initializing components
        self.dice_display = DiceUI(self.screen, (100, 200), (100, 100))
        self.battery_display = Battery(self.screen, (1100, 0), (200, 512))
        self.buttons = []
        self.cases = []

        self.__initializing_board()
        self.game = Game()
        self.game.cases = self.cases
        self.game.update_player_pos()

        # Creating the buttons
        button = Button(self.screen, (200, 40), (150, 30), 'Déplacement', 5)
        button.set_on_click(self.game.play_displace)
        self.buttons.append(button)
        
        button = Button(self.screen, (200, 80), (150, 30), 'Recharge', 5)
        button.set_on_click(self.game.play_charge_car)
        self.buttons.append(button)

    def __update_interface(self):
        self.screen.fill(IHM.WHITE)
        for b in self.buttons:
            b.draw()
        
        for case in self.cases:
            case.draw()

        self.battery_display.set_battery_lvl(self.game.players[0].get_charge_lvl())
        self.dice_display.set_value(self.game.dice.get_value())

        self.battery_display.draw()
        self.dice_display.draw()

        self.game.update_player_pos()
        for p in self.game.players:
            center = p.current_case.get_position()
            case_dim = p.current_case.get_dimension()
            center = (center[0] + case_dim[0]/2, center[1] + case_dim[1]/2)
            pygame.draw.circle(self.screen, IHM.BLACK, center, 5)

        # index = player.get_position() + 1
        # pawn_pos = cases[-index]
        # pawn_pos = (pawn_pos._position[0] + pawn_pos._dimension[0]/2, pawn_pos._position[1] + pawn_pos._dimension[1]/2)
        # pygame.draw.circle(screen, black, pawn_pos, 5)
    
    def __initializing_board(self):
        #variable de grandeur d'une case
        case_size = (50,50)
        screen_ctr  = (math.floor(self.screen_size[0] / 2), math.floor(self.screen_size[1] / 2))

        #initialisation des variable du plateau
        pos_next = (screen_ctr[0] - case_size[0], screen_ctr[1] - case_size[1])
        line_case_count = 3
        placed = 0
        row = True
        reverse = False

        #Fonction du plateau à 60 case
        for i in range(60, 0, -1):
            self.cases.append(Case(self.screen, pos_next, case_size, i))
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
        
    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        
            self.__update_interface()
            pygame.display.update()
