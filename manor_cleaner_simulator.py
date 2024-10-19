import dirt_world as world
import vac_bot as agent

debug_step_by_step = False

dirt_world = world.world()
agent = agent.random_bot()
run_score = 0

def draw_world():
	r = "\n"
	for y in range(0, dirt_world.height):
		for x in range(0, dirt_world.width):
			symbol = ""
			if dirt_world.rooms[y][x].clean:
				symbol = "."
			else:
				symbol = "d"
			if y == agent.y and x == agent.x:
				r = r + "{" + symbol + "}"
			else:
				r = r + " " + symbol + " "
		r = r + "\n"
	r = r + "\n"
	print(r)

# win state
## returns false when there is dirt
def all_clean():
	for room in dirt_world.get_room_list():
		if not room.clean:
			return False
	return True

# -------------------------------
dirt_world.make_n_rooms_dirty(1)

# main loop
while not all_clean():
	# update agent info
	agent.current_room = dirt_world.room(agent.x, agent.y)
	agent.adjacent_rooms = dirt_world.adjacent_rooms(agent.x, agent.y)
	# get action from agent
	action = agent.roll_action() 
	# affect change
	if action == "suck":
		if not dirt_world.room(agent.x, agent.y).clean:
			dirt_world.clean_room(agent.x, agent.y)
		else:
			run_score += 1
	elif action == "move":
		run_score += 1
	if debug_step_by_step:
		input("~~~")

print(run_score)
