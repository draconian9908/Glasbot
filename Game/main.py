import pygame, sys, time, math
import Textures
import glob
from mapengine import *
from player import *
from NPC import *
from inventory import *
from meloonatic_gui import *
from UltraColor import *
from collectable import *


pygame.init()

pygame.font.init()
fps_font = pygame.font.Font(None, 20)
amount_font = pygame.font.Font(None, 20)

sky = pygame.image.load("Graphics/sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

logo_img_temp = pygame.image.load('Graphics/back.jpg')
#logo_img_temp = pygame.transform.scale(logo_img_temp, (900, 420))
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0, 0))
del logo_img_temp


terrain = Map_engine.load_map("maps/testmap")


# Reads the map given and makes the data into lists so we can read it
global tile_data
with open('maps/testmap', "r") as mapfile:
    map_data = mapfile.read()

map_data = map_data.split('-')

map_size = map_data[len(map_data)-1]
map_data.remove(map_size)
map_size = map_size.split(",")
map_size[0] = int(map_size[0]) * Tiles.size
map_size[1] = int(map_size[1]) * Tiles.size

tiles = []

for tile in range(len(map_data)):
    map_data[tile] = map_data[tile].replace('\n','')
    tiles.append(map_data[tile].split(":"))

for tile in tiles:
    tile[0] = tile[0].split(",")
    pos = tile[0]
    for p in pos:
        pos[pos.index(p)] = int(p)

    tiles[tiles.index(tile)] = [pos[0] * Tiles.size, pos[1] * Tiles.size, tile[1]]

tile_data = tiles

placeable_tiles = []

# Making a list of tiles that can have tiles placed on top - right now set to grass, dirt, tree and flower
for tile in tile_data:
    # if grass
    if tile[2] == '1':
        placeable_tiles.append(tile)
    # if dirt
    if tile[2] == '4':
        placeable_tiles.append(tile)
    # if flower
    if tile[2] == '6':
        placeable_tiles.append(tile)
    # if tree
    if tile[2] == '7':
        placeable_tiles.append(tile)

print(placeable_tiles)

def show_fps():
#Shows fps on the screen
    fps_overlay = fps_font.render(str(FPS), True, (255,0,0))
    window.blit(fps_overlay,(0,0))

def create_window():
#Creates the window for the game

    global window, window_height, window_width, window_title, clock

    window_width, window_height = 800, 600
    window_title = "Glasbot"
    #Makes the window width set to default as well as adds the title

    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    #Actually makes the window with the title
    clock = pygame.time.Clock()

cSec = 0
cFrame = 0
FPS = 0

def count_fps():
#Keeps track of the fps of the game

    global cSec, cFrame, FPS, deltatime

    FPS = clock.get_fps()
    if FPS > 0:
        deltatime = 1/FPS

#Calls the function to make the window
create_window()

player = Player("player")
player_w, player_h = player.width, player.height
player_x = round(window_width/2 - player_w/2 - glob.Globals.camera_x) / Tiles.size
player_y = round(window_height/2 - player_h/2 - glob.Globals.camera_y) / Tiles.size

item = 'None'
grass = Grass(336, 560)
flower = Flowers(368, 560)
tree = Tree(400, 560)
hoe = Hoe(432, 560)

tile1 = [0,0,'5']

#INITIALIZE MUSIC
pygame.mixer.music.load('Music/title.wav')
pygame.mixer.music.play(-1)
#INITIALIZE SOUNDS
btnSound = pygame.mixer.Sound('Sounds/btnClick.wav')


#INITIALIZE GUI
def Play():
    glob.Globals.scene = 'game'
    pygame.mixer.music.load('Music/Hero - Logic Type Beat.wav')
    pygame.mixer.music.play(-1)

def Exit():
    global isRunning
    isRunning = False

btnPlay = Menu.Button(text = "Play", rect = (0,0,300,60),
                                bg = Color.Gray, fg = Color.White,
                                bgr = Color.CornflowerBlue, tag = ("menu", None))
btnPlay.Left = window_width /2 - btnPlay.Width/2
btnPlay.Top = window_height/2 - btnPlay.Height/2
btnPlay.Command = Play

btnExit = Menu.Button(text = 'Exit', rect = (0,0,300,60),
                        bg = Color.Gray, fg = Color.White,
                        bgr = Color.CornflowerBlue, tag = ("menu", None))
btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 3
btnExit.Command = Exit

menuTitle = Menu.Text(text = 'GLASBOT', color = Color.Black, font = Font.Large)

