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
user_cell = palgame.get_random_user()

# This function updates the position of any cell.
def update_cell_position(cell, speed):
	pass

# This function updates the position of only the user cell.
def update_user_cell_position(cell):
	pass

# This function returns True if cell1 and cell2 have collided, and False otherwise.
def cells_collide(cell1, cell2):
	pass

# This function allows the cell to eat smaller cells that it reaches. It can be used with any cell.
def eat_cells(cell):
	pass

# This function allows the cell to eat nearby food. It can be used with any cell.
def eat_food(cell):
	pass

# This function draws all of the cells and food by calling palgame.draw_circle,
# and using their x, y, and radius values.
def draw_objects():
	pass


while True:
	palgame.get_event()


	### Write code here that will update the user's cell
	### and update all the other cells. Make sure you first
	### fill in the update_user_ball_position() and update_ball_position
	### functions and then call them here.


	### Now we want to eat the food. Fill in the eat_food function
	### and then call it here


	### Now we want to eat the other cells. Fill in the eat_cells function
	### and then call it here


	palgame.clear_screen()

	### Now we want to actually draw all our objects to the screen.
	### Fill in the draw_objects function. Make sure to draw all the
	### cells and all the food.

	palgame.draw_everything()
