import string

class InteractiveObject(object):

	def __init__(self):
		self.name = ''
		self.items = []
		self.droppable_items = []
		self.map_side_to_change = None
		self.unlock_items = []
		self.unlock_text = ''
		self.keywords = []
		self.examine_text = ''
		self.equippable = None
		self.strength = 0
		self.intellect = 0
		self.alt_text_dir = None


	def setItems(self, items):
		self.items = items

	def getItems(self):
		return self.items

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setAltDescDirection(self, dir):
		self.alt_text_dir = dir

	def getAltDescDirection(self):
		return self.alt_text_dir

	def setDirectionToChange(self, dir):
		if dir is not None:
			self.map_side_to_change = dir

	def getDirectionToChange(self):
		return self.map_side_to_change

	def setKeywords(self, kws ):
		self.keywords = kws

	def getKeywords(self):
		return self.keywords

	def getUnlockItems(self):
		return self.unlock_items

	def setUnlockItems(self, items):
		for i in items:
			self.unlock_items.append(string.lower(i))

	def getUnlockText(self):
		return self.unlock_text

	def setUnlockText(self, text):
		self.unlock_text = text

	def setExamineText(self, text):
		self.examine_text = text

	def getExamineText(self):
		return self.examine_text

	def getEquippable(self):
		return self.equippable

	def setEquippable(self, bool):
		self.equippable = bool

	def getStrength(self):
		return self.strength

	def setStrength(self, num):
		self.strength = num

	def getIntellect(self):
		return self.intellect

	def setIntellect(self, num):
		self.intellect = num

	def getDroppableItems(self):
		return self.droppable_items

	def setDroppableItems(self, items):
		self.droppable_items = items

