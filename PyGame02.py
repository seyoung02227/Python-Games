import pygame
pygame.init() #initialize 초기화 과정 시작을 의미

onScreen = pygame.display.set_mode((400,300)) #Window Size 정의
pygame.display.set_caption('Pygame Window Open')

finish = False

while not finish: #while True: 와 같은 의미
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        pygame.display.flip()
