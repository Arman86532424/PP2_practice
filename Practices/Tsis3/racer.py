import pygame
import random

# Constants for easy adjustment
LANE_LEFT = 75
LANE_RIGHT = 425

class Player(pygame.sprite.Sprite):
    def __init__(self, color="blue"):
        super().__init__()
        # Try to load colored version, fallback to default
        
        path = f'Practices/Tsis3/accets/player_car_{color}.png'
        self.image = pygame.image.load(path).convert_alpha()
        
            
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect(center=(250, 800))
        self.speed = 7
        self.shielded = False
        self.nitro_timer = 0

    

    def move(self):
        keys = pygame.key.get_pressed()
        current_speed = self.speed * 2 if self.nitro_timer > 0 else self.speed
        if keys[pygame.K_a] and self.rect.left > LANE_LEFT:
            self.rect.x -= current_speed
        if keys[pygame.K_d] and self.rect.right < LANE_RIGHT:
            self.rect.x += current_speed
        
        if self.nitro_timer > 0:
            self.nitro_timer -= 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.image.load('Practices/Tsis3/accets/enemy_car.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect(center=(random.randint(100, 400), -100))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 900:
            self.kill()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
    
        obs_type = random.choice(['oil.png', 'barrier.png'])
        self.image = pygame.image.load(f'Practices/Tsis3/accets/{obs_type}').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(center=(random.randint(100, 400), -100))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed #Practices\Tsis3\accets\oil.png
        if self.rect.top > 900:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.type = random.choice(['nitro', 'shield', 'repair'])
        # Load image based on the random type (nitro.png, shield.png, repair.png)
        self.image = pygame.image.load(f'Practices/Tsis3/accets/{self.type}.png').convert_alpha()          #Practices\Tsis3\accets\nitro.png
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(random.randint(100, 400), -100))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 900:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        # Load your coin image
        self.image = pygame.image.load('C:/TT/Python/Practices/Tsis3/accets/coin.png').convert_alpha()
        
        self.weight = random.choice([1, 2, 3]) #randon wieght fot coins
        
        size = 20 + (self.weight * 10)                           #make coins bigger based on size
        self.image = pygame.transform.scale(self.image, (size, size))    
        
        self.rect = self.image.get_rect(center=(random.randint(100, 400), -50))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 900:
            self.kill()