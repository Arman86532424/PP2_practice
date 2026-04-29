import sys
import pygame
import random
from race import Player, Enemy, Coin

def show_score(score, num):
    score_surf = font.render(f"Score: {score}  Avoided Enemy: {num}", True, (255, 255, 255))
    score_rect = score_surf.get_rect(center=(250, 50))
    screen.blit(score_surf, score_rect)

pygame.init()

Screen_W = 500
Screen_H = 900
screen = pygame.display.set_mode((Screen_W, Screen_H))

# Ensure these paths match your local folder structure
road_surf = pygame.image.load('C:/TT/Python/Practices/Tsis3/img/road.webp').convert_alpha()
clock = pygame.time.Clock()

objects = pygame.sprite.Group()
player_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

player = Player(250, 850)
player_group.add(player)

score = 0
coins_collected_count = 0
ENEMY_SPEED = 5
SPEED_INCREMENT_THRESHOLD = 5 # This is 'N'
font = pygame.font.Font(None, 40)

# Timers
SPAWN_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ENEMY, 2000)

SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 3000)

num = 0

ENEMY_COUNT = pygame.USEREVENT + 3
pygame.time.set_timer(ENEMY_COUNT, 2000 + 60 * ENEMY_SPEED)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SPAWN_ENEMY:
            new_enemy = Enemy(ENEMY_SPEED)
            objects.add(new_enemy)

        if event.type == SPAWN_COIN:
            new_coin = Coin()
            coin_group.add(new_coin)

        if event.type == ENEMY_COUNT:
            num += 1

    player.move()

    # Collision Logic
    if player.check_collisions(objects):
        pygame.quit()
        sys.exit()

    # Handle Coin collection with different weights
    coins_hit = player.check_collisions_coin(coin_group)
    for coin in coins_hit:
        score += coin.weight
        coins_collected_count += 1
        
        # Increase speed every N coins earned
        if coins_collected_count % SPEED_INCREMENT_THRESHOLD == 0:
            ENEMY_SPEED += 1
            # Optional: increase existing enemies' speed too
            for enemy in objects:
                enemy.speed = ENEMY_SPEED

    # Drawing
    screen.fill((0, 130, 0))
    screen.blit(road_surf, (75, 0))

    objects.update()
    objects.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    player_group.draw(screen)

    


    
    show_score(score, num - 1)

    pygame.display.update()
    clock.tick(60)