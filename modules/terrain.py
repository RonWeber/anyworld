BASE_COLOR = (0, 0, 0)
WATER_COLOR = (0, 0, 200)
GRASSLAND_COLOR = (10, 250, 10)
DESERT_COLOR = (150, 113, 23)

class BaseTerrain():
    color = BASE_COLOR
    isWater = False
    isGrassland = False
    
class Water(BaseTerrain):
    color = WATER_COLOR
    isWater = True

class Grassland(BaseTerrain):
    color = GRASSLAND_COLOR
    isGrassland = True

class Desert(BaseTerrain):
    color = DESERT_COLOR
    
