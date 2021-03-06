import string, yaml
from InteractiveObject import *
from Ability import *

class Player(object):
	
	def __init__(self):
		self.abilities = []
		self.inventory = []
		self.equipped = []
		self.strength = 0
		self.intellect = 0
		self.hp = 100
		self.mp = 100
		self.pos = (0,0)
		self.xp = 0
		self.next_level_xp = 100
		self.level = 1

		### Load player abilities
		### Load ability data   
		ability_yaml_path = 'config/player_abilities.yaml'
		ability_data = yaml.load_all( open(ability_yaml_path, 'r') )
		for a in ability_data:
			new_a = Ability()
			new_a.setName(a['name'])
			new_a.setDescription(a['description'])
			new_a.setLevelReq(a['level_req'])
			new_a.setDamage(a['damage'])
			new_a.setForPlayer(a['for_player'])
			self.abilities.append(new_a)

	def setLevel(self, level):
		self.level = level

	def getLevel(self):
		return self.level

	def setNextLevelXP(self, xp):
		self.next_level_up = xp

	def getNextLevelXP(self):
		return self.next_level_xp

	def getXP(self):
		return self.xp

	def setXP(self, xp):
		self.xp = xp

	def getHP(self):
		return self.hp

	def getMP(self):
		return self.mp

	def setHP(self, hp):
		self.hp = hp

	def setMP(self, mp):
		self.mp = mp

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

	def getEquippedItemByName(self, name):
		for i in self.equipped:
			if string.lower(i.getName()) == string.lower(name):
				return i
		return None


	def getEquipped(self):
		return self.equipped

	def getEquippedItemByName(self, name):
		for item in self.equipped:
			if string.lower(name) == string.lower(item.getName()):
				return item
		return None 
		#return [string.lower(x.getName()) for x in self.equipped]

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

	def getAbilities(self):
		return self.abilities

	def getAbilityByName(self,name):
		for abil in self.abilities:
			if string.lower(abil.getName()) == string.lower(name):
				return abil
		return None
	
