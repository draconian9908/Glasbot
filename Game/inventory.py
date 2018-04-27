import pygame
import glob

# Creates the classes for items in the inventory
# Used only for inventory display purposes

class Item(pygame.sprite.Sprite):
    # Creates a broad item class
    def __init__(self, x, y, image, points, amount, damage):
        pygame.sprite.Sprite.__init__(self)
        # Gets the image of the item
        self.image = (pygame.image.load(image))
        self.rect = self.image.get_rect()
        # Gets the position for the item
        self.rect.x = x
        self.rect.y = y
        # Value of planting the item - n/a for the hoe
        self.points = points
        # Amount of seeds you have - only 1 hoe
        self.amount = amount
        # Amount of damage dealt - only for the hoe
        self.damage = damage

# Initialized all of the item classes
class Grass(Item):
    def __init__(self, x=-1000, y=-1000, image = 'Graphics/grass.png', points = 1, amount=0, damage=0):
        super().__init__(x, y, image, points, amount,damage)


class Flowers(Item):
    def __init__(self, x=-1000, y=-1000, image = 'Graphics/flowers.png', points =2, amount=0,damage=0):
        super().__init__(x,y,image,points,amount,damage)

class Tree(Item):
    def __init__(self, x=-1000, y=-1000, image='Graphics/tree.png', points=4, amount=0,damage=0):
        super().__init__(x,y,image,points,amount,damage)

class Hoe(Item):
    def __init__(self, x=-1000, y=-1000, image='Graphics/hoe.png', points=0, amount =1, damage=1):
        super().__init__(x,y,image,points,amount,damage)
