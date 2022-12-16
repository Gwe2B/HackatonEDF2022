from enum import Enum
from tkinter import *
from tkinter import messagebox



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
        :return: True if the two object are identique, otherwise false
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


    MAX_CHARGE:int = 6

    def __init__(self) -> None:
        self.current_case = 0
        self.__position:int = 0
        self.__charge_lvl:int = 6
    
    def deplacement(self, distance:int, inclinaison:int = PenteEnum.NONE) -> None:
        """simulate the car deplacement

        :param inclinaison: Specify the type of deplacement, defaults to PenteEnum.NONE
        :type inclinaison: int
        """
        decharge_lvl:int = self.current_case.get_needed_battery()
        self.__decharge(decharge_lvl)
        raccourcis = self.current_case.action_to_take()
        self.__position = self.__position + (distance + raccourcis)
        
    
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
            tkinter.messagebox.showinfo(title="info", message="sorry, your battery level is low !", **options)
    
    def charge(self, lvl: int) -> None:
        if (self.__charge_lvl + lvl) <= Voiture.MAX_CHARGE:
            self.__charge_lvl = self.__charge_lvl + lvl
        else:
            self.__charge_lvl = Voiture.MAX_CHARGE