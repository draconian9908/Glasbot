import pygame

class Bag(pygame.sprite.Sprite):

    def __init__ (self, contain, file, x,y, kind):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        # amount of seeds contained
        self.contents = contain
        self.image = (pygame.image.load(file))
        self.rect = self.image.get_rect()
        # placement of bag
        self.tile = [self.image, x *32, y *32]
        # shows what kind of bag it is
        self.type = kind


# create bag group
bag_group = pygame.sprite.Group()

# Three types of bags
grass_bag_pic = "Graphics/grassbag.png"
flower_bag_pic = "Graphics/flowerbag.png"
tree_bag_pic = "Graphics/treebag.png"

# Creates bags and initializes type, contents and position
bag1 = Bag(4, grass_bag_pic, 5, 6, 'grass')
bag_group.add(bag1)

bag2 = Bag(2, flower_bag_pic, 10, 20, 'flowers')
bag_group.add(bag2)
