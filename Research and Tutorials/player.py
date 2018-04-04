import pygame
from NPC import *

pygame.init()

class Player:

    def __init__(self,name):
        self.name = name
        sprite = pygame.image.load("Graphics/player.png")
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]

        # Get player faces
        self.faces = get_faces(sprite)
