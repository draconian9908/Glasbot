import pygame
import glob

class Grass(pygame.sprite.Sprite):
    def __init__(self, x=-1000, y=-1000):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = (pygame.image.load('Graphics/grass.png'))
        self.points = 1
        self.amount = 20
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
    def update(self):
        self.change_x = glob.Globals.move_x
        self.change_y = glob.Globals.move_y
        self.rect.x += self.change_x
        self.rect.y += self.change_y


class Flowers(pygame.sprite.Sprite):
    def __init__(self, x=-1000, y=-1000):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = (pygame.image.load('Graphics/flowers.png'))
        self.points = 2
        self.amount = 10
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Tree(pygame.sprite.Sprite):
    def __init__(self, x=-1000, y=-1000):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = (pygame.image.load('Graphics/tree.png'))
        self.points = 4
        self.amount = 2
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class hoe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.damage = 1
