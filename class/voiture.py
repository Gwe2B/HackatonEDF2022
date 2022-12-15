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
    Version    : 1
    Description: Car representation
    """
    
    DOWN_DECHARGE:int = 1
    FLAT_DECHARGE:int = 2
    CLIMB_DECHARGE:int = 4

    def __init__(self) -> None:
        self.__charge_lvl:int = 6
    
    def deplacement(self, inclinaison:int = PenteEnum.NONE) -> None:
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
    
    def get_charge_lvl(self) -> int:
        return self.__charge_lvl

    def __decharge(self, lvl: int) -> None:
        """
        :raises NotEnoughCharge: if the car does not have enough charge to perform the deplacement.
        """
        if lvl <= self.__charge_lvl:
            self.__charge_lvl = self.__charge_lvl - lvl
        else:
            raise NotEnoughCharge
    
    def charge(self, lvl: int) -> None:
        self.__charge_lvl = self.__charge_lvl + lvl