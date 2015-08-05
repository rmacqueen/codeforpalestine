import palgame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

palgame.build_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

xdir = 1
ydir = 1

while True:
	palgame.get_event()
	palgame.clear_screen()
	palgame.draw_circle(x, y, 10)
	if x > SCREEN_WIDTH:
		xdir = -1
	if x < 0:
		xdir = 1
	if y > SCREEN_HEIGHT:
		ydir = -1
	if y < 0:
		ydir = 1
	x = x + xdir * 10
	y = y + ydir * 10
