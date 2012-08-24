import string

class InteractiveObject(object):

	def __init__(self):
		self.name = ''
		self.items = []
		self.map_side_to_change = None
		self.unlock_items = []
		self.keywords = []
		self.examine_text = ''

	def setItems(self, items):
		self.items = items

	def getItems(self):
		return self.items

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setDirectionToChange(self, dir):
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

	def setExamineText(self, text):
		self.examine_text = text

	def getExamineText(self):
		return self.examine_text
