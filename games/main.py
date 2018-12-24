import pygame
import random
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 400)
W = 1072
H = 634
WHITE = (255, 255, 255)

keys = pygame.key.get_pressed()
MUSIC = ('background_music.mp3')
random.shuffle([MUSIC])
pygame.mixer.music.load(MUSIC)
pygame.mixer.music.play(-1)

sound1 = pygame.mixer.Sound('udar1.wav')
sound2 = pygame.mixer.Sound('udar_hero.wav')


class Hero (pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp, damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_straight = 7
        self.speed_diagonal = 5
        self.x = self.rect.x
        self.y = self.rect.y
        self.hp = hp
        self.damage = damage

    def update(self, x, y):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if keys[pygame.K_UP]:
                    if self.rect.x > 90:
                        self.rect.x -= self.speed_diagonal
                        self.x = self.rect.x
                    if self.rect.y > 90:
                        self.rect.y -= self.speed_diagonal
                        self.y = self.rect.y
            if keys[pygame.K_DOWN]:
                    if self.rect.x > 90:
                        self.rect.x -= self.speed_diagonal
                        self.x = self.rect.x
                    if self.rect.y < H-190:
                        self.rect.y += self.speed_diagonal
                        self.y = self.rect.y
            if keys[pygame.K_DOWN] == 0 and keys[pygame.K_UP] == 0 and self.rect.x > 90:
                self.rect.x -= self.speed_straight
                self.x = self.rect.x

        if keys[pygame.K_RIGHT] == 1:
            if keys[pygame.K_UP] == 1:
                if self.rect.x < W - 190:
                    self.rect.x += self.speed_diagonal
                    self.x = self.rect.x
                if self.rect.y > 90:
                    self.rect.y -= self.speed_diagonal
                    self.y = self.rect.y
            if keys[pygame.K_DOWN] == 1:
                if self.rect.x < W - 190:
                    self.rect.x += self.speed_diagonal
                    self.x = self.rect.x
                if self.rect.y < H-190:
                    self.rect.y += self.speed_diagonal
                    self.y = self.rect.y
            if keys[pygame.K_DOWN] == 0 and keys[pygame.K_UP] == 0 and  self.rect.x < W -190:
                self.rect.x += self.speed_straight
                self.x = self.rect.x
        if keys[pygame.K_UP] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and self.rect.y >90:
            self.rect.y -= self.speed_straight
            self.y = self.rect.y
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and self.rect.y < H-190:
            self.rect.y += self.speed_straight
            self.y = self.rect.y


dop_hp = 0
dop_speed = 0
SHOT_READY = True


class Bullet (Hero):
    def __init__(self, x, y, surf, group, speed_x, speed_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, x, y):
        if self.speed_x == 0 and self.speed_y == 0:
            self.kill()
            Bullet(hero1.x + 45, hero1.y + 100, BULLET_SURF[0], BULLETS, 0, 0)

        if self.speed_y > 0:
            if self.rect.y > 90:
                self.rect.y += self.speed_y
            if self.rect.y <= 90:
                self.kill()
            if MONSTER_STATUS == True and (
                    self.rect.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                    and self.rect.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
                self.kill()
                monster1.hp -= hero1.damage
                sound2.play()

        if self.speed_y < 0:
            if self.rect.y < H - 90:
                self.rect.y += self.speed_y
            if self.rect.y >= H - 90:
                self.kill()
            if MONSTER_STATUS == True and (
                    self.rect.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                    and self.rect.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
                self.kill()
                monster1.hp -= hero1.damage
                sound2.play()

        if self.speed_x < 0:
            if self.rect.x > 90:
                self.rect.x += self.speed_x
            if self.rect.x <= 90 or keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_s]:
                self.kill()
            if MONSTER_STATUS == True and (
                    self.rect.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                    and self.rect.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
                self.kill()
                monster1.hp -= hero1.damage
                sound2.play()

        if self.speed_x > 0:
            if self.rect.x < W - 90:
                self.rect.x += self.speed_x
            if self.rect.x >= W - 90 or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s]:
                self.kill()
            if MONSTER_STATUS == True and (
                    self.rect.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                    and self.rect.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
                self.kill()
                monster1.hp -= hero1.damage
                sound2.play()



class Item (Hero):
    def __init__(self, x, y, surf, group, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.type = type
        self.add(group)
    def update(self):
        if self.rect.x in range (hero1.x-10, hero1.x +90) and self.rect.y in range (hero1.y, hero1.y +120):
            if self.type == 1:
                hero1.damage += 2
                hero1.hp += 5
            if self.type == 0:
                hero1.speed_straight += 1
                hero1.speed_diagonal += 1
            self.kill()


class Monsters (Hero):
    def __init__(self, x, y, filename, hp, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect_monster = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.x = self.rect_monster.x
        self.y = self.rect_monster.y
        self.hp = hp

    def move(self):
        if self.rect_monster.x < hero1.x + 30:
            self.rect_monster.x += self.speed
            self.x = self.rect_monster.x
            if self.rect_monster.y < hero1.y + 30:
                self.rect_monster.y += self.speed
                self.y = self.rect_monster.y
            if self.rect_monster.y > hero1.y + 30:
                self.rect_monster.y -= self.speed
                self.y = self.rect_monster.y

        elif self.rect_monster.x > hero1.x +30:
            self.rect_monster.x -= self.speed
            self.x = self.rect_monster.x
            if self.rect_monster.y < hero1.y +30:
                self.rect_monster.y += self.speed
                self.y = self.rect_monster.y
            if self.rect_monster.y > hero1.y +30:
                self.rect_monster.y -= self.speed
                self.y = self.rect_monster.y

        elif self.rect_monster.x == hero1.x +30:
            if self.rect_monster.y < hero1.y +30:
                self.rect_monster.y += self.speed
                self.y = self.rect_monster.y
            if self.rect_monster.y > hero1.y + 30:
                self.rect_monster.y -= self.speed
                self.y = self.rect_monster.y
        if self.hp <= 0:
            global MONSTER_STATUS
            Item(monster1.x, monster1.y, ITEM_SURF[0], ITEMS, 0)
            MONSTER_STATUS = False
    def attack(self):
        hero1.hp -= 1
        sound1.play()


FREE_BULLETS = True
MONSTER_STATUS = True

sc = pygame.display.set_mode((W, H))

image1 = pygame.image.load('circle-color.png').convert()
image1.set_colorkey((255, 255, 255))
image2 = pygame.image.load('pop.image.png').convert()
image2.set_colorkey((255, 255, 255))

crown = pygame.image.load('crown.png').convert()
crown.set_colorkey((255, 255, 255))
bread = pygame.image.load('bread.png').convert()
bread.set_colorkey((255, 255, 255))


BULLETS_SKIN = (image1, image2)
BULLET_SURF = []

ITEM_SKIN = (crown, bread)
ITEM_SURF = []




for i in range(len(BULLETS_SKIN)):
    BULLET_SURF.append(BULLETS_SKIN[i])

for i in range(len(ITEM_SKIN)):
    ITEM_SURF.append(ITEM_SKIN[i])

FIELD = ['field.png', 'field1.png', 'field2.png', 'field3.png', 'field4.png', 'field5.png']

background_surf = pygame.image.load(FIELD[0]).convert()
background_rect = background_surf.get_rect(topleft=(0, 0))

background_surf_1 = pygame.image.load(FIELD[1]).convert()
background_rect_1 = background_surf_1.get_rect(topleft=(0, 0))

background_surf_2 = pygame.image.load(FIELD[2]).convert()
background_rect_2 = background_surf_2.get_rect(topleft=(0, 0))

background_surf_3 = pygame.image.load(FIELD[3]).convert()
background_rect_3 = background_surf_3.get_rect(topleft=(0, 0))

background_surf_4 = pygame.image.load(FIELD[4]).convert()
background_rect_4 = background_surf_4.get_rect(topleft=(0, 0))

background_surf_5 = pygame.image.load(FIELD[5]).convert()
background_rect_5 = background_surf_5.get_rect(topleft=(0, 0))
sc.blit(background_surf, background_rect)


hero1 = Hero(W/2, H/2, 'hero.png', 100, randint(20, 30))
BULLETS = pygame.sprite.Group()

ITEMS = pygame.sprite.Group()
tick = 0

monster1 = Monsters(randint(1,W-90), 90, 'monster1.png', 100, 2)

Bullet(hero1.x + 45, hero1.y + 100, BULLET_SURF[0], BULLETS, 0, 0)
Item(randint(90, W-90), randint(100, H-90), ITEM_SURF[1], ITEMS, 1)


HP_NAMESPACE = pygame.font.Font(None,30)
HP_TEXT = HP_NAMESPACE.render ('HP: {}'.format(hero1.hp), 1, (180, 0,0))
HP_PLACE = HP_TEXT.get_rect(center =(50, 20))
sc.blit(HP_TEXT, HP_PLACE)

HP_MONSTER_NAMESPACE = pygame.font.Font(None,13)
HP_MONSTER_TEXT = HP_NAMESPACE.render('{}/{}'.format(hero1.hp, 100+dop_hp), 1, (0, 100,0))
HP_MONSTER_PLACE = HP_MONSTER_TEXT.get_rect(center=(monster1.x + 30, monster1.y - 10))
sc.blit (HP_MONSTER_TEXT, HP_MONSTER_PLACE)

MENU_STATUS = True
surf1 = pygame.Surface((300, 100))
surf1.fill((250, 250, 250))
rect_1 = pygame.Rect((W/2-150, H/2 - 150, 0, 0))
sc.blit(surf1, rect_1)

MENU_NAMESPACE_1 = pygame.font.Font(None,70)
MENU_TEXT_1 = MENU_NAMESPACE_1.render('Hello, sir.', 1, (0, 0,0))
MENU_PLACE_1 = MENU_TEXT_1.get_rect(center=(150, 50))
sc.blit (MENU_TEXT_1,MENU_PLACE_1)

surf2 = pygame.Surface((300, 100))
surf2.fill((220, 200, 0))
rect_2 = pygame.Rect((W/2-150, H/2 + 150, 0, 0))
sc.blit(surf2, rect_2)

MENU_NAMESPACE_2 = pygame.font.Font(None,80)
MENU_TEXT_2 = MENU_NAMESPACE_2.render('START', 1, (0, 0,0))
MENU_PLACE_2 = MENU_TEXT_2.get_rect(center=(150, 50))
sc.blit (MENU_TEXT_2,MENU_PLACE_2)

surf_death = pygame.Surface((500, 100))
surf_death.fill ((250, 250, 250))
rect_DEATH = pygame.Rect((W/2-250, H/2 - 150, 0, 0))
sc.blit(surf_death, rect_DEATH)

DEATH_NAMESPACE = pygame.font.Font(None, 80)
DEATH_TEXT = DEATH_NAMESPACE.render('YOU ARE DEAD', 1, (0, 0,0))
DEATH_PLACE = DEATH_TEXT.get_rect(center=(250, 50))
sc.blit(DEATH_TEXT, DEATH_PLACE)

surf3 = pygame.Surface((200, 80))
surf3.fill((250, 250, 250))
rect_3 = pygame.Rect((W/2-100, H/2 + 150, 0, 0))
sc.blit(surf3, rect_3)

MENU_NAMESPACE_3 = pygame.font.Font(None, 60)
MENU_TEXT_3 = MENU_NAMESPACE_3.render('Try again', 1, (0, 0,0))
MENU_PLACE_3 = MENU_TEXT_3.get_rect(center=(100, 50))

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.USEREVENT:
            SHOT_READY = True
            tick += 1
        if MENU_STATUS == True:
            if hero1.hp > 0:
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1 and i.pos[0] in range(int(W/2 - 150), int(W/2 + 150) ) \
                            and i.pos[1] in range(int(H/2 + 150), int(H/2 + 250)):
                        MENU_STATUS = False
            if hero1.hp <= 0:
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1 and i.pos[0] in range(int(W/2 - 100), int(W/2 + 100) ) \
                            and i.pos[1] in range(int(H/2 + 150), int(H/2 + 230)):
                        hero1.hp = 100
                        monster1.hp = 100
                        monster1 = Monsters(randint(1, W - 90), 90, 'monster1.png', 100, 2)
                        MENU_STATUS = False

        if i.type == pygame.KEYUP:
            if i.key == pygame.K_1:
                pygame.mixer.music.pause()
            elif i.key == pygame.K_2:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(0.3)
            elif i.key == pygame.K_3:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(1)



    keys = pygame.key.get_pressed()
    if MENU_STATUS == True:
        if hero1.hp > 0:
            sc.blit(background_surf, background_rect)
            sc.blit(surf1, rect_1)
            surf1.blit(MENU_TEXT_1, MENU_PLACE_1)
            sc.blit(surf2, rect_2)
            surf2.blit(MENU_TEXT_2, MENU_PLACE_2)
            pygame.time.delay(40)
            pygame.display.update()
        if hero1.hp <= 0:
            sc.blit(background_surf_5, background_rect_5)
            sc.blit(surf_death, rect_DEATH)
            surf_death.blit(DEATH_TEXT, DEATH_PLACE)

            sc.blit(surf3, rect_3)
            surf3.blit(MENU_TEXT_3, MENU_PLACE_3)

            pygame.time.delay(40)
            pygame.display.update()

    if MENU_STATUS == False:
        if hero1.hp >= 100:
            sc.blit(background_surf, background_rect)
            sc.blit(hero1.image, hero1.rect)
        elif 75 < hero1.hp < 100 :
            sc.blit(background_surf_1, background_rect_1)
            sc.blit(hero1.image, hero1.rect)
        elif 50 < hero1.hp <= 75:
            sc.blit(background_surf_2, background_rect_2)
            sc.blit(hero1.image, hero1.rect)
        elif 30 < hero1.hp <= 50:
            sc.blit(background_surf_3, background_rect_3)
            sc.blit(hero1.image, hero1.rect)
        elif 15 < hero1.hp <= 30:
            sc.blit(background_surf_4, background_rect_4)
            sc.blit(hero1.image, hero1.rect)
        elif hero1.hp <= 15:
            sc.blit(background_surf_5, background_rect_5)
            sc.blit(hero1.image, hero1.rect)
        if hero1.hp <= 0:
            MENU_STATUS = True
            dop_hp = 0
        hero1.damage = randint(20, 30)
        sc.blit(hero1.image, hero1.rect)

        if keys[pygame.K_w] and SHOT_READY == True:
            Bullet(hero1.x + 40, hero1.y + 100, BULLET_SURF[0], BULLETS, 0, -10)
            SHOT_READY = False
        if keys[pygame.K_s] and SHOT_READY == True:
            Bullet(hero1.x + 40, hero1.y + 100, BULLET_SURF[0], BULLETS, 0, 10)
            SHOT_READY = False
        if keys[pygame.K_a] and SHOT_READY == True:
            Bullet(hero1.x + 40, hero1.y + 100, BULLET_SURF[0], BULLETS, -10, 0)
            SHOT_READY = False
        if keys[pygame.K_d] and SHOT_READY == True:
            Bullet(hero1.x + 40, hero1.y + 100, BULLET_SURF[0], BULLETS, 10, 0)
            SHOT_READY = False


        BULLETS.update(hero1.x + 45, hero1.y + 110)
        BULLETS.draw(sc)

        if tick == 12:
            Item(randint(90, W-90), randint(100, H-90), ITEM_SURF[1], ITEMS, 1)
            tick = 0

        ITEMS.update()
        ITEMS.draw(sc)


        HP_TEXT = HP_NAMESPACE.render('HP: {}'.format(hero1.hp), 1, (180, 0, 0))
        sc.blit(HP_TEXT, HP_PLACE)
        if MONSTER_STATUS == True:
            HP_MONSTER_TEXT = HP_NAMESPACE.render('{}/{}'.format(monster1.hp, 100+dop_hp), 1, (0, 100, 0))
            HP_MONSTER_PLACE = HP_MONSTER_TEXT.get_rect(center=(monster1.x + 30, monster1.y - 10))
            sc.blit(HP_MONSTER_TEXT, HP_MONSTER_PLACE)
        if MONSTER_STATUS == False and monster1 == True:
            del monster1
        if MONSTER_STATUS == True:
            sc.blit(monster1.image, monster1.rect_monster)

        pygame.time.delay(40)

        hero1.update(W/2, H/2)
        if MONSTER_STATUS == True:
            monster1.move()
        pygame.display.update()
        if MONSTER_STATUS == True:
            if monster1.x in range (hero1.x-30, hero1.x +70) and monster1.y in range (hero1.y - 60, hero1.y +80):
                monster1.attack()
        if MONSTER_STATUS == False:
            dop_hp += 25
            dop_speed += 1
            monster1.hp = 100
            monster1 = Monsters(randint(1, W - 90), 90, 'monster1.png', monster1.hp + dop_hp, 2 + dop_speed)
            MONSTER_STATUS = True
        print( hero1.speed_straight, hero1.speed_diagonal)