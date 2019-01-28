from personnage import *

class Monstre(Personnage):
	"""docstring for ClassName"""
	def __init__(self, pv, force, defense):
		super(Monstre, self).__init__(pv,force,defense)
		
	def affiche(self):
		print("PV :",self._pv)
		print("FORCE :",self._force)
		print("DEFENCE",self._defense)

Herry=Monstre(80,6,6)
Herry.affiche()
