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
    coordinates =  breakout.get_mouse_location()
    x = coordinates[0]
    breakout.set_x(paddle, breakout.clamp(x + breakout.get_x_velocity(paddle), 0, constants.SCREEN_WIDTH - breakout.get_width(paddle)))

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

def ball_bounce_off(ball):
    breakout.set_y_velocity(ball, -breakout.get_y_velocity(ball))


# Render all objects on screen using pygame draw methods
def draw_objects():
    # First wipe canvas clean
    breakout.clear_screen()
    # Draw the paddle, ball, and wall of bricks
    breakout.draw_rectangle(breakout.get_x(paddle), breakout.get_y(paddle), breakout.get_width(paddle), breakout.get_height(paddle), breakout.get_color(paddle))
    breakout.draw_circle(breakout.get_x(ball), breakout.get_y(ball), breakout.get_radius(ball), breakout.get_color(ball))
    for brick in bricks:
        breakout.draw_rectangle(breakout.get_x(brick), breakout.get_y(brick), breakout.get_width(brick), breakout.get_height(brick), breakout.get_color(brick))
    # Tell pygame to actually redraw everything
    pygame.display.flip()


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


#Ignore the following code
breakout.build_screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

#Create the ball, paddle, bricks, boolean start and lives here 
lives = constants.NUM_LIVES
paddle = breakout.create_new_paddle()
ball = breakout.create_new_ball()
bricks = build_bricks();
start = False

# # Call function play here and pass in required variables 
# play(paddle, ball, bricks, start)
running = True
lives = constants.NUM_LIVES
while running:
    if lives == 0:
        running = False

    #Setup the keyboard events 
    for event in pygame.event.get():     
        if pygame.mouse.get_pressed() == (1, 0, 0):
            start = True        
        if event.type == pygame.QUIT:
            running = False

    # Only if start is True you want the ball to be moving. This boolean is used to keep the ball at the centre before the user hits the UP key 
    if start:
        ball_update_position(ball)
    
    #Update the position of the paddle based on the mouse
    paddle_update_position(paddle)
    
    #Check for collisions 
    if breakout.ball_did_collide_with(ball, paddle, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT):
        ball_bounce_off(ball)

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
            if  breakout.ball_did_collide_with(ball, brick, constants.BRICK_WIDTH, constants.BRICK_HEIGHT):
                ball_bounce_off(ball)
                bricks.remove(brick)


    # Redraw everything at the end of the while loop
    draw_objects()

pygame.display.update()

