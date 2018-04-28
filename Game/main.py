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

current_map = 'maps/map1'
pygame.init()

# intializes fonts for the game
pygame.font.init()
fps_font = pygame.font.Font(None, 20)
amount_font = pygame.font.Font(None, 20)

# Makes the background behind the map
sky = pygame.image.load("Graphics/sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

# Makes the logo features to load in the background
logo_img_temp = pygame.image.load('Graphics/back.jpg')
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0, 0))
del logo_img_temp

# loads the map
terrain = Map_engine.load_map(current_map)

# Dialog background
dialog_bkgr = pygame.image.load('Graphics/Text_Box.png')
Dialog_Bkgr = pygame.Surface(dialog_bkgr.get_size(), pygame.HWSURFACE|pygame.SRCALPHA)
Dialog_Bkgr.blit(dialog_bkgr, (0, 0))
Dialog_Bkgr_width, Dialog_Bkgr_height = Dialog_Bkgr.get_size()
del dialog_bkgr

# Reads the map given and makes the data into lists so we can read it
# same as code in the map engine
global tile_data
with open(current_map, "r") as mapfile:
    map_data = mapfile.read()

map_data = map_data.split('-')
print(map_data)

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
    print(tile)
    for p in pos:
        print(p)
        pos[pos.index(p)] = int(p)

    tiles[tiles.index(tile)] = [pos[0] * Tiles.size, pos[1] * Tiles.size, tile[1]]

tile_data = tiles

placeable_tiles = []
placed_tiles = []

# Making a list of tiles that can have tiles placed on top
for tile in tile_data:
    # if dirt
    if tile[2] == '4':
        placeable_tiles.append(tile)


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
    global cSec, cFrame, FPS

    FPS = clock.get_fps()
    if FPS > 0:
        glob.Globals.deltatime = 1/FPS

#Calls the function to make the window
create_window()

# Makes a player and the position of the player
player = Player("player", window_width, window_height)
player_w, player_h = player.width, player.height
player_x = player.x
player_y = player.y

# Creates the items for the inventory and selects the item in hand
item = 'None'
grass = Grass(336, 560)
flower = Flowers(368, 560)
tree = Tree(400, 560)
hoe = Hoe(432, 560)

# Makes a default tile1
tile1 = [0,0,'5']

# makes an enemy
enemy_test = Enemy1(name = 'enemy', pos = (500, 100), target = player)

#INITIALIZE SOUNDS
btnSound = pygame.mixer.Sound('Sounds/btnClick.wav')
enemy_hit_sound = pygame.mixer.Sound('Sounds/enemy_hit.wav')
planting_sound = pygame.mixer.Sound('Sounds/planting.wav')
failed_planting_sound = pygame.mixer.Sound('Sounds/failed_planting.wav')

#INITIALIZE GUI
def Play():
    # Sets the play command to change to the game
    glob.Globals.scene = 'game'
    pygame.mixer.music.load('Music/Abyss(1).wav')
    pygame.mixer.music.play(-1)

def Exit():
    # sets the exit command to quit the game
    global isRunning
    isRunning = False

def Instructions():
    # Instructions command redirects to the instructions page
    glob.Globals.scene = 'instructions'

def Game_over():
    # Game over command redirects to a game over screen
    glob.Globals.scene = 'gameover'

# Buttons for the main menu
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

btnInst = Menu.Button(text = 'Instructions', rect = (0,0,300,60),
                        bg = Color.Gray, fg = Color.White,
                        bgr = Color.CornflowerBlue, tag = ("menu", None))
btnInst.Left = btnPlay.Left
btnInst.Top = btnExit.Top + btnInst.Height + 3
btnInst.Command = Instructions

# Buttons for the instructions screen
btnPlay2 = Inst_screen.Button(text = "Play", rect = (0,0,300,60),
                                bg = Color.Gray, fg = Color.White,
                                bgr = Color.CornflowerBlue, tag = ("instructions", None))
btnPlay2.Left = window_width/2 - btnPlay2.Width - 50
btnPlay2.Top = window_height - btnPlay2.Height - 50
btnPlay2.Command = Play

btnExit2 = Inst_screen.Button(text = 'Exit', rect = (0,0,300,60),
                        bg = Color.Gray, fg = Color.White,
                        bgr = Color.CornflowerBlue, tag = ("instructions", None))
btnExit2.Left = window_width/2 + 50
btnExit2.Top = window_height - btnExit2.Height - 50
btnExit2.Command = Exit

# Buttons for the game over screen
btnExit3 = Gameover.Button(text = 'Exit', rect = (0,0,300,60),
                        bg = Color.Gray, fg = Color.White,
                        bgr = Color.CornflowerBlue, tag = ("gameover", None))
