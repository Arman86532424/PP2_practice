import pygame
import math



def draw_pencil(surface, color, start, end, size):       #pencil
    pygame.draw.line(surface, color, start, end, size)



def draw_eraser(surface, start, end, size):        #eraser
    pygame.draw.line(surface, (255, 255, 255), start, end, size)



def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)           #line



def draw_rectangle(surface, color, start, end, size):               #rectangle
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
    pygame.draw.rect(surface, color, rect, size)



def draw_circle(surface, color, start, end, size):                 #circle
    x1, y1 = start
    x2, y2 = end
    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    pygame.draw.circle(surface, color, start, radius, size)



def flood_fill(surface, x, y, new_color):               #fill
    width, height = surface.get_size()
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        px, py = stack.pop()

        if px < 0 or px >= width or py < 70 or py >= height:
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        stack.append((px + 1, py))
        stack.append((px - 1, py))
        stack.append((px, py + 1))
        stack.append((px, py - 1))



def draw_text(surface, font, text, pos, color):      #text
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)






def draw_right_triangle(surface, color, start, end, size):       #right triangle
    x1, y1 = start
    x2, y2 = end
    # Vertices: Start point, the corner below it, and the end point
    points = [(x1, y1), (x1, y2), (x2, y2)]
    pygame.draw.polygon(surface, color, points, size)


def draw_equilateral_triangle(surface, color, start, end, size):      #equ triangle
    x1, y1 = start
    x2, y2 = end
    width = x2 - x1
    
    height = int(abs(width) * (math.sqrt(3) / 2))         #formula for hight 
    
    
    direction = 1 if y2 > y1 else -1 # Determine  direction 
    new_y2 = y1 + (height * direction)
    
    points = [((x1 + x2) / 2, y1), (x1, new_y2), (x2, new_y2)]
    pygame.draw.polygon(surface, color, points, size)


def draw_rhombus(surface, color, start, end, size):            #rombus
    x1, y1 = start
    x2, y2 = end
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    # Vertices: Top center, right center, bottom center, left center
    points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
    pygame.draw.polygon(surface, color, points, size)

