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

# This function will chnage the direction of the ball when it hits the paddle 
def ball_bounce_off_paddle(ball, paddle):
    pass

# If we hit a brick, bounce off in the right direction depending on
# whether we hit the brick from the side or from on top/below
def ball_bounce_off_brick(ball, brick):
    # We hit the brick from on top or from below so change y direction
    # We hit the brick from the side so change x direction
    pass

# Check and see if the ball and another obj collided with each other 
def ball_did_collide_with(ball, obj):
    pass


"""
Play
"""
def play(screen, paddle, ball, bricks, start): 
    pass  
    
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
    # Hint: You need a double for loop to draw the set of bricks on top. Set the brick color based on row number by using the colors in the constants.py
    # file (You can add other colors if you wish). When you create a new brick and set the x,y, and color 
    pass



if __name__ == '__main__':

    #Ignore the following code
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption('Breakout')
    clock = pygame.time.Clock()

    #Create the ball, paddle, bricks and lives here 
   
    # Create a boolean variable here to control when the ball starts moving 

    # Call function play here and pass in required variables 

