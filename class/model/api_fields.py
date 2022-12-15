from datetime import datetime

class ApiField:
    def __init__(self, **kwargs) -> None:
        self.__signal_strenght = kwargs['puissance_maximale'] / 100
        self.__etat_system = kwargs['etat_du_systeme_electrique_pour_la_recharge']

        buf:str = kwargs['date']
        self.__date = datetime.strptime(buf.split('+')[0], '%Y-%m-%dT%H:%M:%S')
    
    def get_signal_strenght(self) -> float:
        return self.__signal_strenght
    
    def get_etat_system(self) -> str:
        return self.__etat_system
    
    def get_date(self):
        return self.__date
    
    def __repr__(self) -> str:
        return f"Signal Strenght: {self.__signal_strenght}\nSystem State: {self.__etat_system}\nDate: {self.__date}"