"Constantes du jeu Half-Vie 3"

import random, math, decimal, pygame
from pygame.locals import *

fenetre = pygame.display.set_mode((1024, 768))

# menus 1024*768
image_accueil = pygame.image.load("ressources/menus/ecrantitre.png").convert()
image_credit = pygame.image.load("ressources/menus/ecrancredit.png").convert()
image_choixperso = pygame.image.load("ressources/menus/ecranperso.png").convert()
image_choixmob = pygame.image.load("ressources/menus/ecranmob.png").convert()
image_aide = pygame.image.load("ressources/menus/ecranaide1.png").convert()
image_aide2 = pygame.image.load("ressources/menus/ecranaide2.png").convert()
image_jeu = pygame.image.load("ressources/menus/ecranjeu.png").convert()
image_fin = pygame.image.load("ressources/menus/ecranfin.png").convert()
image_choixatt = pygame.image.load("ressources/menus/choixatt.png").convert()

# personnages 512*324
image_guerrier = "ressources/personnages/guerrier.png"
image_mage = "ressources/personnages/mage.png"
image_archer = "ressources/personnages/archer.png"
image_paladin = "ressources/personnages/paladin.png"
image_gobelin = "ressources/personnages/gobelin.png"
image_araignee = "ressources/personnages/araignee.png"
image_paladin2 = "ressources/personnages/paladin2.png"
image_sorcier = "ressources/personnages/sorcier.png"

