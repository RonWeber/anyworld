import pygame
from pygame import Rect
from node import Node
import random
from random import randint
import terrain

NUM_LAKES = 25
MAX_LAKE_SIZE = 11
GRASSLAND_SPREAD = 6

class World():
    def __init__(self, cols, rows, node_width, node_height):
        self.nodes = {}
        self.node_width = node_width
        self.node_height = node_height
        for x in xrange(cols - 1):
            for y in xrange(rows - 1):
                self.nodes[(x,y)] = stage1Node(x, y, Rect(x * node_width, y * node_height, node_width, node_height))

        generateNeighbors(self.nodes, cols, rows)
        generateLakes(self.nodes)
        generateTerrain(self.nodes)

    def draw(self, surface):
        for n in self.nodes.values():
            n.drawSelf(surface)
    def underCursor(self, pos):
        thing = None
        try:
            thing = self.nodes[(pos[0] / self.node_width, pos[1] / self.node_height)]
        except KeyError:
            pass
        return thing
        
def stage1Node(col, row, nodeRectangle):
    return Node(nodeRectangle, terrain.Desert())

def spreadGrassland(nodes):
    for n in nodes.values():
        if n.previousTerrain.isGrassland:
            for n2 in n.neighbors:
                if not n2.terrain.isWater:
                    n2.terrain = terrain.Grassland()
    for n in nodes.values():
        n.previousTerrain = n.terrain

def generateLakes(nodes):
    for i in xrange(NUM_LAKES):
        generateLake(random.choice(nodes.values()), randint(1, MAX_LAKE_SIZE))    
        
def generateLake(source, size):
    if size <= 0: return
    source.terrain = terrain.Water()
    landNeighbors = [n for n in source.neighbors if not n.terrain.isWater]
    if landNeighbors:
        generateLake(random.choice(landNeighbors), size - 1)
    
def generateTerrain(nodes):
    for n in nodes.values():
        n.previousTerrain = n.terrain
    #Step 1, spread water a bit.
    for n in nodes.values():
        if n.previousTerrain.isWater:
            for n2 in n.neighbors:
                n2.terrain = terrain.Water()
    for n in nodes.values():
        n.previousTerrain = n.terrain
    #Step 2, add grassland
    for n in nodes.values():
        if n.terrain.isWater:
            for n2 in n.neighbors:
                if not n2.terrain.isWater:
                    n2.terrain = terrain.Grassland()
                    n2.previousTerrain = n2.terrain
    #Step 3, spread grassland farther
    for x in xrange(GRASSLAND_SPREAD):
        spreadGrassland(nodes)

def generateNeighbors(nodes, cols, rows):
    #Set up neighbors
    for x in xrange(cols):
        for y in xrange(rows):
                try:
                    nodes[(x,y)].addNeighbor(nodes[(x+1,y)])
                except KeyError:
                    pass
                try:
                    nodes[(x,y)].addNeighbor(nodes[(x-1,y)])
                except KeyError:
                    pass
                try:
                    nodes[(x,y)].addNeighbor(nodes[(x,y+1)])
                except KeyError:
                    pass
                try:
                    nodes[(x,y)].addNeighbor(nodes[(x,y-1)])
                except KeyError:
                    pass                
