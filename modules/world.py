import pygame
from pygame import Rect
from node import Node, WaterNode
from random import randint
import terrain

class World():
    def __init__(self, cols, rows, node_width, node_height):
        self.nodes = {}
        self.node_width = node_width
        self.node_height = node_height
        for x in xrange(cols - 1):
            for y in xrange(rows - 1):
                self.nodes[(x,y)] = stage1Node(x, y, Rect(x * node_width, y * node_height, node_width, node_height))

        #Set up neighbors
        for x in xrange(cols - 1):
            for y in xrange(rows - 1):
                for other_coord in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                     try:
                         self.nodes[(x,y)].addNeighbor(self.nodes[other_coord[0],other_coord[1]])
                     except KeyError:
                         #There are boundaries.
                         pass

    def draw(self, surface):
        for pos, n in self.nodes.items():
            n.drawSelf(surface)

    def underCursor(self, pos):
        thing = None
        try:
            thing = self.nodes[(pos[0] / self.node_width, pos[1] / self.node_height)]
        except KeyError:
            pass
        return thing
                     
def stage1Node(x, y, rectangle):
    if randint(1, 25) == 1:
        return Node(rectangle, terrain.Water())
    else:
        return Node(rectangle, terrain.Desert())

def generateTerrain(nodes):
    for n in nodes:
        n.previousTerrain = n.terrain
    #Step 1, spread water a bit.
    for n in nodes:
        if n.previousTerrain.isWater:
            for n2 in n.neighbors:
                n2.terrain = terrain.Water()
    #Step 2, add grassland
    for n in nodes:
        if n.terrain.isWater:
            for n2 in n.neighbors:
                if !n2.isWater:
                    n2.terrain = terrain.Grassland()
                    n2.previousTerrain = n2.terrain
    #Step 3, spread grassland farther
    for n in nodes:
        if n.previousTerrain.isGrassland:
            for n2 in n.neighbors:
                if not n2.isWater:
                    n2.terrain = terrain.Grassland()
