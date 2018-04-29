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
    #random bags
bag1 = Bag(4, grass_bag_pic, 5, 6, 'grass')
bag_group.add(bag1)

bag2 = Bag(2, flower_bag_pic, 10, 20, 'flowers')
bag_group.add(bag2)

bag7 = Bag(3, grass_bag_pic, 30, 26, 'grass')
bag_group.add(bag7)

bag8 = Bag(2, grass_bag_pic, 31, 47, 'grass')
bag_group.add(bag8)

    #arena bags
bag3 = Bag(2, grass_bag_pic, 13, 74, 'grass')
bag_group.add(bag3)

bag4 = Bag(5, grass_bag_pic, 17, 78, 'grass')
bag_group.add(bag4)

bag5 = Bag(2, flower_bag_pic, 22, 75, 'flowers')
bag_group.add(bag5)

bag6 = Bag(1, tree_bag_pic, 17, 80, 'tree')
bag_group.add(bag6)

    #maze bags
bag9 = Bag(2, grass_bag_pic, 58, 16, 'grass')
bag_group.add(bag9)

bag10 = Bag(4, grass_bag_pic, 77, 17, 'grass')
bag_group.add(bag10)

bag11 = Bag(3, flower_bag_pic, 90, 21, 'flowers')
bag_group.add(bag11)

bag12 = Bag(5, grass_bag_pic, 74, 2, 'grass')
bag_group.add(bag12)

bag13 = Bag(1, tree_bag_pic, 138, 5, 'tree')
bag_group.add(bag13)

bag14 = Bag(2, tree_bag_pic, 139, 15, 'tree')
bag_group.add(bag14)

bag15 = Bag(4, flower_bag_pic, 134, 19, 'flowers')
bag_group.add(bag15)

bag16 = Bag(2, flower_bag_pic, 151, 11, 'flowers')
bag_group.add(bag16)

bag17 = Bag(4, grass_bag_pic, 143, 9, 'grass')
bag_group.add(bag17)

bag18 = Bag(2, grass_bag_pic, 149, 4, 'grass')
bag_group.add(bag18)
