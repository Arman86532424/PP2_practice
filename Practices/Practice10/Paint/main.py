import pygame
import sys

pygame.init()

Screen_w = 900
Screen_h = 900

active_size = 10
active_color = (0, 0, 0)
active_shape = "circle"                   #initial values

painting = []

drawing_rect = False
rect_start = (0, 0)

screen = pygame.display.set_mode((Screen_w, Screen_h))
clock = pygame.time.Clock()


def draw_menu():
    pygame.draw.rect(screen, 'grey', [0, 0, Screen_w, 70])
    pygame.draw.line(screen, "black", (0, 70), (Screen_w, 70), 3)

    
    Super_large_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)

    Large_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)

    Medium_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])                                        #brush buttons
    pygame.draw.circle(screen, 'white', (155, 35), 10)
                                                                                                      
    Small_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215, 35), 5)

    Rectangle_brush = pygame.draw.rect(screen, 'black', [250, 10, 50, 50])
    pygame.draw.rect(screen, 'white', [262, 22, 25, 25])

    eraser = pygame.draw.rect(screen, 'black', [310, 10, 50, 50])
    pygame.draw.rect(screen, 'grey', [320, 20, 30, 30])

    
    red = pygame.draw.rect(screen, (255, 0, 0), [Screen_w - 35, 10, 25, 25])
    blue = pygame.draw.rect(screen, (0, 0, 255), [Screen_w - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [Screen_w - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [Screen_w - 60, 35, 25, 25])            #color buttons
    teal = pygame.draw.rect(screen, (0, 255, 255), [Screen_w - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [Screen_w - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [Screen_w - 110, 10, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [Screen_w - 110, 35, 25, 25])

    brush_list = [Super_large_brush, Large_brush, Medium_brush, Small_brush, Rectangle_brush, eraser]
    color_list = [red, blue, green, yellow, teal, purple, black, white]
    rgb_list = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_list, rgb_list


def draw_painting(paints):                #draw based on all info
    for paint in paints:
        color, pos, size, shape = paint

        if shape == "circle":
            pygame.draw.circle(screen, color, pos, size)
        elif shape == "rect":
            pygame.draw.rect(screen, color, pos)


while True:
    screen.fill((255, 255, 255))                  #bedore event loop because it overlaps
    brushes, colors, rgbs = draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            
            for i in range(len(brushes)):              #chose brush
                if brushes[i].collidepoint(mouse_pos):
                    if i == 4:
                        active_shape = "rect"
                    elif i == 5:
                        active_shape = "circle"
                        active_color = (255, 255, 255)
                    else:
                        active_shape = "circle"
                        active_size = 20 - (i * 5)

            
            for i in range(len(colors)):
                if colors[i].collidepoint(mouse_pos):          #chose color
                    active_color = rgbs[i]

            
            if active_shape == "rect" and mouse_pos[1] > 70:            #taking starting position of rectangle
                drawing_rect = True
                rect_start = mouse_pos

        if event.type == pygame.MOUSEBUTTONUP:                               #second position  of rect
            if active_shape == "rect" and drawing_rect:
                rect_end = event.pos

                x1, y1 = rect_start
                x2, y2 = rect_end

                rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)

                painting.append((active_color, rect, 0, "rect"))

                drawing_rect = False

    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    
    if left_click and mouse[1] > 70 and active_shape == "circle":
        painting.append((active_color, mouse, active_size, "circle"))

    draw_painting(painting)

    
    if drawing_rect:
        mouse_pos = pygame.mouse.get_pos()
        x1, y1 = rect_start
        x2, y2 = mouse_pos
        pygame.draw.rect(screen, active_color, (x1, y1, x2 - x1, y2 - y1), 2)

    
    if mouse[1] > 70:          #check to not draw o the menu
        if active_shape == "circle":
            pygame.draw.circle(screen, active_color, mouse, active_size)
        elif not drawing_rect:
            pygame.draw.rect(screen, active_color, (mouse[0], mouse[1], active_size * 2, active_size * 2))

    pygame.display.update()
    clock.tick(240)            #more fps smooth lines