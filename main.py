import pygame
import pytmx


pygame.init()
BLACK = (0, 0, 0)
RED = (255, 0, 0)

display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
gameMap = pytmx.load_pygame("Tiles\provona.tmx")
FPS=60
spostamento_x=-725
spostamento_y=-850
var_spost = 3
x_blocco=1013
y_blocco=1138

def blit_button(pos_x, pos_y, dim_x, dim_y, color, image_def):
    button=pygame.Rect(pos_x, pos_y, dim_x, dim_y)
    image = pygame.image.load('IMAGESOW/wood.jpg')
    image= pygame.transform.scale(image, (dim_x,dim_y)) 
    display.blit(image, button)
    return button

controllo_up=0
controllo_down=0
controllo_dx=0
controllo_sx=0

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
            if controllo_sx==0:
                spostamento_x+=var_spost
                x_blocco-=var_spost
        if keys[pygame.K_RIGHT]:
            if controllo_dx==0:
                spostamento_x-=var_spost
                x_blocco+=var_spost
        if keys[pygame.K_UP]:
            if controllo_up==0:
                spostamento_y+=var_spost
                y_blocco-=var_spost
        if keys[pygame.K_DOWN]:
            if controllo_down==0:
                spostamento_y-=var_spost
                y_blocco+=var_spost
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
            controllo_up=0
            controllo_down=0
            controllo_dx=0
            controllo_sx=0
            if layer.name == "hit block":
                for obj in layer:
                    if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(block) == True:
                        if obj.x>x_blocco:
                            controllo_dx=1
                        elif (obj.x+obj.width-4)<x_blocco:
                            controllo_sx=1
                        if obj.y>y_blocco:
                            controllo_down=1
                        elif (obj.y+obj.height-4)<y_blocco:
                            controllo_up=1
                    
    
    
    a=blit_button(288, 288, 24, 24, RED, "wood.jpg")
    #print ('tick={}, fps={}'.format(clock.tick(FPS), clock.get_fps()))
    pygame.display.update()