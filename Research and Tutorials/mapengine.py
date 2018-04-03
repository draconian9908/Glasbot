import pygame
from Textures import *

class Map_engine:

    def add_tile(tile, pos, addTo):

        addTo.blit(tile, (pos[0]*Tiles.size, pos[1]*Tiles.size))

    def load_map(file):

        with open(file, "r") as mapfile:
            map_data = mapfile.read()

        # Read tile map_data
        map_data = map_data.split("-") #Split into list of tiles

        map_size = map_data[len(map_data)-1] #Get map dimensions
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * Tiles.size
        map_size[1] = int(map_size[1]) * Tiles.size

        tiles = []
        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":")) # Split pos from texture

        for tile in tiles:
            tile[0] = tile[0].split(",") # Split pos into list
            pos = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p) #convert to integer

            tiles[tiles.index(tile)] = (pos, tile[1]) #save to tile list

        #Create terrain
        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in Tiles.texture_tags:
                Map_engine.add_tile(Tiles.texture_tags[tile[1]], tile[0], terrain)

        return terrain
