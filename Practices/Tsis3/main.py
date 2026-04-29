import pygame
import sys
import random
from racer import Player, Enemy, Obstacle, Coin, PowerUp
from ui import draw_text, Button, get_username
from persistence import load_leaderboard, save_score, load_settings, save_settings

def show_leaderboard(screen):
    """Retrieves and displays the top 10 scores."""
    scores = load_leaderboard()                         #here i take data from persisatnce file
    back_btn = Button("Back", 250, 850, 200, 50, (100, 0, 0), (200, 0, 0))

    while True:
        screen.fill((20, 20, 20))
        draw_text(screen, "TOP 10 SCORES", 50, 250, 80, (255, 215, 0))
        
        
        draw_text(screen, "NAME", 30, 100, 150, (150, 150, 150))              #general info about run
        draw_text(screen, "SCORE", 30, 250, 150, (150, 150, 150))
        draw_text(screen, "DIST", 30, 400, 150, (150, 150, 150))

        # Render each score entry
        for i, entry in enumerate(scores):
            y_pos = 200 + (i * 45)
            draw_text(screen, f"{i+1}. {entry['name']}", 25, 100, y_pos)
            draw_text(screen, str(entry['score']), 25, 250, y_pos)
            draw_text(screen, f"{entry['distance']}m", 25, 400, y_pos)

        back_btn.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if back_btn.is_clicked(event):
                return # Exit back to main_menu


pygame.init()


pygame.mixer.init()


pygame.mixer.music.load('Practices/Tsis3/accets/ost.mp3')          #my background music
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) # basicalily mean forever


crash_sound = pygame.mixer.Sound('Practices/Tsis3/accets/crush.mp3')
coin_sound = pygame.mixer.Sound('Practices/Tsis3/accets/coin.mp3')


screen = pygame.display.set_mode((500, 900))

CLOCK = pygame.time.Clock()
FINISH_DISTANCE = 5000 

def show_settings(screen):                  #showing settings screen where you can choose color and difficulty
    settings = load_settings()
    back_btn = Button("Save & Back", 250, 800, 250, 50, (0, 100, 0), (0, 200, 0))
    
    # Selection buttons
    sound_btn = Button(f"Sound: {'ON' if settings['sound'] else 'OFF'}", 250, 300, 300, 50, (50, 50, 50), (100, 100, 100))
    color_btn = Button(f"Color: {settings['car_color'].upper()}", 250, 400, 300, 50, (50, 50, 50), (100, 100, 100))
    diff_btn = Button(f"Difficulty: {settings['difficulty']}", 250, 500, 300, 50, (50, 50, 50), (100, 100, 100))

    colors = ["red", "blue", "green"]
    difficulties = ["Easy", "Medium", "Hard"]

    while True:
        screen.fill((20, 20, 20))
        draw_text(screen, "SETTINGS", 60, 250, 100, (255, 215, 0))

        sound_btn.draw(screen)
        color_btn.draw(screen)
        diff_btn.draw(screen)
        back_btn.draw(screen)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            if sound_btn.is_clicked(event):
                settings['sound'] = not settings['sound']
                sound_btn.text = f"Sound: {'ON' if settings['sound'] else 'OFF'}"
    
                                     
                if settings['sound']:                   # Apply change immediately
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            
            if color_btn.is_clicked(event):
                idx = (colors.index(settings['car_color']) + 1) % len(colors)
                settings['car_color'] = colors[idx]
                color_btn.text = f"Color: {settings['car_color'].upper()}"
            
            if diff_btn.is_clicked(event):
                idx = (difficulties.index(settings['difficulty']) + 1) % len(difficulties)
                settings['difficulty'] = difficulties[idx]
                diff_btn.text = f"Difficulty: {settings['difficulty']}"

            if back_btn.is_clicked(event):
                save_settings(settings)
                return

def show_game_over(screen, score, distance, win=False):                #thing to display the final results
    title = "YOU WIN!" if win else "GAME OVER"
    color = (0, 255, 0) if win else (255, 0, 0)
    
    retry_btn = Button("Play Again", 250, 600, 200, 50, (0, 100, 0), (0, 200, 0))
    menu_btn = Button("Main Menu", 250, 700, 200, 50, (0, 0, 100), (0, 0, 200))

    while True:
        screen.fill((10, 10, 10))
        draw_text(screen, title, 70, 250, 200, color)
        draw_text(screen, f"Final Score: {score}", 40, 250, 350)
        draw_text(screen, f"Distance: {int(distance)}m", 40, 250, 420)

        retry_btn.draw(screen)
        menu_btn.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if retry_btn.is_clicked(event):
                return "PLAY"
            if menu_btn.is_clicked(event):
                return "MENU"

