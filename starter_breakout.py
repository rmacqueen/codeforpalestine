"""
Breakout game.

Bouncing and movement functions taken from this particle simulation: http://www.petercollingridge.co.uk/book/export/html/6
Pygame installed for Python3 o n Mac (Yosemite) from this tutorial: https://jamesfriend.com.au/installing-pygame-python-3-mac-os-yosemite
"""

import pygame
import math
import breakout
import constants

def clamp(n, min_n, max_n):
    return max(min(max_n, n), min_n)

"""
Paddle: Methods
"""
# Update the position of the paddle. It is confined to the boundaries
# of the screen
def paddle_update_position(paddle):
    breakout.set_x(paddle, constants.clamp(breakout.get_x(paddle) + breakout.get_x_velocity(paddle), 0, constants.SCREEN_WIDTH - breakout.get_width(paddle)))

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
    #if breakout.get_x(ball) in range(breakout.get_x(brick), breakout.get_x(brick) + breakout.get_width(brick)):
    if breakout.get_y(ball) + breakout.get_radius(ball) >= breakout.get_y(brick) and breakout.get_y(ball) - breakout.get_radius(ball) < breakout.get_y(brick) + breakout.get_height(brick):
        y_v = breakout.get_y_velocity(ball)
        breakout.set_y_velocity(ball, -y_v)  


def ball_did_collide_with(ball, obj):
    if breakout.get_x(ball) + breakout.get_radius(ball) >= breakout.get_x(obj) and breakout.get_x(ball) - breakout.get_radius(ball) <= breakout.get_x(obj) + breakout.get_width(obj) and breakout.get_y(ball) + breakout.get_radius(ball) >= breakout.get_y(obj) and breakout.get_y(ball) - breakout.get_radius(ball) < breakout.get_y(obj) + breakout.get_height(obj):
        return True 



def play(screen, paddle, ball, bricks, start, lives):
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    running = True
    while running:
        if lives == 0:
            running = False
            loseText = font.render("You Lose.", True, constants.WHITE)
            screen.blit(loseText, (200, 200))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    start = True            
            if event.type == pygame.QUIT:
                running = False
        coordinates =  breakout.get_mouse_position()
        x = coordinates[0]
        breakout.set_x(paddle,  x)

        if start:
            ball_update_position(ball)
        
        paddle_update_position(paddle)
        
        if ball_did_collide_with(ball, paddle):
            ball_bounce_off_paddle(ball, paddle)

        # If ball went out of bounds, we lose a life, and start
        # with a new ball.
        elif (breakout.get_y(ball) > constants.SCREEN_HEIGHT):
            lives -= 1
            ball = breakout.create_new_ball()
            start = False

        if len(bricks) == 0:
            running = False;
            loseText = font.render("You Win.", True, constants.WHITE)
            screen.blit(loseText, (200, 200))

        else:
            for brick in bricks:
                if  ball_did_collide_with(ball, brick):
                    ball_bounce_off_brick(ball, brick)
                    bricks.remove(brick)


        # Redraw everything at the end of the while loop
        breakout.draw_objects(screen, paddle, ball, bricks)
    pygame.display.update()
    event =  pygame.event.wait()
    if event.type == pygame.QUIT:
        
        pygame.quit()


def build_bricks():
    bricks = []
    for i in range(constants.NUM_ROWS):
        for j in range(constants.BRICKS_PER_ROW):
            x_position = constants.GAP + (j * (constants.BRICK_WIDTH + constants.GAP))
            y_position = i * (constants.BRICK_HEIGHT + constants.GAP)
            color = None
            if (i == 0 or i == 1):
                color = constants.RED
            elif (i == 2 or i  == 3):
                color = constants.ORANGE
            elif (i  == 4 or i  == 5):
                color = constants.GREEN
            elif (i == 6 or i  == 7):
                color = constants.YELLOW
            else: 
                color = constants.YELLOW

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
    lives = constants.NUM_LIVES
    paddle = breakout.create_new_paddle()
    ball = breakout.create_new_ball()
    bricks = build_bricks();

    start = False
    play(screen, paddle, ball, bricks, start, lives)

