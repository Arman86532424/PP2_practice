import pygame
from ball import Ball

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

clock = pygame.time.Clock()


ball = Ball(WIDTH // 2, HEIGHT // 2, 25, WIDTH, HEIGHT)

running = True

while running:
    screen.fill((255, 255, 255))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ball.move(0, -ball.speed)
            elif event.key == pygame.K_s:
                ball.move(0, ball.speed)
            elif event.key == pygame.K_a:
                ball.move(-ball.speed, 0)
            elif event.key == pygame.K_d:
                ball.move(ball.speed, 0)

    ball.draw(screen)

    pygame.display.update()
    clock.tick(60)  

pygame.quit()