import pygame

BRICKS_PER_ROW = 10
NUM_ROWS = 5
GAP = 5

BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_COLOR = (0, 0, 0)

PADDLE_COLOR = (0, 0, 255)
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_COLOR = (255, 0, 0)

BALL_RADIUS = 5
BALL_COLOR = (0, 255, 0)

SCREEN_WIDTH = GAP + (BRICKS_PER_ROW * (GAP + BRICK_WIDTH))
SCREEN_HEIGHT = 600
SCREEN_COLOR = (100, 100, 100)

NUM_LIVES = 10

def clamp(n, min_n, max_n):
    return max(min(max_n, n), min_n)

"""
Paddle: A class to represent the paddle, or bat, that is controlled by the
user.
"""
class Paddle(object):

    def __init__(self):
        self.x = (SCREEN_WIDTH - PADDLE_WIDTH) / 2
        self.y = SCREEN_HEIGHT - GAP - PADDLE_HEIGHT
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT

        self.x_velocity = 0

    def move_left(self):
        self.x_velocity = -2

    def move_right(self):
        self.x_velocity = 2

    def stop(self):
        self.x_velocity = 0

    # Update the position of the paddle. It is confined to the boundaries
    # of the screen
    def update_position(self):
        self.x = clamp(self.x + self.x_velocity, 0, SCREEN_WIDTH - self.width)

"""
Ball: A class to represent the ball
"""
class Ball(object):

    def __init__(self):
        self.radius = BALL_RADIUS
        self.x_velocity = 1
        self.y_velocity = 1
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

    def update_position(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        # If it hits the side walls, bounce off them
        if self.x >= SCREEN_WIDTH:
            self.x_velocity = -1
        if self.x < 0:
            self.x_velocity = 1

        # If it hits the ceiling, bounce off it
        if self.y < 0:
            self.y_velocity = 1

    # No matter at what angle you hit the paddle, start going upwards.
    # Slighly crude approach, but this prevents weird behaviour where the ball
    # gets sort of stuck under the paddle. The behaviour occurs because the
    # paddle can move faster than the ball and so can hit the ball and then
    # 'get on top of it' so to speak. And because we have no notion of
    # force and acceleration in this world, it looks weird to the human eye.
    def bounce_off_paddle(self, paddle):
        self.y_velocity = -1

    # If we hit a brick, bounce off in the right direction depending on
    # whether we hit the brick from the side or from on top/below
    def bounce_off_brick(self, brick):
        # We hit the brick from the side so change x direction
        if self.y in range(brick.y, brick.y + brick.height):
            self.x_velocity = -self.x_velocity
        # We hit the brick from on top or from below so change
        # y direction
        if self.x in range(brick.x, brick.x + brick.width):
            self.y_velocity = -self.y_velocity

    def get_radius(self):
        return self.radius

    def did_collide_with(self, obj):
        if self.x + self.radius >= obj.x and self.x - self.radius <= obj.x + obj.width and self.y + self.radius >= obj.y and self.y - self.radius < obj.y + obj.height:
            return True 

class Brick(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BRICK_WIDTH
        self.height = BRICK_HEIGHT

class Breakout(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Breakout')
        self.clock = pygame.time.Clock()

        self.lives = NUM_LIVES
        self.paddle = Paddle()
        self.ball = Ball()
        self.build_bricks()
        self.draw_objects()

    # Render all objects on screen using pygame draw methods
    def draw_objects(self):
        # First wipe canvas clean
        self.screen.fill(SCREEN_COLOR)

        # Draw the paddle, ball, and wall of bricks
        pygame.draw.rect(self.screen, PADDLE_COLOR, (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height))
        pygame.draw.circle(self.screen, BALL_COLOR, (self.ball.x, self.ball.y), self.ball.get_radius())
        for brick in self.bricks:
            pygame.draw.rect(self.screen, BRICK_COLOR, (brick.x, brick.y, BRICK_WIDTH, BRICK_HEIGHT), 0)

        # Tell pygame to actually redraw everything
        pygame.display.flip()

    def play(self):
        while self.lives > 0:
            self.clock.tick(500)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.paddle.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.paddle.move_right()
                if event.type == pygame.KEYUP:
                    self.paddle.stop()

            self.ball.update_position()
            self.paddle.update_position()

            if self.ball.did_collide_with(self.paddle):
                self.ball.bounce_off_paddle(self.paddle)

            for brick in self.bricks:
                if self.ball.did_collide_with(brick):
                    self.ball.bounce_off_brick(brick)
                    self.bricks.remove(brick)

            # If ball went out of bounds, we lose a life, and start
            # with a new ball.
            if (self.ball.y > SCREEN_HEIGHT):
                self.lives -= 1
                self.ball = Ball()

            # Redraw everything at the end of the while loop
            self.draw_objects()

    def build_bricks(self):
        self.bricks = []
        for i in range(NUM_ROWS):
            for j in range(BRICKS_PER_ROW):
                x_position = GAP + (j * (BRICK_WIDTH + GAP))
                y_position = i * (BRICK_HEIGHT + GAP)
                new_brick = Brick(x_position, y_position)
                self.bricks.append(new_brick)

if __name__ == '__main__':
    game = Breakout()
    game.play()
