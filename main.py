#importation du module pygame
import pygame
from pygame.locals import *
from pygame import rect, Rect
import sys

#intialition pygame
pygame.init()



# Initialing Color
white = (255,255,255)
black = (0,0,0)

#création de la fenetre du jeu 
size_x = 1500
size_y = 600
screen = pygame.display.set_mode((size_x,size_y))
screen.fill(white)



#initialisation de la valeur run
run = True
while run:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              run = False # Flag that we are done so we can exit the while loop

    
    
    # Drawing plateau
    font = pygame.font.SysFont("Forte", 25)
    fichier = open("plateau.txt","r")

    niv = []
    for ligne in fichier:
        ligne_niv = []
        for i in ligne:
            if i != '\n':
                ligne_niv.append(i)
        niv.append(ligne_niv)  
    fichier.close()

    num_ligne = 0
    number = 0
    for ligne in niv:
        num_case = 0
        for i in ligne:
            if i == 'X':
                pygame.draw.rect(screen, (black), (54*num_case,54*num_ligne, 50, 50), 2)
                screen.blit(font.render(str(number), True, black), (54*num_case,54*num_ligne))
                number += 1
            elif i == 'o':
                pygame.draw.rect(screen, (white), (54*num_case,54*num_ligne, 50, 50), 2)
            num_case += 1
        num_ligne += 1 
    pygame.display.flip()
        
pygame.quit()