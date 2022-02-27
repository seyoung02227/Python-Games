import pygame
pygame.init()

displayWidth = 1200
displayHeight = 100

onScreen = pygame.display.set_mode((displayWidth, displayHeight))

photoimg = pygame.image.load('./image/fall.jpg')

def imgLocation (xx,y):
    onScreen.blit(photoimg,(x,y))

x = (displayWidth * 0.35)
y = (displayWidth * 0.35)

finish = False

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

        onScreen.fill((128,1288,128))
        imgLocation(xx,y)
        pygame.display.flip()
