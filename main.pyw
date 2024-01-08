# all static files (sprites) must be in the same path as main.pyw for proper working
# importing modules
import pygame
import random
import sys

# importing sub-modules
from random import randint

# initializing modules
pygame.init()
pygame.mixer.init()

# game settings
# game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hit"

FPS = 60
SPEED = 12

# rgb color tuples
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ALPHA = GREEN

# game variables
health_value = 4

__version__ = "v0.1"

running = True
debugging = True

# setting up screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TITLE = pygame.display.set_caption(f"{SCREEN_TITLE} {__version__}")
MOUSE_VISIBILITY = pygame.mouse.set_visible(False)

# game classes
# class player
class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x=375, pos_y=275):
		super().__init__()
		self.image = pygame.image.load("player.png").convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	def update(self):
		# player movement
		self.rect.x = pygame.mouse.get_pos()[0]
		self.rect.y = 551

# class z(hit)os
class Hit(pygame.sprite.Sprite):
	def __init__(self, pos_x=random.randint(0, SCREEN_WIDTH - 20), pos_y=-20):
		super().__init__()
		self.image = pygame.image.load("hit.png").convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	def update(self):
		# hit movement
		self.rect.y += SPEED
		if self.rect.y >= SCREEN_HEIGHT:
			self.rect.x = random.randint(0, SCREEN_WIDTH - 10)
			self.rect.y = -20

class Crossover(pygame.sprite.Sprite):
	def __init__(self, pos_x=0, pos_y=0):
		super().__init__()
		self.image = pygame.image.load("crossover.png").convert()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect(center = [pos_x, pos_y])

	# player movement
	def update(self):
		self.rect.x = pygame.mouse.get_pos()[0] + 26
		self.rect.y = pygame.mouse.get_pos()[1] + 26

# game functions
# exit game function
def exit():
	pygame.quit()
	sys.exit()
	running = False

# creating sprite groups
# player sprite group
player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)

# hit sprite group
hit_group = pygame.sprite.Group()
hit = Hit()
hit_group.add(hit)

crossover_group = pygame.sprite.Group()
crossover = Crossover()
crossover_group.add(crossover)

# loading health image
h = pygame.image.load("hit.png").convert()
h.set_colorkey(ALPHA)

# main game loop
while running:
	# if key pressed statements
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	# checking collisions
	if pygame.sprite.groupcollide(player_group, hit_group, False, True):
		hit_group = pygame.sprite.Group()
		hit = Hit(pos_x=random.randint(0, SCREEN_WIDTH))
		hit_group.add(hit)

	# drawing screen, etc...
	SCREEN.fill(WHITE)

	# game over mechanic
	if hit.rect.y > (SCREEN_HEIGHT - 20):
		health_value -= 1

	if health_value >= 3:
		SCREEN.blit(h, (10, 10))
		SCREEN.blit(h, (25, 10))
		SCREEN.blit(h, (40, 10))

	if health_value == 2:
		SCREEN.blit(h, (10, 10))
		SCREEN.blit(h, (25, 10))

	if health_value == 1:
		SCREEN.blit(h, (10, 10))

	if health_value < 0:
		exit()

	# drawing sprites on the screen
	hit_group.update()
	hit_group.draw(SCREEN)

	player_group.update()
	player_group.draw(SCREEN)

	crossover_group.update()
	crossover_group.draw(SCREEN)

	# fps counter
	pygame.display.flip()
	pygame.time.Clock().tick(FPS)
