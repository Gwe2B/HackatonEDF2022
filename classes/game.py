from classes.dice import Dice
from classes.voiture import NotEnoughCharge, Voiture


class Game:
    def __init__(self) -> None:
        self.players = [Voiture()]

        self.dice = Dice()
        self.player_to_play = 0
        self.cases = []

        self.dice.throw()

    def update_player_pos(self):
        for p in self.players:
            p.current_case = self.cases[-(p.get_position()+1)]

    def play_charge_car(self):
        self.players[self.player_to_play].charge(self.dice.get_value())
        self.__next_player()
        self.dice.throw()
    
    def play_displace(self):
        try:
            self.players[self.player_to_play].deplacement(self.dice.get_value())
            self.__next_player()
            self.dice.throw()
        except NotEnoughCharge:
            print('You can\'t')

    def __next_player(self):
        self.player_to_play = self.player_to_play + 1
        if self.player_to_play > (len(self.players) - 1):
            self.player_to_play = 0