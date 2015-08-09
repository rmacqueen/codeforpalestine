"""
Breakout game.

"""

import pygame
import math
import breakout
import constants

"""
Paddle: Methods
"""
# Update the position of the paddle. It is confined to the boundaries
# of the screen
def paddle_update_position(paddle):
    coordinates =  breakout.get_mouse_position()
    x = coordinates[0]
    breakout.set_x(paddle, constants.clamp(x + breakout.get_x_velocity(paddle), 0, constants.SCREEN_WIDTH - breakout.get_width(paddle)))

"""
Ball: Methods
"""

def ball_update_position(ball):
    x = breakout.get_x(ball)
    y = breakout.get_y(ball)
    x += breakout.get_x_velocity(ball)
    y += breakout.get_y_velocity(ball)
    breakout.set_x(ball, x)
    breakout.set_y(ball, y)

    # If it hits the side walls, bounce off them
    if breakout.get_x(ball) >= constants.SCREEN_WIDTH:
        breakout.set_x_velocity(ball, -breakout.get_x_velocity(ball))
    if breakout.get_x(ball) < 0:
        breakout.set_x_velocity(ball, -breakout.get_x_velocity(ball))

    # If it hits the ceiling, bounce off it
    if breakout.get_y(ball) < 0:
        breakout.set_y_velocity(ball, -breakout.get_y_velocity(ball))

def ball_bounce_off_paddle(ball, paddle):
    breakout.set_y_velocity(ball, -breakout.get_y_velocity(ball))

# If we hit a brick, bounce off in the right direction depending on
# whether we hit the brick from the side or from on top/below
def ball_bounce_off_brick(ball, brick):
    # We hit the brick from on top or from below so change y direction
    #if breakout.get_y(ball) in range(breakout.get_y(brick), breakout.get_y(brick) + breakout.get_height(brick)):
    if breakout.get_x(ball) + breakout.get_radius(ball) >= breakout.get_x(brick) and breakout.get_x(ball) - breakout.get_radius(ball) <= breakout.get_x(brick) + breakout.get_width(brick):
        x_v = breakout.get_x_velocity(ball)
        breakout.set_x_velocity(ball, -x_v)

    # We hit the brick from the side so change x direction
    # if breakout.get_x(ball) in range(breakout.get_x(brick), breakout.get_x(brick) + breakout.get_width(brick)):
    if breakout.get_y(ball) + breakout.get_radius(ball) >= breakout.get_y(brick) and breakout.get_y(ball) - breakout.get_radius(ball) < breakout.get_y(brick) + breakout.get_height(brick):
        y_v = breakout.get_y_velocity(ball)
        breakout.set_y_velocity(ball, -y_v)  


# Check and see if the ball and another obj collided with each other 
def ball_did_collide_with(ball, obj):
    if breakout.get_x(ball) + breakout.get_radius(ball) >= breakout.get_x(obj) and breakout.get_x(ball) - breakout.get_radius(ball) <= breakout.get_x(obj) + breakout.get_width(obj) and breakout.get_y(ball) + breakout.get_radius(ball) >= breakout.get_y(obj) and breakout.get_y(ball) - breakout.get_radius(ball) < breakout.get_y(obj) + breakout.get_height(obj):
        return True 


def play(screen, paddle, ball, bricks, start):
    running = True
    lives = constants.NUM_LIVES
    while running:
        if lives == 0:
            running = False

        #Setup the keyboard events 
        for event in pygame.event.get():
            # If you press the up key, the ball will start moving 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    start = True            
            if event.type == pygame.QUIT:
                running = False

        # Only if start is True you want the ball to be moving. This boolean is used to keep the ball at the centre before the user hits the UP key 
        if start:
            ball_update_position(ball)
        
        #Update the position of the paddle based on the mouse
        paddle_update_position(paddle)
        
        #Check for collisions 
        if ball_did_collide_with(ball, paddle):
            ball_bounce_off_paddle(ball, paddle)

        # If ball went out of bounds, we lose a life, and start
        # with a new ball.
        elif (breakout.get_y(ball) > constants.SCREEN_HEIGHT):
            lives -= 1
            ball = breakout.create_new_ball()
            start = False

        # If bricks are over, you won! 
        if len(bricks) == 0:
            running = False;

        # Else, loop through the entire bricks array to see if the ball collided with any brick 
        else:
            for brick in bricks:
                if  ball_did_collide_with(ball, brick):
                    ball_bounce_off_brick(ball, brick)
                    bricks.remove(brick)


        # Redraw everything at the end of the while loop
        breakout.draw_objects(screen, paddle, ball, bricks)

    pygame.display.update()

    #Wait for event to exit screen 
    event =  pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()


# The following function will draw the set of bricks at the top of the screen. 
def build_bricks():
    #Create an empty array
    bricks = []
    for row in range(constants.NUM_ROWS):
        for col in range(constants.BRICKS_PER_ROW):
            x_position = constants.GAP + (col * (constants.BRICK_WIDTH + constants.GAP))
            y_position = row* (constants.BRICK_HEIGHT + constants.GAP)

            # Set the brick color based on row number 
            color = None
            if (row == 0 or row == 1):
                color = constants.RED
            elif (row == 2 or row  == 3):
                color = constants.ORANGE
            elif (row  == 4 or row  == 5):
                color = constants.GREEN
            elif (row == 6 or row  == 7):
                color = constants.YELLOcol
            else: 
                color = constants.YELLOW

            #Create a new brick and set the x,y, and color 
            b = breakout.create_new_brick()
            breakout.set_x(b, x_position)
            breakout.set_y(b, y_position)
            breakout.set_color(b, color)
            bricks.append(b)
    return bricks


if __name__ == '__main__':

    #Ignore the following code
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption('Breakout')
    clock = pygame.time.Clock()

    #Create the ball, paddle, bricks, boolean start and lives here 
    lives = constants.NUM_LIVES
    paddle = breakout.create_new_paddle()
    ball = breakout.create_new_ball()
    bricks = build_bricks();
    start = False

    # Call function play here and pass in required variables 
    play(screen, paddle, ball, bricks, start)

