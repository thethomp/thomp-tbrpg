
from colorama import Fore, Back, Style
import colorama


class Parser(object):

	def __init__(self):
		colorama.init()

	def parse( self, cmd ):
		# parse command
		# return a colored string to print
		return Fore.RED + cmd + Fore.RESET
