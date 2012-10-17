import yaml
from Room import *
from Ability import *
from Enemy import *
from InteractiveObject import *

class Map(object):
	
	def __init__(self):
		yaml_path = 'config/airplane_1.yaml'
		self.rooms = {}
		self.abilities = []
		self.enemies = {}
		room_data = yaml.load_all( open(yaml_path, 'r') )
	
		### Load enemy data
		#enemy_yaml = 'config/enemies.yaml'
		#enemy_data = yaml.load_all( open(enemy_yaml, 'r') )
		#for e in enemy_data:
	#		new_e = Enemy()
#			id = e['id']
#			new_e.setName(e['name'])
#			new_e.setHP(e['hp'])	
#			new_e.setMP(e['mp'])
#			self.enemies[id] = new_e
		
	
		### Load map data
		print "Loading map file..."
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
				new_obj.setEquippable(item['equippable'])
				if new_obj.getEquippable():
					new_obj.setStrength(item['strength'])
					new_obj.setIntellect(item['intellect'])
				room_items.append(new_obj)		
			newroom.setItems(room_items)
			newroom.setEnemies(d['enemies'])
		print "Map file loaded!"
	
		### Load ability data	
#		ability_yaml_path = 'config/abilities.yaml'
#		ability_data = yaml.load_all( open(ability_yaml_path, 'r') )
#		for a in ability_data:
#			new_a = Ability()
#			new_a.setName(a['name'])
#			new_a.setLevelReq(a['level_req'])
#			new_a.setDamage(a['damage'])
#			new_a.setForPlayer(a['for_player'])
#			self.abilities.append(new_a)
		

	def getRooms(self):
		return self.rooms

	def getAbilities(self):
		return self.abilities

	def getEnemies(self):
		return self.enemies
