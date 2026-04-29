import pygame
import random

class Food:
    def __init__(self, cells):
        self.cells = cells
        self.pos = [0, 0]
        self.weight = 1
        self.spawn_time = 0
        self.lifetime = 5000
        self.new_food([])

    def draw(self, screen, size):
        color = (255, 0, 0) if self.weight == 1 else (0, 0, 255)
        pygame.draw.rect(screen, color, (self.pos[0]*size, self.pos[1]*size, size, size))

    def new_food(self, bad_pos):
        while True:
            self.pos = [random.randint(0, self.cells-1), random.randint(0, self.cells-1)]
            if self.pos not in bad_pos: break
        self.weight = random.choices([1, 3], weights=[80, 20])[0]
        self.spawn_time = pygame.time.get_ticks()

class PoisonFood:
    def __init__(self, cells):
        self.cells = cells
        self.pos = [0, 0]
        self.spawn_time = 0
        self.lifetime = 7000
        self.new_poison([])

    def draw(self, screen, size):
        pygame.draw.rect(screen, (139, 0, 0), (self.pos[0]*size, self.pos[1]*size, size, size))

    def new_poison(self, bad_pos):
        while True:
            self.pos = [random.randint(0, self.cells-1), random.randint(0, self.cells-1)]
            if self.pos not in bad_pos: break
        self.spawn_time = pygame.time.get_ticks()

class PowerUp:
    def __init__(self, cells):
        self.cells = cells
        self.pos = [0, 0]
        self.type = None # SPEED, SLOW, SHIELD
        self.active = False
        self.spawn_time = 0
        self.lifetime = 8000

    def spawn(self, bad_pos):
        while True:
            self.pos = [random.randint(0, self.cells-1), random.randint(0, self.cells-1)]
            if self.pos not in bad_pos: break
        self.type = random.choice(["SPEED", "SLOW", "SHIELD"])
        self.active = True
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, screen, size):
        if not self.active: return
        colors = {"SPEED": (255, 215, 0), "SLOW": (128, 0, 128), "SHIELD": (0, 255, 255)}
        pygame.draw.circle(screen, colors[self.type], (self.pos[0]*size + size//2, self.pos[1]*size + size//2), size//2)

class Obstacle:
    def __init__(self, cells, bad_pos):
        self.cells = cells
        self.blocks = []
        while len(self.blocks) < 8:
            pos = [random.randint(0, self.cells-1), random.randint(0, self.cells-1)]
            if pos not in bad_pos: self.blocks.append(pos)

    def draw(self, screen, size):
        for b in self.blocks:
            pygame.draw.rect(screen, (100, 100, 100), (b[0]*size, b[1]*size, size, size))

class Snake:
    def __init__(self, x, y):
        self.body = [[x, y], [x-1, y], [x-2, y]]
        self.direction = [1, 0]

    def draw(self, screen, size, color):
        for part in self.body:
            pygame.draw.rect(screen, color, (part[0]*size, part[1]*size, size, size))

    def update(self):
        new_head = [self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]]
        self.body.insert(0, new_head)
        self.body.pop()