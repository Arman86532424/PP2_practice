import pygame
import sys
from datetime import datetime
import tools

pygame.init()

Screen_w, Screen_h = 900, 900
screen = pygame.display.set_mode((Screen_w, Screen_h))
clock = pygame.time.Clock()

canvas = pygame.Surface((Screen_w, Screen_h))
canvas.fill((255, 255, 255))

color = (0, 0, 0)
brush_size = 5
tool = "pencil"

drawing = False
start_pos = None
last_pos = None

font = pygame.font.SysFont(None, 32)
text_input = ""
text_pos = None
typing = False


# ===================== MENU =====================
def draw_menu():
    pygame.draw.rect(screen, "grey", (0, 0, Screen_w, 70))

    pencil_icon = pygame.image.load("C:/TT/Python/Practices/Tsis2/accets/—Pngtree—pencil icon_5069217.png").convert_alpha()
    pencil_icon = pygame.transform.scale(pencil_icon,(60,50))
    screen.blit(pencil_icon,(10,10))

    line_icon = pygame.image.load("C:/TT/Python/Practices/Tsis2/accets/line.png").convert_alpha()
    line_icon = pygame.transform.scale(line_icon,(60,50))
    screen.blit(line_icon,(80,10))

    rect_icon = pygame.image.load("C:/TT/Python/Practices/Tsis2/accets/rectan.png").convert_alpha()
    rect_icon = pygame.transform.scale(rect_icon,(60,50))
    screen.blit(rect_icon,(150,10))

    circle_icon = pygame.image.load("Practices/Tsis2/accets/circle.png").convert_alpha()
    circle_icon = pygame.transform.scale(circle_icon,(60,50))
    screen.blit(circle_icon,(220,10))

    fill_icon = pygame.image.load("Practices/Tsis2/accets/fill.png").convert_alpha()
    fill_icon = pygame.transform.scale(fill_icon,(60,50))
    screen.blit(fill_icon,(290,10))                                                                              #icons for evey tool

    text_icon = pygame.image.load("Practices/Tsis2/accets/images.png").convert_alpha()
    text_icon = pygame.transform.scale(text_icon,(60,50))
    screen.blit(text_icon,(360,10))

    eras_icon = pygame.image.load("Practices/Tsis2/accets/eras.png").convert_alpha()
    eras_icon = pygame.transform.scale(eras_icon,(60,50))
    screen.blit(eras_icon,(430,10))

    right_tri = pygame.image.load("Practices/Tsis2/accets/right-angle.png").convert_alpha()
    right_tri = pygame.transform.scale(right_tri,(50,40))
    screen.blit(right_tri,(500,15))

    equ_tri = pygame.image.load("Practices/Tsis2/accets/equilateral-triangle.png").convert_alpha()
    equ_tri = pygame.transform.scale(equ_tri,(50,40))
    screen.blit(equ_tri,(575,15))

    rom = pygame.image.load("Practices/Tsis2/accets/rhombus.png").convert_alpha()
    rom = pygame.transform.scale(rom,(60,50))
    screen.blit(rom,(640,10))




    tools_rects = {
        "pencil": pygame.Rect(10, 10, 60, 50),
        "line": pygame.Rect(80, 10, 60, 50),
        "rect": pygame.Rect(150, 10, 60, 50),
        "circle": pygame.Rect(220, 10, 60, 50),
        "fill": pygame.Rect(290, 10, 60, 50),
        "text": pygame.Rect(360, 10, 60, 50),                   #tools botton coordinates 
        "eraser": pygame.Rect(430, 10, 60, 50),
        "right_tri": pygame.Rect(500, 10, 60, 50),
        "equi_tri": pygame.Rect(570, 10, 60, 50),
        "rhombus": pygame.Rect(640, 10, 60, 50),
    }

    for rect in tools_rects.values():
        pygame.draw.rect(screen, "black", rect, 2)

    colors = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255),
        (0, 0, 0), (255, 255, 255)                               #defining available colors
    ]

    color_rects = []

    start_x = Screen_w - 180        # shift left 
    y = 20                  

    for i, c in enumerate(colors):
        x = start_x + i * 30
        rect = pygame.Rect(x, y, 25, 25)
        pygame.draw.rect(screen, c, rect)  
        color_rects.append((rect, c))

    return tools_rects, color_rects



while True:
    screen.fill((255, 255, 255))
    screen.blit(canvas, (0, 0))

    tool_rects, color_rects = draw_menu()             

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        if event.type == pygame.MOUSEBUTTONDOWN:                          #mouse botton tap
            x, y = event.pos

            if y < 70:
                for name, rect in tool_rects.items():
                    if rect.collidepoint(event.pos):
                        tool = name

                for rect, c in color_rects:
                    if rect.collidepoint(event.pos):
                        color = c

            else:
                if tool == "fill":
                    tools.flood_fill(canvas, x, y, color)

                elif tool == "text":
                    typing = True
                    text_input = ""
                    text_pos = event.pos

                else:
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos

        
        if event.type == pygame.MOUSEBUTTONUP:                                          #events when we stop holding mouse botton
            if drawing:
                end_pos = event.pos

                if tool == "line":
                    tools.draw_line(canvas, color, start_pos, end_pos, brush_size)

                elif tool == "rect":
                    tools.draw_rectangle(canvas, color, start_pos, end_pos, brush_size)

                elif tool == "circle":
                    tools.draw_circle(canvas, color, start_pos, end_pos, brush_size)

                elif tool == "right_tri":
                    tools.draw_right_triangle(canvas, color, start_pos, end_pos, brush_size)
                elif tool == "equi_tri":
                    tools.draw_equilateral_triangle(canvas, color, start_pos, end_pos, brush_size)
                elif tool == "rhombus":
                    tools.draw_rhombus(canvas, color, start_pos, end_pos, brush_size)

                drawing = False

        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:                     #choosing brush size
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")            #saving art by holding hot key
                pygame.image.save(canvas, filename)
                

            if typing:
                if event.key == pygame.K_RETURN:
                    tools.draw_text(canvas, font, text_input, text_pos, color)
                    typing = False

                elif event.key == pygame.K_ESCAPE:                              #takeing user text input
                    typing = False

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

    
    if drawing:
        mouse = pygame.mouse.get_pos()

        if tool == "pencil":
            tools.draw_pencil(canvas, color, last_pos, mouse, brush_size)                      #pencil and eraser draw part
            last_pos = mouse

        elif tool == "eraser":
            tools.draw_eraser(canvas, last_pos, mouse, brush_size)
            last_pos = mouse

    
    if drawing:
        mouse = pygame.mouse.get_pos()

        if tool == "line":
            pygame.draw.line(screen, color, start_pos, mouse, brush_size)

        elif tool == "rect":
            pygame.draw.rect(screen, color, (*start_pos, mouse[0]-start_pos[0], mouse[1]-start_pos[1]), 2)            #preview for tools 

        elif tool == "circle":
            radius = int(((mouse[0]-start_pos[0])**2 + (mouse[1]-start_pos[1])**2)**0.5)
            pygame.draw.circle(screen, color, start_pos, radius, 2)

   
    if typing:
        preview = font.render(text_input, True, color)
        screen.blit(preview, text_pos)                   #text preview

    pygame.display.update()
    clock.tick(240)