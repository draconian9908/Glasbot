import pygame

pygame.init()

class Tiles:

    size = 32

    blocked = []

    blockedNPC = []

    blocked_types = ["3", '9','30','31','32','33','34','35','36','37','38']

    def blocked_at(pos):
        if list(pos) in Tiles.blocked:
            return True
        else:
            return False

    def blocked_at_NPC(pos):
        if list(pos) in Tiles.blockedNPC:
            return True
        else:
            return False

    def load_texture(file, size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (size, size))

        surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0,0))

        return surface

    # basic tiles
    grass = load_texture("Graphics/grass.png", size)
    stone = load_texture("Graphics/stone.png", size)
    water = load_texture("Graphics/water.png", size)
    dirt = load_texture("Graphics/dirt.png", size)
    empty = load_texture("Graphics/empty.png", size)
    flowers = load_texture('Graphics/flowers.png', size)
    tree = load_texture('Graphics/tree.png', size)
    rock = load_texture('Graphics/rock.png', size)
    wood = load_texture('Graphics/wood.png', size)
    black =  load_texture('Graphics/blk.png', size)
    # rock and water tiles 10s
    rockwaterbottomleftturn = load_texture('Graphics/rockwaterbottomleftturn.png', size)
    rockwaterbottomrightturn = load_texture('Graphics/rockwaterbottomrightturn.png', size)
    rockwaterside = load_texture('Graphics/rockwaterside.png', size)
    rockwatersidedirtleft = load_texture('Graphics/rockwatersidedirtleft.png', size)
    rockwatersidedirtright = load_texture("Graphics/rockwatersidedirtright.png", size)
    rockwatertopleftturn = load_texture('Graphics/rockwatertopleftturn.png', size)
    rockwatertoprightturn = load_texture('Graphics/rockwatertoprightturn.png', size)
    rockwaterupdown = load_texture('Graphics/rockwaterupdown.png', size)
    rockwaterupdowndirtbottom = load_texture('Graphics/rockwaterupdowndirtbottom.png', size)
    rockwaterupdowndirttop = load_texture('Graphics/rockwaterupdowndirttop.png', size)
    # stone and dirt Tiles 20s
    stonebottom = load_texture('Graphics/stonebottom.png', size)
    stonebottomleft = load_texture('Graphics/stonebottomleft.png', size)
    stonebottomright = load_texture('Graphics/stonebottomright.png', size)
    stonehalf = load_texture('Graphics/stonehalf.png', size)
    stoneleft = load_texture('Graphics/stoneleft.png', size)
    stoneright = load_texture('Graphics/stoneright.png', size)
    stonetopleft = load_texture('Graphics/stonetopleft.png', size)
    stonetopright = load_texture('Graphics/stonetopright.png', size)
    stonetop = load_texture('Graphics/stonetop.png', size)
    # water and dirt Tiles 30s
    waterbarrel = load_texture('Graphics/waterbarrel.png', size)
    waterbottom = load_texture('Graphics/waterbottom.png', size)
    waterbottomleft = load_texture('Graphics/waterbottomleft.png', size)
    waterbottomright = load_texture('Graphics/waterbottomright.png', size)
    waterleft = load_texture('Graphics/waterleft.png', size)
    wateroil = load_texture('Graphics/wateroil.png', size)
    waterright = load_texture('Graphics/waterright.png', size)
    watertop = load_texture('Graphics/watertop.png', size)
    watertopleft = load_texture('Graphics/watertopleft.png', size)
    watertopright = load_texture('Graphics/watertopright.png', size)
    # Wood dirt Tiles 40s
    woodbottom = load_texture('Graphics/woodbottom.png', size)
    woodbottomleft = load_texture('Graphics/woodbottomleft.png', size)
    woodbottomright = load_texture('Graphics/woodbottomright.png', size)
    woodleft = load_texture("Graphics/woodleft.png", size)
    woodright = load_texture('Graphics/woodright.png', size)
    woodtop = load_texture('Graphics/woodtop.png', size)
    woodtopleft = load_texture('Graphics/woodtopleft.png', size)
    woodtopright = load_texture('Graphics/woodtopright.png', size)


    texture_tags = {"1": grass, "2":stone, "3": water, "4": dirt, '5':empty, '6':flowers, '7':tree, '8':wood, '9':black,
                    '10': rockwaterbottomleftturn, '11':rockwaterbottomrightturn, '12':rockwaterside, '13':rockwatersidedirtleft, '14':rockwatersidedirtright,
                    '15':rockwatertopleftturn, '16':rockwatertoprightturn, '17':rockwaterupdown, '18':rockwaterupdowndirtbottom, '19':rockwaterupdowndirttop,
                    '20':stonebottom, '21':stonebottomleft, '22':stonebottomright, '23':stonehalf, '24': stoneleft, '25':stoneright,
                    '26':stonetop, '27':stonetopleft, '28': stonetopright,
                    '30':waterbarrel, '31':waterbottom, '32':waterbottomleft, '33':waterbottomright, '34':waterleft,
                    '35':wateroil, '36':waterright, '37':watertop, '38':watertopleft, '39':watertopright,
                    '40':woodbottom, '41':woodbottomleft, '42':woodbottomright, '43':woodleft, '44':woodright, '45':woodtop,
                    '46':woodtopleft, '47':woodtopright}
