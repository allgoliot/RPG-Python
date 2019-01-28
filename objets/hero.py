from personnage import *
from armes.epee import *

class Hero(Personnage):
	"""docstring for ClassName"""
	def __init__(self,nom, pv, force, defense):
		#super(Personnage,self).__init__(nom,pv,force,defense)
		Personnage.__init__(self,nom,pv,force,defense)
		self._arme=Epee()

	def _get_degats_arme(self):
		return self._arme._get_degats_arme()

	def Presentation(self):
		Personnage.Presentation(self)
		print("Degat arme",self._arme._degat)
		
	def choix(self,bot=1):
		choix=None
		if bot==1:
			choix=random.randint(0,1)
		else:
			print("")
			choix=int(input("1"))

hero=Hero("toto",100,10,5)
hero.Presentation()