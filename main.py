import pygame as pg

from random import randint

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
DARKRED = (126,0,0)
DARKGREEN = (0,126,0)
BLUE = (150,222,209)
COOLGREEN = (175,225,175)
RANDOM = (153,223,67)

box_color = RANDOM

screen = pg.display.set_mode((900,900))

fps_counter = 0

x = 50
y = 50

speed = 4

direction_x = 1
direction_y = 1

FPS = 120
clock = pg.time.Clock()

character = pg.image.load("lIdle_0.png")
character = pg.transform.scale(character, (100,100))

playing = True
while playing: #gameloop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    screen.fill(COOLGREEN)
    

    #move box
    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= speed
    if keys[pg.K_a]:
        x -= speed
    if keys[pg.K_s]:
        y += speed
    if keys[pg.K_d]:
        x += speed
    
    # skjekk hvis utfor skjerm

    

    if x > 820:
        x = 820
        #box_color= (randint(0,255),randint(0,255),randint(0,255))
    
    if x < -25:
        x = -25
        #box_color= (randint(0,255),randint(0,255),randint(0,255))
    
    if y > 800:
        y = 800
        #box_color= (randint(0,255),randint(0,255),randint(0,255))
    
    if y < -30:
        y = -30
        #box_color= (randint(0,255),randint(0,255),randint(0,255))


    


    #box = pg.Rect(x,y, 50,50)
    #pg.draw.rect(screen, box_color, box)

    screen.blit(character, (x, y,))
    

   
    
    pg.display.update()

