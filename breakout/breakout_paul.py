"""
Breakout game.

Bouncing and movement functions taken from this particle simulation: http://www.petercollingridge.co.uk/book/export/html/6
Pygame installed for Python3 on Mac (Yosemite) from this tutorial: https://jamesfriend.com.au/installing-pygame-python-3-mac-os-yosemite
Collision detection function from this: http://www.reddit.com/r/pygame/comments/2pxiha/rectanglar_circle_hit_detection/
(simpler solutions in original StackOverflow: http://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection)
"""

import pygame
import random
import math

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 153, 0)
RED = (255, 0, 0)

STARTING_LIVES = 5

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

NUM_ROWS = 8
BRICKS_PER_ROW = 10
GAP = 4

BALL_SPEED = 5
BALL_RADIUS = 8

PADDLE_COLOR = RED
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_X = (SCREEN_WIDTH - PADDLE_WIDTH) / 2
PADDLE_Y = SCREEN_HEIGHT - GAP - PADDLE_HEIGHT

# BRICKS_PER_ROW - 1 gaps between bricks and one gap on either side
BRICK_WIDTH = (SCREEN_WIDTH - (BRICKS_PER_ROW + 1) * GAP) / BRICKS_PER_ROW;
BRICK_HEIGHT = 8
GAP_ABOVE_BRICKS = 45

class Ball():
    def __init__(self):
        self.x = (SCREEN_WIDTH - BALL_RADIUS) / 2
        self.y = (SCREEN_HEIGHT - BALL_RADIUS) / 2
        self.radius = BALL_RADIUS
        self.speed = BALL_SPEED
        self.angle = random.uniform(math.pi + math.pi/4, math.pi - math.pi/4) #somewhere between bottom left corner and bottom right corner
        self.color = RED

    def display(self):
        pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), self.radius)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounce_off_walls(self):
        # we're checking if the ball has gone past a wall
        # Bounce off of the right wall
        if self.x > SCREEN_WIDTH - self.radius:
            self.x = 2 * (SCREEN_WIDTH - self.radius) - self.x
            # self.angle = -self.angle
            self.bounce_leftright()
            return "R"

        # Bounce off of the left wall
        elif self.x < self.radius:
            self.x = 2 * self.radius - self.x
            # self.angle = -self.angle
            self.bounce_leftright()
            return "L"

        # Bounce off of the bottom wall
        if self.y > SCREEN_HEIGHT - self.radius:
            self.y = 2 * (SCREEN_HEIGHT - self.radius) - self.y
            # self.angle = math.pi - self.angle
            self.bounce_updown()
            return "B"

        # Bounce off of the top wall
        elif self.y < self.radius:
            self.y = 2 * self.radius - self.y
            # self.angle = math.pi - self.angle
            self.bounce_updown()
            return "T"


    # If we hit a brick, bounce off in the right direction depending on
    # whether we hit the brick from the side or from on top/below
    def bounce_off_object(self, obj):
        if self.y >= PADDLE_Y:
            self.y = PADDLE_Y - GAP

        # self.bounce_updown()

        # We hit the brick from the side so change x direction
        if obj.y <= self.y <= obj.y + obj.height:
            self.bounce_leftright()

        # We hit the brick from on top or from below
        elif obj.x <= self.x <= obj.x + obj.width:
            self.bounce_updown()

        # else:
        #     print("WTF?")

    def bounce_updown(self):
        self.angle = math.pi - self.angle

    def bounce_leftright(self):
        self.angle = -self.angle

    def collided(self, obj):
        centerx = obj.x + obj.width / 2
        centery = obj.y + obj.height / 2
        circle_distance_x = abs(self.x - centerx)
        circle_distance_y = abs(self.y - centery)
        if circle_distance_x > obj.width/2.0 + self.radius or circle_distance_y > obj.height/2.0 + self.radius:
            return False
        if circle_distance_x <= obj.width/2.0 or circle_distance_y <= obj.height/2.0:
            return True
        corner_x = circle_distance_x-obj.width/2.0
        corner_y = circle_distance_y-obj.height/2.0
        corner_distance_sq = corner_x**2.0 +corner_y**2.0
        return corner_distance_sq <= self.radius**2.0

class Brick():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = BRICK_WIDTH
        self.height = BRICK_HEIGHT

class Paddle(object):
    def __init__(self):
        self.x = PADDLE_X
        self.y = PADDLE_Y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT

    def move(self, xy):
        if xy[0] < self.width / 2:
            self.x = 0
        elif xy[0] > SCREEN_WIDTH - self.width / 2:
            self.x = SCREEN_WIDTH - self.width
        else:
            self.x = xy[0] - .5 * self.width

class Breakout():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Breakout')
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

        self.loseText = self.font.render("You Lose.", True, WHITE)
        self.winText = self.font.render("You Win!", True, WHITE)

        self.lay_bricks()
        self.ball = Ball()
        self.paddle = Paddle()

        
    def play(self):
        lives = STARTING_LIVES
        running = True
        while running:
            # check to make sure we haven't exited the program via the 'X' button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.paddle.move(event.pos)

            if lives == 0:
                self.screen.blit(selfloseText, (200, 200))
                pygame.display.update()

            elif len(self.bricks) == 0:
                text = self.font.render("You Won!", True, WHITE)
                # textpos = text.get_rect(centerx=self.screen.get_width()/2)
                # textpos.top = 300
                self.screen.blit(text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)) 
                pygame.display.update()

            else:
                self.ball.move()
                if self.ball.bounce_off_walls() == "B":
                    lives -= 1
                    self.ball = Ball()

                if self.ball.collided(self.paddle):
                    self.ball.bounce_off_object(self.paddle)

                for brick in self.bricks:
                    if self.ball.collided(brick):
                        self.ball.bounce_off_object(brick)
                        self.bricks.remove(brick)

                self.draw()   

        pygame.quit()

    def draw(self):
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, PADDLE_COLOR, (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height))
        pygame.draw.circle(self.screen, self.ball.color, (int(self.ball.x), int(self.ball.y)), self.ball.radius)
        
        for brick in self.bricks:
            pygame.draw.rect(self.screen, brick.color, (brick.x, brick.y, BRICK_WIDTH, BRICK_HEIGHT), 0)

        pygame.display.flip()

    def lay_bricks(self):
        self.bricks = []

        for row in range(NUM_ROWS):
            for brick in range(BRICKS_PER_ROW):
                x = GAP + (brick * (BRICK_WIDTH + GAP))
                y = GAP_ABOVE_BRICKS + (row * (BRICK_HEIGHT + GAP))

                color = None
                if (row == 0 or row == 1):
                    color = RED
                elif (row == 2 or row == 3):
                    color = ORANGE
                elif (row == 4 or row == 5):
                    color = GREEN
                elif (row == 6 or row == 7):
                    color = YELLOW
                else: 
                    color = YELLOW

                self.bricks.append(Brick(x, y, color))

if __name__ == '__main__':
    game = Breakout()
    game.play()