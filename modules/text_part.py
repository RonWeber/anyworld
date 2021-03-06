import pygame
from pygame import Rect


TEXT_COLOR = (255, 255, 255)
BACK_COLOR = (0, 0, 0)

class TextPart:
    selected_thing = None
    def __init__(self, surface_size):
        self.font = pygame.font.Font(pygame.font.get_default_font(), 12)
        self.surface = pygame.Surface(surface_size)

    def get_surface(self):
        return self.surface
    def update_text(self):
        self.surface.fill(BACK_COLOR)
        if self.selected_thing is None:
            words = "Nothing selected"
        else:
            words = str(self.selected_thing)

        lines = words.split('\n')
        height = 0
        for l in lines:
            textSurface = self.font.render(l, 1, TEXT_COLOR)
            self.surface.blit(textSurface, (0, height))
            height += textSurface.get_height()

