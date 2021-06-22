import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red

pygame.display.set_caption('My new game')
#icon = pygame.image.load('')
pygame.display.set_caption('Game')
running = True
while running():
    for event in pygame.event.get():
        if event.type == pygame.QUiT():
            pygame.quit()
            sys.exit()
