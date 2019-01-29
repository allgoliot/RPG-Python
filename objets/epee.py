import random
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
