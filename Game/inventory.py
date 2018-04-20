import pygame
import glob

class Grass(pygame.sprite.Sprite):
    def __init__(self, x=-1000, y=-1000):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = (pygame.image.load('Graphics/grass.png'))
        self.points = 1
        self.amount = 0
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Flowers(pygame.sprite.Sprite):
    def __init__(self, x=-1000, y=-1000):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = (pygame.image.load('Graphics/flowers.png'))
        self.points = 2
        self.amount = 0
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Tree(pygame.sprite.Sprite):
    def __init__(self, x=-1000, y=-1000):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = (pygame.image.load('Graphics/tree.png'))
        self.points = 4
        self.amount = 0
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Hoe(pygame.sprite.Sprite):
    def __init__(self, x=-1000, y=-1000):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.damage = 1
        self.image = (pygame.image.load("Graphics/hoe.png"))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.amount = 1
