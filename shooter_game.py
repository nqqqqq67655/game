#Создай собственный Шутер!

from pygame import *
from random import randint

font.init()
font1 = font.Font(None, 80)
win = font1.render("YOU WIN!", True, (255,255,255))
lose = font1.render("YOU LOSE", True, (180, 0, 0))
font2 = font.Font(None, 36)
#фоновая музыка
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")
#картинки
img_back = "galaxy.jpg" #фон игры
img_hero = "rocket.png" #герой
img_enemy = "ufo.png" #враг
img_bullet = "bullet.png" #пуля

score = 0
goal = 10
lost = 0
max_lost = 3
clock = time.Clock()
FPS = 60
clock.tick(FPS)

#класс родитель для др спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        #метод отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #класс главного игрока
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x< win_width - 80:
            self.rect.x += self.speed
#методвыстрел
    def fire(self):
        bullet = Bullet (imag.bullet, self.rect.centerx, self.rect.top, 15,10,-15)
        bullets.add(bullet)   
#класс врага
class Enemy(GameSprite):
    def upsate(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randit(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
#клвсс пуля
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if seelf.rect.y < 0:
            self.kill()

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
ship = Player(img_hero, 5, win_height - 100,80,100,10)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1,5))
    monsters.add(monster)
asteroids = sprite.Group()
for i in range(1,3):
    asteroids = Enremybullets = sprite.Group()
finish = False
run = True

rel_time = False

run_fire = 0

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                in run fire < 5 and rel_time == False
                run_fire_sound.play()
                ship.fire()
                fire_sound.play()
                ship.fire()

    if not finish:
        window.blit(background, (0,0))
        ship.update()
        monsters.update()
        asteroids.update()
        bullets.update()

        ship.reset()
        monsters.draw(window)
        asteroids.draw(window)
        bullets.draw(window)

        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3
            reload = font2.render("Wait, reload....", 1, (150, 0, 0))
            window.blit(reload, (260, 460))
        else:
            rum_fire = 0
            rel_time = False

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collibes:
            score = score + 1
            moster = Enemy(img_enemy,randit(80, win_width -80), -40, 80, 50, randint(1,5))
            monsters.add(monster)
                
        if spritecollide(ship, monsers, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200,200))
        if score >= goal:
            finish = True
            window.blit(win, (200,200))

        text = font2.render("счет: " +str(score), 1 (255, 255, 255))
        window.blit(text, (10,20))

        text_lose = font2.render("пропущено: " +str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        display.update()

    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(3000)
        for i in range(1, 6):
            monster = Enemy(img_enemy, randint(80, win_width -80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

time.delay(50)
