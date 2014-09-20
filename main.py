#!/usr/bin/env python

from CmdLine import *

def main():
	interpretor = CmdLine()
	l = interpretor.precmd('launch')
	r = interpretor.onecmd(l)
	r = interpretor.postcmd(r,l)
	if not r:
		interpretor.cmdloop()

if __name__ == '__main__':
	main()
