import pygame

pygame.init()

class Tiles:

    size = 32

    blocked = []

    blocked_types = ["3"]

    def blocked_at(pos):
        if list(pos) in Tiles.blocked:
            return True
        else:
            return False

    def load_texture(file, size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (size, size))

        surface = pygame.Surface((size, size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0,0))

        return surface

    grass = load_texture("Graphics/grass.png", size)
    stone = load_texture("Graphics/stone.png", size)
    water = load_texture("Graphics/water.png", size)
    dirt = load_texture("Graphics/dirt.png", size)
    empty = load_texture("Graphics/empty.png", size)

    texture_tags = {"1": grass, "2":stone, "3": water, "4": dirt, '5':empty}
