import string

class Room(object):

	def __init__(self):
		self.description = None
		self.north_desc = None
		self.south_desc = None
		self.east_desc = None
		self.west_desc = None
		self.north = None
		self.south = None
		self.east = None
		self.west = None
		self.items = []

	def setDescription(self, desc):
		self.description = desc

	def setDirectionalDescriptions( self, descs ):
		self.north_desc = descs[0]
		self.south_desc = descs[1]
		self.east_desc = descs[2]
		self.west_desc = descs[3]

	def setDirectionalMoves( self, moves ):
		self.north = moves[0]
		self.south = moves[1]
		self.east = moves[2]
		self.west = moves[3]

	def setItems( self, items ):
		self.items = items

	def getItemNames(self):
		name_list = []
		for item in self.items:
			name_list.append(string.lower(item.getName()))
		return name_list

	def getItems(self):
		return self.items

	def getItemByName(self, name):
		for item in self.items:
			if string.lower(item.getName()) == string.lower(name):
				return item
		return None 

	def modifyDirectionalBoundary(self, dir):
		if dir == 'north':
			self.north = self.switchBoolean(self.north)
		elif dir == 'south':
			self.south = self.switchBoolean(self.south)
		elif dir == 'east':
			self.east = self.switchBoolean(self.east)
		elif dir == 'west':
			self.west = self.switchBoolean(self.west)

	def switchBoolean(self, bool):
		if bool == True:
			return False
		else:
			return True



