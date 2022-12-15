import pygame as pg
vec = pg.math.Vector2
from random import randint, choices


character = pg.image.load("lIdle_0.png") #characterleft0
character = pg.transform.scale(character, (45,60)) 

characterleft1 = pg.image.load("lidle_1.png")
characterleft1 = pg.transform.scale(character, (45,55))

characterleft2 = pg.image.load("lidle_2.png")
characterleft2 = pg.transform.scale(characterleft2, (45,60))

characterleft3 = pg.image.load("lidle_3.png")
characterleft3 = pg.transform.scale(characterleft3, (45,65))


characterright = pg.image.load("rIdle_0.png")
characterright = pg.transform.scale(characterright, (45,60))

characterright1 = pg.image.load("ridle_1.png")
characterright1 = pg.transform.scale(characterright1, (45,55))

characterright2 = pg.image.load("ridle_2.png")
characterright2 = pg.transform.scale(characterright2, (45,60))

characterright3 = pg.image.load("ridle_3.png")
characterright3 = pg.transform.scale(characterright3, (45,65))


characterfront = pg.image.load("rTurn_2.png")
characterfront = pg.transform.scale(characterfront, (45,60))

characterfront1 = pg.image.load("rTurn_1.png")
characterfront1 = pg.transform.scale(characterfront1, (45,60))


skeleton = pg.image.load("lIdle_0S.png")
skeleton = pg.transform.scale(skeleton, (90,90))

ghost = pg.image.load("lIdleWalkRun_0.png")
ghost = pg.transform.scale(ghost, (90,90))

slime = pg.image.load("slime_lidle_0.png")
slime = pg.transform.scale(slime, (30,30))

dead_screen = pg.image.load("dead_screen.jpg")
dead_screen = pg.transform.scale(dead_screen, (500,550))

projectile = pg.image.load("projectile_img.png")
projectile = pg.transform.scale(projectile, (20,20))

health_potion = pg.image.load("health_potion_image.png")
health_potion = pg.transform.scale(health_potion, (30,30))

run_potion = pg.image.load("run_potion_image.png")
run_potion = pg.transform.scale(run_potion, (30,30))

birth_screen = pg.image.load("curch_.png")
birth_screen = pg.transform.scale(birth_screen, (1820,1300))


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        pg.sprite.Sprite.__init__(self)
        self.image = character
        self.rect = self.image.get_rect() # henter self.image sin størrelse og lager en hitbox
        self.pos = vec(500,500)
        self.rect.center = self.pos
        self.speed = 2
        self.speed_boost = 2
        self.liv = 50
        self.max_liv = 50
        self.score = 0
        self.current_frame = 0
        self.last_update = 0
        self.direction_x = 0
        self.direction_y = 0

        self.standing_left = False
        self.standing_right = False
        self.standing_down = False
        self.running_left = False
        self.running_right = False
        
        
        self.standing_right_frames = [characterright, characterright1, characterright2, characterright3]

    
        self.standing_left_frames = [character, characterleft1, characterleft2, characterleft3]

   
        self.standing_down_frames = [characterfront, characterfront1]
        

        

    def update(self):    
        self.rect.center = self.pos # flytter rect til character til ny posisjon hver frame
        
        if self.pos.y < 285:
            self.pos.y = 285
        
        if self.pos.y > 960:
            self.pos.y = 960
        
        if self.pos.x < 30:
            self.pos.x = 30

        if self.pos.x > 970:
            self.pos.x = 970

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.standing_down = True
            self.standing_left = False
            self.standing_right = False
            self.image = characterfront
            self.pos.y -= self.speed

        if keys[pg.K_a]:
            self.standing_left = True
            self.standing_right = False
            self.standing_down = False
            self.image = character
            self.pos.x -= self.speed

        if keys[pg.K_s]:
            self.standing_down = True
            self.standing_right = False
            self.standing_left = False
            self.image = characterfront
            self.pos.y += self.speed

        if keys[pg.K_d]:
            self.standing_right = True
            self.standing_left = False
            self.standing_down = False 
            self.image = characterright
            self.pos.x += self.speed
         
        if keys[pg.K_LSHIFT]:
            self.speed = self.speed_boost
        else:
            self.speed = 2

        
        self.attacked = False
        attack_direction_x = 0
        attack_direction_y = 0

        if keys[pg.K_RIGHT]:
            self.attacked = True
            attack_direction_x = 3
            
        if keys[pg.K_LEFT]:
            self.attacked = True
            attack_direction_x = -3

        if keys[pg.K_UP]:
            self.attacked = True
            attack_direction_y = -3
        
        elif keys[pg.K_DOWN]:
            self.attacked = True
            attack_direction_y = 3
        
        if self.attacked:
            self.attack(attack_direction_x, attack_direction_y)

        
        self.animate()

        self.rect.center = self.pos
        self.standing_right = True
    
    def attack(self, x, y):
        Ranged_attack(self.game, self.pos.x, self.pos.y, x, y)


    def animate(self):
        now = pg.time.get_ticks()

        if self.standing_left:
             if now - self.last_update > 350:
                 self.last_update = now
                 self.current_frame = (self.current_frame + 1) % len(self.standing_left_frames)
                 self.image = self.standing_left_frames[self.current_frame]
                 self.rect = self.image.get_rect()
        
        if self.standing_right:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_right_frames)
                self.image = self.standing_right_frames[self.current_frame]
                self.rect = self.image.get_rect()
        
        if self.standing_down:
            if now - self.last_update >350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_down_frames)
                self.image = self.standing_down_frames[self.current_frame]
                self.rect = self.image.get_rect()



