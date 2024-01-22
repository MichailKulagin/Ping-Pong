import pygame
from pygame import *
from random import *
import time

pygame.init()

w = randint(1, 6)
#w =3
if w ==1:
    back = (93, 250, 90)  # цвет фона (background) зеленый

if w ==2:
    back = (108, 149, 214)#голубой
 
if w ==3:
    back = (202, 243, 87)#желтый
if w ==4:
    back = (131, 87, 243)#фиолетовый
if w == 5:
    back = (0, 255, 176)#беризовый

if w ==6:
    back = (243, 84, 84 )#красный

win_width = 700
win_height = 500

window = pygame.display.set_mode((700, 500))  # окно программы (main window)
window.fill(back)
clock = pygame.time.Clock()
game = True
FPS = 70



class GameSprite(sprite.Sprite):
    def __init__(self, x, y, player_image, player_speed, width = 55, height= 55):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect= self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = player_speed
        self.width = width
        self.height = height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 120:
            self.rect.y +=self.speed
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.y == 0:
            self.direction = "down"
        if self.rect.y == 357:
            self.direction = "up"
        

        if self.direction == "down":
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed


platform_1 = Player(30, 70, "platform.png", 5, 30, 120)
platform_2 = Enemy(645, 170, "platform.png", 5, 30, 120)

while game == True:
    window.fill(back)
    keys_pressed = key.get_pressed() 

    for e in event.get():
        if e.type == QUIT:
            game = False


    platform_1.update()
    platform_1.reset()

    platform_2.update()
    platform_2.reset()

    # print(platform_2.rect.y)
    # platform_2.rect.y += 5
    # if platform_2.rect.y >= win_height - 120:
    #     platform_2.rect.y -= 5
    # if platform_2.rect.y <= 0 :
    #     platform_2.rect.y += 5
    # if platform_2.rect.y == 375:
    #     platform_2.rect.y -= 5
    pygame.display.update()
    clock.tick(FPS)
