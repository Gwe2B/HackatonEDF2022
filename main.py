from classes.ui.ihm import IHM
import json

BOARD_CONF_PATH:str = "assets/board_config.json"
file = open(BOARD_CONF_PATH, 'r')
json_data = json.load(file)
file.close()

ihm = IHM((1500, 600), json_data)
ihm.mainloop()