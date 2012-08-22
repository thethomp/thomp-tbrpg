import cmd, pickle
from Parser import *
from colorama import *
from Player import *


class CmdLine(cmd.Cmd):

	prompt = Fore.RED + 'TBRPG>> ' + Fore.RESET
	parser = Parser()
	player = None

######################
# Action methods
######################

	def do_stats(self, s):
		print 'HP: ' + str(self.player.getHP())
		print 'MP: ' + str(self.player.getMP())	

	def do_savegame(self, s):
		if s == '':
			print 'Enter a filename to save with'
		elif self.player == None:
			print 'No active player to save'
		else:
			pickle.dump( self.player, open(str(s) + '.p', 'wb') )	

	def do_loadgame(self, file):
		if file == '':
			print 'Enter a filename to load'
		else:
			if not file.endswith('.p'):
				file = file + '.p'
			print 'Loading game ' + file + ' ...'
			self.player = pickle.load( open( file, 'rb') )
			

	def do_newgame(self, s):
		print 'Starting new game...'
		self.player = Player()

	def do_exit(self, s):
		return True

	def do_attack(self, s):
		print self.parser.parse(s)

########################
# Help methods
########################

	def help_exit(self):
		print 'Exit Game'

	def help_introduction(self):
		print 'introduction'
		print 'a good place for a tutorial'

