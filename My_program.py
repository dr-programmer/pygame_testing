import pygame
import random
from pygame.locals import *
from sys import exit

background_image = 'black.jpg'
boat = 'pacman.png'
boat2 = 'burger.png'

pygame.init()
SCREEN_SIZE = (500, 500)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Pygame Demo")
background = pygame.image.load(background_image).convert()
player = pygame.image.load(boat).convert_alpha()
player1 = pygame.image.load(boat2).convert_alpha()

x, y = 150, 100
x1, y1 = 40, 200
MOVE_RIGHT = 1
MOVE_LEFT = 2
MOVE_UP = 3
MOVE_DOWN = 4
direction = 0
direction1 = 0

 
while True:
    
    for event in pygame.event.get():
         
        if event.type == QUIT:
            exit()
             
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = MOVE_LEFT
            elif event.key == K_RIGHT:
                direction = MOVE_RIGHT
            if event.key == K_UP:
                direction = MOVE_UP
            if event.key == K_DOWN:
                direction = MOVE_DOWN
            if event.key == K_ESCAPE:
                exit()
                 
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                direction = 0
            elif event.key == K_RIGHT:
                direction = 0
            if event.key == K_UP:
                direction=0
            if event.key == K_DOWN:
                direction=0
                 
         
    if(direction == MOVE_LEFT):
        if(x<=0):
            x=0
        else:
            x-=0.3
    elif(direction == MOVE_RIGHT):
        if(x>=464):
            x=464
        else:
            x+=0.3
    elif(direction == MOVE_UP):
        if(y<=0):
            y=0
        else:
            y-=0.3
    elif(direction == MOVE_DOWN):
        if(y>=458):
            y=458
        else:
            y+=0.3

    if(direction1 == MOVE_LEFT):
        if(x1<=0):
            x1=0
        else:
            x1-=4.3
    elif(direction1 == MOVE_RIGHT):
        if(x1>=464):
            x1=464
        else:
            x1+=4.3
    elif(direction1 == MOVE_UP):
        if(y1<=0):
            y1=0
        else:
            y1-=4.3
    elif(direction1 == MOVE_DOWN):
        if(y1>=458):
            y1=458
        else:
            y1+=4.3

    randomizer = random.randint(1,40000)

    if randomizer >= 1 and randomizer <= 10000:
        direction1 = MOVE_LEFT
    if randomizer > 10000 and randomizer <= 20000:
        direction1 = MOVE_RIGHT
    if randomizer > 20000 and randomizer <= 30000:
        direction1 = MOVE_UP
    if randomizer > 30000 and randomizer <= 40000:
        direction1 = MOVE_DOWN

    if direction == MOVE_DOWN:
        direction1 = MOVE_UP
    if direction == MOVE_UP:
        direction1 = MOVE_DOWN
    if direction == MOVE_LEFT:
        direction1 = MOVE_RIGHT
    if direction == MOVE_RIGHT:
        direction1 = MOVE_LEFT


    if (x+30 > x1 and x < x1+36 and y+35 > y1 and y < y1+42):
        exit()

    screen.blit(background, (0, 0))
    screen.blit(player1, (x1, y1))
    screen.blit(player, (x, y))
    pygame.display.update()
