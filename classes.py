import random, math, decimal, pygame
from pygame.locals import *

from constantes import *
pygame.init()
n_perso = 1
n_mob = 1
font=pygame.font.Font(None, 24)
fontg=pygame.font.Font(None, 32)
fontgg=pygame.font.Font(None, 128)


class Perso:
	"""Classe pour les persos"""
	def __init__(self, guerrier, mage, archer, paladin):
		#caractéristiques du personnage
		self.force = 0
		self.dexterite = 0
		self.constitution = 0
		self.agilite = 0
		self.limite = 0
		self.coupmax = 0
		self.pv = 0
		self.ecritique = 0
		self.coup = 0
		self.randparade = 1
		self.mana = 0
		self.potions = 0
		self.poison = 0
		self.camouflage = 0
		self.rescamouflage = 0
		self.rescri = 0
		self.pvplus = 0
		self.arach = 0
		self.leth = 0
		#sortes de personnages
		self.guerrier = pygame.image.load(image_guerrier).convert_alpha()
		self.mage = pygame.image.load(image_mage).convert_alpha() 
		self.archer = pygame.image.load(image_archer).convert_alpha()
		self.paladin = pygame.image.load(image_paladin).convert_alpha()
		#choix par défaut
		self.choix = 'guerrier'
		self.image = self.guerrier

	def coup_epee(self, coup, coupmax, pv, ennemi, pve, randparadee):
		fenetre.blit(fontg.render(str("Quelle est la puissance de votre coup ? (dans console)"),1,(0,0,255)), (350,590))
		pygame.display.flip()
		self.coup = int(input())
		if (self.coup > self.coupmax):
			fenetre.blit(fontg.render(str("Vos capacités limitent votre puissance à     . Réessayez."),1,(0,0,255)), (300,620))
			fenetre.blit(fontg.render(str(self.coupmax),1,(0,0,255)), (730,620))
			pygame.display.flip()
			self.coup = int(input())
		self.coup = self.coup * ennemi.randparadee
		self.coup = int(self.coup)
		testrand = random.randint (0,100)
		if testrand < ennemi.ecritiquee:
			self.coup = 0
			fenetre.blit(fontg.render(str("L'ennemi esquive votre attaque."),1,(0,0,255)), (300,680))
		ennemi.pve = ennemi.pve - self.coup
		if (self.coup > self.limite):
			self.collateral = self.coup - self.limite
			self.pv = self.pv - self.collateral
			fenetre.blit(fontg.render(str("Dans votre rage, vous vous blessez à hauteur de     dommages collatéraux."),1,(0,0,255)), (200,710))
			fenetre.blit(fontg.render(str(self.collateral),1,(0,0,255)), (715,710))
		pygame.display.flip()

	def parade_bouclier(self, pv, randparade):
		self.randparade = (random.randint (3,7))/10
		fenetre.blit(fontg.render(str("Vous parez le prochain coup à hauteur de     %."),1,(0,0,255)), (350,640))
		fenetre.blit(fontg.render(str(int(self.randparade*100)),1,(0,0,255)), (790,640))
		pygame.display.flip()

	def potion_guerrier(self, pv, pvplus):
		if self.potions:
			self.pvplus = (random.randint (1,5))
			self.pv = self.pv + (self.constitution*3*self.pvplus)
			fenetre.blit(fontg.render(str("Vous buvez une potion de vie et récupérez     % de vos PV."),1,(0,0,255)), (250,590))
			fenetre.blit(fontg.render(str(self.pvplus*10),1,(0,0,255)), (700,590))
			self.pvplus = 0
			self.potions = self.potions - 1
			fenetre.blit(fontg.render(str("Il vous reste   potion en stock."),1,(0,0,255)), (350,640))
			fenetre.blit(fontg.render(str(self.potions),1,(0,0,255)), (480,640))
		else:
			fenetre.blit(fontg.render(str("Vous tentez de vous soigner, mais vous n'avez plus aucune potion sur vous."),1,(255,255,255)), (150,590))
		pygame.display.flip()

	def coup_baton(self, coup, coupmax, pv, ennemi, pve, randparadee):
		fenetre.blit(fontg.render(str("Quelle est la puissance de votre coup ? (dans console)"),1,(0,0,255)), (350,590))
		pygame.display.flip()
		self.coup = int(input())
		if (self.coup > self.coupmax):
			fenetre.blit(fontg.render(str("Vos capacités limitent votre puissance à     . Réessayez."),1,(0,0,255)), (300,620))
			fenetre.blit(fontg.render(str(self.coupmax),1,(0,0,255)), (730,620))
			pygame.display.flip()
			self.coup = int(input())
		self.coup = self.coup * ennemi.randparadee
		self.coup = int(self.coup)
		testrand = random.randint (0,100)
		pygame.time.delay(500)
		if testrand < ennemi.ecritiquee:
			self.coup = 0
			fenetre.blit(fontg.render(str("L'ennemi esquive votre attaque."),1,(0,0,255)), (100,680))
		ennemi.pve = ennemi.pve - self.coup
		if (self.coup > self.limite):
			self.collateral = self.coup - self.limite
			self.pv = self.pv - self.collateral
			fenetre.blit(fontg.render(str("Dans votre rage, vous vous blessez à hauteur de     dommages collatéraux."),1,(0,0,255)), (200,710))
			fenetre.blit(fontg.render(str(self.collateral),1,(255,255,255)), (715,710))
		pygame.display.flip()

	def bouledefeu(self, ennemi, pve, poisone):
		ennemi.poisone = random.randint (10,30)
		pygame.time.delay(500)
		fenetre.blit(fontg.render(str("Vous lancez une boule de feu à votre ennemi d'une puissance de      PV par tour."),1,(0,0,255)), (100,620))
		fenetre.blit(fontg.render(str(ennemi.poisone),1,(0,0,255)), (780,620))
		pygame.display.flip()

	def sort_soin(self, pv, pvplus):
		if self.potions:
			self.pvplus = (random.randint (1,5))
			self.pv = self.pv + (self.constitution*3*self.pvplus)
			fenetre.blit(fontg.render(str("Vous utilisez un sort de soin et récupérez     % de vos PV."),1,(0,0,255)), (250,590))
			fenetre.blit(fontg.render(str(self.pvplus*10),1,(0,0,255)), (690,590))
			self.pvplus = 0
			self.potions = self.potions - 1
			fenetre.blit(fontg.render(str("Il vous reste   sorts en stock."),1,(0,0,255)), (350,640))
			fenetre.blit(fontg.render(str(self.potions),1,(0,0,255)), (480,640))
		else:
			fenetre.blit(fontg.render(str("Vous tentez de vous soigner, mais vous n'avez plus aucune potion sur vous."),1,(0,0,255)), (150,590))
		pygame.display.flip()
		pygame.time.delay(500)

	def coup_dague(self, coup, coupmax, pv, ennemi, pve, randparadee):
		fenetre.blit(fontg.render(str("Quelle est la puissance de votre coup ? (dans console)"),1,(0,0,255)), (350,590))
		pygame.display.flip()
		self.coup = int(input())
		if (self.coup > self.coupmax):
			fenetre.blit(fontg.render(str("Vos capacités limitent votre puissance à     . Réessayez."),1,(0,0,255)), (300,620))
			fenetre.blit(fontg.render(str(self.coupmax),1,(0,0,255)), (730,620))
			pygame.display.flip()
			self.coup = int(input())
		self.coup = self.coup * ennemi.randparadee
		self.coup = int(self.coup)
		testrand = random.randint (0,100)
		if testrand < ennemi.ecritiquee:
			self.coup = 0
			fenetre.blit(fontg.render(str("L'ennemi esquive votre attaque."),1,(0,0,255)), (100,680))
		ennemi.pve = ennemi.pve - self.coup
		if (self.coup > self.limite):
			self.collateral = self.coup - self.limite
			self.pv = self.pv - self.collateral
			fenetre.blit(fontg.render(str("Dans votre rage, vous vous blessez à hauteur de     dommages collatéraux."),1,(0,0,255)), (200,710))
			fenetre.blit(fontg.render(str(self.collateral),1,(0,0,255)), (715,710))
		pygame.display.flip()

	def tir_arc(self, coup, coupmax, ennemi, pve):
		fenetre.blit(fontg.render(str("Quelle est la puissance de votre tir ? (entre 1 et 100)"),1,(0,0,255)), (350,590))
		fenetre.blit(fontg.render(str("Plus le tir sera puissant, moins la flèche aura de chances d'atteindre sa cible."),1,(0,0,255)), (150,610))
		pygame.display.flip()
		self.coup = int(input())
		if (self.coup > 100):
			fenetre.blit(fontg.render(str("Vos capacités limitent votre puissance à 100. Réessayez."),1,(0,0,255)), (300,640))
			pygame.display.flip()
			self.coup = int(input())
		testrand = random.randint (0,100)
		if testrand < self.coup:
			fenetre.blit(fontg.render(str("Votre flèche n'a pas atteint sa cible."),1,(0,0,255)), (300,670))
		elif testrand >= self.coup:
			fenetre.blit(fontg.render(str("Votre flèche a atteint sa cible."),1,(0,0,255)), (300,670))
			ennemi.pve = ennemi.pve - self.coup
		pygame.display.flip()

	def acamouflage(self, camouflage, rescamouflage):
		if self.rescamouflage:
			self.rescamouflage = self.rescamouflage - 1
			self.camouflage = 3
			fenetre.blit(fontg.render(str("Vous vous camouflez dans la nature, et ne subirez aucun dégât d'attaque"),1,(0,0,255)), (100,600))
			fenetre.blit(fontg.render(str(" directe lors des trois prochains tours."),1,(0,0,255)), (300,640))
			fenetre.blit(fontg.render(str("Cette action ne sera plus utilisable au cours de la partie."),1,(0,0,255)), (200,710))
		else:
			fenetre.blit(fontg.render(str("Vous tentez de vous camoufler dans le décor environnant, mais votre cosmos n'est plus assez puissant."),1,(0,0,255)), (200,600))
		pygame.display.flip()
		pygame.time.delay(2000)

	def coup_glaive(self, coup, coupmax, pv, ennemi, pve, randparadee):
		fenetre.blit(fontg.render(str("Quelle est la puissance de votre coup ? (dans console)"),1,(0,0,255)), (350,590))
		pygame.display.flip()
		self.coup = int(input())
		if (self.coup > self.coupmax):
			fenetre.blit(fontg.render(str("Vos capacités limitent votre puissance à     . Réessayez."),1,(0,0,255)), (300,620))
			fenetre.blit(fontg.render(str(self.coupmax),1,(0,0,255)), (730,620))
			pygame.display.flip()
			self.coup = int(input())
		self.coup = self.coup * ennemi.randparadee
		self.coup = int(self.coup)
		testrand = random.randint (0,100)
		if testrand < ennemi.ecritiquee:
			self.coup = 0
			fenetre.blit(fontg.render(str("L'ennemi esquive votre attaque."),1,(0,0,255)), (100,680))
		ennemi.pve = ennemi.pve - self.coup
		if (self.coup > self.limite):
			self.collateral = self.coup - self.limite
			self.pv = self.pv - self.collateral
			fenetre.blit(fontg.render(str("Dans votre rage, vous vous blessez à hauteur de     dommages collatéraux."),1,(0,0,255)), (200,710))
			fenetre.blit(fontg.render(str(self.collateral),1,(0,0,255)), (715,710))
		pygame.display.flip()

	def crideguerre(self, rescri, ennemi, peure):
		if self.rescri:
			self.rescri = self.rescri - 1
			ennemi.peure = 2
			fenetre.blit(fontg.render(str("Vous terrorisez votre adversaire, qui reste paralysé de peur durant les deux prochains tours."),1,(0,0,255)), (20,600))
			fenetre.blit(fontg.render(str("Cette action ne sera plus utilisable au cours de la partie."),1,(0,0,255)), (200,680))
		else:
			fenetre.blit(fontg.render(str("Vous hurlez sur votre adversaire pour l'intimider, mais il garde son sang-froid."),1,(0,0,255)), (50,600))
		pygame.display.flip()
		pygame.time.delay(2000)

	def secondsouffle(self, pv, pvplus):
		if self.potions:
			self.pvplus = (random.randint (1,5))
			self.pv = self.pv + (self.constitution*3*self.pvplus)
			fenetre.blit(fontg.render(str("Vous soufflez un coup et récupérez     % de vos PV."),1,(0,0,255)), (250,590))
			fenetre.blit(fontg.render(str(self.pvplus*10),1,(0,0,255)), (620,590))
			self.pvplus = 0
			self.potions = self.potions - 1
			fenetre.blit(fontg.render(str("Il vous reste   seconds souffles en stock."),1,(0,0,255)), (350,640))
			fenetre.blit(fontg.render(str(self.potions),1,(0,0,255)), (480,640))	
		else:
			fenetre.blit(fontg.render(str("Vous tentez de vous ressourcer en faisant appel à la Nature,"),1,(0,0,255)), (100,680))
			fenetre.blit(fontg.render(str(" mais votre cosmos n'est plus assez puissant."),1,(0,0,255)), (100,710))
		pygame.display.flip()
		pygame.time.delay(1000)
		

