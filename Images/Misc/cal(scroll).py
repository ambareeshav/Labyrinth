#init variables \/
truescroll = [0,0]

#in main loop
truescroll[0]+=(player_rect.x-truescroll[0]-152)/20
truescroll[1]+=(player_rect.y-truescroll[1]-106)/20
scroll=truescroll.copy()
scroll[0]=int(scroll[0])
scroll[1]=int(scroll[1])

#drawing
#drawing dirt,grass
#for tiles
#display.blit(x_img,(x*16-scroll[0],y*16-scroll[1]))
#[no scrolling while drawing for 0 in file]

display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1])
