# Défis EDF (Hackaton 2022)

## Problèmatique
La mobilité électrique est un enjeu fort pour EDF, aujourd’hui et pour les années à venir.

Les infrastructures du réseau électrique vont être de plus en plus sollicitées par les usages
liés à la recharge et le comportement des utilisateurs de véhicules électriques est important
pour la bonne réussite de la transition énergétique.

A travers ce défi, nous souhaitons sensibiliser les usagers à ces problématiques, pour qu’ils
prennent conscience de l’importance du pilotage de la recharge des véhicules électriques en
réalisant un jeu autour de ce thème.

## Rendu attendue

Application Web ou/et mobile qui permettra de simuler un jeu de la mobilité électrique.
Parcours séquentiel sur une soixantaine de cases inspiré du jeu de l’oie
- un pion étant une voiture électrique avec 7 niveaux de charge (0 à 6)
- à chaque tour le(s) joueur(s) peut
    1. tirer un dé (de 1 à 6) pour avancer (si son niveau de batterie le permet)
    2. rester un tour sans bouger et tirer un dé pour recharger (dé de 1 à 6) Chaque
déplacement utilise 2 niveaux de batterie en réglé générale, sauf
- si on part d’une case « montée » le déplacement va couter 4 niveaux de batterie
- si on part d’une case « descente » le déplacement va couter 1 niveau de batterie
Aux codeurs de placer ces cases (3 ou plus cases montée, 3 ou plus cases descente)
En option placer aussi
- 2 ou plus cases « tunnel / raccourci », qui permettent, quand on y atterri de sauter
directement à des cases plus élevées (+N cases)
- 2 ou plus cases « dépannage / retour en arrière » qui obligent, quand on y atterri, à reculer
vers des cases plus basses (-N cases)
Le jeu devra également prendre en compte le signal Recharge Vehicule Electrique, publié
par EDF sur son OpenData :
Il faudra alors une notion de temps, ex. le jeu commence à 0h, à chaque tour le temps
avance de (1h 2h 3h, etc. à ajuster).
3
Le signal indique pour chaque heure
- 1 : sur ces heures, la recharge conseillée (dés de recharge de 0 à 6) - 0 : sur ces heures, la
recharge déconseillé (dés de recharge de 0 à 3)
-> Restituer un classement.