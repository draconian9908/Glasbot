import pygame
from NPC import *
from Textures import Tiles
from glob import Globals

pygame.init()

class Player:

    def __init__(self,name, window_width, window_height):
        self.name = name
        self.facing = "Nonesouth"
        self.health = 100
        sprite = pygame.image.load("Graphics/player.png")
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]
        self.points = 0

        self.image = pygame.image.load("Graphics/player.png")
        self.rect = self.image.get_rect()
        # Get player faces
        self.faces = get_faces(sprite)
        self.x = round(window_width/2 - self.width/2 - Globals.camera_x) / Tiles.size
        self.y = round(window_height/2 - self.height/2 - Globals.camera_y) / Tiles.size

    def render(self, surface, pos):
        surface.blit(self.faces[self.facing], pos)
