

class Enemy(object):
	
	def __init__(self):
		self.name = 'Tyranosaur'
		self.hp = 100
		self.mp = 100
		self.abilities = []

	def setName(self, n):
		self.name = n

	def setHP(self, h):
		self.hp = h

	def setMP(self, m):
		self.mp = m

	def getName(self):
		return self.name

	def getHP(self):
		return self.hp

	def getMP(self):
		return self.mp
