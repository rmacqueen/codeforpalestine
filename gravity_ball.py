import palgame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

palgame.build_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

x = SCREEN_WIDTH / 2
y = 0

vx = 1
vy = 0

while True:
	palgame.get_event()
	palgame.clear_screen()
	palgame.draw_circle(x, int(y), 10)
	vy = vy + (2.8 / 2)
	if x > SCREEN_WIDTH:
		vx = -1 * vx
	if x < 0:
		vx = -1 * vx
	if y > SCREEN_HEIGHT:
		vy = -0.8 * vy
	if y < 0:
		vy = -1 * vy
	x = x + vx
	y = y + vy
