#init variables
movingright = False
movingleft = False
jump = 0

#main loop
player_movement = [0,0]
    if movingright == True:
        player_movement[0] += 2
    if movingleft == True:
        player_movement[0] -= 2
    player_movement[1] += jump
    jump += 0.2
    if jump > 3:
        jump = 3

#code for jump and collision 
if collisions['bottom'] == True:
        airtimer = 0
        jump = 0
    else:
        airtimer += 1
        
#movement and jumping with part-collision
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
            if airtimer < 6:
                jump = -5
    if event.type==KEYUP:
        if event.key==K_d:
            movingright=False
        if event.key==K_a:
            movingleft=False

