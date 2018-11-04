import pygame
pygame.init()
W = 1072
H = 634
WHITE = (255, 255, 255)

keys = pygame.key.get_pressed()


class Hero (pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        # прячем фон белого цвета
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3
        self.x = self.rect.x
        self.y = self.rect.y

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
            if keys[pygame.K_DOWN] :
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

    def strike(self):
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
                self.rect_bullet.x += self.strike_speed


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

    def move_w(self):
        if self.rect_bullet.y > 90:
            self.rect_bullet.y -= self.strike_speed
        else:
            self.kill()
            global MOVE_W
            MOVE_W = False
    def move_s(self):
        if self.rect_bullet.y < H-90:
            self.rect_bullet.y += self.strike_speed
        else:
            self.kill()
            global MOVE_S
            MOVE_S = False
    def move_a(self):
        if self.rect_bullet.x > 90:
            self.rect_bullet.x -= self.strike_speed
        else:
            self.kill()
            global MOVE_A
            MOVE_A = False

    def move_d(self):
        if self.rect_bullet.x < W-90:
            self.rect_bullet.x += self.strike_speed
        else:
            self.kill()
            global MOVE_D
            MOVE_D = False


class Monsters (Hero):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)



sc = pygame.display.set_mode((W, H))

background_surf = pygame.image.load('field.png').convert()
background_rect = background_surf.get_rect(topleft=(0, 0))
sc.blit(background_surf, background_rect)

BULLETS_SURF = []


hero1 = Hero(W/2, H/2, 'hero.png')

bullet1 = Bullet(hero1.x, hero1.y, 'pop.image.png')


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
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

    sc.blit(bullet1.image, bullet1.rect_bullet )
    pygame.display.update()
    pygame.time.delay(20)

    hero1.update(W/2, H/2)

    print(hero1.x, hero1.y)

