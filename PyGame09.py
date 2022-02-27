import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
fallimg = pygame.image.load('fall.jpg')
x = 10
y = 10
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        x += 10
        if x == 280:
            direction = 'down'
    elif direction == 'down':
        y += 10
        if y == 160:
            direction = 'left'
    elif direction == 'left':
        x -= 10
        if x == 10:
            direction = 'up'
    elif direction == 'up':
        y -= 10
        if y == 10:
            direction = 'right'

    DISPLAYSURF.blit(fallimg , (x,y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
