import pygame, random, math
from Time import *
from glob import Globals
from Textures import *
from player import *
import math

pygame.init()


# Function in order to move the enemy and track the player
def move_enemy(npc, player):
    # Checks to see that the player is close to the enemy - variable distance
    dist = math.sqrt((player.x - npc.x/Tiles.size)**2 + (player.y - npc.y/Tiles.size)**2)
    #print(dist)
    if dist <= 10:
        if round(player.y) > round(npc.y / Tiles.size):
            # Sees where the player is relative to the NPC
            npc.facing = 'npc_south'
            # Makes the npc face the player
        elif round(player.y) < round(npc.y / Tiles.size):
            npc.facing = 'npc_north'
        elif round(player.x) > round(npc.x / Tiles.size):
            npc.facing = 'npc_east'
        elif round(player.x) < round(npc.x / Tiles.size):
            npc.facing = 'npc_west'
        # Saying that the NPC is moving
        npc.walking = True
    else:
        # if the player is not close enough generate a random direction for the NPC and randomly choose if moving
        npc.facing = random.choice(('npc_south', 'npc_north', 'npc_east', 'npc_west'))
        npc.walking = random.choice((True, False))


class Dialog:
    # Creates the class for the dialog
    def __init__(self, text):
        self.page = 0
        self.text = text #[('blah blah blah', 'blahblah blah'), ('blah blah')]

enemy_group = pygame.sprite.Group()
class NPC(pygame.sprite.Sprite):
    # NPC class for enemies mostly - lists for NPCs and then another for only enemies
    all_npc = []
    enemy_npcs = []

    def __init__(self, name, pos, dialog, sprite, hostile, health, target):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.name = name
        # Sets the position of the NPC for the start
        self.x = pos[0]
        self.y = pos[1]
        # Sets the dialog for the NPC if any
        self.dialog = dialog
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        # Says if NPC is moving or not
        self.walking = False
        # Uses timers for the NPC and make movement at every step
        self.timer = Timer(1)
        self.timer.on_next = None
        self.timer.start()

        # Get the last location of the NPC
        self.last_location = [0, 0]

        # Says if NPC is hostile or not as well as the health and the target of the enemy
        self.hostile = hostile
        self.health = health
        self.target = target

        #shows the direction of the NPC
        self.facing = 'npc_south'
        self.faces = get_faces(sprite)


    def render(self, surface):
        # Updates the timer on the NPC
        self.timer.update()
        # Gets the x and y position
        x = self.x/Tiles.size
        y = self.y/Tiles.size
        if self.walking:
        # if it is supposed to move...
            move_speed = 75 * Globals.deltatime
            # Speed of the NPC
            if self.facing == 'npc_south':
            # Checks to see which direction facing
                if not Tiles.blocked_at_NPC((round(x),math.floor(y)+1)):
                    # if the tile in that direction is not blocked to the NPC
                    self.y += move_speed
                    # move the speed of the NPC in that direction
            elif self.facing == 'npc_north':
                if not Tiles.blocked_at_NPC((round(x),math.ceil(y)-1)):
                    self.y -= move_speed
            elif self.facing == 'npc_west':
                if not Tiles.blocked_at_NPC((math.floor(x)-1,round(y))):
                    self.x -= move_speed
            elif self.facing == 'npc_east':
                if not Tiles.blocked_at_NPC((math.floor(x)+1,round(y))):
                    self.x += move_speed
            # Gets the current location of the NPC
            location = [round(self.x / Tiles.size), round(self.y / Tiles.size)]
            if self.last_location in Tiles.blocked:
                # Removes the last location of the NPC from the blocked player tiles
                Tiles.blocked.remove(self.last_location)
            if not location in Tiles.blocked:
                # Adds the current location to blocked player tiles - so player cannot walk on it
                Tiles.blocked.append(location)
                # Updates the last location variable to the current location
                self.last_location = location
        # Blits the NPC to the location with the direction it is facing
        surface.blit(self.faces[self.facing], (self.x + Globals.camera_x, self.y + Globals.camera_y))

class TestNPC(NPC):
    # The NPC class that is not enemies
    def __init__(self, name, pos, hostile, health, dialog = None):
        # Makes an npc that is not an enemy
        super().__init__(name, pos, dialog, pygame.image.load("Graphics/cookie.png"), hostile, health)
        # Appends this NPC to the list
        NPC.all_npc.append(self)

class Enemy1(NPC):
    def __init__(self, name, pos,  target, dialog = None, hostile = True, health = 4):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics/cookie.png"), hostile, health, target)

        #sets NPC movement to that defined bt the move_enemy function
        self.timer.on_next = lambda: move_enemy(self, target)
        #appends NPC to enemy list
        enemy_group.add(self)
        NPC.enemy_npcs.append(self)



def get_faces(sprite):
    # decides which image is rendered based on direction
    faces = {}

    size = sprite.get_size()
    tile_size = (int(size[0]), int(size[1]))

    #for NPC
    npc_south = pygame.image.load("Graphics/NPC/eyefront.png")
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(npc_south, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["npc_south"] = south

    npc_north = pygame.image.load("Graphics/NPC/eyeback.png")
    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(npc_north, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["npc_north"] = north

    npc_east = pygame.image.load("Graphics/NPC/eyeright.png")
    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(npc_east, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["npc_east"] = east

    npc_west = pygame.image.load("Graphics/NPC/eyeleft.png")
    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(npc_west, (0,0), (0,0,tile_size[0],tile_size[1]))
    faces["npc_west"] = west

    # FOR THE PLAYER
    #with nothing in hand
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

    #with grass in hand
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

    #with flowers in hand
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

    #with tree in hand
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

    #with hoe in hand
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
