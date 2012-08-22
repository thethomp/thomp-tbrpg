
class Player(object):
	
	def __init__(self):
		self.hp = 10
		self.mp = 10
		self.pos = (0,0)

	def getHP(self):
		return self.hp

	def getMP(self):
		return self.mp

	def getPos(self):
		return self.pos

	def setPos( self, pos ):
		self.pos = pos

	