menuTitle.Left, menuTitle.Top = window_width/2 - menuTitle.Width/2, 0

logo = Menu.Image(bitmap = logo_img)

isRunning = True
#Variable that is consistent when the game is running

#Game loop created when the game is running
while isRunning:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        #exits the game
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                glob.Globals.camera_move = 1
                player.facing = item + 'north'
            elif event.key == pygame.K_s:
                glob.Globals.camera_move = 2
                player.facing = item + 'south'
            elif event.key == pygame.K_a:
                glob.Globals.camera_move = 3
                player.facing = item + 'east'
            elif event.key == pygame.K_d:
                glob.Globals.camera_move = 4
                player.facing = item + 'west'

            elif event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_1:
                item = 'grass'
            elif event.key == pygame.K_2:
                item = 'flowers'
            elif event.key == pygame.K_3:
                item = 'tree'
            elif event.key == pygame.K_4:
                item = 'hoe'

            # plant
            elif event.key == pygame.K_SPACE:
                # Placement directions
                x_south_north = round((window_width/2 - player_w/2 - glob.Globals.camera_x)/Tiles.size)*Tiles.size
                y_south = round((window_height/2 - player_h/2 - glob.Globals.camera_y +32)/Tiles.size)*Tiles.size
                y_north = round((window_height/2 - player_h/2 - glob.Globals.camera_y - 32)/Tiles.size)*Tiles.size

                y_west_east = round((window_height/2 - player_h/2 - glob.Globals.camera_y)/Tiles.size)*Tiles.size
                x_west = round((window_width/2 - player_w/2 - glob.Globals.camera_x +32)/Tiles.size)*Tiles.size
                x_east = round((window_width/2 - player_w/2 - glob.Globals.camera_x - 32)/Tiles.size)*Tiles.size

                # Texture packs
                grass_texture = '1'
                flower_texture = '6'
                tree_texture = '7'

                # Sees which item is in hand and then makes sure there are seeds to place
                if item == 'grass':
                    if grass.amount == 0:
                        # if inventory is empty does not allow to place
                        tile1 = [0,0,'5']
                    else:
                        # if it is in inventory base direction off of way facing and texture out of item
                        if player.facing == 'grasssouth':
                            tile1 = [x_south_north, y_south, grass_texture]
                        elif player.facing == 'grassnorth':
                            tile1 = [x_south_north, y_north, grass_texture]
                        elif player.facing == 'grasswest':
                            tile1 = [x_west, y_west_east, grass_texture]
                        elif player.facing == 'grasseast':
                            tile1 = [x_east, y_west_east , grass_texture]
                elif item == 'flowers':
                    if flower.amount == 0:
                        tile1 = [0,0,'5']
                    else:
                        if player.facing == 'flowerssouth':
                            tile1 = [x_south_north, y_south, flower_texture]
                        elif player.facing == 'flowersnorth':
                            tile1 = [x_south_north, y_north, flower_texture]
                        elif player.facing == 'flowerswest':
                            tile1 = [x_west, y_west_east, flower_texture]
                        elif player.facing == 'flowerseast':
                            tile1 = [x_east, y_west_east, flower_texture]
                elif item == 'tree':
                    if tree.amount == 0:
                        tile1 = [0,0,'5']
                    else:
                        if player.facing == 'treesouth':
                            tile1 = [x_south_north, y_south, tree_texture]
                        elif player.facing == 'treenorth':
                            tile1 = [x_south_north, y_north, tree_texture]
                        elif player.facing == 'treewest':
                            tile1 = [x_west, y_west_east, tree_texture]
                        elif player.facing == 'treeeast':
                            tile1 = [x_west, y_west_east, tree_texture]

                # Tile1 is reassigned to match the direction and item in hand

                # Sees if the position of the tile1 - want to place is in the tiles that can be
                # placed over
                for t in placeable_tiles:
                    if t[0] == tile1[0] and t[1] == tile1[1]:
                        contain = True
                if contain:
                    # if it is a tile that can be placed over - place the tile
                    terrain.blit(Tiles.texture_tags[tile1[2]],(tile1[0], tile1[1]))
                    # update the score and contents of inventory based on action and item
                    if item == 'grass':
                        grass.amount -= 1
                        player.points += grass.points
                    elif item =='flowers':
                        flower.amount -= 1
                        player.points += flower.points
                    elif item =='tree':
                        tree.amount -= 1
                        player.points += tree.points

                elif item == 'hoe':
                    None
                elif item == 'None':
                    None
                print(player.facing)

                contain = False


        elif event.type == pygame.KEYUP:
            glob.Globals.camera_move = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #LEFT CLICK
                for btn in Menu.Button.All:
                    if btn.Tag[0] == glob.Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command() #DO BUTTON EVENT
                        btnSound.play()
                        btn.Rolling = False
                        break

    #RENDER SCENEelif glob.Globals.scene == 'menu':

    if glob.Globals.scene == 'game':

    #LOGIC

        if glob.Globals.camera_move == 1:
            if not Tiles.blocked_at((round(player_x),math.floor(player_y))):
                glob.Globals.camera_y += deltatime * 100
        elif glob.Globals.camera_move == 2:
            if not Tiles.blocked_at((round(player_x),math.ceil(player_y))):
                glob.Globals.camera_y -= deltatime * 100
        elif glob.Globals.camera_move == 3:
            if not Tiles.blocked_at((math.floor(player_x),round(player_y))):
                glob.Globals.camera_x += deltatime * 100
        elif glob.Globals.camera_move == 4:
            if not Tiles.blocked_at((math.ceil(player_x),round(player_y))):
                glob.Globals.camera_x -= deltatime * 100


        player_x = (window_width/2 - player_w/2 - glob.Globals.camera_x) / Tiles.size
        player_y = (window_height/2 - player_h/2 - glob.Globals.camera_y) / Tiles.size

        #RENDER GRAPHICS

        window.blit(Sky, (0,0))

        window.blit(terrain,(glob.Globals.camera_x, glob.Globals.camera_y))

        player.render(window, (window_width/2 - player_w/2, window_height/2 - player_h/2))


        text = fps_font.render("Score: %s" % player.points, 1, (255, 255, 255))
        textpos = text.get_rect(centerx= 200, centery = 50)
        window.blit(text, textpos)

        htext = fps_font.render("Health: %s" % player.health, 1, (255, 255, 255))
        hpos = htext.get_rect(centerx = 100, centery = 50)
        window.blit(htext, hpos)

        # inventory display

        # inventory title blit
        itext = fps_font.render("Inventory", 1, (255, 255, 255))
        ipos = htext.get_rect(centerx = 400, centery = 550)
        window.blit(itext, ipos)

        # Display the tiles at bottom of the screen
        window.blit(grass.image, (grass.rect.x, grass.rect.y))
        window.blit(flower.image, (flower.rect.x, flower.rect.y))
        window.blit(tree.image, (tree.rect.x, tree.rect.y))
        window.blit(hoe.image, (hoe.rect.x, hoe.rect.y))

        # Display the amounts in the inventory on the pictures at bottom of the screen
        gatext = amount_font.render("%s" % grass.amount, 1, (255,255,255))
        gapos = gatext.get_rect(centerx = 356, centery = 580)
        window.blit(gatext, gapos)

        fltext = amount_font.render("%s" % flower.amount, 1, (255,255,255))
        flpos = fltext.get_rect(centerx = 388, centery = 580)
        window.blit(fltext, flpos)

        trtext = amount_font.render("%s" % tree.amount, 1, (255,255,255))
        trpos = trtext.get_rect(centerx = 420, centery = 580)
        window.blit(trtext, trpos)

        # Will display the white border on top of corresponding inventory item based on selected item in hand
        if item == 'grass':
            window.blit(pygame.image.load("Graphics/border.png"), (grass.rect.x, grass.rect.y))
        elif item == 'flowers':
            window.blit(pygame.image.load("Graphics/border.png"), (flower.rect.x, flower.rect.y))
        elif item == 'tree':
            window.blit(pygame.image.load("Graphics/border.png"), (tree.rect.x, tree.rect.y))
        elif item == 'hoe':
            window.blit(pygame.image.load("Graphics/border.png"), (hoe.rect.x, hoe.rect.y))

        for bag in bag_group:
            tile = bag.tile
            terrain.blit(tile[0], (tile[1], tile[2]))


        #PROCESS MENU
    elif glob.Globals.scene == 'menu':
        window.fill(Color.Fog)

        logo.Render(window, (0, -70))
        logo.Left = window_width/2 - logo.Width/2
        #logo.Top = window_height/2 - logo.Height/2

        menuTitle.Render(window)

        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                btn.Render(window)

    show_fps()
    pygame.display.update()
    clock.tick()
    count_fps()

pygame.quit()
sys.exit()
