import yaml
from Room import *
from InteractiveObject import *

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
			room_items = []
			for item in d['items']:
				new_obj = InteractiveObject()
				new_obj.setName(item['name'])
				new_obj.setItems(item['item_list'])
				new_obj.setUnlockItems(item['unlock_item'])
				new_obj.setKeywords(item['keyword'])
				new_obj.setDirectionToChange(item['map_side_to_change'])
				new_obj.setExamineText(item['examine_text'])
				room_items.append(new_obj)		
			newroom.setItems(room_items)

	def getRooms(self):
		return self.rooms
