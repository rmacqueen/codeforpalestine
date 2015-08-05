import palgame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

palgame.build_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

palgame.draw_circle(x, y, 10)
