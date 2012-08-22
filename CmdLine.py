import cmd, pickle, os
from colorama import *
from Parser import *
from Player import *
from Map import *
from Room import *


"""
General notes ---
save format - [player,map]

"""

#######################
# Utility methods
#######################

def red( txt ):
	return Fore.RED + txt + Fore.RESET

def red_bg( txt ):
	return Back.RED + txt + Back.RESET

def green( txt ):
	return Fore.GREEN + txt + Fore.RESET

def green_bg( txt ):
	return Back.GREEN + txt + Back.RESET

def magenta( txt ):
	return Fore.MAGENTA + txt + Fore.RESET	

def magenta_bg( txt ):
	return Back.MAGENTA + txt + Back.RESET	

def yellow( txt ):
	return Fore.YELLOW + txt + Fore.RESET

def yellow_bg( txt ):
	return Back.YELLOW + txt + Back.RESET

def cyan( txt ):
	return Fore.CYAN + txt + Fore.RESET

def cyan_bg( txt ):
	return Back.CYAN + txt + Back.RESET

def white_bg( txt ):
	return Back.WHITE + txt + Back.RESET

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

	"""
	Command Line system methods
	"""
	#def preloop(self):
	#	print 'Hello'
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
			if os.path.exists(filename):
				self.onecmd('load ' + filename)
			else:
				print filename + " can't be found"

	######################
	# Action methods
	######################

	def do_look(self, s):
		cur_room = self.map.getRooms()[self.player.getPos()]
		if s == '':
			print magenta(cur_room.description)
		elif s.lower() == 'north':
			print magenta(cur_room.north_desc)
		elif s.lower() == 'south':
			print magenta(cur_room.south_desc)
		elif s.lower() == 'east':
			print magenta(cur_room.east_desc)
		elif s.lower() == 'west':
			print magenta(cur_room.west_desc)
		else:
			return

	def do_move(self, s):
		cur_room = self.map.getRooms()[self.player.getPos()]
		player_x = self.player.getPos()[0]
		player_y = self.player.getPos()[1]

		if s == '':
			print red('You have to specify what direction to move!')
		elif s.lower() == 'north':
			if cur_room.north:
				self.player.setPos( (player_x, player_y - 1) )
			else:
				print red("You can't move in that direction")
		elif s.lower() == 'south':
			if cur_room.south:
				self.player.setPos( (player_x, player_y + 1) )
			else:
				print red("You can't move in that direction")
		elif s.lower() == 'east':
			if cur_room.east:
				self.player.setPos( (player_x + 1, player_y) )
			else:
				print red("You can't move in that direction")
		elif s.lower() == 'west':
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
		if s == '':
			print 'Enter a filename to save with'
		elif self.player == None:
			print 'No active player to save'
		else:
			to_save = [self.player, self.map]	
			pickle.dump( to_save, open(str(s) + '.p', 'wb') )
			print 'Game saved to ' + str(s) + '.p'

	def do_load(self, file):
		if file == '':
			print 'Enter a filename to load'
		else:
			if not file.endswith('.p'):
				file = file + '.p'
			print 'Loading game ' + file + ' ...'
			to_load = pickle.load( open( file, 'rb') )
			self.player = to_load[0]
			self.map = to_load[1]
			

	def do_new(self, s):
		print 'Starting new game...'
		self.map = Map()
		self.player = Player()
		self.player.setPos((5,5))

	def do_exit(self, s):
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

