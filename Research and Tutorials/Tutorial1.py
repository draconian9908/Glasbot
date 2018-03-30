import pygame, sys, time

pygame.init()

pygame.font.init()
fps_font = pygame.font.Font(None, 20)

tile_size = 32

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

    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
        #Adding the amount of frames
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        #Setting the value for FPS in that second and resetting process

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

    #LOGIC
    count_fps()

    #RENDER GRAPHICS
    #Makes the background filled black
    window.fill((0,0,0))

    # - Render simple Terrain Grid
    for x in range(0,640,tile_size):
        for y in range(0, 480, tile_size):
            pygame.draw.rect(window, (255, 255, 255), (x,y,tile_size+1,tile_size+1),1)


    show_fps()

    pygame.display.update()

pygame.quit()
sys.exit()
