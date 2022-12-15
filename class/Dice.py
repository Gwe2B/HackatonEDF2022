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
    
    def throw(self) :
        return random.randint(Dice.BORNE_INF, Dice.BORNE_SUP)



