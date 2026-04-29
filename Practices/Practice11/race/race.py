import pygame
import random

# Create sprite classes
class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        # Using relative paths is recommended for portability
        self.image = pygame.image.load('C:\TT\Python\Practices\Tsis3\img\player_car.png')
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)

    def move(self): 
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_d] and self.rect.right < 425:
            self.rect.x += 7 
        if keys[pygame.K_a] and self.rect.left > 75:
            self.rect.x -= 7

    def check_collisions(self, objects):
        return pygame.sprite.spritecollide(self, objects, False)
    
    def check_collisions_coin(self, coin_group):
        # Returns a list of all coins collided with
        return pygame.sprite.spritecollide(self, coin_group, True)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\TT\Python\Practices\Tsis3\img\enemy_car.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, 400), -100)
        self.speed = speed # Store dynamic speed

    def update(self):
        self.rect.y += self.speed
        # Remove enemy if it goes off screen to save memory
        if self.rect.top > 900:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Randomly assign a weight (1, 2, or 3)
        self.weight = random.choice([1, 2, 3])
        self.image = pygame.image.load('C:\TT\Python\Practices\Tsis3\img\coin.png')
        
        # Scale size based on weight (heavier coins are larger)
        size = 20 + (self.weight * 15) 
        self.image = pygame.transform.scale(self.image, (size, size))
        
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, 400), -50)

    def update(self):
        self.rect.y += 5
        if self.rect.top > 900:
            self.kill()