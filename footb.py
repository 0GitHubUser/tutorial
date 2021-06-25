import pygame, sys,random
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT
from mmap import MADV_REMOVE

pygame.init()

sc_width, sc_height = 1200, 700

screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption('game')

black = (0, 0, 0)
white = (255, 255, 255)
blue  = (0, 0, 255)
red  = (255, 0, 0)
green = (0, 255, 0)

font1 = pygame.font.SysFont("Helvetica", 70)

screen = pygame.display.set_mode((sc_width, sc_height))
screen.fill(white)
pygame.display.set_caption('game')

speed = 5

fp = pygame.time.Clock()
fp.tick(60)

class FootBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('football.png').convert()
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.surf = pygame.Surface((60, 60))
        self.rect = self.surf.get_rect(center = (random.randint(40, 360)  ,0)) 

    def move(self):
        global speed
        # pressed_keys = pygame.key.get_pressed()
        self.rect.move_ip(0, speed)
        if self.rect.bottom > sc_height:
            speed = - speed
        
        print(self.rect.top)
  

ball = FootBall()

Balls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
Balls.add(ball)
all_sprites.add(ball)
# all_sprites.add(e1)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    for entity in all_sprites:      
        entity.move()
        
    screen.blit(entity.surf, entity.rect)

    pygame.display.update()
    fp.tick(30)








