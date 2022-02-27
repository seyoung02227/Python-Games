import pygame
pygame.init()

onScreen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Keydown Color Change')

finish = False
colorOn = True

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            colorOn = not colorOn

        if colorOn:
            color = (0,128,255)
        else:
            color = (255, 255, 255)

        pygame.draw.rect(onScreen, color, pygame.Rect(20, 20, 100, 100))
        pygame.display.flip()
