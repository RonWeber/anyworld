import pygame
from modules import *

WIDTH = 1000
HEIGHT = 600


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    running = True
    #Enter main loop
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
    
main()
