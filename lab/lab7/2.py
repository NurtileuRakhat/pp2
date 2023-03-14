import pygame
import os
from random import choice
pygame.init()
w,h = 400,600
begin , is_sing = False,False
global musics
global i
vol,i = 1, 0
stop , volumeUP,volumeDown = True,False,False
icon = None

def load_music():
    songs = []
    list_of_music = os.listdir(r'C:\Users\Nurtileu\Desktop\git\lab\lab7\music')
    for files in list_of_music:
        if files.endswith('.mp3'):
            songs.append(files) 
    return songs
musics = load_music()

sc = pygame.display.set_mode(( w , h))
pygame.display.set_caption("Media Player")
pygame.display.set_icon(pygame.image.load(r"C:\Users\Nurtileu\Desktop\git\lab\lab7\image\icon2.png"))

surf_1 = pygame.Surface((340, 55))

# image = pygame.image.load(r'C:\Users\Nurtileu\Desktop\git\lab\lab7\image\image.png').convert_alpha()
# image = pygame.transform.scale(image,(image.get_width()//2,image.get_height()//2))
# image_rect = image.get_rect(center = (w//2,h//2))

icon_play = pygame.image.load(r'C:\\Users\\Nurtileu\Desktop\\git\\lab\\lab7\\image\\1-18309_big-image-media-player-buttons-png (6).png').convert_alpha()
icon_stop = pygame.image.load(r'C:\\Users\\Nurtileu\Desktop\\git\\lab\\lab7\\image\\1-18309_big-image-media-player-buttons-png (3).png').convert_alpha()
icon_next = pygame.image.load(r'C:\\Users\\Nurtileu\Desktop\\git\\lab\\lab7\\image\\1-18309_big-image-media-player-buttons-png (5).png').convert_alpha()
icon_previous = pygame.image.load(r'C:\\Users\\Nurtileu\Desktop\\git\\lab\\lab7\\image\\1-18309_big-image-media-player-buttons-png (4).png').convert_alpha()
juzz_icon = pygame.image.load(r"C:\\Users\\Nurtileu\Desktop\\git\\lab\\lab7\\image\\1200x1200bf-60.jpg").convert()
stan_icon = pygame.image.load(r"C:\\Users\\Nurtileu\Desktop\\git\\lab\\lab7\\image\s-l1600-4-1.jpg")
loseYorself_icon = pygame.image.load(r"C:\\Users\\Nurtileu\Desktop\\git\\lab\\lab7\\image\\800x800bb.jpg")
Godzila_icon = pygame.image.load(r"C:\\Users\\Nurtileu\Desktop\\git\\lab\\lab7\\image\\Eminem.jpg")

icon_play = pygame.transform.scale(icon_play,(icon_play.get_width()//8,icon_play.get_height()//8))
icon_stop = pygame.transform.scale(icon_stop,(icon_stop.get_width()//8,icon_stop.get_height()//8))
icon_next = pygame.transform.scale(icon_next,(icon_next.get_width()//10,icon_next.get_height()//10))
icon_previous = pygame.transform.scale(icon_previous,(icon_previous.get_width()//10,icon_previous.get_height()//10))
juzz_icon = pygame.transform.scale(juzz_icon,(juzz_icon.get_width()//4.9,juzz_icon.get_height()//4.9))
stan_icon = pygame.transform.scale(stan_icon,(stan_icon.get_width()//4.19,stan_icon.get_height()//4.19))
loseYorself_icon = pygame.transform.scale(loseYorself_icon,(loseYorself_icon.get_width()//3.27,loseYorself_icon.get_height()//3.27))
Godzila_icon = pygame.transform.scale(Godzila_icon,(Godzila_icon.get_width()//5.03,Godzila_icon.get_height()//3.58))

icon_play_rect = icon_play.get_rect(center = (w//2,h//1.2))
icon_stop_rect = icon_stop.get_rect(center = (w//2,h//1.2))
icon_next_rect = icon_next.get_rect(center = (290,h//1.2))
icon_previous_rect = icon_previous.get_rect(center = (110,h//1.2))

clock = pygame.time.Clock()
x = 33
while 1:
    sc.fill((0,0,0))
    # sc.blit(image,image_rect)
    sc.blit(icon_play,icon_play_rect)
    sc.blit(icon_next,icon_next_rect)
    sc.blit(icon_previous,icon_previous_rect)
    if pygame.mixer.music.get_busy() == True:
        is_sing = True
    else:
        is_sing = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                begin = True
                music = musics[0]
                i = musics.index(music)
                pygame.mixer.music.load(f'music\{music}')
                pygame.mixer.music.play()
                icon = 0
                x = 33
                stop = False
                
            if event.key == pygame.K_SPACE: 
                if not is_sing:
                    pygame.mixer.music.unpause()
                    stop = False
                else:
                    pygame.mixer.music.pause()
                    stop = True

            if event.key == pygame.K_RIGHT and is_sing:
                x = 33
                if i == len(musics) - 1:
                    i = 0
                    icon = 0
                else:
                    i += 1
                    icon += 1
                pygame.mixer.music.load(f'music\{musics[i]}')
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT and is_sing:
                x = 33
                if i == 0:
                    icon = len(musics) - 1
                    i = len(musics) - 1
                else:
                    i -= 1
                    icon -= 1
        
                pygame.mixer.music.rewind()
                pygame.mixer.music.load(f'music\{musics[i]}')
                pygame.mixer.music.play()
        
            if event.key == pygame.K_UP: 
                volumeUP = True
                
            if event.key == pygame.K_DOWN:
                volumeDown = True

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP,pygame.K_DOWN]:
                volumeUP , volumeDown = False , False

    font = pygame.font.SysFont('Tahoma', 16, True) 

    if stop:
        sc.fill((0,0,0))
        sc.blit(icon_next,icon_next_rect)
        sc.blit(icon_previous,icon_previous_rect)
        sc.blit(icon_play,icon_play_rect)
        
    if stop == False:
        sc.fill((0,0,0))
        sc.blit(icon_next,icon_next_rect)
        sc.blit(icon_previous,icon_previous_rect)
        sc.blit(icon_stop,icon_stop_rect)
        x+=0.5
    
    sc.blit(surf_1, (30, 350))
    surf_1.fill((50,50,50))

    if begin:
        s = font.render(musics[i][:-4], True, 'white')  
        sc.blit(s, (x, 350)) 
    
    if x >=200:
        x = 33

    if volumeUP == True:
        vol += 0.01
        pygame.mixer.music.set_volume(vol)
    if volumeDown == True:
        vol -= 0.01
        pygame.mixer.music.set_volume(vol)

    if icon == 0 or icon == 1:
        sc.blit(juzz_icon,(80,90))
    if icon == 2:
        sc.blit(Godzila_icon, (80,90))
    if icon == 3:
        sc.blit(loseYorself_icon, (80,90))
    if icon == 4:
        sc.blit(stan_icon, (80,90))
    
    pygame.display.update()
    clock.tick(60)