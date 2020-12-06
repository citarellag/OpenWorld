import pygame
import pytmx


pygame.init()
BLACK = (0, 0, 0)
RED = (255, 0, 0)

display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
gameMap = pytmx.load_pygame("Tiles\provona.tmx")
FPS=300
spostamento_x=0
spostamento_y=0

def blit_button(pos_x, pos_y, dim_x, dim_y, color, image_def):
    button=pygame.Rect(pos_x, pos_y, dim_x, dim_y)
    image = pygame.image.load('IMAGESOW/wood.jpg')
    image= pygame.transform.scale(image, (dim_x,dim_y)) 
    display.blit(image, button)


while True:
    display = pygame.display.set_mode((600,600))
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
            quit()
        if keys[pygame.K_LEFT]: 
                spostamento_x+=2
        if keys[pygame.K_RIGHT]:
                spostamento_x-=2
        if keys[pygame.K_UP]:
                spostamento_y+=2
        if keys[pygame.K_DOWN]:
                spostamento_y-=2

    display.fill(BLACK)
    for layer in gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = gameMap.get_tile_image_by_gid(gid)
                if(tile != None):
                    display.blit(tile, (x * gameMap.tilewidth+spostamento_x, y * gameMap.tileheight+spostamento_y))
    blit_button(288, 288, 24, 24, RED, "wood.jpg")
    print ('tick={}, fps={}'.format(clock.tick(FPS), clock.get_fps()))

    pygame.display.update()