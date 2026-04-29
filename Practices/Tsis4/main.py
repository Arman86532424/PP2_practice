import pygame, sys, json,random
from snake import Food, Snake, PoisonFood, Obstacle, PowerUp
import db


def load_settings():            #func for settings
    try:
        with open('settings.json', 'r') as f: return json.load(f)
    except: return {"snake_color": [0, 255, 0], "grid_on": True, "sound_on": True}

def save_settings(data):
    with open('settings.json', 'w') as f: json.dump(data, f, indent=4)

pygame.init()
settings = load_settings()
SIZE, CELLS = 30, 25
screen = pygame.display.set_mode((SIZE*CELLS, SIZE*CELLS))
clock, font = pygame.time.Clock(), pygame.font.Font(None, 40)

#inisial variables
state = "MENU"
user_input = ""
score, level, pb = 0, 1, 0
has_shield, effect_start = False, 0
cur_speed = 200


def start_game():
    global s, f, p, pw, obs, score, level, has_shield, state
    s = Snake(12, 12)
    f, p, pw = Food(CELLS), PoisonFood(CELLS), PowerUp(CELLS)
    obs = None
    score, level, has_shield = 0, 1, False
    state = "PLAYING"

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, cur_speed)         #to make snake move slower than fps

def draw_btn(text, x, y, w, h, color):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, border_radius=10)
    txt = font.render(text, True, "White")
    screen.blit(txt, (x + (w - txt.get_width())//2, y + (h - txt.get_height())//2))
    return rect

while True:
    now = pygame.time.get_ticks()
    m_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        
        if state == "MENU":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: user_input = user_input[:-1]
                else: user_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_play.collidepoint(m_pos) and user_input:
                    try: pb = db.get_personal_best(user_input)
                    except: pb = 0
                    start_game()
                if b_lead.collidepoint(m_pos): state = "LEADERBOARD"
                if b_sett.collidepoint(m_pos): state = "SETTINGS"

        elif state == "PLAYING":
            if event.type == SNAKE_UPDATE: s.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and s.direction != [0, 1]: s.direction = [0, -1]
                if event.key == pygame.K_s and s.direction != [0, -1]: s.direction = [0, 1]
                if event.key == pygame.K_a and s.direction != [1, 0]: s.direction = [-1, 0]
                if event.key == pygame.K_d and s.direction != [-1, 0]: s.direction = [1, 0]
        
        elif state in ["LEADERBOARD", "SETTINGS", "GAMEOVER"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == "SETTINGS":
                    if b_grid.collidepoint(m_pos): settings['grid_on'] = not settings['grid_on']
                    if b_color.collidepoint(m_pos): settings['snake_color'] = [random.randint(0,255) for _ in range(3)]
                if b_back.collidepoint(m_pos): save_settings(settings); state = "MENU"

    screen.fill((20, 20, 20))

    if state == "MENU":
        screen.blit(font.render(f"Name: {user_input}_", True, "Yellow"), (250, 150))
        b_play = draw_btn("PLAY", 275, 250, 200, 50, (0, 150, 0))
        b_lead = draw_btn("LEADERBOARD", 275, 320, 200, 50, (0, 0, 150))
        b_sett = draw_btn("SETTINGS", 275, 390, 200, 50, (100, 100, 100))

    elif state == "PLAYING":
        bad = s.body + [f.pos] + (obs.blocks if obs else [])
        if level >= 2 and obs is None: obs = Obstacle(CELLS, bad)
        if now - f.spawn_time > f.lifetime: f.new_food(bad)
        if now - p.spawn_time > p.lifetime: p.new_poison(bad)
        if not pw.active and random.randint(0, 500) == 1: pw.spawn(bad)
        if pw.active and now - pw.spawn_time > pw.lifetime: pw.active = False

        if s.body[0] == f.pos:
            score += f.weight; s.body.append(list(s.body[-1])); f.new_food(bad)
            if score // 5 >= level:
                level += 1; cur_speed = max(50, 200 - (level*20))
                pygame.time.set_timer(SNAKE_UPDATE, cur_speed)

        if pw.active and s.body[0] == pw.pos:
            pw.active = False; effect_start = now
            if pw.type == "SPEED": pygame.time.set_timer(SNAKE_UPDATE, 80)
            elif pw.type == "SLOW": pygame.time.set_timer(SNAKE_UPDATE, 350)
            elif pw.type == "SHIELD": has_shield = True

        if effect_start and now - effect_start > 5000:
            pygame.time.set_timer(SNAKE_UPDATE, cur_speed); effect_start = 0

        if s.body[0] == p.pos:
            s.body = s.body[:-2]
            if len(s.body) <= 1: state = "GAMEOVER"; db.save_game_result(user_input, score, level)
            p.new_poison(bad)

        head = s.body[0]
        hit = head in s.body[1:] or not (0<=head[0]<CELLS and 0<=head[1]<CELLS) or (obs and head in obs.blocks)
        if hit:
            if has_shield: has_shield = False
            else: state = "GAMEOVER"; db.save_game_result(user_input, score, level)

        if settings['grid_on']:
            for x in range(0, SIZE*CELLS, SIZE): pygame.draw.line(screen, (40,40,40), (x,0), (x,SIZE*CELLS))
        f.draw(screen, SIZE); p.draw(screen, SIZE); pw.draw(screen, SIZE)
        if obs: obs.draw(screen, SIZE)
        s.draw(screen, SIZE, settings['snake_color'])
        screen.blit(font.render(f"Score: {score} Lvl: {level} PB: {pb}", True, "White"), (10, 10))

    elif state == "SETTINGS":
        b_grid = draw_btn(f"Grid: {'ON' if settings['grid_on'] else 'OFF'}", 225, 200, 300, 50, (50, 50, 50))
        b_color = draw_btn("Change Color", 225, 280, 300, 50, settings['snake_color'])
        b_back = draw_btn("BACK", 225, 400, 300, 50, (150, 0, 0))

    elif state == "LEADERBOARD":
        data = db.get_leaderboard()
        for i, r in enumerate(data):
            screen.blit(font.render(f"{i+1}. {r[0]} - {r[1]} (Lvl {r[2]})", True, "White"), (200, 100+i*40))
        b_back = draw_btn("BACK", 275, 600, 200, 50, (150, 0, 0))

    elif state == "GAMEOVER":
        screen.blit(font.render("GAME OVER", True, "Red"), (290, 200))
        screen.blit(font.render(f"Score: {score} | Level: {level}", True, "White"), (250, 260))
        b_back = draw_btn("MAIN MENU", 275, 350, 200, 50, (0, 100, 200))

    pygame.display.update()
    clock.tick(60)