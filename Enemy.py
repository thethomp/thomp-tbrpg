

class Enemy(object):
	
	def __init__(self):
		self.name = ''
		self.hp = 100
		self.mp = 100
		self.abilities = []
		self.pos = (0,0)

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

	def addAbility(self, a):
		self.abilities.append(a)

	def getAbilities(self):
		return self.abilities

	def setPos(self, pos):
		self.pos = pos

	def getPos(self):
		return self.pos
