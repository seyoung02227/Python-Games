#coding=utf-8

import pygame
pygame.init()

onScreen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Rect Drawing')

finish = False

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        pygame.draw.rect(onScreen, (0,128,255), pygame.Rect(20, 20, 100, 100))
        pygame.display.flip()
