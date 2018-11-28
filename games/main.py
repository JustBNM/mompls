import pygame
import random
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 3000)
W = 1072
H = 634
WHITE = (255, 255, 255)

keys = pygame.key.get_pressed()
MUSIC = ('background_music.mp3')
random.shuffle([MUSIC])
#TODO: Прописать, чтобы можно было листать музыку клавишей.
pygame.mixer.music.load(MUSIC)
pygame.mixer.music.play(-1)

sound1 = pygame.mixer.Sound('udar1.wav')
sound2 = pygame.mixer.Sound('udar_hero.wav')


class Hero (pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        # прячем фон белого цвета
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_straight = 7
        self.speed_diagonal = 5
        self.x = self.rect.x
        self.y = self.rect.y
        self.hp = hp

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
                if self.rect.x < W -190:
                    self.rect.x += self.speed_diagonal
                    self.x = self.rect.x
                if self.rect.y > 90:
                    self.rect.y -= self.speed_diagonal
                    self.y = self.rect.y
            if keys[pygame.K_DOWN] == 1:
                if self.rect.x < W- 190:
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



MOVE_W = False
MOVE_S = False
MOVE_A = False
MOVE_D = False
dop_hp = 0
dop_speed = 0

class Bullet (Hero):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        # прячем фон белого цвета
        self.image.set_colorkey((255, 255, 255))
        self.rect_bullet = self.image.get_rect(center=(x, y))
        self.strike_speed = 10

    def update(self, x, y):
        global bullet1
        bullet1 = Bullet(hero1.x + 45, hero1.y + 110, BULLET_SKIN)


    def move_w(self):
        if self.rect_bullet.y > 90:
            self.rect_bullet.y -= self.strike_speed
        if self.rect_bullet.y <= 90 or keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_s]:
            self.kill()
            global MOVE_W
            MOVE_W = False
        if MONSTER_STATUS == True and (self.rect_bullet.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                and self.rect_bullet.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
            self.kill()
            MOVE_W = False
            monster1.hp -= 25
            sound2.play()

    def move_s(self):
        if self.rect_bullet.y < H-90:
            self.rect_bullet.y += self.strike_speed
        if self.rect_bullet.y >= H-90 or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d]:
            self.kill()
            global MOVE_S
            MOVE_S = False
        if MONSTER_STATUS == True and (self.rect_bullet.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                and self.rect_bullet.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
            self.kill()
            MOVE_S = False
            monster1.hp -= 25
            sound2.play()
    def move_a(self):
        if self.rect_bullet.x > 90:
            self.rect_bullet.x -= self.strike_speed
        if self.rect_bullet.x <= 90 or keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_s]:
            self.kill()
            global MOVE_A
            MOVE_A = False
        if MONSTER_STATUS == True and (self.rect_bullet.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                and self.rect_bullet.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
            self.kill()
            MOVE_A = False
            monster1.hp -= 25
            sound2.play()

    def move_d(self):
        if self.rect_bullet.x < W-90:
            self.rect_bullet.x += self.strike_speed
        if self.rect_bullet.x >= W-90 or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s]:
            self.kill()
            global MOVE_D
            MOVE_D = False
        if MONSTER_STATUS == True and (self.rect_bullet.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                and self.rect_bullet.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
            self.kill()
            MOVE_D = False
            monster1.hp -= 25
            sound2.play()


class Monsters (Hero):
    def __init__(self, x, y, filename, hp, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        # прячем фон белого цвета
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
            MONSTER_STATUS = False
    def attack(self):
        hero1.hp -= 1
        sound1.play()

FREE_BULLETS = True
MONSTER_STATUS = True

BULLETS_SURF = []
BULLET_SKIN = 'circle-color.png'
FIELD = ['field.png', 'field1.png','field2.png','field3.png','field4.png','field5.png']


sc = pygame.display.set_mode((W, H))
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


hero1 = Hero(W/2, H/2, 'hero.png', 100)
#MONSTERS = pygame.sprite.Group()
#MONSTERS.add (Monsters(randint(1,W-90), 90, 'monster1.png', 100))
monster1 = Monsters(randint(1,W-90), 90, 'monster1.png', 100, 2)

bullet1 = Bullet(hero1.x + 45, hero1.y + 110, BULLET_SKIN)
bullet2 = Bullet (randint(90, W-90), randint(90, H-90), 'pop.image.png')


HP_NAMESPACE = pygame.font.Font(None,30)
HP_TEXT = HP_NAMESPACE.render ('HP: {}'.format(hero1.hp), 1, (180, 0,0))
HP_PLACE = HP_TEXT.get_rect(center =(50, 20))
sc.blit(HP_TEXT, HP_PLACE)

HP_MONSTER_NAMESPACE = pygame.font.Font(None,13)
HP_MONSTER_TEXT = HP_NAMESPACE.render ('{}/{}'.format(hero1.hp, 100+dop_hp), 1, (0, 100,0))
HP_MONSTER_PLACE = HP_MONSTER_TEXT.get_rect(center =(monster1.x + 30, monster1.y - 10))
sc.blit (HP_MONSTER_TEXT, HP_MONSTER_PLACE)

MENU_STATUS = True
surf1 = pygame.Surface((300, 100))
surf1.fill((250, 250, 250))
rect_1 = pygame.Rect((W/2-150, H/2 - 150, 0, 0))
sc.blit(surf1, rect_1)

MENU_NAMESPACE_1 = pygame.font.Font(None,70)
MENU_TEXT_1 = MENU_NAMESPACE_1.render ('Hello, sir.', 1, (0, 0,0))
MENU_PLACE_1 = MENU_TEXT_1.get_rect(center =(150, 50))
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
MENU_PLACE_3 = MENU_TEXT_3.get_rect(center =(100, 50))

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
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
                        monster1 = Monsters(randint(1, W - 90), 90, 'monster1.png', 100)
                        MENU_STATUS = False

        if i.type == pygame.KEYUP:
            if i.key == pygame.K_1:
                pygame.mixer.music.pause()
                #в этом случае музыка будет начинаться сначала
                # pygame.mixer.music.stop()
            elif i.key == pygame.K_2:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.3)
            elif i.key == pygame.K_3:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
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
        sc.blit(hero1.image, hero1.rect)
        if keys[pygame.K_w]:
            bullet1 = Bullet(hero1.x + 40, hero1.y + 110, BULLET_SKIN)
            MOVE_W = True
        if keys[pygame.K_s]:
            bullet1 = Bullet(hero1.x + 40, hero1.y + 110, BULLET_SKIN)
            MOVE_S = True
        if keys[pygame.K_a]:
            bullet1 = Bullet(hero1.x + 40, hero1.y + 110, BULLET_SKIN)
            MOVE_A = True
        if keys[pygame.K_d]:
            bullet1 = Bullet(hero1.x + 40, hero1.y + 110, BULLET_SKIN)
            MOVE_D = True

        if MOVE_W == True:
            bullet1.move_w()
        if MOVE_S == True:
            bullet1.move_s()
        if MOVE_A == True:
            bullet1.move_a()
        if MOVE_D == True:
            bullet1.move_d()

        if MOVE_W == False and MOVE_A == False and MOVE_S == False and MOVE_D == False:
            bullet1.update(hero1.x + 45, hero1.y + 110)

        if hero1.x in range(bullet2.rect_bullet.x - 90, bullet2.rect_bullet.x + 90)\
        and hero1.y in range(bullet2.rect_bullet.y -120, bullet2.rect_bullet.y +20) :
            BULLET_SKIN = 'pop.image.png'
            FREE_BULLETS = False

        sc.blit(bullet1.image, bullet1.rect_bullet)
        HP_TEXT = HP_NAMESPACE.render('HP: {}'.format(hero1.hp), 1, (180, 0, 0))
        sc.blit(HP_TEXT, HP_PLACE)
        if MONSTER_STATUS == True:
            HP_MONSTER_TEXT = HP_NAMESPACE.render('{}/{}'.format(monster1.hp, 100+dop_hp), 1, (0, 100, 0))
            HP_MONSTER_PLACE = HP_MONSTER_TEXT.get_rect(center=(monster1.x + 30, monster1.y - 10))
            sc.blit(HP_MONSTER_TEXT, HP_MONSTER_PLACE)
        if MONSTER_STATUS == False and monster1 == True:
            del monster1
        if FREE_BULLETS == True:
            sc.blit(bullet2.image, bullet2.rect_bullet)
        else:
            bullet2 = Bullet(W-40, 40, 'pop.image.png')
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
            monster1.hp += 100
            monster1 = Monsters(randint(1, W - 90), 90, 'monster1.png', monster1.hp + dop_hp, 2 + dop_speed)
            MONSTER_STATUS = True
        '''print(hero1.x, hero1.y)
        print(monster1.x, monster1.y)'''
        print(MOVE_W)
        print(bullet1.rect_bullet.y)
        print(FREE_BULLETS)
        print(monster1)
