from colorama import *

#######################
# Utility methods
#######################

def bright( txt ):
	return Style.BRIGHT + txt

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
