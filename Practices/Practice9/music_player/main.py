import pygame
from player import MusicPlayer

pygame.init()


WIDTH, HEIGHT = 1400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")


font = pygame.font.Font(None, 36)


player = MusicPlayer("music")

clock = pygame.time.Clock()
running = True

def draw():
    screen.fill((0, 0, 0))

    track_text = font.render(f"Track: {player.get_current_track()}", True, (255, 255, 255))
    screen.blit(track_text, (20, 50))

    status = "Playing" if player.is_playing else "Stopped"
    status_text = font.render(f"Status: {status}", True, (200, 200, 200))
    screen.blit(status_text, (20, 100))

    position = player.get_position()
    pos_text = font.render(f"Time: {position}s", True, (200, 200, 200))
    screen.blit(pos_text, (20, 150))

    controls = font.render("P S N B Q", True, (150, 150, 150))
    screen.blit(controls, (20, 220))

    pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.previous_track()
            elif event.key == pygame.K_q:
                running = False

    draw()
    clock.tick(60)

pygame.quit()