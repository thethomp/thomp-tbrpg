import cmd, pickle, os, readline, string
from colorama import *
from Parser import *
from Player import *
from Map import *
from Room import *
from TextUtilities import red, red_bg, green, green_bg, magenta, magenta_bg, yellow, yellow_bg, cyan, cyan_bg, white_bg, bright

"""
General notes ---
save format - [player,map]

"""

##########################
# Command line class
# Holds all logic for all commands
##########################

class CmdLine(cmd.Cmd):

	map = None
	prompt = Fore.RED + 'TBRPG>> ' + Fore.RESET
	parser = Parser()
	player = None
	inCombat = False	

	#####################
	# Command Line system methods
	######################

	def do_launch(self, s):
		print cyan('Welcome ') +  yellow('to') + magenta(" Thomp's") + green(" Text Based") + red(" RPG!")
		print "(1) New Game"
		print "(2) Load Game"
		response = raw_input('What would you like to do? ')
		if response == '1':
			self.onecmd('new')
		elif response == '2':
			filename = raw_input('File to load: ')
			if not filename.endswith('.p'):
				filename = filename + '.p'
				self.onecmd('load ' + filename)
			#else:
			#	print filename + " can't be found"

	######################
	# Action methods
	######################

	def do_drop( self , s ):
		cur_room = self.map.getRooms()[self.player.getPos()]
		itemtodrop = self.player.getInventoryItemByName(s.strip())
		if itemtodrop == None:
			print self.parser.parseDescription("You don't have a <i>" + s + " to drop.")
		else:
			cur_room.addToDroppedItems(itemtodrop)
			self.player.getInventory().remove(itemtodrop)
			print self.parser.parseDescription("You dropped <i>" + s + '.')	

	def do_use( self, s ):
		if len(s.split()) < 3:
			print self.parser.parseDescription("USE syntax: use <i><item1> on <i><item2>")
			return
		cur_room = self.map.getRooms()[self.player.getPos()]
		room_items = cur_room.getItems()
		string1 = s.split()[0]
		string2 = s.split()[2]
		playeritem = self.player.getInventoryItemByName(string1)
		roomitem = cur_room.getItemByName(string2)
		if string.lower(playeritem.getName()) in roomitem.getUnlockItems():
			cur_room.modifyDirectionalBoundary(roomitem.getDirectionToChange())
			print 'You used ' + yellow(string1) + ' on ' + yellow(string2) + '.'
			if cur_room.getDirectionByName(roomitem.getDirectionToChange()):
				print 'The ' + cyan(roomitem.getDirectionToChange()) + cyan('ern') + ' passage has opened!'
			else:
				print 'The ' + cyan(roomitem.getDirectionToChange()) + cyan('ern') + ' passage has closed!'
		else:
			print "You can't use " + yellow(string1) + ' on ' + yellow(string2) + '!'

	def do_take( self, s ):
		cur_room = self.map.getRooms()[self.player.getPos()]
		for item in cur_room.getItems() + cur_room.getDroppedItems():
			if string.lower(item.getName()) == string.lower(s):
				if 'take' in item.getKeywords():
					print yellow(item.getName()) + ' added to your' + magenta(' inventory')
					self.player.addToInventory(item)
					# Either remove the item from the list of room items, or list of dropped room items
					try: cur_room.getItems().remove(item)
					except ValueError: cur_room.getDroppedItems().remove(item)
					return		
				else:
					print red("You can't take that.")
					return		
		print "You don't see anything that looks like a " + yellow(s) + '.' 

	def do_examine( self, s ):
		cur_room = self.map.getRooms()[self.player.getPos()]
		for item in cur_room.getItems() + cur_room.getDroppedItems():
			if string.lower(item.getName()) == string.lower(s):
				print self.parser.parseDescription(item.getExamineText())
				return
		print "You don't see anything that looks like a " + yellow(s) + '.'

	def do_inventory( self, s ):
		inv = self.player.getInventory()
		print magenta('=== INVENTORY ===')
		for item in inv:
			print yellow(item.getName())
		print magenta('=================')

	def do_look(self, s):
		cur_room = self.map.getRooms()[self.player.getPos()]
		if s == '':
			print self.parser.parseDescription(cur_room.description)
		elif s.lower() == 'north':
			print self.parser.parseDescription(cur_room.north_desc)
			#print magenta(cur_room.north_desc)
		elif s.lower() == 'south':
			print self.parser.parseDescription(cur_room.south_desc)
		elif s.lower() == 'east':
			print self.parser.parseDescription(cur_room.east_desc)
			#print magenta(cur_room.east_desc)
		elif s.lower() == 'west':
			print self.parser.parseDescription(cur_room.west_desc)
		else:
			return
		if len(cur_room.getDroppedItems()) > 0:
			print "=== Dropped Items ==="
			for i in cur_room.getDroppedItems():
				print yellow(i.getName())

	def do_move(self, s):
		cur_room = self.map.getRooms()[self.player.getPos()]
		player_x = self.player.getPos()[0]
		player_y = self.player.getPos()[1]

		if s == '':
			print red('You have to specify what direction to move!')
		elif s.lower() == 'north' or s.lower() == 'n':
			if cur_room.north:
				self.player.setPos( (player_x, player_y - 1) )
			else:
				print red("You can't move in that direction")
		elif s.lower() == 'south' or s.lower() == 's':
			if cur_room.south:
				self.player.setPos( (player_x, player_y + 1) )
			else:
				print red("You can't move in that direction")
		elif s.lower() == 'east' or s.lower() == 'e':
			if cur_room.east:
				self.player.setPos( (player_x + 1, player_y) )
			else:
				print red("You can't move in that direction")
		elif s.lower() == 'west' or s.lower() == 'w':
			if cur_room.west:
				self.player.setPost( (player_x - 1, player_y) )
			else:
				print red("You can't move in that direction")
		else:
			return
	
	def do_stats(self, s):
		print 'HP: ' + str(self.player.getHP())
		print 'MP: ' + str(self.player.getMP())	

	def do_save(self, s):
		save_path = 'saved_games/'
		if s == '':
			print 'Enter a filename to save with'
		elif self.player == None:
			print 'No active player to save'
		else:
			to_save = [self.player, self.map]	
			pickle.dump( to_save, open( save_path + str(s) + '.p', 'wb') )
			print 'Game saved to ' + save_path + str(s) + '.p'

	def do_load(self, file):
		load_path = 'saved_games/'
		if file == '':
			print 'Enter a filename to load'
		else:
			if not file.endswith('.p'):
				file = file + '.p'
			print 'Loading game ' + load_path + file + ' ...'
			to_load = pickle.load( open(load_path + file, 'rb') )
			self.player = to_load[0]
			self.map = to_load[1]
			

	def do_new(self, s):
		print 'Starting new game...'
		self.map = Map()
		self.player = Player()
		self.player.setPos((5,5))

	def do_exit(self, s):
		return True

	def do_quit(self,s):
		return True

	def do_attack(self, s):
		print self.parser.parse(s)

	########################
	# Help methods
	########################
	def help_look(self):
		print 'Look around the room.'
		print 'You can also look in different directions to discover new things.'
		print 'e.g. look north, look east, etc...'

	def help_move(self):
		print 'Move around the map'
		print "Try things like 'move north', 'move south', etc..."

	def help_stats(self):
		print 'Show the core stats of your character.'
	
	def help_new(self):
		print 'Start a new game.' 
		print red('WARNING - You will lose any unsaved changes')

	def help_load(self):
		print 'Load a saved game file.'

	def help_save(self):
		print 'Save game.'
		print red('WARNING - If you give the name of a file that already exists, this file will be overwritten.')

	def help_exit(self):
		print 'Exit Game'
		print red('WARNING - Any unsaved changes will be lost.')
	
	def help_quit(self):
		print 'Exit Game'
		print red('WARNING - Any unsaved changes will be lost.')

