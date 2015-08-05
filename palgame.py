import pygame, sys
BALL_COLOR = (255, 0, 0)
SCREEN_COLOR = (100, 100, 100)

pygame.init()
clock = pygame.time.Clock()
screen = None

def build_screen(width, height):
	global screen
	screen = pygame.display.set_mode((width, height))

def draw_circle(x, y, radius):
	pygame.draw.circle(screen, BALL_COLOR, (x, y), radius)
	pygame.display.flip()

def draw_rect(x, y, width, height):
	pygame.draw.rect(screen, BALL_COLOR, (x, y, width, height), 0)
	pygame.display.flip()

def clear_screen():
	screen.fill(SCREEN_COLOR)

def get_event():
	clock.tick(20)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit(0)
