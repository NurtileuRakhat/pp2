import pygame
import datetime
pygame.init()
w = 600
h = 400
angle1 = 0
angle2 = 0

pygame.mixer.music.load("sound\\background.mp3")
pygame.mixer.music.play(-1)

f_sys = pygame.font.SysFont('twcen',30)
sc = pygame.display.set_mode((w,h),pygame.RESIZABLE)

pygame.display.set_caption("simple clock")
pygame.display.set_icon(pygame.image.load("image\icon.bmp"))

white = (255,255,255)
sc.fill(white)

mickey_surf = pygame.image.load("image\mickeyclock.jpg")

left_hand_surf = pygame.image.load("image\left_hand.png").convert_alpha()
right_hand_surf = pygame.image.load("image\\right_hand.png").convert_alpha()

mickey_surf = pygame.transform.scale( mickey_surf ,(mickey_surf.get_width()//2.7 , mickey_surf.get_height()//2.7))
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            exit()
    t = datetime.datetime.now()
    angle1 = -t.second*6
    angle2 = -t.minute * 6

    sc_f_sys = f_sys.render(f'{t:%H-%M-%S}', 1 , (0,0,0),(255,255,255))
    
    left_hand_surf1 = pygame.transform.rotate(left_hand_surf,angle1)
    right_hand_surf1 = pygame.transform.rotate(right_hand_surf,angle2)
    
    right_hand_surf1=pygame.transform.scale(right_hand_surf1,(right_hand_surf1.get_width()//1.2 ,right_hand_surf1.get_height()//1.5))
    left_hand_surf1=pygame.transform.scale(left_hand_surf1,(left_hand_surf1.get_width()//1.2 , left_hand_surf.get_height()//1.5))
    
    mickeyrect = mickey_surf.get_rect(center = (w//2,h//2))
    left_hand_rect = left_hand_surf1.get_rect(center = (w//2,h//2))
    right_hand_rect = right_hand_surf1.get_rect(center = (w//2,h//2))
    
    left_hand_surf1.set_colorkey((0,0,0))
    right_hand_surf1.set_colorkey((0,0,0))
    
    sc.blit(mickey_surf,mickeyrect)
    sc.blit(left_hand_surf1,left_hand_rect)
    sc.blit(right_hand_surf1,right_hand_rect)
    sc.blit(sc_f_sys,(10,10))    

    pygame.display.update()

    clock.tick(60)