from mmap import MADV_REMOVE
import pygame , random, sys, time

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP

pygame.init()

sc_width, sc_height = 1200, 700

black = (0, 0, 0)
white = (255, 255, 255)
blue  = (0, 0, 255)
red  = (255, 0, 0)
green = (0, 255, 0)

e_speed = 5
POINT = 0

font = pygame.font.SysFont("Helvetica", 70)
font_small = pygame.font.SysFont("Helvetica", 35)
end_font = pygame.font.SysFont("Helvetica", 35)
Game_Over = font.render("<-- Game Over -->", True, green)

screen = pygame.display.set_mode((sc_width, sc_height))
screen.fill(white)
pygame.display.set_caption('game')

fp = pygame.time.Clock()
fp.tick(60)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png').convert()
        self.image = pygame.transform.scale(self.image, (60, 120))

        self.surf = pygame.Surface((60, 120))
        self.rect = self.surf.get_rect()

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            
        if self.rect.right < sc_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
            
        if self.rect.bottom < sc_height:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
   
    def draw(self):
        screen.blit(self.surf, self.rect)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png").convert()
        self.image = pygame.transform.scale(self.image, (60, 120))
        self.image = pygame.transform.rotate(self.image, 180)
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40, 360)  ,0)) 

      def move(self):
        global POINT
        self.rect.move_ip(0,e_speed)
        if (self.rect.bottom > sc_height):
            POINT += 1
            
            self.rect.center = (random.randint(25, sc_width), 0)

      def draw(self):
        screen.blit(self.surf, self.rect) 

p1 = Player()
e1 = Enemy()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemies.add(e1)
all_sprites.add(p1)
all_sprites.add(e1)

while True:
    
    speed_event = pygame.USEREVENT + 1
    pygame.time.set_timer(speed_event, 5000)

    for event in pygame.event.get():
        if event.type == speed_event:
            e_speed += 0.1

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill(white)
    points = font_small.render(str(POINT), True, green)
    screen.blit(points, (22, 22))
    
 

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        entity.move()

    if  pygame.sprite.spritecollideany(p1, enemies):
        screen.fill(red)
        screen.blit(Game_Over, (sc_width//2, sc_height//2))
        t_score = end_font.render('Your Score --> ' + str(POINT), True, blue)
        screen.blit(t_score, (sc_width//2 + 90, sc_height//2 + 70))
        pygame.display.update()

        for entities in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    fp.tick(60)

    




