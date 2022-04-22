import pygame
import pgzrun
import random
import math


WIDTH = 1000
HEIGHT = 1000

colors = [(255,0,0),(0,255,0)]
current_color = 0

drawing_surface = pygame.Surface((WIDTH, HEIGHT))
drawing_surface.fill("white")

number_of_sections = 1


def draw():
    screen.blit(drawing_surface, (0,0))
    mouse_pos = pygame.mouse.get_pos()
    screen.draw.filled_circle(mouse_pos, 10, colors[current_color])

def update():
    is_pressed = pygame.mouse.get_pressed()[0]
    if is_pressed:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(drawing_surface, colors[current_color], mouse_pos, 10)
        x, y = mouse_pos
        x -= WIDTH / 2
        y -= HEIGHT / 2
        angle = 0
        while angle < 360:
            angle += 360 / number_of_sections
            rad = math.radians(angle)
            nx = x * math.cos(rad) - y * math.sin(rad)
            ny = x * math.sin(rad) + y * math.cos(rad)
            nx += WIDTH / 2
            ny += HEIGHT / 2
            n_pos = (nx, ny)
            pygame.draw.circle(drawing_surface, colors[current_color], n_pos, 10)
def on_key_down(key):
    global current_color, number_of_sections
    if key == keys.C:
        current_color += 1
        current_color %= len(colors)
    if key == keys.M:
        number_of_sections += 1
    if key == keys.N:
        number_of_sections -= 1
        if number_of_sections < 1:
            number_of_sections = 1

def on_mouse_down(pos, button):
    if button == mouse.RIGHT:
        drawing_surface.fill("white")

pygame.mouse.set_visible(False)
pgzrun.go()