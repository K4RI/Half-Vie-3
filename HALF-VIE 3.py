# Ceci est le code en Python de "Half-Vie 3".
# Voilà.
import random, math, decimal, pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init() # initialisation de Pygame

#Ouverture de la fenêtre Pygame

fenetre = pygame.display.set_mode((1024, 768))
continuer_accueil = 1
continuer = 1
testrand = 0
ntour = 0
choixattperso = 0
font=pygame.font.Font(None, 24)
fontg=pygame.font.Font(None, 32)
fontgg=pygame.font.Font(None, 128)
pévé = font.render(str("/         PV"),1,(255,255,255))
tpoison = font.render(str("POISON       PV/SEC"),1,(0,255,0))
tfeu = font.render(str("ENFLAMMÉ       PV/SEC"),1,(255,0,0))
tparade = font.render(str("PARADE        %"),1,(0,0,255))
tpeur = font.render(str("EFFRAYÉ"),1,(0,255,255))
tarach = font.render(str("ÉTOURDI"),1,(255,0,255))
tleth = font.render(str("LÉTHARGIE"),1,(255,255,0))
tcam = font.render(str("CAMOUFLÉ"),1,(255,255,255))

zik = pygame.mixer.Sound("ressources/zik.wav")
zik.play(loops=-1, maxtime=0, fade_ms=0)



#BOUCLE PRINCIPALE

