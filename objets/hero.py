from personnage import *
from armes.epee import *

class Hero(Personnage):
	"""docstring for ClassName"""
	def __init__(self,nom, pv, force, defense):
		super(Monstre, self).__init__(nom,pv,force,defense)
		self._arme=Epee()

		
	
