from colorama import *
import cmd, time
from TextUtilities import red, red_bg, green, green_bg, magenta, magenta_bg, yellow, yellow_bg, cyan, cyan_bg, white_bg, bright, format_string

class CombatCmdLine(cmd.Cmd):
	
	def __init__(self, player, enemy):
		cmd.Cmd.__init__(self)
		self.player = player
		self.enemy = enemy
		self.prompt = red_bg('(Combat)>>') + ' '

	def do_action(self,s):
		print 'Enemy name: ' + self.enemy.getName()
		print 'HP remaining: ' + str(self.enemy.getHP())
		ability = self.player.getAbilityByName(s)
		if ability is None:
			print "You don't have an ability called " + s
		else:
			print "You used the " + ability.getName() + " ability!"
			print "You dealt " + magenta(str(ability.getDamage())) + " to " + red(self.enemy.getName())
			self.enemy.setHP(self.enemy.getHP() - ability.getDamage())
		if self.enemy.getHP() > 0:
			enemy_ability = self.enemy.getAbilities()[0]
			self.print_enemy_status(self.enemy)
			print red("--------- Enemy's Turn --------------")
			time.sleep(1.0)
			print self.enemy.getName() + " used " + self.enemy.getAbilities()[0].getName() + "!"
			time.sleep(1.0)
			self.player.setHP(self.player.getHP() - enemy_ability.getDamage())
			print self.enemy.getName() + " dealt " + magenta(str(enemy_ability.getDamage())) + " to you!"
			time.sleep(1.0)
			self.print_player_status()
			print red("--------- End Enemy's Turn --------------")
		else:
			time.sleep(1.0)
			print red("You defeated " + red(self.enemy.getName()))
			self.enemy.setHP(0)
			return True


	def do_exit(self, s):
		return True

	def do_abilities(self, s):
		INDENT = '   '
		for a in self.player.getAbilities():
			print magenta(a.getName())
			print INDENT + cyan(a.getDescription())
			print INDENT + cyan('Damage: ' + str(a.getDamage()))

	## Utility Methods
	def print_enemy_status(self, enemy):
		print cyan(enemy.getName())
		print '  HP: ' + str(enemy.getHP())
		print '  MP: ' + str(enemy.getMP())

	def print_player_status(self):
		print cyan('Player')
		print '  HP: ' + str(self.player.getHP())
		print '  MP: ' + str(self.player.getMP())


		
