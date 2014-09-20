
from colorama import Fore, Back, Style
import colorama


class Parser(object):

	def __init__(self):
		colorama.init()

	def parse( self, cmd ):
		# parse command
		# return a colored string to print
		return Fore.RED + cmd + Fore.RESET

	def parseDescription( self, message ):
		final_msg = ''
		for word in message.split(' '):
			if '<i>' in word:
				final_msg = final_msg + ' '+ Fore.YELLOW + word + Fore.RESET
			else:
				final_msg = final_msg + ' ' + word
		return final_msg.replace('<i>', '').lstrip(' ')
