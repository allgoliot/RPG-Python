from objets.personnage import *
#from objets.monstre import *



def creationPersonnage():
	#nettoye()
	fin=0
	hero=None
	while fin == 0 :
		print("--- Menu de creation de persnnage---")
		print("1. Epéeiste (Epée longue)")
		print("2. Paladin (Bouclier & masse)")
		print("2. Mage (Baguette magique")
		print("3. Assasin (Dagues)")
		print("[DEV] default. personnage de base ")
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
		elif classe == "default":
			hero=Personnage(100,10,5)
			fin=1
		else:
			print("Ceci n'est pas possible !\n")
	return hero


def menu():
	print("Bienvenu dans notre jeu !")
	fin=0
	hero=None
	while fin == 0:
		if hero == None:
			print("Création du personnage !")
			hero=creationPersonnage()
			#hero.affiche()
		else:
			hero.affiche()

menu()