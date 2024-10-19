import sys
import random as r

# discussing rooms
# (x,y)
# (0,0) (1,0)
# (0,1) (1,1)
# 
# accessing matrix
# [y][x]
# [0][0] [0][1]
# [1][0] [1][1]

class room:
	x = 0
	y = 0
	clean = True
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return f"({self.x},{self.y}) clean={str(self.clean)}"

class world:
	width  = 3
	height = 3
	rooms = []
	
	def __init__(self):
		self.reset()
	
	def reset(self):
		self.rooms = [[ room(x, y) for x in range(0, self.width)] for y in range(0, self.height)]
	def room(self, x, y):
		return self.rooms[y][x]
	
	def get_room_list(self):
		r = []
		for y in range(0, self.height):
			r = r + self.rooms[y]
		return r
	
	def apply_dirt(self, x, y):
		self.rooms[y][x].clean = False
	
	def clean_room(self, x, y):
		self.rooms[y][x].clean = True
	
	def make_n_rooms_dirty(self, quantity):
		clean_rooms =  list(filter(lambda x: x.clean == True, self.get_room_list()))
		if quantity >= len(clean_rooms):
			quantity = len(clean_rooms)
		r.shuffle(clean_rooms)
		for i in range(0, quantity):
			clean_rooms[i].clean = False
	
	def __str__(self):
		r = ""
		for y in range(0, self.height):
			for x in range(0, self.width):
				if self.rooms[y][x].clean:
					r = r + "[ ]"
				else:
					r = r + "[d]"
			r = r + "\n"
		r = r + "\n"
		return r
