#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
MONEY = 0
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")
music = pygame.mixer.Sound('background.wav').play(-1)
#Create a white screen 
sc = pygame.display.set_mode((400,600))
sc.fill(WHITE)
pygame.display.set_caption("Game")

tenge_surf = pygame.image.load("tenge.png")
tenge_surf = pygame.transform.scale(tenge_surf, (tenge_surf.get_width()//8 ,tenge_surf.get_height()//8))

x,x1, = None,None

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        global x
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            x = self.rect.center

class coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("tenge.png")
        self.image = pygame.transform.scale(tenge_surf, (tenge_surf.get_width()//5 ,tenge_surf.get_height()//5))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global x1
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            x1 = self.rect.center

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
    
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
E2 = coin()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)



#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

s = 0

#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5   
            #   y -= 0.5   
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # анимируем движущийся фон
    sc.blit(pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, s % SCREEN_HEIGHT))
    sc.blit(pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, -SCREEN_HEIGHT + (s % SCREEN_HEIGHT)))
    s += SPEED / 2
    
    scores = font_small.render(str(SCORE), True, BLACK)
    sc.blit(scores, (10,575))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        sc.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          sc.fill(RED)
          sc.blit(game_over, (30,250))
          
          pygame.display.update()
          pygame.mixer.pause() # останавливаем музыку
          for entity in all_sprites:
                entity.kill() 
          pygame.mixer.Sound("46de0aab24bdde4.mp3").play()
          time.sleep(2)
          pygame.quit()
          sys.exit()        

    for entity in coins:
        entity.move()
        sc.blit(entity.image, entity.rect)
    
    if pygame.sprite.spritecollideany(E1, coins):
        E2.center = (random.randint(30, SCREEN_WIDTH - 30), 0)
    if pygame.sprite.spritecollideany(P1,coins):
        pygame.mixer.Sound('Bag-of-Coins-A-www.fesliyanstudios.com.mp3').play()
        x != x1
    for c in coins:
        if pygame.sprite.collide_rect(P1,c): # если игровая машинка получит монетку
            c.kill() 
            MONEY+= 200
            new = coin() # заново создаем объект монетки
            coins.add(new) # добавляем новый объект в группу 
    money = font_small.render(str(MONEY),True, BLACK)
    sc.blit(money, (200,10))
    pygame.display.update()
    FramePerSec.tick(FPS)