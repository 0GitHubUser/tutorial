import pygame, sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('game')

while True:
    pygame.display.update()
    for events in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


