import pygame, sys, time
import Textures
import glob

pygame.init()

pygame.font.init()
fps_font = pygame.font.Font(None, 20)

sky = pygame.image.load("Graphics/sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

map_data = []

for x in range(10):
    for y in range(6):
        map_data.append((x,y, "1"))
for x in range(10, 15):
    for y in range(6, 10):
        map_data.append((x,y,"2"))

def show_fps():
#Shows fps on the screen
    fps_overlay = fps_font.render(str(FPS), True, (255,0,0))
    window.blit(fps_overlay,(0,0))

def create_window():
#Creates the window for the game

    global window, window_height, window_width, window_title

    window_width, window_height = 800, 600
    window_title = "Glasbot"
    #Makes the window width set to default as well as adds the title

    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    #Actually makes the window with the title

cSec = 0
cFrame = 0
FPS = 0

def count_fps():
#Keeps track of the fps of the game

    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime("%S"):
        cFrame += 1
        #Adding the amount of frames
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        #Setting the value for FPS in that second and resetting process
        if FPS > 0:
            deltatime = 1/FPS

#Calls the function to make the window
create_window()

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
            elif event.key == pygame.K_s:
                glob.Globals.camera_move = 2
            elif event.key == pygame.K_a:
                glob.Globals.camera_move = 3
            elif event.key == pygame.K_d:
                glob.Globals.camera_move = 4

        elif event.type == pygame.KEYUP:
            glob.Globals.camera_move = 0

    #LOGIC

    if glob.Globals.camera_move == 1:
        glob.Globals.camera_y += deltatime * 100
    elif glob.Globals.camera_move == 2:
        glob.Globals.camera_y -= deltatime * 100
    elif glob.Globals.camera_move == 3:
        glob.Globals.camera_x += deltatime * 100
    elif glob.Globals.camera_move == 4:
        glob.Globals.camera_x -= deltatime * 100

    #RENDER GRAPHICS
    #Makes the background filled black
    # window.fill((0,0,0))

    window.blit(Sky, (0,0))

    # - Render simple Terrain Grid
    for x in range(0,640,Textures.Tiles.size):
        for y in range(0, 480, Textures.Tiles.size):
            # pygame.draw.rect(window, (255, 255, 255), (x,y,tile_size+1,tile_size+1),1)
            # window.blit(Textures.Tiles.grass, (x + glob.Globals.camera_x,y + glob.Globals.camera_y))
            for i in map_data:
                tile = (i[0] * Textures.Tiles.size, i[1]*Textures.Tiles.size)
                if(x,y) == tile:
                    window.blit(Textures.Tiles.texture_tags[i[2]], (x+glob.Globals.camera_x, y+glob.Globals.camera_y))


    show_fps()

    pygame.display.update()

    count_fps()

pygame.quit()
sys.exit()
