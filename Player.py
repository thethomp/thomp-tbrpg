import string

class Player(object):
	
	def __init__(self):
		self.inventory = []
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

	def addToInventory( self, item ):
		self.inventory.append(item)

	def getInventory(self):
		return self.inventory

	def getInventoryItemByName(self, name):
		for i in self.inventory:
			if string.lower(i.getName()) == string.lower(name):
				return i
		return None
	
