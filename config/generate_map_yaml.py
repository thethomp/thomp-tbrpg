#!/usr/bin/python

import os, sys, string


def main( coord_list ):
	for coord in coord_list:
		x = coord.split(',')[0].strip()
		y = coord.split(',')[1].strip()
		print '---'
		print 'x: ' + x
		print 'y: ' + y
		print 'description:'
		print 'look_north: '
		print 'look_south: '
		print 'look_east:'
		print 'look_west:'
		print 'north:'
		print 'south:'
		print 'east:'
		print 'west:'
		print 'items: []'
		print 'enemies: []'	


if __name__ == '__main__':
	
	filein = sys.argv[1]
	coords = open( filein, 'r' ).readlines()
	main(coords)
