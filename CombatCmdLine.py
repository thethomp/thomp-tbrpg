from colorama import *
import cmd

class CombatCmdLine(cmd.Cmd):
	
	def __init__(self, enemy):
		cmd.Cmd.__init__(self)
		self.enemy = enemy
		self.prompt = Fore.RED + 'TBRPG(Combat)>> '  + Fore.RESET

	def do_action(self,s):
		print 'Enemy name: ' + self.enemy.getName()
		print 'HP remaining: ' + str(self.enemy.getHP())

	def do_exit(self, s):
		return True

