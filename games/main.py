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
        self.speed = 3
        self.x = self.rect.x
        self.y = self.rect.y
        self.hp = hp

    def update(self, x, y):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if keys[pygame.K_UP]:
                    if self.rect.x > 90:
                        self.rect.x -= 2
                        self.x = self.rect.x
                    if self.rect.y > 90:
                        self.rect.y -= 2
                        self.y = self.rect.y
            if keys[pygame.K_DOWN]:
                    if self.rect.x > 90:
                        self.rect.x -= 2
                        self.x = self.rect.x
                    if self.rect.y < H-190:
                        self.rect.y += 2
                        self.y = self.rect.y
            if keys[pygame.K_DOWN] == 0 and keys[pygame.K_UP] == 0 and self.rect.x > 90:
                self.rect.x -= 3
                self.x = self.rect.x

        if keys[pygame.K_RIGHT] == 1:
            if keys[pygame.K_UP] == 1:
                if self.rect.x < W -190:
                    self.rect.x += 2
                    self.x = self.rect.x
                if self.rect.y > 90:
                    self.rect.y -= 2
                    self.y = self.rect.y
            if keys[pygame.K_DOWN] == 1:
                if self.rect.x < W- 190:
                    self.rect.x += 2
                    self.x = self.rect.x
                if self.rect.y < H-190:
                    self.rect.y += 2
                    self.y = self.rect.y
            if keys[pygame.K_DOWN] == 0 and keys[pygame.K_UP] == 0 and  self.rect.x < W -190:
                self.rect.x += 3
                self.x = self.rect.x
        if keys[pygame.K_UP] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and self.rect.y >90:
            self.rect.y -= 3
            self.y = self.rect.y
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and self.rect.y < H-190:
            self.rect.y += 3
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
        self.strike_speed = 5

    def update(self, x, y):
        self.rect_bullet.y == hero1.y
        self.rect_bullet.x == hero1.x

    def move_w(self):
        if self.rect_bullet.y > 90:
            self.rect_bullet.y -= self.strike_speed
        if self.rect_bullet.y <= 90 or keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_s]:
            self.kill()
            global MOVE_W
            MOVE_W = False

    def move_s(self):
        if self.rect_bullet.y < H-90:
            self.rect_bullet.y += self.strike_speed
        if self.rect_bullet.y >= H-90 or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d]:
            self.kill()
            global MOVE_S
            MOVE_S = False

    def move_a(self):
        if self.rect_bullet.x > 90:
            self.rect_bullet.x -= self.strike_speed
        if self.rect_bullet.x <= 90 or keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_s]:
            self.kill()
            global MOVE_A
            MOVE_A = False

    def move_d(self):
        if self.rect_bullet.x < W-90:
            self.rect_bullet.x += self.strike_speed
        if self.rect_bullet.x >= W-90 or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s]:
            self.kill()
            global MOVE_D
            MOVE_D = False


class Monsters (Hero):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        # прячем фон белого цвета
        self.image.set_colorkey((255, 255, 255))
        self.rect_monster = self.image.get_rect(center=(x, y))
        self.speed = 1
        self.x = self.rect_monster.x
        self.y = self.rect_monster.y

    def move(self):
        if self.rect_monster.x < hero1.x:
            self.rect_monster.x += self.speed
            self.x = self.rect_monster.x
            if self.rect_monster.y < hero1.y:
                self.rect_monster.y += self.speed
                self.y = self.rect_monster.y
            if self.rect_monster.y > hero1.y:
                self.rect_monster.y -= self.speed
                self.y = self.rect_monster.y

        elif self.rect_monster.x > hero1.x:
            self.rect_monster.x -= self.speed
            self.x = self.rect_monster.x
            if self.rect_monster.y < hero1.y:
                self.rect_monster.y += self.speed
                self.y = self.rect_monster.y
            if self.rect_monster.y > hero1.y:
                self.rect_monster.y -= self.speed
                self.y = self.rect_monster.y

        elif self.rect_monster.x == hero1.x:
            if self.rect_monster.y < hero1.y:
                self.rect_monster.y += self.speed
                self.y = self.rect_monster.y
            if self.rect_monster.y > hero1.y:
                self.rect_monster.y -= self.speed
                self.y = self.rect_monster.y
    def attack(self):
        hero1.hp -= 1

sc = pygame.display.set_mode((W, H))

background_surf = pygame.image.load('field.png').convert()
background_rect = background_surf.get_rect(topleft=(0, 0))
sc.blit(background_surf, background_rect)

BULLETS_SURF = []


hero1 = Hero(W/2, H/2, 'hero.png', 100)

monster1 = Monsters(randint(1,W-90), 90, 'monster1.png')

bullet1 = Bullet(hero1.x, hero1.y, 'pop.image.png')


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
        bullet1 = Bullet(hero1.x, hero1.y, 'pop.image.png')
        MOVE_W = True
    if keys[pygame.K_s]:
        bullet1 = Bullet(hero1.x, hero1.y, 'pop.image.png')
        MOVE_S = True
    if keys[pygame.K_a]:
        bullet1 = Bullet(hero1.x, hero1.y, 'pop.image.png')
        MOVE_A = True
    if keys[pygame.K_d]:
        bullet1 = Bullet(hero1.x, hero1.y, 'pop.image.png')
        MOVE_D = True

    if MOVE_W == True:
        bullet1.move_w()
    if MOVE_S == True:
        bullet1.move_s()
    if MOVE_A == True:
        bullet1.move_a()
    if MOVE_D == True:
        bullet1.move_d()

    sc.blit(bullet1.image, bullet1.rect_bullet)
    sc.blit(monster1.image, monster1.rect_monster)
    pygame.display.update()
    pygame.time.delay(20)

    hero1.update(W/2, H/2)

    monster1.move()
    if monster1.x == hero1.x and monster1.y == hero1.y:
        monster1.attack()
    '''print(hero1.x, hero1.y)
    print(monster1.x, monster1.y)
    print(hero1.hp)'''
    print (MOVE_W)
    print (bullet1.rect_bullet.y)