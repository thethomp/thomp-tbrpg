import string
from InteractiveObject import *

class Player(object):
	
	def __init__(self):
		self.inventory = []
		self.equipped = []
		self.strength = 0
		self.intellect = 0
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

	def getEquipped(self):
		return self.equipped

	def equipItem(self, i):
		self.equipped.append(i)
		self.inventory.remove(i)
		self.strength += i.getStrength()
		self.intellect += i.getIntellect()

	def unequipItem(self, i):
		self.inventory.append(i)
		self.equipped.remove(i)
		self.strength -= i.getStrength()
		self.intellect -= i.getIntellect()

	def getStrength(self):
		return self.strength

	def getIntellect(self):
		return self.intellect

	
