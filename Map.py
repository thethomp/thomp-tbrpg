import yaml
from Room import *
from Ability import *
from Enemy import *
from InteractiveObject import *

class Map(object):
	
	def __init__(self):
		yaml_path = 'config/airplane_1_alpha.yaml'
		self.rooms = {}
		self.abilities = []
		self.ability_dict = {}
		self.enemies = {}
		room_data = yaml.load_all( open(yaml_path, 'r') )
	
		### Load map data
		print "Loading map file..."
		for d in room_data:
			newroom = Room()
			newroom.setDescription(d['description'])
			directional_descs = [d['look_north'], d['look_south'], d['look_east'], d['look_west']]
			newroom.setDirectionalDescriptions(directional_descs)
			## Check for alt descriptions
			if 'look_alt_north' in d.keys():
				newroom.setAltDesc('north', d['look_alt_north'])	
				newroom.setAltDescBool('north', False)
			if 'look_alt_south' in d.keys():
				newroom.setAltDesc('south', d['look_alt_south'])	
				newroom.setAltDescBool('south', False)	
			if 'look_alt_east' in d.keys():
				newroom.setAltDesc('east', d['look_alt_east'])	
				newroom.setAltDescBool('east', False)	
			if 'look_alt_west' in d.keys():
				newroom.setAltDesc('west', d['look_alt_west'])	
				newroom.setAltDescBool('west', False)
			moves = [d['north'], d['south'], d['east'], d['west']]
			newroom.setDirectionalMoves(moves)
			self.rooms[(d['x'],d['y'])] = newroom
			room_items = []
			for item in d['items']:
				new_obj = InteractiveObject()
				new_obj.setName(item['name'])
				new_obj.setItems(item['item_list'])
				new_obj.setUnlockItems(item['unlock_item'])
				if len(new_obj.getUnlockItems()) > 0:
					new_obj.setUnlockText(item['unlock_text'])
				new_obj.setKeywords(item['keyword'])
				new_obj.setDirectionToChange(item['map_side_to_change'])
				new_obj.setExamineText(item['examine_text'])
				new_obj.setEquippable(item['equippable'])
				if new_obj.getEquippable():
					new_obj.setStrength(item['strength'])
					new_obj.setIntellect(item['intellect'])
				# Alt text to change
				if 'alt_text_dir' in item.keys():
					new_obj.setAltDescDirection(item['alt_text_dir'])	
				## Droppable items, if any
				d_items = []
				for d_item in item['droppable_items']:
					d_obj = InteractiveObject()
					d_obj.setName(d_item['name'])
					d_obj.setItems(d_item['item_list'])
					d_obj.setUnlockItems(d_item['unlock_item'])
					if len(d_obj.getUnlockItems()) > 0:
						d_obj.setUnlockText(d_item['unlock_text'])
					d_obj.setKeywords(d_item['keyword'])
					d_obj.setDirectionToChange(d_item['map_side_to_change'])
					d_obj.setExamineText(d_item['examine_text'])
					d_obj.setEquippable(d_item['equippable'])
					if d_obj.getEquippable():
						d_obj.setStrength(d_item['strength'])
						d_obj.setIntellect(d_item['intellect'])
					d_items.append(d_obj)
				new_obj.setDroppableItems(d_items)
				room_items.append(new_obj)		
			newroom.setItems(room_items)
			newroom.setEnemies(d['enemies'])
		print "Map file loaded!"
	
		### Load ability data	
		ability_yaml_path = 'config/ability_bank.yaml'
		ability_data = yaml.load_all( open(ability_yaml_path, 'r') )
		for a in ability_data:
			new_a = Ability()
			new_a.setName(a['name'])
			new_a.setLevelReq(a['level_req'])
			new_a.setDamage(a['damage'])
			new_a.setForPlayer(a['for_player'])
			self.ability_dict[a['id']] = new_a
			#self.abilities.append(new_a)

		### Load enemy data
		enemy_yaml = 'config/enemies.yaml'
		enemy_data = yaml.load_all( open(enemy_yaml, 'r') )
		for e in enemy_data:
			new_e = Enemy()
			id = e['id']
			#new_e.setPos((e['x'], e['y']))
			new_e.setName(e['name'])
			new_e.setHP(e['hp'])	
			new_e.setMP(e['mp'])
			for a_id in e['abilities']:
				new_e.addAbility(self.ability_dict[a_id])
			self.enemies[id] = new_e

	def getRooms(self):
		return self.rooms

	def getAbilities(self):
		return self.abilities

	def getEnemies(self):
		return self.enemies

	def getEnemiesAtPos(self, pos):
		e_at_pos = []
		for e in self.enemies:
			if e.getPos() == pos:
				e_at_pos.append(e)
		return e_at_pos
