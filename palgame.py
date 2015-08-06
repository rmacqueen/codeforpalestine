import pygame, sys, math
BALL_COLOR = (255, 0, 0)
SCREEN_COLOR = (100, 100, 100)

pygame.init()
clock = pygame.time.Clock()
screen = None

def build_screen(width, height):
	global screen
	screen = pygame.display.set_mode((width, height))

def draw_circle(x, y, radius):
	pygame.draw.circle(screen, BALL_COLOR, (x, y), radius)
	pygame.display.flip()

def draw_rect(x, y, width, height):
	pygame.draw.rect(screen, BALL_COLOR, (x, y, width, height), 0)
	pygame.display.flip()

def clear_screen():
	screen.fill(SCREEN_COLOR)

def get_event():
	clock.tick(20)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit(0)

# Returns the location of the mouse as (x, y). For example:
# event = get_mouse_location()
# print "x: " + event[0] + ", y: " + event[1]
def get_mouse_location():
    return pygame.mouse.get_pos()

# Returns the direction for the user cell as (xdir, ydir). Uses the user location,
# user radius, and mouse location to figure out the speed of the user. Using
# that, figures out the x-direction and y-direction of the user cell.
# To use:
# 	user_direction = get_user_direction(user_x, user_y, user_radius)
# 	user_xdir = user_direction[0]
# 	user_ydir = user_direction[1]
def get_user_direction(user_x, user_y, user_radius):
	mouse_location = get_mouse_location()
	mouse_x = mouse_location[0]
	mouse_y = mouse_location[1]

	user_speed = get_speed(user_radius)
	distance = math.sqrt((mouse_x - user_x)**2 + (mouse_y - user_y)**2)

	if abs(mouse_x - user_x) < radius:
		xdir = 0
	else:
		xdir = int(user_speed * (mouse_x - user_x) / distance)

	if abs(mouse_y - user_y) < radius:
		ydir = 0
	else:
		ydir = int(user_speed * (mouse_y - user_y) / distance)

	return (xdir, ydir)
