import pygame
from pygame import mixer

#Imposto i colori
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Inizializzo pygame 
pygame.init() 
mixer.init()
#creo lo schermo e il clock
x_main=480
y_main=533

clock = pygame.time.Clock()
FPS = 120
 


def blit_background(pos_x, pos_y, dim_x, dim_y, color, image_def):
    button=pygame.Rect(pos_x, pos_y, dim_x, dim_y)
    image = pygame.image.load('IMAGESOW/gradientbg.jpeg')
    image= pygame.transform.scale(image, (dim_x,dim_y)) 
    main.blit(image, button)

def blit_button(pos_x, pos_y, dim_x, dim_y, color, image_def):
    button=pygame.Rect(pos_x, pos_y, dim_x, dim_y)
    image = pygame.image.load('IMAGESOW/wood.jpg')
    image= pygame.transform.scale(image, (dim_x,dim_y)) 
    main.blit(image, button)
x=0
y=0

while True:
    main =pygame.display.set_mode((x_main, y_main))
    main.fill(BLACK)

    blit_background(x,y, 6000, 4000, RED, "gradientbg.jpeg")
    blit_button(240, 250, 30, 30, RED, "wood.jpg")

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
            quit()
        if keys[pygame.K_LEFT]: 
                x+=10
        if keys[pygame.K_RIGHT]:
                x-=10
        if keys[pygame.K_UP]:
                y+=10
        if keys[pygame.K_DOWN]:
                y-=10



    pygame.display.update()