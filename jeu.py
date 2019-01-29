#from objets.hero import *
from objets.personnage import *
import random

def nettoyer():
	import sys,os
	os.system('cls||clear')


def creationPersonnage():
	#nettoye()
	fin=0
	hero=None
	while fin == 0 :
		print("--- Menu de creation de persnnage---")
		print("1. Epéeiste (Epée longue)")
		print("2. Paladin (Bouclier & masse)")
		print("2. Mage (Baguette magique)")
		print("3. Assasin (Dagues)")
		print("[DEV] 0. personnage de base ")
		classe=input("Quel classe souhaitez vous incarner ?")
		if classe == 1:
			#hero=Epeeiste()
			print("Pas encore developpé")
		elif classe == 2:
			#hero=Paladin()
			print("Pas encore developpé")
		elif classe == 3:
			#hero=Mage()
			print("Pas encore developpé")
		elif classe == 4:
			#hero=Assasin()
			print("Pas encore developpé")
		elif classe == "0":
			nom=input("Le nom de votre personnage : ")
			hero=Hero(nom,100,10,5)
			fin=1
		else:
			print("Ceci n est pas possible !\n")
	nettoyer()
	return hero

def lancede(nombre_de_face):
	return random.randint(1,nombre_de_face)

def QuiCommence(hero,adversaire): # retourne le personnage qui commencera chaque tour du combat
	resultat=None
	initiative_adv=lancede(15)
	initiative_hero=lancede(20)
	#print(hero.get_nom(), " Lance un dés 20, resultat : ",initiative_hero)
	#print(adversaire.get_nom(), " Lance un dés 15, resultat : ",initiative_adv)
	while resultat == None:
		if initiative_adv > initiative_hero:
			print("votre adversaire tapera en premier durant tout le combat")
			resultat="adversaire"
		elif initiative_hero > initiative_adv:
			print("vous tapez en premier durant tout le combat")
			resultat="hero"
		else:
			initiative_adv=lancede(15)
			initiative_hero=lancede(20)
	return resultat

def combat(joueur1, joueur2):
	nbtour=0
	joueurmort=None
	while joueurmort == None:

		if nbtour == 0:
			point_de_degats=joueur1._force - joueur2._defense # le joueur 2 se defend
			print(joueur1._nom,"(",joueur1._pv,"PV) inflige ",point_de_degats,"à ",joueur2._nom,"(",joueur2._pv,"PV)")
			if point_de_degats < joueur2._pv:
				pv_restant=joueur2._pv - point_de_degats
				nbtour=1
			elif point_de_degats > joueur2._pv:
				pv_restant=0
				joueurmort=joueur2
			joueur2._set_pv(pv_restant)
		elif nbtour==1:
			point_de_degats=joueur2._force - joueur1._defense
			print(joueur2._nom,"(",joueur2._pv,"PV) inflige ",point_de_degats,"à ",joueur1._nom,"(",joueur1._pv,"PV)")
			if point_de_degats < joueur1._pv:
				pv_restant=joueur1._pv - point_de_degats
				nbtour=0
			elif point_de_degats > joueur1._pv:
				pv_restant=0
				joueurmort=joueur1
			joueur1._set_pv(pv_restant)
	return joueurmort


		
		

def Run():
	print("Bienvenu dans notre jeu !")
	fin=0
	hero=None
	while fin == 0:
		if hero == None:
			print("Création du personnage !")
			hero=creationPersonnage()
			fin=1
	adversaire=Personnage("Murloc",60,6,3)

	ordre=QuiCommence(hero,adversaire)
	#hero.Presentation()
	print(combat(hero,adversaire)._nom," à etait tué")
	#if ordre == "hero":
		
	#else:
	#	combat(adversaire,hero)

Run()