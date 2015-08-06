import pygame
import sys
import random
import math

BALL_COLOR = (255, 0, 0)
SCREEN_COLOR = (100, 100, 100)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

pygame.init()
clock = pygame.time.Clock()
screen = None

def build_screen(width, height):
	global screen
	screen = pygame.display.set_mode((width, height))

def draw_circle(x, y, radius, color):
	pygame.draw.circle(screen, color, (x, y), radius)

def draw_rect(x, y, width, height):
	pygame.draw.rect(screen, BALL_COLOR, (x, y, width, height), 0)

def clear_screen():
	screen.fill(SCREEN_COLOR)

def draw_everything():
	pygame.display.flip()

def get_event():
	clock.tick(20)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit(0)

def get_x(ball):
	return ball[0]

def get_y(ball):
	return ball[1]

def set_x(ball, x):
	ball[0] = x

def set_y(ball, y):
	ball[1] = y

def get_radius(ball):
	return ball[2]

def set_radius(ball, r):
	ball[2] = r

def get_random_ball():
	return [random.randint(0, SCREEN_WIDTH), 
		random.randint(0, SCREEN_HEIGHT),
		random.randint(6, 20),
		1, -1]

def get_random_food():
	return [random.randint(0, SCREEN_WIDTH), 
		random.randint(0, SCREEN_HEIGHT), 
		5]

def get_speed(radius):
	return 1 + int(50 / (radius * 0.3))

def get_vx(speed, mx, my, x, y):
	if abs(mx - x) <= 1 or abs(my - y) <= 1:
		return 0
	return (speed * (mx - x) / math.sqrt((mx - x)**2 + (my - y)**2))

def get_vy(speed, mx, my, x, y):
	if abs(mx - x) <= 1 or abs(my - y) <= 1:
		return 0
	return (speed * (my - y) / math.sqrt((mx - x)**2 + (my - y)**2))


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
