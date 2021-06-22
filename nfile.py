import pygame, sys
from pygame import surface

from pygame.constants import K_LEFT, K_RIGHT

pygame.init()

sc_length, sc_height = 600, 400

black = (0, 0, 0)
white = (255, 255, 255)
blue  = (0, 0, 255)
red  = (255, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((sc_length, sc_height))
screen.fill((255, 255, 255))
pygame.display.set_caption('game')

fp = pygame.time.Clock()
fp.tick(60)

image = pygame.image.load('player.png').convert()
image = pygame.transform.scale(image, (50, 50))  
surf = pygame.Surface((50, 50))                    #image is also surface
rect0 = surf.get_rect()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(image, (sc_length//2, sc_height//2))   #rect not allowed, surface allowed
    #pygame.draw.rect(screen, red, rect0, 5)
    fp.tick(60)

    pygame.display.update()
    




