import pygame, sys, math
from Textures import *

def export_map(file):
    map_data = ""
    #get map dimensions
    max_x = 0
    max_y = 0

    # Getting the map size
    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    #save map Tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0]/Tiles.size)) + ',' + str(int(tile[1]/Tiles.size)) + ':' + tile[2] + '-'

    #save map dimensions
    map_data = map_data + str(int(max_x/Tiles.size)) + ',' + str(int(max_y/Tiles.size))

    #write fille
    with open(file, 'w') as mapfile:
        mapfile.write(map_data)

def load_map(file):
    # loading a pre saved map
    # almost the same as the map engine
    global tile_data
    # opens the actual file
    with open(file, "r") as mapfile:
        map_data = mapfile.read()

    # Splits the data to get the tiles different
    map_data = map_data.split('-')

    # Gets the map size, collects x and y and removes it from the tile list
    map_size = map_data[len(map_data)-1]
    map_data.remove(map_size)
    map_size = map_size.split(",")
    map_size[0] = int(map_size[0]) * Tiles.size
    map_size[1] = int(map_size[1]) * Tiles.size

    tiles = []

    for tile in range(len(map_data)):
        # Appends the data by the position of the tiles
        map_data[tile] = map_data[tile].replace('\n','')
        tiles.append(map_data[tile].split(":"))

    for tile in tiles:
        tile[0] = tile[0].split(",")
        pos = tile[0]
        for p in pos:
            pos[pos.index(p)] = int(p)

        tiles[tiles.index(tile)] = [pos[0] * Tiles.size, pos[1] * Tiles.size, tile[1]]
    # append tile to tile data
    tile_data = tiles

window = pygame.display.set_mode((1280,720), pygame.HWSURFACE)
# Sets the window and the caption
pygame.display.set_caption("Map Editor")

# sets the clock for the game
clock = pygame.time.Clock()

txt_font = pygame.font.Font(None, 20)

# Gets the mouse position
mouse_pos = 0
mouse_x = 0
mouse_y = 0

# Has a base map size
map_width = 100 * Tiles.size
map_height = 100 * Tiles.size

# The selector for highlighting where your mouse is
selector = pygame.Surface((Tiles.size, Tiles.size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill((255,255,255,100))

# has an empty list for tile data
tile_data = []

# sets the camera location and movement
camera_x = 0
camera_y = 0
camera_move = 0

# shows the brush type - the key
brush = '2'

# Intiailize default map
for x in range(0, map_width, Tiles.size):
    for y in range(0, map_height, Tiles.size):
        tile_data.append([x,y, "4"])

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # Camera movements
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4
            elif event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_l:
                # Allows to load the map with the file name
                name = input("map name: ")
                load_map("maps/" + name)
                print("map loaded")
            #brushes
            if event.key == pygame.K_r:
                brush = 'r'
                # remove the tile
            elif event.key == pygame.K_1:
                brush = '1'
            elif event.key == pygame.K_2:
                brush = '2'
            elif event.key == pygame.K_3:
                brush = '3'
            elif event.key == pygame.K_4:
                brush = '4'
            elif event.key == pygame.K_5:
                brush = '5'
            elif event.key == pygame.K_6:
                brush = '6'
            elif event.key == pygame.K_7:
                brush = '7'
            elif event.key == pygame.K_8:
                brush = '8'
            elif event.key == pygame.K_9:
                brush = '9'
            elif event.key == pygame.K_i:
                # allows to input the number of the type of tile
                num = input("tile: ")
                brush = num

            #save map
            elif event.key == pygame.K_RETURN:
                name = input("Map name:")
                export_map(name)

        elif event.type == pygame.KEYUP:
            # If not pressing down not moving
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            # Follows the mouse motion
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0]/Tiles.size) * Tiles.size
            mouse_y = math.floor(mouse_pos[1]/Tiles.size) * Tiles.size

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Gets the location of the mouse when pressed and makes tile with brush selected
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush] # KEEP AS list

            found = False

            for t in tile_data:
                # Checks if there is a tile or not
                if t[0] == tile[0] and t[1] == tile[1]:
                        found = True
            if not found:
                if not brush == 'r':
                    tile_data.append(tile)
                # if the brush is not removed then add the tile to the tile data
            else:
                if brush == 'r':
                    # Remove the tile from the list if brush is r
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print("Tile removed")
                else:
                    # if not r and there is a tile then say need to remove
                    print("A tile is already placed here")

# Logic
    # moves the camera based on the direction key pressed
    if camera_move == 1:
        camera_y += Tiles.size
    elif camera_move == 2:
        camera_y -=  Tiles.size
    elif camera_move == 3:
        camera_x +=  Tiles.size
    elif camera_move == 4:
        camera_x -=  Tiles.size

    # fills the background
    window.fill((0,0,255))

    # Draw map
    for tile in tile_data:
        try:
            window.blit(Tiles.texture_tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass

    # Draw Tile Highlighter (selector)
    window.blit(selector, (mouse_x, mouse_y))

    pygame.display.update()

    # Uptades the clock
    clock.tick(60)

pygame.quit()
sys.exit()
