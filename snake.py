import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(1,0)
    
    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, pygame.Color("blue"),block_rect)
    
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy
    
    def add_block(self):
        self.body.insert(0, self.body[0] + self.direction)

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

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.eat_fruit()
        self.collision()
    
    def draw_objects(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def eat_fruit(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()  # reposition the fruit
            self.snake.add_block()  # add another block to the snake
    
    def collision(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:  # snake hits the wall
            self.game_over()

        for block in self.snake.body[1:]:    # snake hits itself
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        print("GAME OVER")
        pygame.quit()
        sys.exit()

pygame.init()
# create a grid (the illusion of a grid actually)
cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

game = MAIN()

SCREENUPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREENUPDATE, 150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREENUPDATE:
            game.update() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)
            elif event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)


    screen.fill(pygame.Color(50, 168, 151))
    game.draw_objects()
    pygame.display.update()
    clock.tick(60)

