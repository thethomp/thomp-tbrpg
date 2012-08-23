import yaml
from Room import *

class Map(object):
	
	def __init__(self):
		yaml_path = 'config/map.yaml'
		self.rooms = {}
		room_data = yaml.load_all( open(yaml_path, 'r') )
		for d in room_data:
			newroom = Room()
			newroom.setDescription(d['description'])
			directional_descs = [d['look_north'], d['look_south'], d['look_east'], d['look_west']]
			newroom.setDirectionalDescriptions(directional_descs)
			moves = [d['north'], d['south'], d['east'], d['west']]
			newroom.setDirectionalMoves(moves)
			self.rooms[(d['x'],d['y'])] = newroom

	def getRooms(self):
		return self.rooms
