

class Ability(object):

	def __init__(self):
		self.name = ''
		self.description = ''
		self.level_req = 1
		self.for_player = False
		self.damage = 1

	def setDescription(self, s):
		self.description = s

	def getDescription(self):
		return self.description

	def setName(self, s):
		self.name = s

	def getName(self):
		return self.name

	def setLevelReq(self, i):
		self.level_req = i

	def getLevelReq(self):
		return self.level_req

	def setDamage(self, d):
		self.damage = d

	def getDamage(self):
		return self.damage

	def setForPlayer(self, a):
		self.for_player = a

	def getForPlayer(self):
		return self.for_player
