import pygame 
import numpy as np
import sys
#import pygame_gui
from source import Button,object,world

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720


# aint gon lie, i aint designing another input systemm with s1 s2 s3 etc, imma call another librarie 
#nvmd shi needs a whole ahh refractor
popped=False




pygame.init()
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("mohamed pyhsics engine")
font=pygame.font.Font(None,36)


board=pygame.image.load("window.png").convert_alpha()
board=pygame.transform.scale(board,(1200,680))







beige=(200, 150, 120)
essp=(80, 65, 55)
esp_h=(10, 55, 80)
green= (0, 255, 0)
black= (0, 0, 0)
menu=Button(1150,50,100,50,"menu",essp,esp_h)
x=Button(50,50,50,50,"X",essp,esp_h)
worldo=world(15,screen,8)
obji=object(100,50,100,100,8000,1,0.7,False,pygame.Color('red'))
objii=object(100,200,100,100,1500,1,0.7,False,pygame.Color('blue'))
floor=object(0,700,1280,720,1,0.5,0.5,True,pygame.Color('black'))
ceil=object(0,-10,1280,20,1,0.5,0.5,True,pygame.Color('black'))
lw=object(-10,20,20,690,1,0.5,0.5,True,pygame.Color('black'))
rw=object(1270,20,20,690,1,0.5,0.5,True,pygame.Color('black'))

worldo.addobj(obji)
worldo.addobj(objii)
worldo.addobj(floor)
worldo.addobj(ceil)
worldo.addobj(rw)
worldo.addobj(lw)
clock =pygame.time.Clock()
while True:
    dt =clock.tick(60)/1000.0
    screen.fill(beige)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            worldo.pick(*event.pos)


        elif event.type==pygame.MOUSEBUTTONUP:
            worldo.release()
        elif event.type==pygame.MOUSEMOTION:
            worldo.set_mouse(*event.pos)
        menu.handle_event(event)
        if menu.clicked:
            popped=True
        if popped:
            x.handle_event(event)
        if x.clicked:
            popped=False


    menu.draw(screen)
    worldo.update(dt)
    worldo.render()
    menu.draw(screen)
    if popped :
        screen.blit(board,(20,20))
        x.draw(screen)
    
    pygame.display.flip()






