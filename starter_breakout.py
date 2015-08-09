"""
Breakout game.

Bouncing and movement functions taken from this particle simulation: http://www.petercollingridge.co.uk/book/export/html/6
Pygame installed for Python3 o n Mac (Yosemite) from this tutorial: https://jamesfriend.com.au/installing-pygame-python-3-mac-os-yosemite
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
    pass

"""
Ball: Methods
"""

# This function must update the coordinates of the ball and changes the direction of the ball bounces of either the left, top, or right walls 
def ball_update_position(ball):
    pass
    #TODO

# This function will change the direction of the ball when it hits the paddle 
def ball_bounce_off_paddle(ball, paddle):
    pass

# If we hit a brick, bounce off in the right direction depending on
# whether we hit the brick from the side or from on top/below
def ball_bounce_off_brick(ball, brick):
    # ALWAYS change y direction
    pass

# Render all objects on screen using pygame draw methods
def draw_objects(paddle, ball, bricks):
    # First wipe canvas clean by calling breakout.clear_screen()
    # TODO

    # Draw the paddle, ball, and wall of bricks
    # TODO

    # Tell pygame to actually redraw everything (DON'T CHANGE)
    pygame.display.flip()


#The following function will draw the set of bricks at the top of the screen. 
def build_bricks():
    # Create an empty array
    # Hint: You need a double for loop to draw the set of bricks on top. Set the brick color based on row number by using the colors in the constants.py
    # file (You can add other colors if you wish). When you create a new brick and set the x,y, and color 
    pass



# Creating the screen 
breakout.build_screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

# Create the ball, paddle, bricks and lives here 
# TODO

running = True
start = False

# TODO
while running:
    # If number of lives left is 0, break out of the while loop
    # TODO

    # Setup the mouse events 
    # DO NOT change this code
    for event in pygame.event.get():
        # If you click the mouse, the ball will start moving 
        if pygame.mouse.get_pressed() == (1, 0, 0):
            start = True 

    if start == True:
        # Make the ball update its position. 
        pass

    # Update the position of the paddle based on the mouse
    # TODO 
        
    # Check for collisions using breakout.ball_did_collide_with(obj, brick, width, height) 
    # TODO 

    # If ball went out of bounds, we lose a life, and start
    # with a new ball.
    # TODO 

    # If bricks are over, you won! 
    # TODO 

    # Else, loop through the entire bricks array to see if the ball collided with any brick 
    # TODO 

    # Redraw everything at the end of the while loop

pygame.display.update()