def game_loop(username):
    settings = load_settings()
    if settings['sound']:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()
    # Adjust starting speed based on difficulty
    diff_speeds = {"Easy": 3, "Medium": 5, "Hard": 8}
    enemy_speed = diff_speeds.get(settings['difficulty'], 5)
    
    player = Player(color=settings['car_color'])
    enemies = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)

    score = 0
    distance = 0
    active_powerup = None

    road_surf = pygame.image.load('Practices/Tsis3/accets/road.webp').convert() 
    road_surf = pygame.transform.scale(road_surf, (350, 900))

    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 1500)

    running = True
    while running:
        dt = CLOCK.tick(60)
        distance += enemy_speed * 0.1 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            if event.type == SPAWN_EVENT:
                enemy_speed += 0.05
                new_timer = max(400, 1500 - int(distance / 5))
                pygame.time.set_timer(SPAWN_EVENT, new_timer)
                
                obj_type = random.choices(['enemy', 'obstacle', 'coin', 'powerup'], [0.4, 0.2, 0.3, 0.1])[0]       #chose with random chances
                new_obj = None
                
                if obj_type == 'enemy': 
                    new_obj = Enemy(enemy_speed)
                elif obj_type == 'obstacle': 
                    new_obj = Obstacle(enemy_speed)
                elif obj_type == 'coin': 
                    new_obj = Coin(enemy_speed)
                elif obj_type == 'powerup': 
                    new_obj = PowerUp(enemy_speed)
                
                if new_obj:
                    if not new_obj.rect.colliderect(player.rect.inflate(0, 600)):
                        if obj_type == 'enemy': 
                            enemies.add(new_obj)
                        elif obj_type == 'obstacle': 
                            obstacles.add(new_obj)
                        elif obj_type == 'coin':
                            coins.add(new_obj)
                        else: 
                            powerups.add(new_obj)
                        all_sprites.add(new_obj)

        player.move()
        all_sprites.update()

        
        hit_hazard = pygame.sprite.spritecollide(player, enemies, True) or pygame.sprite.spritecollide(player, obstacles, True) #collision with hazzards
        
        if hit_hazard:
            if player.shielded:
                player.shielded = False      #checks for shield
                active_powerup = None
            else:
                if settings.get('sound', True):
                    crash_sound.play()
                    pygame.mixer.music.stop()
                
                save_score(username, score, distance)
                return show_game_over(screen, score, distance, win=False)

        
        for p in pygame.sprite.spritecollide(player, powerups, True):       #collition with items
            active_powerup = p.type
            if p.type == 'nitro': player.nitro_timer = 300 
            elif p.type == 'shield': player.shielded = True
            elif p.type == 'repair': score += 50 

        for coin in pygame.sprite.spritecollide(player, coins, True):
            if settings.get('sound', True):
                coin_sound.play()
            score += coin.weight * 10

        
        screen.fill((0, 120, 0))
        screen.blit(road_surf, (75, 0)) 
        all_sprites.draw(screen)

        if player.shielded:
            pygame.draw.rect(screen, (0, 255, 255), player.rect.inflate(10, 10), 3)     #make shild visible
        
        draw_text(screen, f"Score: {score}", 30, 250, 30)
        draw_text(screen, f"Dist: {int(distance)} / {FINISH_DISTANCE}", 25, 250, 60)
        
        if distance >= FINISH_DISTANCE:
            save_score(username, score, distance)
            return show_game_over(screen, score, distance, win=True)    #finish the game when disyance over 5000
                                                                        #added because it was in a guide
        pygame.display.flip()

def main_menu():
    user = get_username(screen)
    
    play_btn = Button("Play", 250, 300, 200, 50, (0, 100, 0), (0, 200, 0))
    leader_btn = Button("Leaderboard", 250, 400, 200, 50, (0, 0, 100), (0, 0, 200))
    settings_btn = Button("Settings", 250, 500, 200, 50, (50, 50, 50), (100, 100, 100))
    quit_btn = Button("Quit", 250, 600, 200, 50, (100, 0, 0), (200, 0, 0))

    while True:
        screen.fill((20, 20, 20))
        draw_text(screen, "STREET RACER", 60, 250, 100, (255, 215, 0))
        draw_text(screen, f"Player: {user}", 30, 250, 180)
        
        play_btn.draw(screen)
        leader_btn.draw(screen)
        settings_btn.draw(screen)
        quit_btn.draw(screen)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            if play_btn.is_clicked(event):
                result = game_loop(user)
                while result == "PLAY": # Handle "Play Again" loop
                    result = game_loop(user)
            
            if leader_btn.is_clicked(event):
                show_leaderboard(screen) 
            
            if settings_btn.is_clicked(event):
                show_settings(screen)
                
            if quit_btn.is_clicked(event):
                pygame.quit(); sys.exit()

main_menu()