from typing import Tuple
from enum import Enum


class NotEnoughCharge(ValueError):
    """
    Author     : Gwenaël
    Date       : 15/12/2022
    Version    : 1
    Description: Notify the code that the car has not enough charge to perform
    the deplacement.
    """
    pass

class Voiture:
    """
    Author     : Gwenaël
    Date       : 15/12/2022
    Version    : 2
    Description: Car representation
    """


    MAX_CHARGE:int = 6
    COEFF_DEPLACEMENT:int = 10
    COEFF_CHARGE_FAVORABLE:int = 10
    COEFF_CHARGE_DEFAVORABLE:int = 2

    def __init__(self) -> None:
        self.current_case = 0
        self.__position:int = 0
        self.__charge_lvl:int = 6

        self.__score:int = 0
        self.__stats:Tuple[int, int] = (0, 0)
    
    def deplacement(self, distance:int) -> None:
        decharge_lvl:int = self.current_case.get_needed_battery()
        self.__decharge(decharge_lvl)
        raccourcis = self.current_case.action_to_take()
        self.__position = self.__position + (distance + raccourcis)
        
        self.__score = self.__score + distance * Voiture.COEFF_DEPLACEMENT
    
    def get_charge_lvl(self) -> int:
        return self.__charge_lvl

    def get_position(self) -> int:
        return self.__position

    def __decharge(self, lvl: int) -> None:
        """
        :raises NotEnoughCharge: if the car does not have enough charge to perform the deplacement.
        """
        if lvl <= self.__charge_lvl:
            self.__charge_lvl = self.__charge_lvl - lvl
        else:
            raise NotEnoughCharge
        
    def increment_score_charge(self, value:int, favorable:bool):
        if favorable:
            self.__stats = (self.__stats[0] + 1, self.__stats[1])
            self.__score += Voiture.COEFF_CHARGE_FAVORABLE * value
        else:
            self.__stats += (self.__stats[0], self.__stats[1] + 1)
            self.__score += Voiture.COEFF_CHARGE_DEFAVORABLE * value
    
    def charge(self, lvl: int) -> None:
        if (self.__charge_lvl + lvl) <= Voiture.MAX_CHARGE:
            self.__charge_lvl = self.__charge_lvl + lvl
        else:
            self.__charge_lvl = Voiture.MAX_CHARGE