class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = skeleton
        self.rect = self.image.get_rect() # henter self.image sin størrelse og lager en hitbox
        self.pos = vec(1200,randint(300,950))
        self.rect.center = self.pos
        self.speed = randint(1,3)
        self.liv = 40

    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed

        if self.pos.x < -200:
            self.speed = randint(3,5)
            self.pos.x = 1200
            self.pos.y = randint(300,900)
        
        if self.liv < 0:
            self.kill()
        
        

class Enemy2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = ghost
        self.rect = self.image.get_rect() # henter self.image sin størrelse og lager en hitbox
        self.pos = vec(randint(0,1000),randint(-300,-150))
        self.rect.center = self.pos
        self.speed = 0.5
        self.liv = 70
    
    def update(self):
        self.rect.center = self.pos

        self.pos.y += self.speed

        if self.pos.y > 1200:
            self.pos.y = -200
            self.pos.x = randint(100,900)

      
        if self.liv < 0:
            self.kill()



class Enemy3(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = slime
        self.rect = self.image.get_rect()
        self.pos = vec(randint(100, 900), 300)
        self.rect.center = self.pos
        self.speed = 2
        self.liv = 30
        self.direction_x = 5
        self.direction_y = 5
        
    def update(self):
         self.pos.x += self.direction_x
         self.pos.y += self.direction_y
         self.rect.center = self.pos
 
         if self.pos.x > 925:   
            self.direction_x = -self.speed
         
         if self.pos.x < 75:
            self.direction_x = self.speed

         if self.pos.y < 300:
            self.direction_y = self.speed

         if self.pos.y > 970:
            self.direction_y = -self.speed

         if self.liv < 0:
            self.kill()
       


class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, game, x ,y, direction_x, direction_y):
        self.groups = game.all_sprites, game.projectiles_group # legger til i sprite gruppe
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = projectile
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) # start posisjon
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.rect.center = self.pos

        self.image = projectile
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.direction = 20

        self.angle = 0
        self.spawn_tick = pg.time.get_ticks()

        self.last_attack = 0
        self.current_attack = 2000


    
    def update(self):
        self.rect.center = self.pos
        self.pos.x += self.direction_x
        self.pos.y += self.direction_y
        self.angle += 10 

        now = pg.time.get_ticks()
        if now - self.spawn_tick > self.current_attack:
            self.kill()

        self.image, self.rect = self.rot_center(self.orig_image, self.angle, self.pos.x, self.pos.y)

    def rot_center(self, image, angle, x, y):   
        rotated_image = pg.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
 

        return rotated_image, new_rect

class Healing_potion(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.health_potion_group # legger til i sprite gruppe
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = health_potion
        self.rect = self.image.get_rect()
        self.pos = vec(639, 300) # start posisjon
        self.rect.center = self.pos

    def update(self):
        self.rect.center = self.pos
 
    def give_liv(self):
        self.game.digger.max_liv += randint(20,40)
        self.game.digger.liv = self.game.digger.max_liv

class Running_potion(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.run_potion_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game 
        self.image = run_potion
        self.rect = self.image.get_rect()
        self.pos = vec(639, 300)
    
    def update(self):
        self.rect.center = self.pos
    
    def give_run(self):
        self.game.digger.speed_boost = 4

