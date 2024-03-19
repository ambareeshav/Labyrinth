import pygame
import sys
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init() 
pygame.mixer.init()
pygame.display.set_caption('Labyrinth')
WINDOW_SIZE = (1920,1080)
screen=pygame.display.set_mode(WINDOW_SIZE,0,64)
display=pygame.Surface((960,540))
movingright = False
movingleft = False
jump = 0
airtimer = 0
truescroll = [0,0]

#loading all files
grass_img=pygame.image.load('Images/ig/floor.png')
dirt_img=pygame.image.load('Images/ig/wall.png')
bg=pygame.image.load('Images/ig/bg1.png')
mleft=[pygame.image.load('Images/l/0.png'),pygame.image.load('Images/l/1.png'),pygame.image.load('Images/l/2.png'),pygame.image.load('Images/l/3.png'),pygame.image.load('Images/l/4.png'),pygame.image.load('Images/l/5.png'),pygame.image.load('Images/l/0.png'),pygame.image.load('Images/l/1.png'),pygame.image.load('Images/l/2.png'),pygame.image.load('Images/l/3.png'),pygame.image.load('Images/l/4.png'),pygame.image.load('Images/l/5.png')]
mright=[pygame.image.load('Images/r/0.png'),pygame.image.load('Images/r/1.png'),pygame.image.load('Images/r/2.png'),pygame.image.load('Images/r/3.png'),pygame.image.load('Images/r/4.png'),pygame.image.load('Images/r/5.png'),pygame.image.load('Images/r/0.png'),pygame.image.load('Images/r/1.png'),pygame.image.load('Images/r/2.png'),pygame.image.load('Images/r/3.png'),pygame.image.load('Images/r/4.png'),pygame.image.load('Images/r/5.png')]
pfront=[pygame.image.load('Images/s/0.png'),pygame.image.load('Images/s/1.png'),pygame.image.load('Images/s/2.png'),pygame.image.load('Images/s/3.png'),pygame.image.load('Images/s/4.png')]
menu_anim=[pygame.image.load('Images/ig/menu.png'),pygame.image.load('Images/ig/menu1.png')]
menu1_anim=[pygame.image.load('Images/m/1.png'),pygame.image.load('Images/m/2.png'),pygame.image.load('Images/m/3.png'),pygame.image.load('Images/m/4.png')]
level_anim=[pygame.image.load('Images/lg/1.png'),pygame.image.load('Images/lg/2.png'),pygame.image.load('Images/lg/3.png'),pygame.image.load('Images/lg/4.png')]
mgame_img=pygame.image.load('Images/ig/midgame.png')
opt_img=pygame.image.load('Images/ig/opt.png')
ls_img=pygame.image.load('Images/ig/levels.png')
t_img=pygame.image.load('Images/ig/Text.png')
t1_img=pygame.image.load('Images/ig/Text1.png')
pygame.mixer.music.load('Music/theme.wav')
player_rect = pygame.Rect(1200,100,16,16)
bob=pygame.Rect(1500,200,500,250)
truescroll[0]+=(player_rect.x-truescroll[0]-150)
truescroll[1]+=(player_rect.y-truescroll[1]-110)

#collision
def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list   

#movement,physics
def move(rect,movement,tiles):
    collision_types={'top':False,'bottom':False,'right':False,'left':False}
    rect.x+=movement[0]
    hit_list=collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right=tile.left
            collision_types['right']=True
        elif movement[0] < 0:
            rect.left=tile.right
            collision_types['left']=True
    rect.y+=movement[1]
    hit_list=collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom=tile.top
            collision_types['bottom']=True
        elif movement[1]<0:
            rect.top = tile.bottom
            collision_types['top']=True
    return rect, collision_types

