import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
	def __init__(self):
		self.randomize()

	def draw_fruit(self):
		fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		pygame.draw.rect(screen,(pygame.Color("yellow")),fruit_rect)

	def randomize(self):
		self.x = random.randint(0,cell_number - 1)
		self.y = random.randint(0,cell_number - 1)
		self.pos = Vector2(self.x,self.y)



pygame.init()
# create a grid (the illusion of a grid actually)
cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(50, 168, 151))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)



pygame.quit()
sys.exit()
