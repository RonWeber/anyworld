BASE_COLOR = (0, 0, 0)
WATER_COLOR = (0, 0, 200)
GRASSLAND_COLOR = (10, 250, 10)
DESERT_COLOR = (150, 113, 23)

class BaseTerrain():
    name = "Base Terrain"
    color = BASE_COLOR
    isWater = False
    isGrassland = False
    def __str__(self):
        return self.name
    
class Water(BaseTerrain):
    name = "Water"
    color = WATER_COLOR
    isWater = True

class Grassland(BaseTerrain):
    name = "Grassland"
    color = GRASSLAND_COLOR
    isGrassland = True

class Desert(BaseTerrain):
    name = "Desert"
    color = DESERT_COLOR
    
