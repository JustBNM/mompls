import pygame
import random
from random import randint

pygame.init()
W = 1072
H = 634
WHITE = (255, 255, 255)

keys = pygame.key.get_pressed()
MUSIC = ('background_music.mp3')
random.shuffle([MUSIC])
#TODO: Прописать, чтобы можно было листать музыку клавишей.
pygame.mixer.music.load(MUSIC)
pygame.mixer.music.play(-1)

sound1 = pygame.mixer.Sound('frog.wav')
sound2 = pygame.mixer.Sound('Грустный тромбон.ogg')


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

    '''def strike(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.rect_bullet.y > 0:
                self.rect_bullet.y -= self.strike_speed
        if keys[pygame.K_s]:
            if self.rect_bullet.y < H:
                self.rect_bullet.y += self.strike_speed
        if keys[pygame.K_a]:
            if self.rect_bullet.x > 0:
                self.rect_bullet.x -= self.strike_speed
        if keys[pygame.K_d]:
            if self.rect_bullet.x < W:
                self.rect_bullet.x += self.strike_speed'''

MOVE_W = False
MOVE_S = False
MOVE_A = False
MOVE_D = False


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
        if self.rect_bullet.y <= 90 or keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_s]\
            or (self.rect_bullet.x in range (monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                and self.rect_bullet.y in range (monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
            self.kill()
            global MOVE_W
            MOVE_W = False

    def move_s(self):
        if self.rect_bullet.y < H-90:
            self.rect_bullet.y += self.strike_speed
        if self.rect_bullet.y >= H-90 or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d] \
            or (self.rect_bullet.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                and self.rect_bullet.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
            self.kill()
            global MOVE_S
            MOVE_S = False

    def move_a(self):
        if self.rect_bullet.x > 90:
            self.rect_bullet.x -= self.strike_speed
        if self.rect_bullet.x <= 90 or keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_s] \
            or (self.rect_bullet.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                and self.rect_bullet.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
            self.kill()
            global MOVE_A
            MOVE_A = False

    def move_d(self):
        if self.rect_bullet.x < W-90:
            self.rect_bullet.x += self.strike_speed
        if self.rect_bullet.x >= W-90 or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] \
            or (self.rect_bullet.x in range(monster1.rect_monster.x - 30, monster1.rect_monster.x + 30)
                and self.rect_bullet.y in range(monster1.rect_monster.y - 30, monster1.rect_monster.y + 70)):
            self.kill()
            global MOVE_D
            MOVE_D = False


class Monsters (Hero):
    def __init__(self, x, y, filename, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        # прячем фон белого цвета
        self.image.set_colorkey((255, 255, 255))
        self.rect_monster = self.image.get_rect(center=(x, y))
        self.speed = 2
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
    def attack(self):
        hero1.hp -= 1

sc = pygame.display.set_mode((W, H))

background_surf = pygame.image.load('field.png').convert()
background_rect = background_surf.get_rect(topleft=(0, 0))
sc.blit(background_surf, background_rect)

FREE_BULLETS = True

BULLETS_SURF = []
BULLET_SKIN = 'circle-color.png'

hero1 = Hero(W/2, H/2, 'hero.png', 100)

monster1 = Monsters(randint(1,W-90), 90, 'monster1.png', 100)

bullet1 = Bullet(hero1.x + 45, hero1.y + 110, BULLET_SKIN)
bullet2 = Bullet (randint(90, W-90), randint(90, H-90), 'pop.image.png')

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_1:
                pygame.mixer.music.pause()
                #в этом случае музыка будет начинаться сначала
                # pygame.mixer.music.stop()
            elif i.key == pygame.K_2:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)
            elif i.key == pygame.K_3:
                pygame.mixer.music.unpause()
                # pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
        elif i.type == pygame.MOUSEBUTTONUP:
            if i.button == 1:
                sound1.play()
            elif i.button == 3:
                sound2.play()
    keys = pygame.key.get_pressed()

    sc.blit(background_surf, background_rect)
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
    if FREE_BULLETS == True:
        sc.blit(bullet2.image, bullet2.rect_bullet)
    else:
        bullet2 = Bullet(W-40, 40, 'pop.image.png')
    sc.blit(monster1.image, monster1.rect_monster)

    pygame.time.delay(40)

    hero1.update(W/2, H/2)

    monster1.move()
    pygame.display.update()
    if monster1.x == hero1.x and monster1.y == hero1.y:
        monster1.attack()
    '''print(hero1.x, hero1.y)
    print(monster1.x, monster1.y)
    print(hero1.hp)'''
    print (MOVE_W)
    print (bullet1.rect_bullet.y)
    print (FREE_BULLETS)
