import pygame
import pytmx


pygame.init()
BLACK = (0, 0, 0)
RED = (255, 0, 0)

display = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
gameMap = pytmx.load_pygame("Tiles\provona.tmx")
FPS=60
spostamento_x=0
spostamento_y=0
x_blocco=288
y_blocco=288

def blit_button(pos_x, pos_y, dim_x, dim_y, color, image_def):
    button=pygame.Rect(pos_x, pos_y, dim_x, dim_y)
    image = pygame.image.load('IMAGESOW/wood.jpg')
    image= pygame.transform.scale(image, (dim_x,dim_y)) 
    display.blit(image, button)
    return button


while True:
    display = pygame.display.set_mode((600,400))
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
            quit()
        if keys[pygame.K_LEFT]: 
                spostamento_x+=3
                x_blocco-=3
        if keys[pygame.K_RIGHT]:
                spostamento_x-=3
                x_blocco+=3
        if keys[pygame.K_UP]:
                spostamento_y+=3
                y_blocco-=3
        if keys[pygame.K_DOWN]:
                spostamento_y-=3
                y_blocco+=3
    block = pygame.Rect(x_blocco, y_blocco, 24, 24)
    #print("x e y blocco:", x_blocco,y_blocco, "x e t spost", spostamento_x, spostamento_y)
    display.fill(BLACK)
    layer_index = 0
    for layer in gameMap.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x in range(0, 64):
                for y in range(0, 62):
                    image = gameMap.get_tile_image(x, y, layer_index)
                    if image != None:
                        display.blit(image, (x * gameMap.tilewidth+spostamento_x, y * gameMap.tileheight+spostamento_y))
        layer_index += 1
        if isinstance(layer, pytmx.TiledObjectGroup):
            if layer.name == "hit block":
                for obj in layer:
                    if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(block) == True:
                        print ("GIA LO SAI!!")
                        break
    
    a=blit_button(288, 288, 24, 24, RED, "wood.jpg")
    #print ('tick={}, fps={}'.format(clock.tick(FPS), clock.get_fps()))

    pygame.display.update()