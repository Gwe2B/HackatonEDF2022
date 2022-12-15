import random
class Dice:
    """
    Author  : Amine
    Version : 1
    Date    : 15/12/2022
    Description : this class handles generating a random number for dices 
    deplacement dice and charge dice
    """
    
    def __init__(self, type):
        self.type = type
    def throwGod(self) :
        result = random.randint(1, 6)
        return result 



