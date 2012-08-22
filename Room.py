

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
