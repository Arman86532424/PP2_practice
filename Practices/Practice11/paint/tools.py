import pygame


# ===================== PENCIL =====================
def draw_pencil(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)


# ===================== ERASER =====================
def draw_eraser(surface, start, end, size):
    pygame.draw.line(surface, (255, 255, 255), start, end, size)


# ===================== LINE =====================
def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)


# ===================== RECTANGLE =====================
def draw_rectangle(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
    pygame.draw.rect(surface, color, rect, size)


# ===================== CIRCLE =====================
def draw_circle(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    pygame.draw.circle(surface, color, start, radius, size)


# ===================== FLOOD FILL =====================
def flood_fill(surface, x, y, new_color):
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


# ===================== TEXT =====================
def draw_text(surface, font, text, pos, color):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

import pygame
import math

# ... (existing functions: draw_pencil, draw_eraser, draw_line, draw_rectangle, draw_circle)

# ===================== RIGHT TRIANGLE =====================
def draw_right_triangle(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    # Vertices: Start point, the corner below it, and the end point
    points = [(x1, y1), (x1, y2), (x2, y2)]
    pygame.draw.polygon(surface, color, points, size)

# ===================== EQUILATERAL TRIANGLE =====================
def draw_equilateral_triangle(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    width = x2 - x1
    # Height of an equilateral triangle is (sqrt(3)/2) * side
    height = int(abs(width) * (math.sqrt(3) / 2))
    
    # Determine vertical direction based on mouse drag
    direction = 1 if y2 > y1 else -1
    new_y2 = y1 + (height * direction)
    
    points = [((x1 + x2) / 2, y1), (x1, new_y2), (x2, new_y2)]
    pygame.draw.polygon(surface, color, points, size)

# ===================== RHOMBUS =====================
def draw_rhombus(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    # Vertices: Top center, right center, bottom center, left center
    points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
    pygame.draw.polygon(surface, color, points, size)

# ... (existing functions: flood_fill, draw_text)