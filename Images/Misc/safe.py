import pygame
import sys
from sys import exit

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init() 
pygame.display.set_caption('Labyrinth')
WINDOW_SIZE = (1280,720)#1920,1080
screen=pygame.display.set_mode(WINDOW_SIZE,0,32)
display=pygame.Surface((640,360))#620,540
movingright = False
movingleft = False
jump = 0
airtimer = 0
truescroll = [0,0]
level=1

def load_map():
    f=open(f"map_{level}.txt","r")
    data=f.read()
    f.close()
    data=data.split('\n')
    game_map=[]
    for row in data:
        game_map.append(list(row))
        #print(game_map)
    return game_map
    

#loading all files
game_map=load_map()
grass_img=pygame.image.load('floor.png')
dirt_img=pygame.image.load('wall.png')
bg=pygame.image.load('bg1.jpg')
menu_img=pygame.image.load('menu.png')
menu1_img=pygame.image.load('menu1.png')
player_img=pygame.image.load('standing.png')
pleft_img=pygame.image.load('pleft.png')
pright_img=pygame.image.load('pright.png')
mgame_img=pygame.image.load('midgame.png')
opt_img=pygame.image.load('opt.png')
t_img=pygame.image.load('Text.png')
t1_img=pygame.image.load('Text1.png')
pygame.mixer.music.load('theme.wav')
player_img.set_colorkey((255,255,255))
player_rect = pygame.Rect(1200,220,16,16)
truescroll[0]+=(player_rect.x-truescroll[0]-150)
truescroll[1]+=(player_rect.y-truescroll[1]-110)

#collision
def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list   
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

#main
run=True
game=True
menu=True
mid=False
opt=False
m=-1
v=0.1
pygame.mixer.music.play(m)
pygame.mixer.music.set_volume(v)
while run:
   
    while menu:
        screen.blit(menu_img,(0,0))
        pygame.display.update()
        pygame.time.delay(500)
        screen.blit(menu1_img,(0,0))
        pygame.display.update()
        pygame.time.delay(500)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()  
            elif event.type == KEYUP:
                if event.key==K_q:
                    menu=False
                    game=True
                    

        pygame.display.update()
        clock.tick(60)
        #print("m")

    

    while mid:
        screen.blit(mgame_img,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == KEYUP:
                if event.key==K_ESCAPE:
                    menu=False
                    mid=False
                    game=True
                    movingleft=False
                    movingright=False
                if event.key==K_o:
                    menu=False
                    mid=False
                    game=False
                    opt=True
                    
        pygame.display.update()

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
                    v+=0.1
                    pygame.mixer.music.set_volume(v)
                if event.key==K_DOWN:
                    v-=0.1
                    pygame.mixer.music.set_volume(v)
        pygame.display.update()
                
    while game:

        

        display.blit(bg,(0,0))
        
        truescroll[0]+=(player_rect.x-truescroll[0]-150)/10
        truescroll[1]+=(player_rect.y-truescroll[1]-110)/10
        scroll=truescroll.copy()
        scroll[0]=int(scroll[0])
        scroll[1]=int(scroll[1])
    
        tile_rects = []
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '1':
                    display.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))
                    #,(x*16-scroll[0],y*16-scroll[1])
                if tile == '2':
                    display.blit(grass_img,(x*16-scroll[0],y*16-scroll[1]))
                    #,(x*16-scroll[0],y*16-scroll[1])
                if tile == '3':
                    display.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))
                    #,(x*16-scroll[0],y*16-scroll[1])
                if tile == '4':
                    display.blit(t_img,(x*16-scroll[0],y*16-scroll[1]))
                    #,(x*16-scroll[0],y*16-scroll[1])
                if tile == '5':
                    display.blit(t1_img,(x*16-scroll[0],y*16-scroll[1]))
                    #,(x*16-scroll[0],y*16-scroll[1])
                
                if tile != '0':
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                x += 1
            y += 1
            #print(x,y)

        player_movement = [0,0]

        if movingright == False and movingleft == False:
            display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))
            pygame.display.update()

        if movingright == True:
            player_movement[0] += 5
            #for i in mright:
            display.blit(pright_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))
            pygame.display.update()

        if movingleft == True:
            player_movement[0] -= 5
            #for i in mleft:
            display.blit(pleft_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))
            pygame.display.update()

        player_movement[1] += jump
        jump += 0.249
        if jump > 4:
            jump = 4
            
        player_rect,collisions = move(player_rect,player_movement,tile_rects)

        if collisions['bottom'] == True:
            airtimer = 0
            jump = 0
        if collisions['top'] == True:
            airtimer +=1
            jump = 1
        else:
            airtimer += 1
                    
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
                    player_rect = pygame.Rect(1200,220,16,16)
                                    
            #print("g")
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)

