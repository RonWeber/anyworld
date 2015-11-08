import pygame
from modules import *
from modules.world import World
import sys

WIDTH = 1000
HEIGHT = 600

MAIN_WINDOW_WIDTH = 700

LINE_COLOR = (255, 255, 255)

NODE_COLS = 50
NODE_ROWS = 50


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    #Main part is 700 pixels, I guess
    #Line will be 1 px
    #text part is the rest
    textPart = text_part.TextPart(((WIDTH - MAIN_WINDOW_WIDTH - 1), HEIGHT))

    world = World(NODE_COLS, NODE_ROWS, (MAIN_WINDOW_WIDTH / NODE_COLS), (HEIGHT / NODE_ROWS))
    
    running = True
    #Enter main loop
    while running:
        pygame.draw.line(screen, LINE_COLOR, (MAIN_WINDOW_WIDTH + 1, 0),
                         (MAIN_WINDOW_WIDTH + 1, HEIGHT))
        textPart.update_text()
        screen.blit(textPart.get_surface(), (MAIN_WINDOW_WIDTH + 2, 0))
        world.draw(screen)        
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit(0)
            elif e.type == pygame.MOUSEBUTTONUP:
                textPart.selected_thing = world.underCursor(pygame.mouse.get_pos())

    
main()
