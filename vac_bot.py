import random as rand

class vacuum_bot:
	x = 0
	y = 0
	
	current_room = 0
	adjacent_rooms = []

class random_bot(vacuum_bot):
	def roll_action(self):
		roll = rand.randrange(0, 2)
		if roll == 0:
			return "suck"
		else:
			rand.shuffle(self.adjacent_rooms)
			room = self.adjacent_rooms[0]
			self.x = room.x
			self.y = room.y
			return "move"

