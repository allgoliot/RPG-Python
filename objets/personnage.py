#classe personnage : pv, force, defense
## pv = 100
## force = 10
## defense = 5
### méthode attaque : force 
### méthode defense : defense*2 puis force+5 au prochain tour
import random

class Personnage:
	def __init__(self,nom,pv,force,defense):
		self._nom = nom
		self._pv = pv
		self._force = force
		self._defense = defense

	#def Attaque(self):
		#return self._force

	#Récuperer les pv
	def _get_pv(self):
		return self._pv

	#Attribuer une nouvelle valeur à pv
	def _set_pv(self,point_de_vie):
		self._pv = point_de_vie

	#Rendre pv  que par get et set
	#_pv = property(_get_pv,_set_pv)

	#Récuperer la force
	#def _get_force(self):
	#	return self._force

	#Attribuer une nouvelle valeur à force
	#def _set_force(self,new_force):
	#	self._force = new_force

	#Rendre force accessible que par get et set
	#_force = property(_get_force,_set_force)

	#Récupérer la defense
	#def _get_defense(self):
	#	return self._defense

	#Attribuer une nouvelle valeur à defense
	#def _set_defense(self,new_defense):
	#	self._defense = new_defense

	#Rendre defense accesssible que par get et set
	#_defense = property(_get_defense,_set_defense) 
	def get_nom(self):
		return self._nom

	def Presentation(self):
		print("Nom :",self._nom)
		print("PV : ",self._pv)
		print("Force : ",self._force)
		print("Defense : ",self._defense)

class epee():
	"""docstring for Epee_longue"""
	def __init__(self):
		self._nom_arme="Epee longue"
		self._degat=random.randint(1,6)

	def _get_nom_arme(self):
		return self._nom_arme
	#_nom_arme = property(_nom_arme)

	def _get_degats(self):
		return self._degat
	#_degat = property(_degat)


class Hero(Personnage):
	"""docstring for ClassName"""
	def __init__(self,nom, pv, force, defense):
		#super(Personnage,self).__init__(nom,pv,force,defense)
		Personnage.__init__(self,nom,pv,force,defense)
		self._arme=epee()

	def _get_degats_arme(self):
		return self._arme._get_degats_arme()

	def Presentation(self):
		Personnage.Presentation(self)
		print("Arme équipée : ",self._arme._nom_arme)
		print("Dégat arme : ",self._arme._degat)
		
	def choix(self,bot=1):
		choix=None
		if bot==1:
			choix=random.randint(0,1)
		else:
			print("")
			choix=int(input("1"))
