import pygame
import random

cell_size = 30
screen = pygame.display.set_mode((750, 750))

class Food:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.weight = 1
        self.spawn_time = 0
        self.lifetime = 5000 # Food disappears after 5 seconds (5000ms)
        self.new_food()

    def draw(self):
        # Draw different colors based on weight (Green is worth more)
        color = "Red" if self.weight == 1 else "Green"
        food_rect = pygame.Rect(self.pos_x * cell_size, self.pos_y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, color, food_rect)

    def random_pos(self):
        self.pos_x = random.randint(0, 24)
        self.pos_y = random.randint(0, 24)
        # Random weight: 80% chance for 1, 20% chance for 3
        self.weight = random.choices([1, 3], weights=[80, 20])[0]
        # Record the time when food was created
        self.spawn_time = pygame.time.get_ticks()

    def new_food(self):
        self.random_pos()

class Snake:
    def __init__(self, x, y):
        self.body = [[x, y], [x-1, y], [x-2, y]]
        self.direction = [1, 0]

    def draw(self):
        for i in self.body:
            i_rect = (i[0] * cell_size, i[1] * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 255, 255), i_rect)

    def update(self):
        # Movement logic: move the head, and the body follows
        self.body = self.body[:-1]
        new_x = self.body[0][0] + self.direction[0]
        new_y = self.body[0][1] + self.direction[1]
        self.body.insert(0, [new_x, new_y])