import pygame

pygame.init()

def get_faces(sprite):
    faces = {}

    size = sprite.get_size()
    tile_size = (int(size[0]/2), int(size[1]/2))

    #with nothing
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["nonesouth"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0,0), (tile_size[0], tile_size[1],tile_size[0],tile_size[1]))
    faces["nonenorth"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0,0), (tile_size[0], 0,tile_size[0],tile_size[1]))
    faces["noneeast"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0,0), (0, tile_size[1],tile_size[0],tile_size[1]))
    faces["nonewest"] = west

    #with grass
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["grasssouth"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0,0), (tile_size[0], tile_size[1],tile_size[0],tile_size[1]))
    faces["grassnorth"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0,0), (tile_size[0], 0,tile_size[0],tile_size[1]))
    faces["grasseast"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0,0), (0, tile_size[1],tile_size[0],tile_size[1]))
    faces["grasswest"] = west

    #with flowers
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["flowerssouth"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0,0), (tile_size[0], tile_size[1],tile_size[0],tile_size[1]))
    faces["flowersnorth"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0,0), (tile_size[0], 0,tile_size[0],tile_size[1]))
    faces["flowerseast"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0,0), (0, tile_size[1],tile_size[0],tile_size[1]))
    faces["flowerswest"] = west

    #with tree
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["treesouth"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0,0), (tile_size[0], tile_size[1],tile_size[0],tile_size[1]))
    faces["treenorth"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0,0), (tile_size[0], 0,tile_size[0],tile_size[1]))
    faces["treeeast"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0,0), (0, tile_size[1],tile_size[0],tile_size[1]))
    faces["treewest"] = west

    #with hoe
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["hoesouth"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0,0), (tile_size[0], tile_size[1],tile_size[0],tile_size[1]))
    faces["hoenorth"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0,0), (tile_size[0], 0,tile_size[0],tile_size[1]))
    faces["hoeeast"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0,0), (0, tile_size[1],tile_size[0],tile_size[1]))
    faces["hoewest"] = west


    return faces
