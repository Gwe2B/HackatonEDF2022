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

class PenteEnum(Enum):
    """
    Author     : Gwenaël
    Date       : 15/12/2022
    Version    : 1
    Description: Enumerate all the possibilities of the deplacement types.
    """
    
    MONTEE = 1
    NONE = 0
    DESCENTE = -1

    def __eq__(self, __o: object) -> bool:
        """Just compare the current object with the given one

        :param __o: The object to compare to
        :type __o: object
        :return: True if the two object is identique, otherwise false
        :rtype: bool
        """
        return (self.__class__ is __o.__class__) and (self.value == __o.value)

class Voiture:
    """
    Author     : Gwenaël
    Date       : 15/12/2022
    Version    : 2
    Description: Car representation
    """
    
    DOWN_DECHARGE:int = 1
    FLAT_DECHARGE:int = 2
    CLIMB_DECHARGE:int = 4

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
    
    def deplacement(self, distance:int, inclinaison:int = PenteEnum.NONE) -> None:
        """simulate the car deplacement

        :param inclinaison: Specify the type of deplacement, defaults to PenteEnum.NONE
        :type inclinaison: int
        """
        decharge_lvl:int = 0
        if inclinaison == PenteEnum.MONTEE:
            decharge_lvl = Voiture.CLIMB_DECHARGE
        elif inclinaison == PenteEnum.DESCENTE:
            decharge_lvl = Voiture.DOWN_DECHARGE
        else:
            decharge_lvl = Voiture.FLAT_DECHARGE
        
        self.__decharge(decharge_lvl)
        self.__position = self.__position + distance
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