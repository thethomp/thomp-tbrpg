#!/usr/bin/python

import os, sys, string


def main( coord_list ):
	for coord in coord_list:
		x = coord.split(',')[0].strip()
		y = coord.split(',')[1].strip()
		print '---'
		print 'x: ' + x
		print 'y: ' + y
		print 'description: TEMPORARY DESC'
		print 'look_north: FILLER'
		print 'look_south: FILLER'
		print 'look_east: FILLER'
		print 'look_west: FILLER'
		print 'north: True'
		print 'south: True'
		print 'east: True'
		print 'west: True'
		print 'items: []'
		print 'enemies: []'	


if __name__ == '__main__':
	
	filein = sys.argv[1]
	coords = open( filein, 'r' ).readlines()
	main(coords)
