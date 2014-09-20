import string

class Room(object):

	def __init__(self):
		self.description = None
		self.north_desc = None
		self.south_desc = None
		self.east_desc = None
		self.west_desc = None
		self.use_alt_desc_north = False
		self.use_alt_desc_south = False
		self.use_alt_desc_east = False
		self.use_alt_desc_west = False
		self.alt_north_desc = None
		self.alt_south_desc = None
		self.alt_east_desc = None
		self.alt_west_desc = None
		self.north = None
		self.south = None
		self.east = None
		self.west = None
		self.items = []
		self.dropped_items = []
		self.enemies = []

	def getNorth(self):
		return self.north

	def getSouth(self):
		return self.south

	def getWest(self):
		return self.west

	def getEast(self):
		return self.east
	
	def setAltDesc(self, dir, desc):
		low_dir = string.lower(dir)
		if low_dir == 'north':
			self.alt_north_desc = desc
		elif low_dir == 'south':
			self.alt_south_desc = desc
		elif low_dir == 'east':
			self.alt_east_desc = desc
		elif low_dir == 'west':
			self.alt_west_desc = desc

	def setAltDescBool(self, dir, bool):
		low_dir = string.lower(dir)
		if low_dir == 'north':
			self.use_alt_desc_north = bool
		elif low_dir == 'south':
			self.use_alt_desc_south = bool
		elif low_dir == 'east':
			self.use_alt_desc_east = bool
		elif low_dir == 'west':
			self.use_alt_desc_west = bool

	def isAltDescActive(self, dir):
		low_dir = string.lower(dir)
		if low_dir == 'north':
			return self.use_alt_desc_north
		elif low_dir == 'south':
			return self.use_alt_desc_south
		elif low_dir == 'east':
			return self.use_alt_desc_east
		elif low_dir == 'west':
			return self.use_alt_desc_west

	def getAltDesc(self, dir):
		low_dir = string.lower(dir)
		if low_dir == 'north':
			return self.alt_north_desc
		elif low_dir == 'south':
			return self.alt_south_desc
		elif low_dir == 'east':
			return self.alt_east_desc
		elif low_dir == 'west':
			return self.alt_west_desc
		

	def getDirectionByName(self, str):
		if str == 'north':
			return self.north
		elif str == 'south':
			return self.south
		elif str == 'west':
			return self.west
		elif str == 'east':
			return self.east

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

	def getDroppedItems(self):
		return self.dropped_items

	def addToDroppedItems(self, item):
		self.dropped_items.append(item)

	def setEnemies(self, e):
		self.enemies = e

	def getEnemies(self):
		return self.enemies

	def setEnemies(self, e):
		self.enemies = e


