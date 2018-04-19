import pygame, sys, time, math
import Textures
import glob
from mapengine import *
from player import *
from NPC import *
from inventory import *
from meloonatic_gui import *
from UltraColor import *


pygame.init()

pygame.font.init()
fps_font = pygame.font.Font(None, 20)

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

# global tile_data
# with open("maps/testmap", "r") as mapfile:
#     map_data = mapfile.read()
#
# map_data = map_data.split('-')
#
# map_size = map_data[len(map_data)-1]
# map_data.remove(map_size)
# map_size = map_size.split(",")
# map_size[0] = int(map_size[0]) * Tiles.size
# map_size[1] = int(map_size[1]) * Tiles.size
#
# tiles = []
#
# for tile in range(len(map_data)):
#     map_data[tile] = map_data[tile].replace('\n','')
#     tiles.append(map_data[tile].split(":"))
#
# for tile in tiles:
#     tile[0] = tile[0].split(",")
#     pos = tile[0]
#     for p in pos:
#         pos[pos.index(p)] = int(p)
#
# tiles[tiles.index(tile)] = [pos[0] * Tiles.size, pos[1] * Tiles.size, tile[1]]
#
# tile_data = tiles
#


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

grass = Grass()
grass_group = pygame.sprite.Group()
grass_group.add(grass)

flower = Flowers()
flower_group = pygame.sprite.Group()
flower_group.add(flower)

tree = Tree()
tree_group = pygame.sprite.Group()
tree_group.add(tree)


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
                if item == 'grass':
                    player.points += grass.points
                    if player.facing == 'grasssouth':
                        # Map_engine.add_tile(Tiles.texture_tags['1'], (100,100), overlay)
                        # grass_group.add(Grass(368,300))
                        # tile1 = [glob.Globals.camera_x, glob.Globals.camera_y, '3']
                        # for t in tile_data:
                        #     if t[0] == tile1[0] and t[1] == tile1[1] and t[2] != '3':
                        #         tile_data.remove(t)
                        #         tile_data.append(tile1)
                        #     else:
                        #         None
                    elif player.facing == 'grassnorth':
                        None
                    elif player.facing == 'grasswest':
                        None
                    elif player.facing == 'grasseast':
                        None
                elif item == 'flowers':
                    player.points += flower.points
                elif item == 'tree':
                    player.points += tree.points
                elif item == 'hoe':
                    None
                elif item == 'None':
                    None
                print(player.facing)

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

        grass_group.draw(window)
        flower_group.draw(window)
        tree_group.draw(window)

        player.render(window, (window_width/2 - player_w/2, window_height/2 - player_h/2))


        text = fps_font.render("Score: %s" % player.points, 1, (255, 0, 0))
        textpos = text.get_rect(centerx= 200, centery = 50)
        window.blit(text, textpos)

        htext = fps_font.render("Health: %s" % player.health, 1, (255, 0, 0))
        hpos = htext.get_rect(centerx = 100, centery = 50)
        window.blit(htext, hpos)

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
