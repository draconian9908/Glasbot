import pygame, random, math
from Time import *
from glob import Globals
from Textures import Tiles



pygame.init()

def move_npc(npc):
    npc.facing = random.choice(('npc_south', 'npc_north', 'npc_east', 'npc_west'))
    npc.walking = random.choice((True, False))


def move_enemy(npc): #BROKEN
    if math.sqrt((player_x - npc.x)**2 + (player_y - npc.y)**2) <= 500:
        if player_y > npc.y:
            npc.facing = 'npc_south'
        elif player_y < npc.y:
            npc.facing = 'npc_north'
        elif player.y == npc.y:
            if player_x > npc.x:
                npc.facing = 'npc_east'
            elif player_x < npc.x:
                npc.facing = 'npc_west'

        npc.walking = True


class Dialog:
    def __init__(self, text):
        self.page = 0
        self.text = text #[('blah blah blah', 'blahblah blah'), ('blah blah')]


class NPC:

    all_npc = []
    enemy_npcs = []

    def __init__(self, name, pos, dialog, sprite, hostile, health):
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.dialog = dialog
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.walking = False
        self.timer = Timer(1)
        self.timer.on_next = lambda: move_npc(self)
        self.timer.start()

        self.last_location = [0, 0]

        self.hostile = hostile
        self.health = health

        #GET NPC FACES
        self.facing = 'npc_south'
        self.faces = get_faces(sprite)

        #PUBLISH
        #NPC.all_npc.append(self)

    def render(self, surface):
        self.timer.update()
        if self.walking:
            move_speed = 75 * Globals.deltatime
            if self.facing == 'npc_south':
                self.y += move_speed
            elif self.facing == 'npc_north':
                self.y -= move_speed
            elif self.facing == 'npc_east':
                self.x -= move_speed
            elif self.facing == 'npc_west':
                self.x += move_speed

            #BLOCK TILE NPC IS STANDING ON
            location = [round(self.x / Tiles.size), round(self.y / Tiles.size)]
            if self.last_location in Tiles.blocked:
                Tiles.blocked.remove(self.last_location)

            if not location in Tiles.blocked:
                Tiles.blocked.append(location)
                self.last_location = location


        surface.blit(self.faces[self.facing], (self.x + Globals.camera_x, self.y + Globals.camera_y))

class TestNPC(NPC):

    def __init__(self, name, pos, hostile, health, dialog = None):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics/cookie.png"), hostile, health)
        NPC.all_npc.append(self)

class Enemy1(NPC):
    def __init__(self, name, pos, dialog = None, hostile = True, health = 100):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics/cookie.png"), hostile, health)
        self.timer.on_next = lambda: move_npc(self)
        NPC.enemy_npcs.append(self)




def get_faces(sprite):
    faces = {}

    size = sprite.get_size()
    tile_size = (int(size[0]/2), int(size[1]/2))

    #for NPC
    npc_south = pygame.image.load("Graphics/cookie.png")
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(npc_south, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["npc_south"] = south

    npc_north = pygame.image.load("Graphics/cookie.png")
    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(npc_north, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["npc_north"] = north

    npc_east = pygame.image.load("Graphics/cookie.png")
    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(npc_east, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["npc_east"] = east

    npc_west = pygame.image.load("Graphics/cookie.png")
    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(npc_west, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["npc_west"] = west

    #with nothing
    none_south = pygame.image.load("Graphics/robot front.png")
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(none_south, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["Nonesouth"] = south

    none_north = pygame.image.load("Graphics/robot back.png")
    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(none_north, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["Nonenorth"] = north

    none_east = pygame.image.load("Graphics/robot left.png")
    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(none_east, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["Noneeast"] = east

    none_west = pygame.image.load("Graphics/robot right.png")
    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(none_west, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["Nonewest"] = west

    #with grass
    grass_south = pygame.image.load("Graphics/grassfront.png")
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(grass_south, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["grasssouth"] = south

    grass_north = pygame.image.load("Graphics/grassback.png")
    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(grass_north,(0,0), (0,0,tile_size[0],tile_size[1]))
    faces["grassnorth"] = north

    grass_east = pygame.image.load("Graphics/grassleft.png")
    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(grass_east, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["grasseast"] = east

    grass_west = pygame.image.load("Graphics/grassright.png")
    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(grass_west, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["grasswest"] = west

    #with flowers
    flowers_south = pygame.image.load("Graphics/flowerfront.png")
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(flowers_south, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["flowerssouth"] = south

    flowers_north = pygame.image.load("Graphics/flowerback.png")
    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(flowers_north, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["flowersnorth"] = north

    flowers_east = pygame.image.load("Graphics/flowerleft.png")
    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(flowers_east, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["flowerseast"] = east

    flowers_west = pygame.image.load("Graphics/flowerright.png")
    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(flowers_west, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["flowerswest"] = west

    #with tree
    tree_south = pygame.image.load("Graphics/treefront.png")
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(tree_south, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["treesouth"] = south

    tree_north = pygame.image.load("Graphics/treeback.png")
    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(tree_north, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["treenorth"] = north

    tree_east = pygame.image.load("Graphics/treeleft.png")
    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(tree_east, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["treeeast"] = east

    tree_west = pygame.image.load("Graphics/treeright.png")
    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(tree_west, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["treewest"] = west

    #with hoe
    hoe_south = pygame.image.load("Graphics/hoefront.png")
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(hoe_south, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["hoesouth"] = south

    hoe_north = pygame.image.load("Graphics/hoeback.png")
    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(hoe_north, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["hoenorth"] = north

    hoe_east = pygame.image.load("Graphics/hoeleft.png")
    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(hoe_east, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["hoeeast"] = east

    hoe_west = pygame.image.load("Graphics/hoeright.png")
    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(hoe_west, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["hoewest"] = west


    return faces
