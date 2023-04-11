import pygame

pygame.init()
sc = pygame.display.set_mode((800, 600))
surf = pygame.Surface((700, 600))
buttons = pygame.Surface((100, 210)) # создаю панель кнопок
font = pygame.font.SysFont("Verdana", 15)
cur_color = 'white' # текущий цвет который могу менять
# создаем словарь комманд
commands = {
    'rhombus': [4, 4, 44, 44],
    'sqare': [52, 4, 44, 44],
    'right_triangle': [4,50, 44, 44],
    'eraser': [52, 50, 44, 44]
}
# функция для установки панели с кнопочек
def setsurf():
    surf.fill('black')
    buttons.fill('white')
    pygame.draw.rect(buttons, 'black', (2, 2, 96, 206), 1)
    pygame.draw.polygon(buttons, 'black', [[24,4], [4,24], [24,44],[44,24]])
    pygame.draw.rect(buttons, 'black', (58, 10, 32, 32), 1)
    pygame.draw.polygon(buttons, 'black', [[10,60],[40,60],[40,90]])
    pygame.draw.rect(buttons, 'black', (56, 58, 36, 28))
    sc.blit(surf, (0, 0))
    sc.blit(buttons, (700, 0))
# функция для отрисовки ромб
def rhombus(sc, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    b = abs(y1-y2)
    if x1 <= x2:
        if y1 < y2:
            pygame.draw.polygon(sc, color, [[x1+(b/2),y1], [x1,y1+b/2], [x1+b/2,y1+b],[x1+b,y1+b/2]],d)
        else:
            pygame.draw.polygon(sc, color, [[x1+(b/2),y1], [x1,y1-b/2], [x1+b/2,y1-b],[x1+b,y1-b/2]],d)

    else:
        if y1 < y2:
            pygame.draw.polygon(sc, color, [[x1-(b/2),y1], [x1,y1+b/2], [x1-b/2,y1+b],[x1-b,y1+b/2]],d)
        else:
            pygame.draw.polygon(sc, color, [[x1-(b/2),y1], [x1,y1-b/2], [x1-b/2,y1-b],[x1-b,y1-b/2]],d)
        
# функция для отрисовки квадрата
def sqare(sc, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    a = abs(x1-x2)
    if x1 <= x2:
        if y1 < y2:
            pygame.draw.polygon(sc, color , [[x1,y1],[x1,y1+a] ,[x1+a,y1+a],[x1+a,y1]],d)
        else:
            pygame.draw.polygon(sc, color , [[x1,y1],[x1,y1-a] ,[x1+a,y1-a],[x1+a,y1]],d)
    else:
        if y1 < y2:
            pygame.draw.polygon(sc, color , [[x1,y1],[x1-a,y1] ,[x1-a,y1+a],[x1,y1+a]],d)
        else:
            pygame.draw.polygon(sc, color , [[x1,y1],[x1,y1-a] ,[x1-a,y1-a],[x1-a,y1]],d)

# функция для отрисовки прямоугольным треугольником
def right_triangle(sc, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    a = abs(x1-x2)
    b = abs(y1-y2)
    if x1 <= x2:
        if y1 < y2:
            pygame.draw.polygon(sc, color, [[x1,y1], [x1,y1+b], [x1+b,y1+b]],d)
        else:
            pygame.draw.polygon(sc, color, [[x1,y1],[x1,y1-b],[x1+b,y1-b]],d)
    else:
        if y1 < y2:
            pygame.draw.polygon(sc, color, [[x1,y1],[x1,y1+b],[x1-b,y1+b]],d)
        else:
            pygame.draw.polygon(sc, color, [[x1,y1],[x1,y1-b],[x1-b,y1-b]],d)
        

last_pos = (0, 0)
w = 2
draw_rhombus = False
erase = False
ed = 50

d = {
    'rhombus' : True,
    'sqare': False,
    'right_triangle': False,
    'eraser': False
}

setsurf()
running = True
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # меняем цвета при нажатии на клавиши  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                cur_color = 'red'
            if event.key == pygame.K_2:
                cur_color = 'green'
            if event.key == pygame.K_3:
                cur_color = 'blue'
            if event.key == pygame.K_4:
                cur_color = 'white'  
        # при нажатии на область определенной кнопочки меняем значение соответственной команды на True в словаре комманд
        if event.type == pygame.MOUSEBUTTONDOWN:
            for k, v in commands.items():
                if v[0] <= pos[0]-700 <= v[0] + v[2] and v[1] <= pos[1] <= v[1] + v[3]:
                    d[k] = True
                    for i, j in d.items():
                        if i != k:
                            d[i] = False
                    break
        # запускаем функции соответственных комманд  
        if d['rhombus'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                rhombus(surf, last_pos, pos, w, cur_color)
        elif d['sqare'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                sqare(surf, last_pos, pos, w, cur_color)
        elif d['right_triangle'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                right_triangle(surf, last_pos, pos, w, cur_color)
        elif d['eraser'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pos
                pygame.draw.rect(surf, 'black', (x, y, ed, ed))
                erase = True
            if event.type == pygame.MOUSEMOTION:
                if erase:
                    pygame.draw.rect(surf, 'black', (pos[0], pos[1], ed, ed))
            if event.type == pygame.MOUSEBUTTONUP:
                erase = False
    # выделяю красной рамкой выбранную комманду
    for k, v in d.items():
        if v == True:
            pygame.draw.rect(buttons, 'red', commands[k], 1)
        else:
            pygame.draw.rect(buttons, 'black', commands[k], 1)
    
    sc.blit(buttons, (700, 0))
    sc.blit(surf, (0, 0))
    c = font.render('Press:', True, 'black')
    buttons.blit(c, (5, 100))
    r = font.render('1 - Red', True, 'black')
    buttons.blit(r, (5, 120))
    g = font.render('2 - Green', True, 'black')
    buttons.blit(g, (5, 140))
    b = font.render('3 - Blue', True, 'black')
    buttons.blit(b, (5, 160))
    y = font.render('4 - White', True, 'black')
    buttons.blit(y, (5, 180))

    pygame.display.update()
pygame.quit()
    