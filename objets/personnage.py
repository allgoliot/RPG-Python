#classe personnage : pv, force, defense
## pv = 100
## force = 10
## defense = 5
### méthode attaque : force 
### méthode defense : defense*2 puis force+5 au prochain tour


class Personnage:
	def __init__(self,pv,force,defense):
		self._pv = pv
		self._force = force
		self._defense = defense

	def Attaque(self):
		return self._force

Henry = Personnages(100,10,5)
print(Henry.Attaque())
