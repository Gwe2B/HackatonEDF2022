#importation du module pygame
import pygame
import math

#intialition pygame
pygame.init()

# Initialing Color
white = (255,255,255)
black = (0,0,0)

#initialisation de la variable font
font = pygame.font.SysFont("Forte", 25)

#création de la fenetre du jeu 
screen_size = (1500, 600)
screen_ctr  = (math.floor(screen_size[0] / 2), math.floor(screen_size[1] / 2))
screen = pygame.display.set_mode(screen_size)
screen.fill(white)

#variable de grandeur d'une case
case_size = 50

#initialisation des variable du plateau
pos_next = (screen_ctr[0] - case_size, screen_ctr[1] - case_size)
line_case_count = 3
placed = 0
row = True
reverse = False

#Fonction du plateau à 60 case
for i in range(60, 0, -1):
    pygame.draw.rect(screen, (black), (pos_next[0], pos_next[1], case_size, case_size), 2) #création d'une case
    screen.blit(font.render(str(i), True, black), pos_next) #création du nombre à l'intérieur de la case
    placed = placed + 1

    if placed >= line_case_count:
        if(not row):
            reverse = not reverse

        row = not row
        line_case_count = line_case_count + 1
        placed = 1

    if reverse:
        buf = case_size * (-1)
    else:
        buf = case_size

    if row:
        pos_next = (pos_next[0] + buf, pos_next[1])
    else:
        pos_next = (pos_next[0], pos_next[1] + buf)
    
    pygame.display.flip() #update de l'affichage

try:
    while True:
        pass
except KeyboardInterrupt:
    pygame.quit()