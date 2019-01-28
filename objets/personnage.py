#classe personnage : pv, force, defense
## pv = 100
## force = 10
## defense = 5
### méthode attaque : force 
### méthode defense : defense*2 puis force+5 au prochain tour


class Personnage:
	def __init__(self,nom,pv,force,defense):
		self._nom = nom
		self._pv = pv
		self._force = force
		self._defense = defense

	def Attaque(self):
		return self._force

#Récuperer les pv
	def _get_pv(self):
		return self._pv

#Attribuer une nouvelle valeur à pv
	def _set_pv(self,point_de_vie):
		self._pv = point_de_vie

#Rendre pv  que par get et set
	pv = property(_get_pv,_set_pv)

#Récuperer la force
	def _get_force(self):
		return self._force

#Attribuer une nouvelle valeur à force
	def _set_force(self,new_force):
		self._force = new_force

#Rendre force accessible que par get et set
	force = property(_get_force,_set_force)

#Récupérer la defense
	def _get_defense(self):
		return self._defense

#Attribuer une nouvelle valeur à defense
	def _set_defense(self,new_defense):
		self._defense = new_defense

#Rendre defense accesssible que par get et set
	defense = property(_get_defense,_set_defense) 




