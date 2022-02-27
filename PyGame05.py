import pygame
pygame.init()

onScreen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Keydown Color Change')

finish = False
colorOn = True
x=20
y=20
clock = pygame.time.Clock()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        colorOn = not colorOn

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    #onScreen.fill((0,0,0))

    if colorOn:
        color = (255, 128, 0)
    else:
        color = (255, 255, 255)

    pygame.draw.rect(onScreen, color, pygame.Rect(x,y,100,100))
    pygame.display.flip()
    # clock.tick(60)