#main loop
run=True
game=True
menu=True
mid=False
opt=False
levels=False
level=1
m=-1
v=0.1
f=0
pygame.mixer.music.play(m)
pygame.mixer.music.set_volume(v)
while run:
    clock.tick(60)
    while menu:
        def load_map():
            level=1
            f=open(f"Images/Maps/map_{level}.txt","r")
            data=f.read()
            f.close()
            data=data.split('\n')
            game_map=[]
            for row in data:
                game_map.append(list(row))
            return game_map
        game_map=load_map()

        for k in range(2):
            screen.blit(menu_anim[k],(0,0))
            pygame.display.update()
            pygame.time.delay(500)                

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()  
            elif event.type == KEYUP:
                if event.key==K_q:
                    for i in range(1):
                        for k in range(4):
                            screen.blit(menu1_anim[k],(0,0))
                            pygame.display.update()
                            pygame.time.delay(500)
                    menu=False
                    game=True                    

        pygame.display.update()
        clock.tick(60)
   
    while mid:
        screen.blit(mgame_img,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == KEYUP:
                if event.key==K_ESCAPE:
                    mid=False
                    game=True
                    movingleft=False
                    movingright=False
                if event.key==K_o:
                    mid=False
                    opt=True
                if event.key==K_l:
                    mid=False
                    levels=True
                    
        pygame.display.update()
        clock.tick(60)

    while levels:
        screen.blit(ls_img,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key==K_ESCAPE:
                    map_draw=False
                    levels=False
                    mid=True
                if event.key==K_1:
                    level=1
                    player_rect = pygame.Rect(1200,100,16,16)
                    map_draw=True                    
                if event.key==K_2:
                    level=2
                    player_rect = pygame.Rect(2000,100,16,16)
                    map_draw=True
                if event.key==K_3:
                    level=3
                    player_rect = pygame.Rect(2700,100,16,16)
                    map_draw=True
                if event.key==K_4:
                    level=4
                    player_rect = pygame.Rect(2800,100,16,16)
                    map_draw=True
                if map_draw:
                    def load_map():
                        f=open(f"Images/Maps/map_{level}.txt","r")
                        data=f.read()
                        f.close()
                        data=data.split('\n')
                        game_map=[]
                        for row in data:
                            game_map.append(list(row))
                        return game_map
                    game_map=load_map()
                    jump = 0
                    airtimer = 0
                    truescroll[0]+=(player_rect.x-truescroll[0]-150)
                    truescroll[1]+=(player_rect.y-truescroll[1]-110)
                    for k in range(4):
                        screen.blit(level_anim[k],(0,0))
                        pygame.display.update()
                        pygame.time.delay(500)
                        levels=False
                    game=True
        pygame.display.update()
        clock.tick(60)

    while opt:
        screen.blit(opt_img,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == KEYUP:
                if event.key==K_ESCAPE:
                    menu=False
                    mid=False
                    game=False
                    opt=False
                    mid=True
                if event.key==K_t:
                    pygame.mixer.music.pause()
                if event.key==K_r:
                    pygame.mixer.music.unpause()
            if event.type == KEYDOWN:
                if event.key==K_UP:
                    if v<=1:
                        v+=0.1
                        print(v)
                    pygame.mixer.music.set_volume(v)
                if event.key==K_DOWN:
                    if v>=0.1:
                        v-=0.1
                        print(v)
                    pygame.mixer.music.set_volume(v)
        pygame.display.update()
        clock.tick(60)      
    while game:
        
        truescroll[0]+=(player_rect.x-truescroll[0]-150)/20
        truescroll[1]+=(player_rect.y-truescroll[1]-110)/20
        scroll=truescroll.copy()
        scroll[0]=int(scroll[0])
        scroll[1]=int(scroll[1])
        display.blit(bg,(0,0))   
        
        tile_rects = []
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '1':
                    display.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))                    
                if tile == '2':
                    display.blit(grass_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '5':
                    display.blit(t1_img,(x*16-scroll[0],y*16-scroll[1]))                
                if tile != '0':
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                x += 1
            y += 1


        player_movement = [0,0]

        if f+1>60:
            f=0    
            
        elif movingright == True :
            player_movement[0] += 5
            display.blit(mright[f//5],(player_rect.x-scroll[0],player_rect.y-scroll[1]))
            f+=1            
           
        elif movingleft == True :
            player_movement[0] -= 5
            display.blit(mleft[f//5],(player_rect.x-scroll[0],player_rect.y-scroll[1]))
            f+=1
            
        else:
            display.blit(pfront[f//12],(player_rect.x-scroll[0],player_rect.y-scroll[1]))
            f+=1
                   
        player_movement[1] += jump
        jump += 0.249
        if jump > 4:
            jump = 4
        
        player_rect,collisions = move(player_rect,player_movement,tile_rects)
        if collisions['bottom'] == True:
            airtimer = 0
            jump = 0
        if collisions['top'] == True:
            airtimer +=0.5
            jump = 1

        else:
            airtimer += 0.5
                    
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key==K_d:
                    movingright=True
                if event.key==K_a:
                    movingleft= True
                if event.key==K_SPACE:
                    if airtimer < 5:
                        jump = -5
            if event.type==KEYUP:
                if event.key==K_d:
                    movingright=False
                if event.key==K_a:
                    movingleft=False
                if event.key==K_SPACE:
                    if airtimer < 0:
                        jump = 0
            if event.type==KEYUP:
                if event.key==K_ESCAPE:
                    menu=False
                    game=False  
                    mid=True
            if event.type==KEYUP:
                if event.key==K_o:
                    menu=False
                    game=False  
                    mid=False
                    opt=True
                if event.key==K_g:
                    pygame.draw.rect(screen,[0,0,0,],[0,0,1920,1080])
                    pygame.display.update()
                    pygame.time.delay(500)
                    if level==1:
                        player_rect = pygame.Rect(1200,100,16,16)
                    elif level==2:
                        player_rect = pygame.Rect(2000,100,16,16)
                    elif level==3:
                        player_rect = pygame.Rect(2700,100,16,16)
                    elif level==4:
                        player_rect = pygame.Rect(2800,100,16,16)
    
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)
