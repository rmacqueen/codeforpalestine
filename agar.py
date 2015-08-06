import palgame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
NUM_CELLS = 5
NUM_FOOD = 20

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

palgame.build_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

xdir = 1
ydir = 1
cells = []
food = []

for a in range(NUM_CELLS):
	cells.append(palgame.get_random_ball())

for c in range(NUM_FOOD):
	food.append(palgame.get_random_food())

first_cell = palgame.get_random_ball()

def update_cell_position(cell, speed):
	x = palgame.get_x(cell)
	y = palgame.get_y(cell)
	xdir = palgame.get_xdir(cell)
	ydir = palgame.get_ydir(cell)

	if x > SCREEN_WIDTH or x < 0:
		xdir = -1 * xdir
	if y > SCREEN_HEIGHT or y < 0:
		ydir = -1 * ydir
	x = x + xdir * speed
	y = y + ydir * speed

	palgame.set_x(cell, x)
	palgame.set_y(cell, y)
	palgame.set_xdir(cell, xdir)
	palgame.set_ydir(cell, ydir)

def update_user_cell_position(cell):
	vx, vy = palgame.get_user_direction(palgame.get_x(cell), palgame.get_y(cell), palgame.get_radius(cell))
	new_x = palgame.get_x(cell) + vx
	palgame.set_x(cell, new_x)
	new_y = palgame.get_y(cell) + vy
	palgame.set_y(cell, new_y)

def cells_collide(cell1, cell2):
	if ( abs(palgame.get_x(cell2) - palgame.get_x(cell1)) < (palgame.get_radius(cell2) + palgame.get_radius(cell1))
		and abs(palgame.get_y(cell2) - palgame.get_y(cell1)) < (palgame.get_radius(cell2) + palgame.get_radius(cell1)) ):
		return True
	else:
		return False

def eat_cells(cell):
	for b in range(NUM_CELLS):
		other_cell = cells[b]
		if a != b and cells_collide(cell, other_cell):
			radius = palgame.get_radius(cell)
			if radius >= palgame.get_radius(other_cell):
				new_radius = radius + (1 - radius / 100)
				palgame.set_radius(cell, new_radius)
				cells[b] = palgame.get_random_ball()

def eat_food(cell):
	for f in range(NUM_FOOD):
		nom = food[f]
		if cells_collide(cell, nom):
			new_radius = palgame.get_radius(cell) + (1 - palgame.get_radius(cell) / 100)
			palgame.set_radius(cell, new_radius)
			food[f] = palgame.get_random_food()

def draw_objects():
	for f in food:
		palgame.draw_circle(palgame.get_x(f), palgame.get_y(f), palgame.get_radius(f), BLUE)
	for i, b in enumerate(cells):
		if i == 0:
			color = GREEN
		else:
			color = RED
		palgame.draw_circle(palgame.get_x(b), palgame.get_y(b), palgame.get_radius(b), color)

while True:
	palgame.get_event()

	for a in range(NUM_CELLS):
		cell = cells[a]
		speed = palgame.get_speed(palgame.get_radius(cell))
		### Right code here that will update the user's ball
		### and update all the other balls. Make sure you first
		### fill in the update_user_ball_position() and update_ball_position
		### functions and then call them here.
		if a == 0:
			update_user_cell_position(cell)
		else:
			update_cell_position(cell, speed)

		### Now we want to eat the food. Fill in the eat_food function
		### and then call it here
		eat_food(cell)

		### Now we want to eat the other cells. Fill in the eat_cells function
		### and then call it here
		eat_cells(cell)

	palgame.clear_screen()

	### Now we want to actually draw all our objects to the screen
	### Fill in the draw_objects function. Make sure to draw all the
	### cells and all the food
	draw_objects()
	palgame.draw_everything()