while continuer:
	while continuer_accueil: #PHASE 1 : TITRE
		#Chargement et affichage de l'écran d'accueil
		fenetre.blit(image_accueil, (0,0))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE: #quitter le jeu
				pygame.quit()
			elif event.type == KEYDOWN and event.key == K_F1: #PHASE 1B : CREDITS
				continuer_credit = 1
				while continuer_credit:
					fenetre.blit(image_credit, (0,0))
					pygame.display.flip()
					for event in pygame.event.get():
						if event.type == KEYDOWN and event.key == K_ESCAPE:
							continuer_credit = 0
							fenetre.blit(image_accueil, (0,0))
							pygame.display.flip()
			elif event.type == KEYDOWN and event.key == K_F2: #PHASE 1C : AIDE (à terminer, peut-être, non ?)
				continuer_aide = 1
				while continuer_aide:
					fenetre.blit(image_aide, (0,0))
					pygame.display.flip()
					for event in pygame.event.get():
						if event.type == KEYDOWN and event.key == K_RETURN:
							continuer_aide2 = 1
							while continuer_aide2:
								fenetre.blit(image_aide2, (0,0))
								pygame.display.flip()
								for event in pygame.event.get():
									if event.type == KEYDOWN and event.key == K_RETURN:
										continuer_aide2 = 0
										continuer_aide = 0
										fenetre.blit(image_accueil, (0,0))
										pygame.display.flip()


			elif event.type == KEYDOWN and event.key == K_RETURN:  #PHASE 2 : CHOIX PERSO  #sprites de 4 persos en 250*200
				perso = Perso('guerrier', 'mage', 'archer', 'paladin')
				continuer_choixperso = 1
				while continuer_choixperso:
					fenetre.blit(image_choixperso, (0,0))
					if n_perso == 1:
						perso.choix = "Guerrier"
						perso.image = perso.guerrier
						perso.force = 6
						perso.dexterite = 3
						perso.constitution = 7
						perso.agilite = 4
						perso.potions = 2
						tcarac = font.render(str("Force : 6    Dextérité : 3     Constitution : 7       Agilité : 4"),1,(255,255,255)) #afficher caractéristiques en-dessous
						fenetre.blit(tcarac, (310, 515))
						textattp1 = fontg.render(str("Coup d'épée"),1,(255,255,255)) #nom des actions possibles en jeu
						textattp2 = fontg.render(str("Parade au bouclier"),1,(255,255,255))
						textattp3 = fontg.render(str("Potion de vie"),1,(255,255,255))
					elif n_perso == 2:
						perso.choix = "Mage"
						perso.image = perso.mage
						perso.force = 2
						perso.dexterite = 9
						perso.constitution = 5
						perso.agilite = 4
						perso.potions = 3
						tcarac = font.render(str("Force : 2    Dextérité : 9     Constitution : 5       Agilité : 4"),1,(255,255,255))
						fenetre.blit(tcarac, (310, 515))
						textattp1 = fontg.render(str("Coup de bâton"),1,(255,255,255))
						textattp2 = fontg.render(str("Boule de feu"),1,(255,255,255))
						textattp3 = fontg.render(str("Sort de soin"),1,(255,255,255))
					elif n_perso == 3:
						perso.choix = "Archer"
						perso.image = perso.archer
						perso.force = 4
						perso.dexterite = 6
						perso.constitution = 3
						perso.agilite = 7
						perso.rescamouflage = 2
						tcarac = font.render(str("Force : 3    Dextérité : 7     Constitution : 2       Agilité : 8"),1,(255,255,255))
						fenetre.blit(tcarac, (310, 515))
						textattp1 = fontg.render(str("Coup de dague"),1,(255,255,255))
						textattp2 = fontg.render(str("Tir à l'arc"),1,(255,255,255))
						textattp3 = fontg.render(str("Camouflage"),1,(255,255,255))
					elif n_perso == 4:
						perso.choix = "Paladin"
						perso.image = perso.paladin
						perso.force = 8
						perso.dexterite = 2
						perso.constitution = 9
						perso.agilite = 1
						perso.rescri = 1
						perso.potions = 1
						tcarac = font.render(str("Force : 8    Dextérité : 2     Constitution : 9       Agilité : 1"),1,(255,255,255))
						fenetre.blit(tcarac, (310, 515))
						textattp1 = fontg.render(str("Coup de glaive"),1,(255,255,255))
						textattp2 = fontg.render(str("Cri de guerre"),1,(255,255,255))
						textattp3 = fontg.render(str("Second souffle"),1,(255,255,255))
					fenetre.blit(perso.image, (400,200)) #afficher image
					fenetre.blit(fontg.render(str(perso.choix),1,(255,255,255)), (470,450)) #afficher nom du perso
					pygame.display.flip()
					for event in pygame.event.get():
						if event.type == KEYDOWN and event.key == K_ESCAPE:
							continuer_choixperso = 0
							fenetre.blit(image_accueil, (0,0))
							pygame.display.flip()
						if event.type == QUIT: #quitter le jeu
							pygame.quit()
						elif event.type == KEYDOWN and event.key == K_LEFT and n_perso >= 2:
							n_perso = n_perso - 1
						elif event.type == KEYDOWN and event.key == K_RIGHT and n_perso <= 3:
							n_perso = n_perso + 1
						elif event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 160 and event.pos[0] < 240 and event.pos[1] > 260 and event.pos[1] < 390 and n_perso >= 2:
							n_perso = n_perso - 1
						elif event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 790 and event.pos[0] < 880 and event.pos[1] > 260 and event.pos[1] < 380 and n_perso <= 3:
							n_perso = n_perso + 1

							
						elif event.type == KEYDOWN and event.key == K_RETURN: #PHASE 3 : CHOIX ADVERSAIRE   #sprites de 4 mobs en 250*200
							ennemi = Ennemi('gobelin', 'araignee', 'paladin de lombre', 'sorcier')
							n_perso = 1
							continuer_choixmob = 1
							while continuer_choixmob:
								fenetre.blit(image_choixmob, (0,0))
								if n_mob == 1:
									ennemi.choix = "Gobelin"
									ennemi.image = ennemi.gobelin
									ennemi.force = 5
									ennemi.dexterite = 5
									ennemi.constitution = 4
									ennemi.agilite = 6
									tcarace = font.render(str("Force : 5    Dextérité : 5     Constitution : 4       Agilité : 6"),1,(255,255,255))
									fenetre.blit(tcarace, (310, 515))
								if n_mob == 2:
									ennemi.choix = "Araignee"
									ennemi.image = ennemi.araignee
									ennemi.force = 7
									ennemi.dexterite = 4
									ennemi.constitution = 8
									ennemi.agilite = 1
									ennemi.resarach = 1
									tcarace = font.render(str("Force : 7    Dextérité : 4     Constitution : 8       Agilité : 1"),1,(255,255,255))
									fenetre.blit(tcarace, (310, 515))
								if n_mob == 3:
									ennemi.choix = "Paladin de lombre"
									ennemi.image = ennemi.paladin2
									ennemi.force = 8
									ennemi.dexterite = 3
									ennemi.constitution = 7
									ennemi.agilite = 2
									ennemi.potions = 1
									tcarace = font.render(str("Force : 8    Dextérité : 3     Constitution : 7       Agilité : 2"),1,(255,255,255))
									fenetre.blit(tcarace, (310, 515))
								if n_mob == 4:
									ennemi.choix = "Sorcier"
									ennemi.image = ennemi.sorcier
									ennemi.force = 3
									ennemi.dexterite = 8
									ennemi.constitution = 5
									ennemi.agilite = 4
									ennemi.resleth = 1
									ennemi.energ = 3
									tcarace = font.render(str("Force : 3    Dextérité : 8     Constitution : 5       Agilité : 4"),1,(255,255,255))
									fenetre.blit(tcarace, (310, 515))
								fenetre.blit(ennemi.image, (400,200))
								fenetre.blit(fontg.render(str(ennemi.choix),1,(255,255,255)), (470,450))
								pygame.display.flip()
								for event in pygame.event.get():
									if event.type == KEYDOWN and event.key == K_ESCAPE:
										continuer_choixmob = 0
										fenetre.blit(image_choixperso, (0,0))
									elif event.type == QUIT: #quitter le jeu
										pygame.quit()
									elif event.type == KEYDOWN and event.key == K_LEFT and n_mob >= 2:
										n_mob = n_mob - 1
									elif event.type == KEYDOWN and event.key == K_RIGHT and n_mob <= 3:
										n_mob = n_mob + 1
									elif event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 160 and event.pos[0] < 240 and event.pos[1] > 260 and event.pos[1] < 390 and n_mob >= 2:
										n_mob = n_mob - 1
									elif event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 790 and event.pos[0] < 880 and event.pos[1] > 260 and event.pos[1] < 380 and n_mob <= 3:
										n_mob = n_mob + 1
									elif event.type == KEYDOWN and event.key == K_RETURN:
										continuer_choixmob = 0
										continuer_choixperso = 0
										continuer_accueil = 0
										continuer_jeu = 1
										n_mob = 1
										pygame.display.flip()



	#des trucs de correspondances entre caractéristiques et influences dans le jeu
	perso.coupmax = 20 + perso.force * 15
	perso.limite = int((random.randint(2,6) * 5) + perso.dexterite * 2.5)
	perso.pv = 50 + perso.constitution * 30
	pvmax = perso.pv
	tpvmax = font.render(str(pvmax),1,(255,255,255))
	perso.armure = perso.constitution * 20 
	perso.ecritique = perso.agilite * 5
	print ("\nperso =", perso.choix, "\ncoupmax =", perso.coupmax, "\nlimite =", int(10 + perso.dexterite * 2.5), "à", int(30 + perso.dexterite * 2.5), "\nPV =", perso.pv, "\nEsquive critique =", perso.ecritique)
	
	ennemi.coupmaxe = 20 + ennemi.force * 15
	ennemi.limitee = (random.randint(2,6) * 5) + ennemi.dexterite * 5
	ennemi.pve = 50 + ennemi.constitution * 30
	pvemax = ennemi.pve
	tpvmaxe = font.render(str(pvemax),1,(255,255,255))
	ennemi.armuree = ennemi.constitution * 20
	ennemi.ecritiquee = ennemi.agilite * 5
	print ("\nennemi =", ennemi.choix, "\ncoupmax =", ennemi.coupmaxe, "\nlimite =", 10 + ennemi.dexterite * 5, "à", 30 + ennemi.dexterite * 5, "\nPV =", ennemi.pve, "\nEsquive critique =", ennemi.ecritiquee)

	def reload():
		"recharger l'écran"
		global fenetre, font, textpv, textpve, image_jeu, pévé, randparade, tparade, poison, tpoison, \
		tnpoison, arach, tarach, leth, tleth, camouflage, tcam, randparadee, tparade, \
		poisone, tfeu, tnfeu, peure, tpeur, textattp1, textattp2, textattp3	
		fenetre = pygame.display.set_mode((1024, 768))
		textpv = font.render(str(perso.pv),1,(255,255,255)) # afficher points de vie
		textpve = font.render(str(ennemi.pve),1,(255,255,255))
		fenetre.blit(image_jeu, (0,0))
		if perso.pv > 0: # barre de vie perso
			pygame.draw.rect(fenetre, (0,0,255), Rect((106,61), (364*perso.pv/pvmax, 37)))
		if ennemi.pve > 0: # barre de vie ennemi
			pygame.draw.rect(fenetre, (255,0,0), Rect((972-364*ennemi.pve/pvemax,61), (364*ennemi.pve/pvemax, 37)))
		fenetre.blit(perso.image, (50,200)) #afficher les sprites des personnages
		fenetre.blit(ennemi.image, (662,200))
		fenetre.blit(textpv, (360, 70))
		fenetre.blit(tpvmax, (400, 70))
		fenetre.blit(pévé, (390, 70))
		fenetre.blit(textpve, (620, 70))
		fenetre.blit(pévé, (650, 70))
		fenetre.blit(tpvmaxe, (660, 70))
		if perso.randparade<1: # afficher les effets secondaires actifs
			fenetre.blit(tparade, (5, 10))
			fenetre.blit(font.render(str(int(perso.randparade*100)),1,(0,0,255)), (80, 10))
		if perso.poison:
			fenetre.blit(tpoison, (135, 10))
			fenetre.blit(font.render(str(perso.poison),1,(0,255,0)), (205, 10))
		if perso.arach:
			fenetre.blit(tarach, (5, 10))
		if perso.leth:
			fenetre.blit(tleth, (5, 10))
		if perso.camouflage:
			fenetre.blit(tcam, (5, 10))
		if ennemi.randparadee<1:
			fenetre.blit(tparade, (670, 10))
			fenetre.blit(font.render(str(int(ennemi.randparadee*100)),1,(0,0,255)), (745, 10))
		if ennemi.poisone:
			fenetre.blit(tfeu, (800, 10))
			fenetre.blit(font.render(str(ennemi.poisone),1,(255,0,0)), (900, 10))
		if ennemi.peure:
			fenetre.blit(tpeur, (800, 10))
		pygame.display.flip() # recharger l'image


	while continuer_jeu:
		while ennemi.pve > 0 and perso.pv > 0:
			reload() #
			ntour = ntour + 1
			fontg=pygame.font.Font(None, 48)
			textcn1 = fontgg.render(str(ntour),1,(255,255,255))
			fenetre.blit(fontgg.render(str("TOUR N°"),1,(255,255,255)), (300,640))
			fenetre.blit(textcn1, (700,640))
			pygame.display.flip()
			fontg=pygame.font.Font(None, 32)
			pygame.time.delay(2000) #PAUSE 2 SEC
			perso.limite = int((random.randint(2,6) * 5) + perso.dexterite * 2.5)
			for event in pygame.event.get():
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE: #quitter le jeu
					pygame.quit()
			reload()
			if perso.arach <= 0: #BOUCLE D'ATTAQUE PERSO
				fenetre.blit(image_choixatt, (5, 580))
				fenetre.blit(textattp1, (685, 590))
				fenetre.blit(textattp2, (550, 620))
				fenetre.blit(textattp3, (820, 620))
				pygame.display.flip()
				while choixattperso==0:
					for event in pygame.event.get():    #Attente des événements
						if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 650 and event.pos[0] < 1020 and event.pos[1] > 575 and event.pos[1] < 615:
							choixattperso = 1
						elif event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 520 and event.pos[0] < 790 and event.pos[1] > 610 and event.pos[1] < 650:
							choixattperso = 2
						elif event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] > 790 and event.pos[0] < 1020 and event.pos[1] > 610 and event.pos[1] < 650:
							choixattperso = 3
					
				reload()
				if choixattperso == 1:
					if perso.choix == 'Guerrier':
						perso.coup_epee(perso.coup, perso.coupmax, perso.pv, ennemi, ennemi.pve, ennemi.randparadee)
					if perso.choix == 'Mage':
						perso.coup_baton(perso.coup, perso.coupmax, perso.pv, ennemi, ennemi.pve, ennemi.randparadee)
					if perso.choix == 'Archer':
						perso.coup_dague(perso.coup, perso.coupmax, perso.pv, ennemi, ennemi.pve, ennemi.randparadee)
					if perso.choix == 'Paladin':
						perso.coup_glaive(perso.coup, perso.coupmax, perso.pv, ennemi, ennemi.pve, ennemi.randparadee)
				if choixattperso == 2:
					if perso.choix == 'Guerrier':
						perso.parade_bouclier(perso.pv, perso.randparade)
					if perso.choix == 'Mage':
						perso.bouledefeu(ennemi, ennemi.pve, ennemi.poisone)
					if perso.choix == 'Archer':
						perso.tir_arc(perso.coup, perso.coupmax, ennemi, ennemi.pve)
					if perso.choix == 'Paladin':
						perso.crideguerre(perso.rescri, ennemi, ennemi.peure)
				if choixattperso == 3:
					if perso.choix == 'Guerrier':
						perso.potion_guerrier(perso.pv, perso.pvplus)
					if perso.choix == 'Mage':
						perso.sort_soin(perso.pv, perso.pvplus)
					if perso.choix == 'Archer':
						perso.acamouflage(perso.camouflage, perso.rescamouflage)
					if perso.choix == 'Paladin':
						perso.secondsouffle(perso.pv, perso.pvplus)
			else:
				perso.arach = perso.arach - 1
			pygame.time.delay(3000) #PAUSE 2 SEC
			for event in pygame.event.get():
				if event.type == QUIT: #quitter le jeu
					pygame.quit()
			reload() #
			ennemi.randparadee = 1
			choixattperso = 0
			perso.pv = perso.pv - perso.poison
			ennemi.limitee = int((random.randint(2,6) * 5) + ennemi.dexterite * 2.5)
			if ennemi.peure <= 0: #BOUCLE ATTAQUE ENNEMIE
				choixattennemi = random.randint(1,3)
				if choixattennemi == 1:
					if ennemi.choix == 'Gobelin':
						ennemi.coup_lance(ennemi.coupe, ennemi.coupmaxe, ennemi.pve, perso, perso.pv, perso.camouflage)
					if ennemi.choix == 'Araignee':
						ennemi.coup_mandibule(ennemi.coupe, ennemi.coupmaxe, ennemi.pve, perso, perso.pv, perso.camouflage)
					if ennemi.choix == 'Paladin de lombre':
						ennemi.coup_glaivee(ennemi.coupe, ennemi.coupmaxe, ennemi.pve, perso, perso.pv, perso.camouflage)
					if ennemi.choix == 'Sorcier':
						ennemi.coup_baton(ennemi.coupe, ennemi.coupmaxe, ennemi.pve, perso, perso.pv, perso.camouflage)
				if choixattennemi == 2:
					if ennemi.choix == 'Gobelin':
						ennemi.coup_lance(ennemi.coupe, ennemi.coupmaxe, ennemi.pve, perso, perso.pv, perso.camouflage)
					if ennemi.choix == 'Araignee':
						ennemi.morsure(perso, perso.pv, perso.poison)
					if ennemi.choix == 'Paladin de lombre':
						ennemi.parade_boucliere(ennemi.pve, ennemi.randparadee, perso, perso.coup)
					if ennemi.choix == 'Sorcier':
						ennemi.lethargie(ennemi.resleth, perso, perso.coupmax, perso.limite)
				if choixattennemi == 3:
					if ennemi.choix == 'Gobelin':
						ennemi.coup_lance(ennemi.coupe, ennemi.coupmaxe, ennemi.pve, perso, perso.pv, perso.camouflage)
					if ennemi.choix == 'Araignee':
						ennemi.arachno(ennemi.resarach, perso, perso.arach)
					if ennemi.choix == 'Paladin de lombre':
						ennemi.secondsoufflee(ennemi.pve, ennemi.pvpluse, ennemi.potions)
					if ennemi.choix == 'Sorcier':
						ennemi.boule_energie(ennemi.coupe, ennemi.coupmaxe, ennemi.energ, perso, perso.arach, perso.pv, perso.camouflage)
			else:
				ennemi.peure = ennemi.peure - 1
			pygame.time.delay(2000) #PAUSE 2 SEC
			for event in pygame.event.get():
				if event.type == QUIT: #quitter le jeu
					pygame.quit()
			reload() #
			perso.randparade = 1
			ennemi.pve = ennemi.pve - ennemi.poisone
			if perso.camouflage:
				perso.camouflage = perso.camouflage - 1

		continuer_fin = 1
		ntour = 0
		while continuer_fin: #FIN DU JEU (victoire, défaite, ou nul)
			fenetre = pygame.display.set_mode((1024, 768))
			fenetre.blit(image_fin, (0,0))
			if ennemi.pve <= 0 and perso.pv >= 0: # mettre des musiques ptn
				fenetre.blit(fontgg.render("VOUS AVEZ GAGNÉ!",1,(255,0,0)), (100,200))
			if ennemi.pve >= 0 and perso.pv <= 0:
				fenetre.blit(fontgg.render("Vous avez perdu...",1,(255,0,0)), (100,200))
			if ennemi.pve <= 0 and perso.pv <= 0:
				fenetre.blit(pygame.font.Font(None, 72).render("Dans un dernier échange de coups,",1,(255,0,0)), (70,200))
				fenetre.blit(pygame.font.Font(None, 72).render("vous vous entretuez.",1,(255,0,0)), (200,300))
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == QUIT: #quitter le jeu
					pygame.quit()
				elif event.type == KEYDOWN and event.key == K_RETURN: #quitter le jeu
					continuer_fin = 0
					continuer_jeu = 0
					continuer_accueil = 1
