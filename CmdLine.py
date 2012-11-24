import cmd, pickle, os, readline, string, random, time
from CombatCmdLine import *
from colorama import *
from Parser import *
from Player import *
from Map import *
from Room import *
from Enemy import *
from TextUtilities import red, red_bg, green, green_bg, magenta, magenta_bg, yellow, yellow_bg, cyan, cyan_bg, white_bg, bright

"""
General notes ---
save format - [player,map]

"""

##########################
# Command line class
# Holds all logic for all commands
##########################


#############################
# GLOBAL VARS
###########################
GLOBAL_TIME = 0
TIME_TO_DIE = 25
OUTSIDE_PLANE = False
#TURBULENCE = False
#TURBULENCE_START_TIME = 0
#TURBULENCE_STOP_TIME = 0

class CmdLine(cmd.Cmd):

	map = None
	#prompt = Fore.RED + 'TBRPG>> ' + Fore.RESET
	prompt = 'TBRPG>> '
	parser = Parser()
	player = None
	inCombat = False
	
#	combatCmd = CombatCmdLine()

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

	def do_equip( self, s ):
		item = self.player.getInventoryItemByName(s)
		if item == None:
			print "You can't equip an item you don't have!"
		else:
			if not item.getEquippable():
				print "You can't equip that item!"
			else:
				print yellow(s) + ' equipped!'
				self.player.equipItem(item)

	def do_unequip( self, s ):
		item = self.player.getEquippedItemByName(s)
		if item == None:
			print "You don't have anything by that name equipped"
		else:
			self.player.unequipItem(item)
			print yellow(s) + " unequipped and put into your " + magenta('Inventory') + '.'

	def do_attack( self, s ):
		enemy = Enemy()
		i = CombatCmdLine(enemy)
		i.cmdloop()

	def do_drop( self , s ):
		cur_room = self.map.getRooms()[self.player.getPos()]
		itemtodrop = self.player.getInventoryItemByName(s.strip())
		if itemtodrop == None:
			print self.parser.parseDescription("You don't have a <i>" + s + " to drop.")
		else:
			cur_room.addToDroppedItems(itemtodrop)
			self.player.getInventory().remove(itemtodrop)
			print self.parser.parseDescription("You dropped <i>" + s + '.')	

	def do_open( self, s ):
		cur_room = self.map.getRooms()[self.player.getPos()]
		open_item = s.strip()
		roomitem = cur_room.getItemByName(open_item)
		if roomitem == None:
			print yellow(open_item) + ' could not be found!'
			return
		else:
			if 'open' in roomitem.getKeywords():
				cur_room.modifyDirectionalBoundary(roomitem.getDirectionToChange())
				print 'You opened ' + yellow(open_item) + '.'
				if roomitem.getUnlockText() != '':
					print self.parser.parseDescription(roomitem.getUnlockText())
				#if cur_room.getDirectionByName(roomitem.getDirectionToChange()):
				#	print 'The ' + cyan(roomitem.getDirectionToChange()) + cyan('ern') + ' passage has opened!'
				#else:
				#	print 'The ' + cyan(roomitem.getDirectionToChange()) + cyan('ern') + ' passage has closed!'
			else:
				print "You can't open " + yellow(open_item) + '!'
			

	def do_use( self, s ):
		#global GLOBAL_TIME
		#global TURBULENCE_START_TIME
		#global TURBULENCE_STOP_TIME
		
		if 'on' not in s:
			print self.parser.parseDescription("USE syntax: use <i><item1> on <i><item2>")
			return
		string1 = s.split('on')[0].strip()
		string2 = s.split('on')[1].strip()
		#if len(s.split()) < 3:
		#	print self.parser.parseDescription("USE syntax: use <i><item1> on <i><item2>")
		#	return
		cur_room = self.map.getRooms()[self.player.getPos()]
		room_items = cur_room.getItems()
		#string1 = s.split()[0]
		#string2 = s.split()[2]
		playeritem = self.player.getInventoryItemByName(string1)
		roomitem = cur_room.getItemByName(string2)
		## For the case where the player doens't actually have the first item
		## e.g. use latch on door
		if playeritem is None:
			playeritem = cur_room.getItemByName(string1)
		if playeritem is None:
			print "There's no " + yellow(string1) + " that could be found to use."
		elif roomitem is None:
			print "There's no " + yellow(string2) + " that could be found to use."
		elif string.lower(playeritem.getName()) in roomitem.getUnlockItems():
			cur_room.modifyDirectionalBoundary(roomitem.getDirectionToChange())
			print 'You used ' + yellow(string1) + ' on ' + yellow(string2) + '.'
			### Check for lockbox opening and start the countdown to Turbulence
		#	if string.lower(string2) == 'lockbox':
		#		TURBULENCE_START_TIME = GLOBAL_TIME + 2
		#		TURBULENCE_STOP_TIME = GLOBAL_TIME + 7
			if roomitem.getUnlockText() != '':
				print self.parser.parseDescription(roomitem.getUnlockText())
			else:
				if cur_room.getDirectionByName(roomitem.getDirectionToChange()):
					print 'The ' + cyan(roomitem.getDirectionToChange()) + cyan('ern') + ' passage has opened!'
				else:
					print 'The ' + cyan(roomitem.getDirectionToChange()) + cyan('ern') + ' passage has closed!'
			## Check for droppable items - if present, drop them
			if len(roomitem.getDroppableItems()) > 0:
				for item in roomitem.getDroppableItems():
					cur_room.addToDroppedItems(item)
					#roomitem.getDroppableItems().remove(item)
					print yellow(roomitem.getName()) + ' dropped ' + yellow(item.getName()) + '!'
				## Clear out droppable items so they can't drop again
				del roomitem.getDroppableItems()[:]
			## Check both items that were used to see if any alternate descriptions should be used
			if playeritem.getAltDescDirection() is not None:
				cur_room.setAltDescBool(playeritem.getAltDescDirection(), True)	
			if roomitem.getAltDescDirection() is not None:
				cur_room.setAltDescBool(roomitem.getAltDescDirection(), True)
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
					## Check both items that were used to see if any alternate descriptions should be used
					if item.getAltDescDirection() is not None:
						cur_room.setAltDescBool(item.getAltDescDirection(), True)	
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
		print magenta('=== EQUIPPED  ===')
		for item in  self.player.getEquipped():
			print yellow(item.getName())
		print magenta('=================')

	def do_look(self, s):
		cur_room = self.map.getRooms()[self.player.getPos()]
		dir = s.lower()
		if s == '':
			print self.parser.parseDescription(cur_room.description)
		elif dir == 'north' or dir == 'n' or dir == 'forward' or dir == 'f':
			if cur_room.isAltDescActive('north'):
				print self.parser.parseDescription(cur_room.getAltDesc('north'))
			else:
				print self.parser.parseDescription(cur_room.north_desc)
			#print magenta(cur_room.north_desc)
		elif dir == 'south' or dir == 's' or dir == 'back' or dir == 'b':
			if cur_room.isAltDescActive('south'):
				print self.parser.parseDescription(cur_room.getAltDesc('south'))
			else:
				print self.parser.parseDescription(cur_room.south_desc)
		elif dir == 'east' or dir == 'e' or dir == 'right' or dir == 'r':
			if cur_room.isAltDescActive('east'):
				print self.parser.parseDescription(cur_room.getAltDesc('east'))
			else:
				print self.parser.parseDescription(cur_room.east_desc)
			#print magenta(cur_room.east_desc)
		elif dir == 'west' or dir == 'w' or dir == 'left' or dir == 'l':
			if cur_room.isAltDescActive('west'):
				print self.parser.parseDescription(cur_room.getAltDesc('west'))
			else:
				print self.parser.parseDescription(cur_room.west_desc)
		else:
			return
		if len(cur_room.getDroppedItems()) > 0:
			print "=== Dropped Items ==="
			for i in cur_room.getDroppedItems():
				print yellow(i.getName())

	def do_move(self, s):
		global GLOBAL_TIME
		global OUTSIDE_PLANE
		global TIME_TO_DIE
		print 'OUTSIDE_PLANE: ' + str(OUTSIDE_PLANE)
		print 'GLOBAL_TIME: ' + str(GLOBAL_TIME)
		#global TURBULENCE
		#global TURBULENCE_START_TIME
		#global TURBULENCE_STOP_TIME
		if GLOBAL_TIME == TIME_TO_DIE:
			self.print_death()
			return True
		if OUTSIDE_PLANE:
			print "You're still flying!!! Or are you falling..."
			GLOBAL_TIME += 1
			return			
		
	#	player_x = self.player.getPos()[0]
	#	player_y = self.player.getPos()[1]
	#	print 'player_x: ' + str(player_x)
	#	print 'player_y: ' + str(player_y)
	
		#if (player_x == 6 and player_y == 3) or (player_x == 6 and player_y == 7):

		cur_room = self.map.getRooms()[self.player.getPos()]
		player_x = self.player.getPos()[0]
		player_y = self.player.getPos()[1]
		#print 'GLOBAL_TIME = ' + str(GLOBAL_TIME)
		#print 'TURBULENCE_START_TIME = ' + str(TURBULENCE_START_TIME)
		#print 'TURBULENCE_STOP_TIME = ' + str(TURBULENCE_STOP_TIME)
		#print 'TURBULENCE = ' + str(TURBULENCE)



		TURBULENCE = random.randint(1,10)
		if TURBULENCE < 2:
			self.print_turb()
			print 'Turbulence shakes you, forcing you to move in a random direction.'
			dirs = ['n', 's', 'e', 'w']
			s = dirs[random.randint(0,3)]

			

		if s == '':
			print red('You have to specify what direction to move!')
		elif s.lower() == 'north' or s.lower() == 'n' or s.lower() == 'forward' or s.lower() == 'f':
			if cur_room.north:
				self.player.setPos( (player_x, player_y - 1) )
				self.do_look('')
				GLOBAL_TIME += 1
				#if GLOBAL_TIME == TURBULENCE_START_TIME:
				#	TURBULENCE = True
				#if GLOBAL_TIME == TURBULENCE_STOP_TIME:
				#	TURBULENCE = False
			else:
				print red("You can't move in that direction.")
		elif s.lower() == 'south' or s.lower() == 's' or s.lower() == 'back' or s.lower() == 'b':
			if cur_room.south:
				self.player.setPos( (player_x, player_y + 1) )
				self.do_look('')
				GLOBAL_TIME += 1
				#if GLOBAL_TIME == TURBULENCE_START_TIME:
				#	TURBULENCE = True
				#if GLOBAL_TIME == TURBULENCE_STOP_TIME:
				#	TURBULENCE = False
			else:
				print red("You can't move in that direction.")
		elif s.lower() == 'east' or s.lower() == 'e' or s.lower() == 'right' or s.lower() == 'r':
			if player_x + 1 == 7 and player_y == 6:
				print "You're flying!!!!"
				OUTSIDE_PLANE = True
				GLOBAL_TIME += 1
				TIME_TO_DIE = GLOBAL_TIME + 3
				return
			if cur_room.east:
				self.player.setPos( (player_x + 1, player_y) )
				self.do_look('')
				GLOBAL_TIME += 1
				#if GLOBAL_TIME == TURBULENCE_START_TIME:
				#	TURBULENCE = True
				#if GLOBAL_TIME == TURBULENCE_STOP_TIME:
				#	TURBULENCE = False
			else:
				print red("You can't move in that direction.")
		elif s.lower() == 'west' or s.lower() == 'w' or s.lower() == 'left' or s.lower() == 'l':
			if player_x - 1 == 3 and player_y == 6:
				print "You're flying!!!!"
				OUTSIDE_PLANE = True
				GLOBAL_TIME += 1
				TIME_TO_DIE = GLOBAL_TIME + 3
				return
			if cur_room.west:
				self.player.setPos( (player_x - 1, player_y) )
				self.do_look('')
				GLOBAL_TIME += 1
				#if GLOBAL_TIME == TURBULENCE_START_TIME:
				#	TURBULENCE = True
				#if GLOBAL_TIME == TURBULENCE_STOP_TIME:
				#	TURBULENCE = False
			else:
				print red("You can't move in that direction.")
		else:
			return
	
	def do_stats(self, s):
		print 'HP: ' + str(self.player.getHP())
		print 'MP: ' + str(self.player.getMP())	
		print 'Strength: ' + str(self.player.getStrength())	
		print 'Intellect: ' + str(self.player.getIntellect())	

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
		self.player.setPos((6,10))
		self.do_look('')

	def do_exit(self, s):
		return True

    ###################
	# Alternative commands
	###################

	def do_ueq(self, s):
		return self.do_unequip(s)

	def do_eq(self, s):
		return self.do_equip(s)

	def do_e(self, s):
		return self.do_examine(s)

	def do_m(self, s):
		return self.do_move(s)

	def do_l(self, s):
		return self.do_look(s)

	def do_inv(self, s):
		return self.do_inventory(s)

	def do_quit(self,s):
		return self.do_exit(s)	

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
		print red('WARNING - You will lose any unsaved changes.')

	def help_load(self):
		print 'Load a saved game file.'
		print 'USAGE: load example_saved_game'

	def help_save(self):
		print 'Save game.'
		print red('WARNING - If you give the name of a file that already exists, this file will be overwritten.')

	def help_exit(self):
		print 'Exit Game'
		print red('WARNING - Any unsaved changes will be lost.')
	
	def help_quit(self):
		print 'Exit Game'
		print red('WARNING - Any unsaved changes will be lost.')

	######################
	# Debugging commands
	#######################

	def do_enemies(self, s):
		cur_room = self.map.getRooms()[self.player.getPos()]
		global_enemy_defs = self.map.getEnemies()
		enemies = cur_room.getEnemies()
		for id in enemies:
			print global_enemy_defs[id].getName()


	#########################
	# Helper methods
	#########################

	def print_death(self):
		print ' ______   ______   ________   _________  ___   ___'       
		print '/_____/\ /_____/\ /_______/\ /________/\/__/\ /__/\  '    
		print '\:::_ \ \\\\::::_\/_\::: _  \ \\\\__.::.__\/\::\ \\\\  \ \ '     
		print ' \:\ \ \ \\\\:\/___/\\\\::(_)  \ \  \::\ \   \::\/_\ .\ \ '   
		print '  \:\ \ \ \\\\::___\/_\:: __  \ \  \::\ \   \:: ___::\ \ '  
		print '   \:\/.:| |\:\____/\\\\:.\ \  \ \  \::\ \   \: \ \\\\::\ \ ' 
		print '    \____/_/ \_____\/ \__\/\__\/   \__\/    \__\/ \::\/ '

	def print_turb(self):
		turb_lines = []
		turb_lines.append('                                                                                          _..._                        ')
		turb_lines.append('                                               .---.                                   .-\'_..._\'\'.                     ')
		turb_lines.append('                            /|                 |   |      __.....__        _..._     .\' .\'      \'.\     __.....__      ')
		turb_lines.append('                            ||                 |   |  .-\'\'         \'.    .\'     \'.  / .\'            .-\'\'         \'.    ')
		turb_lines.append('     .|             .-,.--. ||                 |   | /     .-\'\'"\'-.  `. .   .-.   .. \'             /     .-\'\'"\'-.  `.  ')
		turb_lines.append('   .\' |_            |  .-. |||  __             |   |/     /________\   \|  \'   \'  || |            /     /________\   \ ')
		turb_lines.append(' .\'     |   _    _  | |  | |||/\'__ \'.   _    _ |   ||                  ||  |   |  || |            |                  | ')
		turb_lines.append('\'--.  .-\'  | \'  / | | |  | ||:/`  \'. \' | \'  / ||   |\    .-------------\'|  |   |  |. \'            \    .-------------\' ')
		turb_lines.append('   |  |   .\' | .\' | | |  \'- ||     | |.\' | .\' ||   | \    \'-.____...---.|  |   |  | \ \'.          .\    \'-.____...---. ')
		turb_lines.append('   |  |   /  | /  | | |     ||\    / \'/  | /  ||   |  `.             .\' |  |   |  |  \'. `._____.-\'/ `.             .\'  ')
		turb_lines.append('   |  \'.\'|   `\'.  | | |     |/\'..\' /|   `\'.  |\'---\'    `\'\'-...... -\'   |  |   |  |    `-.______ /    `\'\'-...... -\'    ')
		turb_lines.append('   |   / \'   .\'|  \'/|_|     \'  `\'-\'` \'   .\'|  \'/                        |  |   |  |             `                      ')
		turb_lines.append('   `\'-\'   `-\'  `--\'                   `-\'  `--\'                         \'--\'   \'--\'                                    ')
		for line in turb_lines:
			print line
			time.sleep(0.1)
