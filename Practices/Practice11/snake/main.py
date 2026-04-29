import pygame
import sys
from snake import Food, Snake

def show_score(score, level):
    score_surf = font.render(f"Score: {score} Level: {level}", False, (255, 255, 255))
    score_rect = score_surf.get_rect(center=(375, 50))
    screen.blit(score_surf, score_rect)

pygame.init()
font = pygame.font.Font(None, 40)

cell_size = 30 
number_of_cells = 25        
Screen_w = cell_size * number_of_cells        
Screen_h = cell_size * number_of_cells

screen = pygame.display.set_mode((Screen_w, Screen_h))
clock = pygame.time.Clock()

f = Food() # Initialize food
s = Snake(12, 12)

score = 0
level = 1

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200) # Initial speed

while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SNAKE_UPDATE:
            s.update()
        if event.type == pygame.KEYDOWN:
            # Control logic with 180-degree turn prevention
            if event.key == pygame.K_w and s.direction != [0, 1]:
                s.direction = [0, -1]
            if event.key == pygame.K_s and s.direction != [0, -1]:
                s.direction = [1, 0] # Wait, correction: should be [0, 1]
                s.direction = [0, 1]
            if event.key == pygame.K_a and s.direction != [1, 0]:
                s.direction = [-1, 0]
            if event.key == pygame.K_d and s.direction != [-1, 0]:
                s.direction = [1, 0]

    # TASK: Disappearing food logic
    # If the current time minus the spawn time is greater than lifetime, reset food
    if current_time - f.spawn_time > f.lifetime:
        f.new_food()

    # Collision with food
    if s.body[0] == [f.pos_x, f.pos_y]:
        # TASK: Add weight to score instead of just +1
        score += f.weight 
        f.new_food()
        
        # Grow the snake
        s.body.append(list(s.body[-1])) 
        
        # Level up logic every 5 points
        if score // 5 >= level:
            level += 1
            # Increase speed by reducing the timer interval
            new_speed = max(50, 200 - (level * 20)) 
            pygame.time.set_timer(SNAKE_UPDATE, new_speed)

    # Wall and Self Collision
    if (s.body[0] in s.body[1:] or 
        not (0 <= s.body[0][0] < number_of_cells) or 
        not (0 <= s.body[0][1] < number_of_cells)):
        pygame.quit()
        sys.exit()
    
    screen.fill("Black")
    f.draw()
    s.draw()
    show_score(score, level)

    pygame.display.update()
    clock.tick(60)