import pygame,sys,random

pygame.init()
pygame.font.init()

size = width , height = 700,700

screen = pygame.display.set_mode(size)

black = 0,0,0
white = 255,255,255
yellow = 255,255,0
red = 255,0,0

clock = pygame.time.Clock()

pos_xy = [[345,345]]
increment_value = [0,0]
food_x = random.randint(2,68)*10 +5
food_y = random.randint(2,68)*10 +5
gamestate =True
fint = pygame.font.Font(pygame.font.get_default_font(), 36)
pos = 0,0


while 1:
    check = True
    clock.tick(10)
    screen.fill(black)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                increment_value = 0,-10
            elif e.key == pygame.K_s:
                increment_value = 0,10
            elif e.key == pygame.K_a:
                increment_value = -10,0
            elif e.key == pygame.K_d:
                increment_value = 10,0
        elif e.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
    if pos_xy[0][0]+increment_value[0] in range(0,700):
        pos_xy[0][0]+= increment_value[0]
    if pos_xy[0][1]+increment_value[1] in range(0,690):
       pos_xy[0][1] += increment_value[1]
    
    if gamestate:
        for i in range(len(pos_xy),0,-1):
        
            pygame.draw.rect(screen,yellow,pygame.Rect(pos_xy[i-1][0],pos_xy[i-1][1],10,10)),
            if i-1 == 0:
                continue
            else:
                pos_xy[i-1] = list([pos_xy[i-2][0],pos_xy[i-2][1]])

            
        pygame.draw.rect(screen,red,pygame.Rect(food_x,food_y,10,10))
    
    if pos_xy[0][0] == food_x and pos_xy[0][1] == food_y:
        pos_xy.append([food_x,food_y])
        food_x = random.randint(2,68)*10 +5
        food_y = random.randint(2,68)*10 +5
        check = False

    if check:
        for i in range(2,len(pos_xy)):
            if pos_xy[0] == pos_xy[i]:
                increment_value = 0,0
                gamestate = False 
        
    if not gamestate:
        pygame.draw.rect(screen,(106,106,106),pygame.Rect(270,330,160,40))
        text = fint.render("RETRY?",True,white)
        screen.blit(text,(280,332))
        if pos[0] in range(270,430):
            if pos[1] in range(330,370):
                pos_xy = [[345,345]]
                increment_value = [0,0]
                food_x = random.randint(2,68)*10 +5
                food_y = random.randint(2,68)*10 +5
                gamestate =True
                pos = 0,0
        
    pygame.display.flip()