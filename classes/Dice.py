import random

class Dice:
    """
    Author  : Amine
    Version : 1
    Date    : 15/12/2022
    Description : this class handles generating a random number for dices 
    deplacement dice and charge dice
    """

    BORNE_INF:int = 1
    BORNE_SUP:int = 6

    def __init__(self) -> None:
        self.__value = 0
    
    def throw(self) -> None:
        self.__value = random.randint(Dice.BORNE_INF, Dice.BORNE_SUP)

    def get_value(self) -> int:
        return self.__value



