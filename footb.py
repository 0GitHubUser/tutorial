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
change = 'dn'

fp = pygame.time.Clock()
fp.tick(60)

class FootBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('football.png').convert()
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.surf = pygame.Surface((60, 60))
        self.rect = self.surf.get_rect(center = (random.randint(40, 360)  ,25)) 

    def move(self):
        global speed
        # pressed_keys = pygame.key.get_pressed()
        self.rect.move_ip(0, speed)
        if self.rect.bottom > sc_height or self.rect.top <  0:
            speed = - speed

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pla1.jpg').convert()
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.surf = pygame.Surface((60, 60))
        self.rect = self.surf.get_rect(center = (35, 35)) 
        

    def move(self):
        global change
        pressed_keys = pygame.key.get_pressed()


        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
                d = {'lt':0, 'rt':180, ''}
                self.image = pygame.transform.rotate(self.image, d[change])
                change = 'lt'
            
        if self.rect.right < sc_width :
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                d = {'rg':180,  'lt':0, 'up':90, 'dn':-90}
                self.image = pygame.transform.rotate(self.image, d[change])
                change = 'rg'

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
                d = {'up':0, 'dn':180, 'rg':-90, 'lt':90}
                self.image = pygame.transform.rotate(self.image, d[change])
                change = 'up'
            
        if self.rect.bottom < sc_height:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
                d = {'dn':0, 'up':180, 'rg':90, 'lt':-90}        
                self.image = pygame.transform.rotate(self.image, d[change])
                change = 'dn'
        

ball = FootBall()
player1 = Player()

playerzz = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
playerzz.add(player1)
all_sprites.add(player1)
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
        
    screen.blit(entity.image, entity.rect)

    for entity in playerzz:      
        entity.move()
        
    screen.blit(entity.image, entity.rect)

    # if  pygame.sprite.spritecollideany(ball, all_sprites):
    #     speed = -speed

    pygame.display.update()
    fp.tick(60)








