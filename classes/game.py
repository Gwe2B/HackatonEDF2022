from math import floor
from classes.dice import Dice
from classes.voiture import NotEnoughCharge, Voiture
from classes.request_manager import RequestManager


class Game:
    """
    Author     : Gwenaël Guiraud & Amine Maourid
    Date       : 15/12/2022
    Version    : 3
    Description: Hold the main logic of the game
    """
    
    def __init__(self) -> None:
        self.players = [Voiture()]

        self.dice = Dice()
        self.player_to_play = 0
        self.cases = []

        # Time in hours (one turn = one hour)
        self.__time = 0
        RequestManager.get(RequestManager.API_URL)

        self.dice.throw()

    def update_player_pos(self) -> None:
        for p in self.players:
            p.current_case = self.cases[-(p.get_position()+1)]

    def play_charge_car(self) -> None:
        """The player choose to charge his car."""
        effective_charge = floor(self.dice.get_value()*RequestManager.records[self.__time].get_signal_strenght())
        self.players[self.player_to_play].increment_score_charge(effective_charge, RequestManager.records[self.__time].get_signal_strenght() == 1.0)

        self.players[self.player_to_play].charge(effective_charge)
        self.__next_player()
        self.dice.throw()
    
    def play_displace(self) -> None:
        """The player choose to displace his car"""
        try:
            self.players[self.player_to_play].deplacement(self.dice.get_value())
            self.__next_player()
            self.dice.throw()
        except NotEnoughCharge:
            print('You can\'t')

    def get_time(self) -> int:
        return self.__time

    def __next_player(self) -> None:
        """Change the player and permit to manage the time advance. (For now only one player is supported)"""
        self.player_to_play = self.player_to_play + 1
        if self.player_to_play > (len(self.players) - 1):
            self.player_to_play = 0

            self.__time = self.__time + 1
            if(self.__time >= 24):
                self.__time = self.__time - 24