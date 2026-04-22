import pygame
import random

#Create sprite classes


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos,y_pos):
        pygame.sprite.Sprite.__init__(self) #inheritate sprite atributes
        self.image = pygame.image.load('Practices/Practice10/racer/img/player_car.png')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos,y_pos)

    def move(self,event):
        if event.key == pygame.K_d:
            self.rect.x += 25
        elif event.key == pygame.K_a:
            self.rect.x -= 25

    def check_collisions(self, objects):
        return pygame.sprite.spritecollide(self, objects, False)  #spritecollide function that returns true or false     this is reason why i use separate groups instead of putting them all in one
    
    def check_collisions_coin(self, coin_group):
        return pygame.sprite.spritecollide(self, coin_group, True) #True means coin dissapers after collision
    

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Practices/Practice10/racer/img/enemy_car.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100,400),0)

    def update(self):
        self.rect.y += 6

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Practices/Practice10/racer/img/coin.png')
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100,400),0)

    def update(self): #overwrite innate function which does nothing
        self.rect.y +=5
        

