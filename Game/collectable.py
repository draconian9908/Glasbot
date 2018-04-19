import pygame

class Bag(pygame.sprite.Sprite):

    def __init__ (self, contain, file, x,y, kind):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.contents = contain
        self.image = (pygame.image.load(file))
        self.rect = self.image.get_rect()
        self.tile = [self.image, x *32, y *32]
        self.type = kind


# create bags

bag_group = pygame.sprite.Group()

grass_bag_pic = "Graphics/bag.png"
# flower_bag_pic =
# tree_bag_pic =

bag1 = Bag(4, grass_bag_pic, 5, 6, 'grass')
bag_group.add(bag1)
