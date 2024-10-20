import dirt_world as world
import vac_bot as agent
import random as rand

debug_step_by_step = False
debug_draw_world = False

# averages a list
def avg(l):
	return sum(l) / len(l)

# returns true 25% of the time
def roll_25():
	roll = rand.randrange(0,4)
	if roll == 0:
		return True
	return False

def draw_world(w, a):
	r = "\n"
	for y in range(0, w.height):
		for x in range(0, w.width):
			symbol = ""
			if w.rooms[y][x].clean:
				symbol = "."
			else:
				symbol = "d"
			if y == a.y and x == a.x:
				r = r + "{" + symbol + "}"
			else:
				r = r + " " + symbol + " "
		r = r + "\n"
	r = r + "\n"
	print(r)

# win state
## returns false when there is dirt
def all_clean(world):
	for room in world.get_room_list():
		if not room.clean:
			return False
	return True

# makes a new room to send to vac_bot on sensor failure
def CHAOS_WORLD_sensor_failure(room):
	new_room = world.room(room.x, room.y)
	new_room.clean = not room.clean
	return new_room


# int dirt_amount = how many rooms initially dirty
# agent agent = random or rational bot
# bool CHAOS_WORLD = true for chaos world else false
# returns list of run scores
def test(dirt_amount = 1, 
		agent = agent.random_bot(), 
		CHAOS_WORLD = False):
	
	run_score = 0
	
	dirt_world = world.world()
	dirt_world.make_n_rooms_dirty(dirt_amount)

	# main loop
	while not all_clean(dirt_world):
		if debug_draw_world:
			draw_world(dirt_world, agent)
		
		if not CHAOS_WORLD:
			agent.current_room = dirt_world.room(agent.x, agent.y)
			agent.adjacent_rooms = dirt_world.adjacent_rooms(agent.x, agent.y)
		else:
			new_adj_rooms = []
			if roll_25():
				agent.current_room = CHAOS_WORLD_sensor_failure(dirt_world.room(agent.x, agent.y))
			else:
				agent.current_room = dirt_world.room(agent.x, agent.y)
			for room in dirt_world.adjacent_rooms(agent.x, agent.y):
				if roll_25():
					new_adj_rooms = new_adj_rooms + [CHAOS_WORLD_sensor_failure(room)]
				else:
					new_adj_rooms = new_adj_rooms + [room]
			agent.adjacent_rooms = new_adj_rooms
		
		action = agent.roll_action() 
		
		if action == "suck":
			if not dirt_world.room(agent.x, agent.y).clean:
				dirt_world.clean_room(agent.x, agent.y)
			else:
				if CHAOS_WORLD:
					if rand.randrange(0,10) == 0:
						dirt_world.apply_dirt(agent.x, agent.y)
				run_score += 1
		elif action == "move":
			run_score += 1
		if debug_step_by_step:
			input("~~~")
	return run_score

def test_set(
		count, 
		dirt_amount = 1, 
		agent = agent.random_bot(), 
		cw = False):
	r = []
	for i in range(0, count):
		r = r + [test(dirt_amount, agent, cw)]
	return r


run_count = 100

rand_1 = test_set(run_count, 1, agent.random_bot(), False)
rand_3 = test_set(run_count, 3, agent.random_bot(), False)
rand_5 = test_set(run_count, 5, agent.random_bot(), False)

rati_1 = test_set(run_count, 1, agent.rational_bot(), False)
rati_3 = test_set(run_count, 3, agent.rational_bot(), False)
rati_5 = test_set(run_count, 5, agent.rational_bot(), False)

rand_1_cw = test_set(run_count, 1, agent.random_bot(), True)
rand_3_cw = test_set(run_count, 3, agent.random_bot(), True)
rand_5_cw = test_set(run_count, 5, agent.random_bot(), True)

rati_1_cw = test_set(run_count, 1, agent.rational_bot(), True)
rati_3_cw = test_set(run_count, 3, agent.rational_bot(), True)
rati_5_cw = test_set(run_count, 5, agent.rational_bot(), True)

print("result set:")
print("random 1 = " + str(avg(rand_1)))
print("random 3 = " + str(avg(rand_3)))
print("random 5 = " + str(avg(rand_5)))
print("---")
print("rational 1 = " + str(avg(rati_1)))
print("rational 3 = " + str(avg(rati_3)))
print("rational 5 = " + str(avg(rati_5)))
print("CHAOS WORLD ---")
print("random 1 = " + str(avg(rand_1_cw)))
print("random 3 = " + str(avg(rand_3_cw)))
print("random 5 = " + str(avg(rand_5_cw)))
print("---")
print("rational 1 = " + str(avg(rati_1_cw)))
print("rational 3 = " + str(avg(rati_3_cw)))
print("rational 5 = " + str(avg(rati_5_cw)))
