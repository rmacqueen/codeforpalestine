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

# This function creates the window for the game. It should be called at
# the beginning of your program.
def build_screen(width, height):
	global screen
	screen = pygame.display.set_mode((width, height))

# This function draws a circle.
def draw_circle(x, y, radius, color):
	pygame.draw.circle(screen, color, (x, y), radius)

# This function draws a rectangle.
def draw_rect(x, y, width, height):
	pygame.draw.rect(screen, BALL_COLOR, (x, y, width, height), 0)

# This function wipes the screen clean by filling it with a color.
# This lets you draw new objects, or make objects look like they've moved.
def clear_screen():
	screen.fill(SCREEN_COLOR)

# This function actually puts all objects on the screen, after you've
# drawn them with draw_circle and draw_rect.
def draw_everything():
	pygame.display.flip()

# This function lets you exit the game if you press the "X" button.
def get_event():
	clock.tick(20)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit(0)

# These functions allow you to get and set x, y, radius, xdir, and ydir for a ball.
def get_x(ball):
	return ball[0]

def get_y(ball):
	return ball[1]

def set_x(ball, x):
	ball[0] = x

def set_y(ball, y):
	ball[1] = y

def get_xdir(ball):
	return ball[3]

def get_ydir(ball):
	return ball[4]

def set_xdir(ball, xdir):
	ball[3] = xdir

def set_ydir(ball, ydir):
	ball[4] = ydir

def get_radius(ball):
	return ball[2]

def set_radius(ball, r):
	ball[2] = r

# This function returns a ball with a random position and random radius.
# We describe a ball as a list: ball[0] is x, ball[1] is y, ball[2] is radius,
# ball[3] is xdir, and ball[4] is ydir.
def get_random_ball():
	return [random.randint(0, SCREEN_WIDTH), 
		random.randint(0, SCREEN_HEIGHT),
		random.randint(6, 20),
		1, -1]

# This function returns a ball to represent food, with a random position and
# radius of 5. This ball does not have xdir or ydir because it doesn't move.
def get_random_food():
	return [random.randint(0, SCREEN_WIDTH), 
		random.randint(0, SCREEN_HEIGHT), 
		5, 0, 0]

# This function returns a ball to represent the user, with radius 3.
def get_random_user():
	ball = get_random_ball()
	set_radius(ball, 3)
	return ball

# This function returns a speed, given a radius. If the radius is larger, the ball
# moves slower. If the radius is smaller, the ball moves faster.
def get_speed(radius):
	return 1 + int(50 / (radius * 0.3))

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

	if abs(mouse_x - user_x) < user_radius:
		xdir = 0
	else:
		xdir = int(user_speed * (mouse_x - user_x) / distance)

	if abs(mouse_y - user_y) < user_radius:
		ydir = 0
	else:
		ydir = int(user_speed * (mouse_y - user_y) / distance)

	return (xdir, ydir)
