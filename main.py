import pygame as pg
from random import randint
from sprites import *

pg.init()

bg = pg.image.load("TilesetGraveyard.png")

WHITE = (255,255,255)
BLACK = (0,0,0)
DARKRED = (126,0,0)
DARKGREEN = (0,126,0)
BLUE = (150,222,209)
COOLGREEN = (175,225,175)
RANDOM = (153,223,67)

WIDTH = 1000
HEIGHT = 1000

box_color = RANDOM

all_sprites = pg.sprite.Group()
enemy_group = pg.sprite.Group()
enemy_group_spawn_ghost = pg.sprite.Group()
enemy_group_spawn_skeleton = pg.sprite.Group()

digger = Player()
skeleton = Enemy()
ghost = Enemy2()
all_sprites.add(digger)

selfrand = randint(1,5)




screen = pg.display.set_mode((WIDTH,HEIGHT))


FPS = 120
clock = pg.time.Clock()
liv = 100

comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
print(digger.liv)

text_player_hp = comic_sans30.render("HP: " + str(digger.liv), False, (DARKRED))



playing = True
while playing: #gameloop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    screen.fill(COOLGREEN)
    screen.blit(bg, (0, 0))

    all_sprites.update() # kjør update funskjon til alle sprites i all_sprites
    hits = pg.sprite.spritecollide(digger, enemy_group, True)
    if hits:
        digger.liv -=10
        print("LIV: ", digger.liv)
        text_player_hp = comic_sans30.render("HP: " + str(digger.liv), False, (DARKRED))
        if digger.liv <= 0:
            digger.kill()
            digger = Player()
            all_sprites.add(digger)
            


    #lag nye fiender
    if len(enemy_group_spawn_skeleton) < 3:
        skeleton = Enemy()
        all_sprites.add(skeleton)
        enemy_group.add(skeleton)
        enemy_group_spawn_skeleton.add(skeleton)

    if len(enemy_group_spawn_ghost) < 3:
        ghost = Enemy2()
        all_sprites.add(ghost)
        enemy_group.add(ghost)
        enemy_group_spawn_ghost.add(ghost)


    
    

    all_sprites.draw(screen) # tegner alle sprites i gruppen all_sprites til screen
    
    screen.blit(text_player_hp, (10, 10))

   
    
    pg.display.update()

