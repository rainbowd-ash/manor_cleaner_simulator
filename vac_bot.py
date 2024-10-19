import random as rand

class vacuum_bot:
	x = 0
	y = 0
	
	current_room = 0
	adjacent_rooms = []
	
	def move_to_room(self, room):
		self.x = room.x
		self.y = room.y

class random_bot(vacuum_bot):
	def roll_action(self):
		roll = rand.randrange(0, 2)
		if roll == 0:
			return "suck"
		else:
			rand.shuffle(self.adjacent_rooms)
			self.move_to_room(self.adjacent_rooms[0])
			return "move"

class rational_bot(vacuum_bot):
	# precept table --
	# if room dirty, suck
	# if any adjacent rooms dirty
	## pick one at random and move to it
	# if in corner, move at random
	# if in center wall, move to center
	# if in center, move at random
	def roll_action(self):
		if not self.current_room.clean:
			return "suck"
		rand.shuffle(self.adjacent_rooms)
		for room in self.adjacent_rooms:
			if not room.clean:
				self.move_to_room(room)
				return "move"
		if len(self.adjacent_rooms) == 2: # corner case
			self.move_to_room(self.adjacent_rooms[0])
			return "move"
		if len(self.adjacent_rooms) == 3: # against wall
			self.x = 1
			self.y = 1
			return "move"
		else: # in center
			self.move_to_room(self.adjacent_rooms[0])
			return "move"
			
