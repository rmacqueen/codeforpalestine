import palgame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
NUM_BALLS = 5
NUM_FOOD = 20

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

palgame.build_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

xdir = 1
ydir = 1
balls = []
food = []

for a in range(NUM_BALLS):
	balls.append(palgame.get_random_ball())

for c in range(NUM_FOOD):
	food.append(palgame.get_random_food())

def update_ball_position(ball, speed):
	x, y, radius, xdir, ydir = ball

	if x > SCREEN_WIDTH or x < 0:
		xdir = -1 * xdir
	if y > SCREEN_HEIGHT or y < 0:
		ydir = -1 * ydir
	x = x + xdir * speed
	y = y + ydir * speed
	return [x, y, radius, xdir, ydir]

def balls_collide(ball1, ball2):
	if ( abs(palgame.get_x(ball2) - palgame.get_x(ball1)) < (palgame.get_radius(ball2) + palgame.get_radius(ball1))
		and abs(palgame.get_y(ball2) - palgame.get_y(ball1)) < (palgame.get_radius(ball2) + palgame.get_radius(ball1)) ):
		return True
	else:
		return False

while True:
	palgame.get_event()
	for a in range(NUM_BALLS):
		ball = balls[a]
		speed = palgame.get_speed(palgame.get_radius(ball))
		if a == 0:
			vx, vy = palgame.get_user_direction(palgame.get_x(ball), palgame.get_y(ball), palgame.get_radius(ball))
			new_x = palgame.get_x(ball) + vx
			palgame.set_x(ball, new_x)
			new_y = palgame.get_y(ball) + vy
			palgame.set_y(ball, new_y)
		else:
			ball = update_ball_position(ball, speed)

		for f in range(NUM_FOOD):
			nom = food[f]
			if balls_collide(ball, nom):
				new_radius = palgame.get_radius(ball) + (1 - palgame.get_radius(ball) / 100)
				palgame.set_radius(ball, new_radius)
				food[f] = palgame.get_random_food()

		for b in range(NUM_BALLS):
			other_ball = balls[b]
			if a != b and balls_collide(ball, other_ball):
				radius = palgame.get_radius(ball)
				if radius >= palgame.get_radius(other_ball):
					new_radius = radius + (1 - radius / 100)
					palgame.set_radius(ball, new_radius)
					balls[b] = palgame.get_random_ball()

		balls[a] = ball
	palgame.clear_screen()
	for f in food:
		palgame.draw_circle(palgame.get_x(f), palgame.get_y(f), palgame.get_radius(f), BLUE)
	for i, b in enumerate(balls):
		if i == 0:
			color = GREEN
		else:
			color = RED
		palgame.draw_circle(palgame.get_x(b), palgame.get_y(b), palgame.get_radius(b), color)

	palgame.draw_everything()
