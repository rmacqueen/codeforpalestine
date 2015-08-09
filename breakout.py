# Globals

import pygame
import constants



"""
Paddle: A class to represent the paddle
"""

class Paddle(object):

    def __init__(self):
        self.x = (constants.SCREEN_WIDTH - constants.PADDLE_WIDTH) / 2
        self.y = constants.SCREEN_HEIGHT - constants.GAP - constants.PADDLE_HEIGHT
        self.width = constants.PADDLE_WIDTH
        self.height = constants.PADDLE_HEIGHT
        self.x_velocity = 0
        self.color = constants.PADDLE_COLOR

"""
Ball: A class to represent the ball
"""
class Ball(object):

    def __init__(self):
        self.radius = constants.BALL_RADIUS
        self.x_velocity = 10
        self.y_velocity = 10
        self.x = constants.SCREEN_WIDTH / 2
        self.y = constants.SCREEN_HEIGHT / 2
        self.color = constants.BALL_COLOR;


"""
Brick: A class to represent the brick
"""
class Brick(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = constants.BRICK_WIDTH
        self.height = constants.BRICK_HEIGHT
        self.color = constants.BRICK_COLOR


def create_new_ball():
	return Ball()


def create_new_paddle():
	return Paddle()

def create_new_brick():
	return Brick()

# Get Methods 

def get_x(self):
    return self.x

def get_y(self):
    return self.y

def get_width(self):
    return self.width

def get_height(self):
    return self.height

def get_x_velocity(self):
    return self.x_velocity

def get_y_velocity(self):
    return self.y_velocity 

def get_radius(self):
    return self.radius 


def get_color(self):
    return self.color 

# Set Methods 

def set_x(self, x):
    self.x = x

def set_y(self, y):
    self.y = y

def set_width(self, w):
    self.width = w

def set_height(self, h):
    self.height = h

def set_x_velocity(self, v):
    self.x_velocity = v

def set_y_velocity(self, v):
    self.y_velocity = v

def set_radius(self, r):
    self.radius = r

def set_color(self, c):
    self.color = c



def clamp(n, min_n, max_n):
    return max(min(max_n, n), min_n)


    # Render all objects on screen using pygame draw methods
def draw_objects(screen, paddle, ball, bricks):
    # First wipe canvas clean
    screen.fill(constants.SCREEN_COLOR)

    # Draw the paddle, ball, and wall of bricks
    pygame.draw.rect(screen, constants.PADDLE_COLOR, (get_x(paddle), get_y(paddle), get_width(paddle), get_height(paddle)))
    pygame.draw.circle(screen, constants.BALL_COLOR, (int(get_x(ball)), int(get_y(ball))), get_radius(ball))
    for brick in bricks:
        
        pygame.draw.rect(screen, get_color(brick), (get_x(brick), get_y(brick), constants.BRICK_WIDTH, constants.BRICK_HEIGHT), 0)
    # Tell pygame to actually redraw everything

    pygame.display.flip()

def get_mouse_position():
    return pygame.mouse.get_pos();