class Ennemi:
	"""Classe pour les persos"""
	def __init__(self, gobelin, araignee, paladin2, sorcier):
		#caractéristiques du personnage
		self.force = 0
		self.dexterite = 0
		self.constitution = 0
		self.agilite = 0
		self.limitee = 0
		self.coupmaxe = 0
		self.pve = 0
		self.ecritiquee = 0
		self.coupe = 0
		self.poisone = 0
		self.peure = 0
		self.randparadee = 1
		self.pvpluse = 0
		self.resleth = 0
		#sortes de personnages
		self.gobelin = pygame.image.load(image_gobelin).convert_alpha()
		self.araignee = pygame.image.load(image_araignee).convert_alpha() 
		self.paladin2 = pygame.image.load(image_paladin2).convert_alpha()
		self.sorcier = pygame.image.load(image_sorcier).convert_alpha()
		#choix par défaut
		self.choix = 'gobelin'
		self.image = self.gobelin

	def coup_lance(self, coupe, coupmaxe, pve, perso, pv, camouflage):
		self.coupe = random.randint(1,coupmaxe)
		self.coupe = self.coupe * perso.randparade
		self.coupe = int(self.coupe)
		testrand = random.randint (0,100)
		if testrand < perso.ecritique:
			self.coupe = 0
			fenetre.blit(fontg.render(str("Vous esquivez l'attaque ennemie."),1,(255,0,0)), (350,590))
			pygame.display.flip()
		if perso.camouflage:
			self.coupe = 0
			fenetre.blit(fontg.render(str("Le gobelin a tenté de vous attaquer, mais vous étiez caché."),1,(255,0,0)), (250,620))
			pygame.display.flip()
		if self.coupe > 0:
			fenetre.blit(fontg.render(str("Le gobelin vous attaque à hauteur de       points d'attaque."),1,(255,0,0)), (250,620))
			fenetre.blit(fontg.render(str(self.coupe),1,(255,0,0)), (645,620))
			pygame.display.flip()
		perso.pv = perso.pv - self.coupe
		if (self.coupe > self.limitee):
			self.collaterale = self.coupe - self.limitee
			self.pve = self.pve - self.collaterale
			fenetre.blit(fontg.render(str("Dans sa rage, le gobelin se blesse à hauteur de      dommages collatéraux."),1,(255,0,0)), (150,670))
			fenetre.blit(fontg.render(str(self.collaterale),1,(255,0,0)), (645,670))
			pygame.display.flip()

	def coup_mandibule(self, coupe, coupmaxe, pve, perso, pv, camouflage):
		self.coupe = random.randint(1,coupmaxe)
		self.coupe = self.coupe * perso.randparade
		self.coupe = int(self.coupe)
		testrand = random.randint (0,100)
		if testrand < perso.ecritique:
			self.coupe = 0
			fenetre.blit(fontg.render(str("Vous esquivez l'attaque ennemie."),1,(255,0,0)), (350,590))
			pygame.display.flip()
		if perso.camouflage:
			self.coupe = 0
			fenetre.blit(fontg.render(str("L'araignée a tenté de vous attaquer, mais vous étiez caché."),1,(255,0,0)), (250,620))
			pygame.display.flip()
		if self.coupe > 0:
			fenetre.blit(fontg.render(str("L'araignée vous attaque à hauteur de       points d'attaque."),1,(255,0,0)), (250,620))
			fenetre.blit(fontg.render(str(self.coupe),1,(255,0,0)), (645,620))
			pygame.display.flip()
		perso.pv = perso.pv - self.coupe
		if (self.coupe > self.limitee):
			self.collaterale = self.coupe - self.limitee
			self.pve = self.pve - self.collaterale
			fenetre.blit(fontg.render(str("Dans sa rage, l'araignée se blesse à hauteur de      dommages collatéraux."),1,(255,0,0)), (150,670))
			fenetre.blit(fontg.render(str(self.collaterale),1,(255,0,0)), (645,670))
			pygame.display.flip()

	def morsure(self, perso, pv, poison):
		perso.poison = random.randint (10,30)
		pygame.time.delay(500)
		fenetre.blit(fontg.render(str("L'araignée vous bondit dessus et vous injecte un violent poison."),1,(255,0,0)), (220,620))
		fenetre.blit(fontg.render(str("A partir de maintenant, vous perdrez     PV par tour."),1,(255,0,0)), (250,660))
		fenetre.blit(fontg.render(str(perso.poison),1,(255,0,0)), (645,660))
		pygame.display.flip()
		
	def arachno(self, resarach, perso, arach):
		if self.resarach:
			self.resarach = self.resarach - 1
			perso.arach = 1
			fenetre.blit(fontg.render(str("L'araignée déclenche chez vous une forte crise d'arachnophobie."),1,(255,0,0)), (220,620))
			fenetre.blit(fontg.render(str("Vous ne pourrez agir durant le prochain tour."),1,(255,0,0)), (270,660))
			pygame.display.flip()
		else:
			fenetre.blit(fontg.render(str("L'araignée reste passive pour ce tour."),1,(255,0,0)), (300,620))
			pygame.display.flip()

	def coup_glaivee(self, coupe, coupmaxe, pve, perso, pv, camouflage):
		self.coupe = 90
		self.coupe = self.coupe * perso.randparade
		self.coupe = int(self.coupe)
		testrand = random.randint (0,100)
		if testrand < perso.ecritique:
			self.coupe = 0
			fenetre.blit(fontg.render(str("Vous esquivez l'attaque ennemie."),1,(255,0,0)), (350,590))
			pygame.display.flip()
		if perso.camouflage:
			self.coupe = 0
			fenetre.blit(fontg.render(str("Le paladin de l'ombre a tenté de vous attaquer, mais vous étiez caché."),1,(255,0,0)), (250,620))
			pygame.display.flip()
		if self.coupe > 0:
			fenetre.blit(fontg.render(str("Le paladin de l'ombre vous attaque à hauteur de       points d'attaque."),1,(255,0,0)), (250,620))
			fenetre.blit(fontg.render(str(self.coupe),1,(255,0,0)), (760,620))
			pygame.display.flip()
		perso.pv = perso.pv - self.coupe
		if (self.coupe > self.limitee):
			self.collaterale = self.coupe - self.limitee
			self.pve = self.pve - self.collaterale
			fenetre.blit(fontg.render(str("Dans sa rage, le paladin de l'ombre se blesse à hauteur de      dommages collatéraux."),1,(255,0,0)), (50,670))
			fenetre.blit(fontg.render(str(self.collaterale),1,(255,0,0)), (665,670))
			pygame.display.flip()

	def parade_boucliere(self, pve, randparadee, perso, coup):
		self.randparadee = (random.randint (3,7))/10
		fenetre.blit(fontg.render(str("Le paladin de l'ombre parera le prochain coup à hauteur de     %."),1,(255,0,0)), (150,640))
		fenetre.blit(fontg.render(str(int(self.randparadee*100)),1,(255,0,0)), (775,640))
		pygame.display.flip()

	def secondsoufflee(self, pve, pvpluse, potions):
		if self.potions:
			self.pvpluse = (random.randint (1,5))
			self.pve = self.pve+(self.constitution*3*self.pvpluse)
			fenetre.blit(fontg.render(str("Le paladin de l'ombre souffle un coup et regagne     % de ses PV."),1,(255,0,0)), (250,590))
			fenetre.blit(fontg.render(str(self.pvpluse*10),1,(255,0,0)), (765,590))
			self.pvpluse = 0
			self.potions = self.potions - 1
			pygame.display.flip()
		else:
			fenetre.blit(fontg.render(str("Le paladin reste passif pour ce tour."),1,(255,0,0)), (300,620))
			pygame.display.flip()
		
	def coup_baton(self, coupe, coupmaxe, pve, perso, pv, camouflage):
		self.coupe = random.randint(1,coupmaxe)
		self.coupe = self.coupe * perso.randparade
		self.coupe = int(self.coupe)
		testrand = random.randint (0,100)
		if testrand < perso.ecritique:
			self.coupe = 0
			fenetre.blit(fontg.render(str("Vous esquivez l'attaque ennemie."),1,(255,0,0)), (350,590))
			pygame.display.flip()
		if perso.camouflage:
			self.coupe = 0
			fenetre.blit(fontg.render(str("Le sorcier a tenté de vous attaquer, mais vous étiez caché."),1,(255,0,0)), (250,620))
			pygame.display.flip()
		if self.coupe > 0:
			fenetre.blit(fontg.render(str("Le sorcier vous attaque à hauteur de       points d'attaque."),1,(255,0,0)), (250,620))
			fenetre.blit(fontg.render(str(self.coupe),1,(255,0,0)), (645,620))
			pygame.display.flip()
		perso.pv = perso.pv - self.coupe
		if (self.coupe > self.limitee):
			self.collaterale = self.coupe - self.limitee
			self.pve = self.pve - self.collaterale
			fenetre.blit(fontg.render(str("Dans sa rage, le sorcier se blesse à hauteur de      dommages collatéraux."),1,(255,0,0)), (150,670))
			fenetre.blit(fontg.render(str(self.collaterale),1,(255,0,0)), (645,670))
			pygame.display.flip()

	def lethargie(self, resleth, perso, coupmax, limite):
		if self.resleth:
			perso.coupmax = perso.coupmax * 0.75
			perso.coupmax = int(perso.coupmax)
			perso.limite = perso.limite * 0.5
			perso.limite = int(perso.limite)
			self.resleth = self.resleth - 1
			perso.leth = 1
			fenetre.blit(fontg.render(str("Le sorcier vous plonge dans une profonde léthargie."),1,(255,0,0)), (200,620))
			fenetre.blit(fontg.render(str("Votre puissance d'attaque et votre résistance aux dommages diminuent définitivement."),1,(255,0,0)), (50,660))
			pygame.display.flip()
		else:
			fenetre.blit(fontg.render(str("Le sorcier reste passif pour ce tour."),1,(255,0,0)), (300,620))
			pygame.display.flip()

	def boule_energie(self, coupe, coupmaxe, energ, perso, arach, pv, camouflage):
		if ennemi.energ:
			perso.arach = 1
			self.coupe = random.randint(1, 20)
			if perso.camouflage:
				self.coupe = 0
			fenetre.blit(fontg.render(str("Le sorcier vous assène une décharge d'énergie noire à hauteur de      PV et vous étourdit."),1,(255,0,0)), (50,670))
			fenetre.blit(fontg.render(str(self.coupe),1,(255,0,0)), (758,670))
			pygame.display.flip()
			perso.pv = perso.pv - self.coupe
		else:
			fenetre.blit(fontg.render(str("Le sorcier reste passif pour ce tour."),1,(255,0,0)), (300,620))
			pygame.display.flip()
		