btnExit3.Left = btnPlay.Left
btnExit3.Top = btnPlay.Top + btnExit.Height + 3
btnExit3.Command = Exit

#Title for the menu page and background image
menuTitle = Menu.Text(text = 'GLASBOT', color = Color.Black, font = Font.Large)
menuTitle.Left, menuTitle.Top = window_width/2 - menuTitle.Width/2, 0
logo = Menu.Image(bitmap = logo_img)

# Title for the instructions page
instTitle = Inst_screen.Text(text = 'INSTRUCTIONS', color = Color.White, font = Font.Large)
instTitle.Left, instTitle.Top = window_width/2 - instTitle.Width/2, 0

# Game over page title
goverTitle = Gameover.Text(text = 'GAME OVER', color = Color.Red, font = Font.Large)
goverTitle.Left, goverTitle.Top = window_width/2 - goverTitle.Width/2, 200

isRunning = True
#Variable that is consistent when the game is running

#Game loop created when the game is running
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        #exits the game
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not glob.Globals.dialog_open:
                # Sees which direction the player want to move and makes sure no dialog
                glob.Globals.camera_move = 1
                # Sets the camera movement to match this
                player.facing = item + 'north'
                # Updates the player direction based on the movement
            elif event.key == pygame.K_s and not glob.Globals.dialog_open:
                glob.Globals.camera_move = 2
                player.facing = item + 'south'
            elif event.key == pygame.K_a and not glob.Globals.dialog_open:
                glob.Globals.camera_move = 3
                player.facing = item + 'east'
            elif event.key == pygame.K_d and not glob.Globals.dialog_open:
                glob.Globals.camera_move = 4
                player.facing = item + 'west'

            if event.key == pygame.K_RETURN:
                # for dialog purposes - moving forward
                if glob.Globals.dialog_open:
                    #handle next page of dialog
                    if glob.Globals.active_dialog.page < len(glob.Globals.active_dialog.text) - 1:
                        glob.Globals.active_dialog.page += 1
                    else:
                        glob.Globals.dialog_open = False
                        glob.Globals.active_dialog.page = 0
                        glob.Globals.active_dialog = None
                        for npc in NPC.all_npc:
                            # Updates the timer
                            if not npc.timer.active:
                                npc.timer.start()
                else:
                    #if dialog isnt open
                    for npc in NPC.all_npc:
                        speaking = False
                        #if player in speech bounds
                        #makes npc coordinates match player coordinates - both by tile now
                        npc_x = npc.x / Tiles.size
                        npc_y = npc.y / Tiles.size
                        if player_x >= npc_x - 2 and player_x <= npc_x + 2 and player_y >= npc_y -2 and player_y <= npc_y + 2:
                            #PLAYER IS NEXT TO NPC (needs to check if they are facing them--)
                            if round(player.y) >= round(npc.y / Tiles.size):
                                # sees where the player is relative to the npc
                                if player.facing == 'hoenorth' or 'flowernorth' or 'treenorth' or 'grassnorth':
                                    # checks to make sure they are facing the npc
                                    speaking = True #says they are speaking
                            elif round(player.y) <= round(npc.y / Tiles.size):
                                if player.facing == 'hoesouth' or 'flowersouth' or 'treesouth' or 'grasssouth':
                                    speaking = True
                            elif round(player.x) >= round(npc.x / Tiles.size):
                                if player.facing == 'hoeeast' or 'flowereast' or 'treeeast' or 'grasseast':
                                    speaking = True
                            elif round(player.x) <= round(npc.x / Tiles.size):
                                if player.facing == 'hoewest' or 'flowerwest' or 'treewest' or 'grasswest':
                                    speaking = True
                        if speaking == True:
                            # opens the dialog if they are speaking
                            glob.Globals.dialog_open = True
                            glob.Globals.active_dialog = npc.dialog
                            npc.timer.pause()
                            npc.walking = False
            elif event.key == pygame.K_ESCAPE:
                # exits the game
                isRunning = False
            elif event.key == pygame.K_1:
                # Updates the image in hand based on the key pressed for inventory
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
                if item == 'hoe':
                    hit = False
                    # Checks to see if the NPC is hit
                    for npc in NPC.enemy_npcs:
                        if player_x >= npc_x - 4 and player_x <= npc_x + 4 and player_y >= npc_y -4 and player_y <= npc_y + 4:
                            # Checks to see if player is close enough
                            if round(player.y) > round(npc.y / Tiles.size):
                                # sees where the player is relative to the enemy
                                if player.facing == 'hoenorth':
                                    # checks to make sure they are facing the enemy
                                    enemy_hit_sound.play()
                                    npc.health -= hoe.damage
                                    hit = True
                                    # says it has been hit, takes away the damage
                            elif round(player.y) < round(npc.y / Tiles.size):
                                if player.facing == 'hoesouth':
                                    enemy_hit_sound.play()
                                    npc.health -= hoe.damage
                                    hit = True
                            elif round(player.x) > round(npc.x / Tiles.size):
                                if player.facing == 'hoeeast':
                                    enemy_hit_sound.play()
                                    npc.health -= hoe.damage
                                    hit = True
                            elif round(player.x) < round(npc.x / Tiles.size):
                                if player.facing == 'hoewest':
                                    enemy_hit_sound.play()
                                    npc.health -= hoe.damage
                                    hit = True
                            if hit == True:
                                # checks to see if the npc has been hit
                                if npc.facing == 'npc_south':
                                    # moves the npc back based on the direction it is facing
                                    npc.y -= 40
                                elif npc.facing == 'npc_north':
                                    npc.y += 40
                                elif npc.facing == 'npc_east':
                                    npc.x -= 40
                                elif npc.facing == 'npc_west':
                                    npc.x += 40

                if item == 'grass':
                    if grass.amount == 0:
                        # if inventory is empty does not allow to place
                        tile1 = [0,0,'5']
                    else:
                        # if it is in inventory base direction off of way facing and texture out of item
                        if player.facing == 'grasssouth':
                            # makes the tile in the spot in front with the correct texture
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
                contain = False
                # Sees if the position of the tile1 - want to place is in the tiles that can be
                # placed over
                for t in placeable_tiles:
                    if t[0] == tile1[0] and t[1] == tile1[1]:
                        contain = True
                for t in placed_tiles:
                    if t[0] == tile1[0] and t[1] == tile1[1]:
                        contain = False
                if contain:
                    planting_sound.play()
                    # if it is a tile that can be placed over - place the tile
                    terrain.blit(Tiles.texture_tags[tile1[2]],(tile1[0], tile1[1]))
                    # update the score and contents of inventory based on action and item
                    placed_tiles.append(tile1)
                    if item == 'grass':
                        grass.amount -= 1
                        player.points += grass.points
                    elif item =='flowers':
                        flower.amount -= 1
                        player.points += flower.points
                    elif item =='tree':
                        tree.amount -= 1
                        player.points += tree.points
                    else:
                        None
                elif not contain and item != 'hoe' or 'None':
                    # makes a failed planting noise if no seeds
                    failed_planting_sound.play()
                elif item == 'None':
                    None

                contain = False

        elif event.type == pygame.KEYUP:
            # stops movement when no keys pressed down
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
                for btn in Inst_screen.Button.All:
                    if btn.Tag[0] == glob.Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command() #DO BUTTON EVENT
                        btnSound.play()
                        btn.Rolling = False
                        break
                for btn in Gameover.Button.All:
                    if btn.Tag[0] == glob.Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command() #DO BUTTON EVENT
                        btnSound.play()
                        btn.Rolling = False
                        break

    if glob.Globals.scene == 'game':
    #LOGIC
        if glob.Globals.camera_move == 1:
            # moves the camera based on the input
            if not Tiles.blocked_at((round(player_x),math.floor(player_y))):
                # makes sure tile is not blocked
                glob.Globals.camera_y += glob.Globals.deltatime * 100
                # moves the camera over
        elif glob.Globals.camera_move == 2:
            if not Tiles.blocked_at((round(player_x),math.ceil(player_y))):
                glob.Globals.camera_y -= glob.Globals.deltatime * 100
        elif glob.Globals.camera_move == 3:
            if not Tiles.blocked_at((math.floor(player_x),round(player_y))):
                glob.Globals.camera_x += glob.Globals.deltatime * 100
        elif glob.Globals.camera_move == 4:
            if not Tiles.blocked_at((math.ceil(player_x),round(player_y))):
                glob.Globals.camera_x -= glob.Globals.deltatime * 100

        for bag in bag_group:
            # cycles through all the bags
            if len(bag_group) > 0:
                tile = bag.tile
                # blits the bags onto the terrain
                terrain.blit(tile[0], (tile[1], tile[2]))
            if bag.tile[1]/32 == round(player_x):
                if bag.tile[2]/32 == round(player_y):
                    # checks if the player is on top of the bag
                    if bag.type == 'grass':
                        # checks what kind of bag
                        grass.amount += bag.contents
                        # adds the seeds to the inventory
                    elif bag.type == 'flowers':
                        flower.amount += bag.contents
                    elif bag.type == 'tree':
                        tree.amount += bag.contents
                    bag_group.remove(bag)
                    for t in tile_data:
                        # places the tile that was there before on top of the bag to hide it
                        if t[0] == bag.tile[1] and t[1] == bag.tile[2]:
                            terrain.blit(Tiles.texture_tags[t[2]], (t[0], t[1]))
                            print(t)
                else:
                    None

        # updates the player position
        player_x = (window_width/2 - player_w/2 - glob.Globals.camera_x) / Tiles.size
        player_y = (window_height/2 - player_h/2 - glob.Globals.camera_y) / Tiles.size
        player.x = player_x
        player.y = player_y


        if player.health <= 0:
            # if you run out of health
            glob.Globals.scene = 'gameover'
        #RENDER GRAPHICS

        window.blit(Sky, (0,0))
        # blits the background

        window.blit(terrain,(glob.Globals.camera_x, glob.Globals.camera_y))
        # blits the piece of terrain inside the camera view

        for npc in NPC.all_npc:
            # blits all NPCs
            npc.render(window)

        for npc in NPC.enemy_npcs:
            npc_x = npc.x / Tiles.size
            npc_y = npc.y / Tiles.size
            if player_x >= npc_x - 1 and player_x <= npc_x + 1 and player_y >= npc_y -1 and player_y <= npc_y + 1:
                # if the npc reaches the player
                player.health -= 1
                # hurts the player while in contact
                if npc.facing == 'npc_south':
                    # Moves the screen based on the direction of the enemy
                    glob.Globals.camera_y -= 2
                elif npc.facing == 'npc_north':
                    glob.Globals.camera_y += 2
                elif npc.facing == 'npc_east':
                    glob.Globals.camera_x -= 2
                elif npc.facing == 'npc_west':
                    glob.Globals.camera_x += 2
            npc.render(window)
            if npc.health <= 0:
                # if the npc dies - exile him
                npc.x = -1000
                npc.y = -1000
                npc.timer.pause()

        player.render(window, (window_width/2 - player_w/2, window_height/2 - player_h/2))
        # renders the player

        if glob.Globals.dialog_open:
            window.blit(Dialog_Bkgr, (window_width /2 - Dialog_Bkgr_width /2, window_height - Dialog_Bkgr_height -2))

            #DRAW DIALOG TEXT
            if glob.Globals.active_dialog != None:
                lines = glob.Globals.active_dialog.text[Globals.active_dialog.page]
                for line in lines:
                    window.blit(Font.Default.render(line, True, Color.White), (130, (window_height - Dialog_Bkgr_height) + 5 + (lines.index(line) * 25)))

        # blits the score and health to the screen
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


    elif glob.Globals.scene == 'instructions':

        window.fill(Color.Fog)

        for btn in Inst_screen.Button.All:
            if btn.Tag[0] == "instructions":
                btn.Render(window)

        instTitle.Render(window)
        # the instructional text in the game

        one = Inst_screen.Text(text = '1.) Move your player with the w-a-s-d keys, select the item in your inventory with the corresponding 1-4 value ', color = Color.White, font = Font.Small)
        one.Left, one.Top = 0, 100
        one.Render(window)

        two = Inst_screen.Text(text = '2.) Use the item in hand by pressing the space bar next to the tile you want ', color = Color.White, font = Font.Small)
        two.Left, two.Top = 0, 120
        two.Render(window)

        three = Inst_screen.Text(text = '3.) Fight your enemies using the hoe and hitting them (space) until they die without letting them hit you', color = Color.White, font = Font.Small)
        three.Left, three.Top = 0, 140
        three.Render(window)

        four = Inst_screen.Text(text = '4.) Plant seeds on dirt tiles (space) to bring Earth back to life', color = Color.White, font = Font.Small)
        four.Left, four.Top = 0, 160
        four.Render(window)

        five = Inst_screen.Text(text = '- Grass is worth 1 point, flowers are worth 2, and trees are worth 4', color = Color.White, font = Font.Small)
        five.Left, five.Top = 20, 180
        five.Render(window)

        six = Inst_screen.Text(text = '5.) Collect more seeds by grabbing the bags scattered around the map', color = Color.White, font = Font.Small)
        six.Left, six.Top = 0, 200
        six.Render(window)

    elif glob.Globals.scene == 'gameover':
        # the game over screen
        window.fill(Color.Fog)

        goverTitle.Render(window)

        for btn in Gameover.Button.All:
            if btn.Tag[0] == "gameover":
                btn.Render(window)


    show_fps()
    pygame.display.update()
    clock.tick()
    count_fps()

pygame.quit()
sys.exit()
