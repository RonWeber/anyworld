import pygame

NODE_OUTLINE_COLOR = (200, 200, 200)

class Node():
    neighbors = []
    def __init__(self, rectangle, terrain):
        self.rect = rectangle
        self.terrain = terrain
    def __str__(self):
        return "Empty node at " + str(self.rect)
    
    def addNeighbor(self, toAdd):
        self.neighbors.append(toAdd)
        
    def drawSelf(self, surface):
        pygame.draw.rect(surface, self.terrain.color, self.rect)
        pygame.draw.rect(surface, NODE_OUTLINE_COLOR, self.rect, 1)
