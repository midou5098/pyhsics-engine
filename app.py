import pygame 
import numpy as np
import sys
#import pygame_gui
from source import Button,object,world,textzone

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720


# aint gon lie, i aint designing another input systemm with s1 s2 s3 etc, imma call another librarie 
#nvmd shi needs a whole ahh refractor
popped=False







def animatepop(wy,opening,closing ):
    if opening  and wy>800:
        wy-=10
    elif closing  and wy <1300:
        wy+=10
    return wy
    















pygame.init()
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("mohamed pyhsics engine")
font=pygame.font.Font(None,26)


board=pygame.image.load("window.png").convert_alpha()
board=pygame.transform.scale(board,(640,920))




error=""


beige=(200, 150, 120)
essp=(80, 65, 55)
esp_h=(10, 55, 80)
green= (0, 255, 0)
black= (0, 0, 0)
menu=Button(1150,50,100,50,"menu",essp,esp_h)
x=Button(1000,50,50,50,"X",essp,esp_h)
worldo=world(1000,screen,8)
obji=object(100,50,100,100,8000,1,0.7,False,pygame.Color('red'),"nigro")
objii=object(100,200,100,100,1500,1,0.7,False,pygame.Color('blue'),"redo")
floor=object(0,700,1280,720,1,0.5,0.5,True,pygame.Color('black'),"bruh")
ceil=object(0,-10,1280,20,1,0.5,0.5,True,pygame.Color('black'),"why tf")
lw=object(-10,20,20,690,1,0.5,0.5,True,pygame.Color('black'),"am i even")
rw=object(1270,20,20,690,1,0.5,0.5,True,pygame.Color('black'),"doing all of this ")

addb=Button(1100,500,100,50,"add",essp,esp_h)
namez=textzone(1100,245,120,30)
massz=textzone(1100,300,120,30)
colorz=textzone(1100,350,120,30)
add="<- adding object ->"
name="name :"
mass="mass :"
color="color :"
xt=1300
txtadd=font.render(add,True,pygame.Color('black'))
txtname=font.render(name,True,pygame.Color('black'))
txtmass=font.render(mass,True,pygame.Color('black'))
txtcolor=font.render(color,True,pygame.Color('black'))

worldo.addobj(obji)
worldo.addobj(objii)
worldo.addobj(floor)
worldo.addobj(ceil)
worldo.addobj(rw)
worldo.addobj(lw)
clock =pygame.time.Clock()
opening =False
closing =False
while True:
    dt =clock.tick(60)/1000.0
    screen.fill(beige)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            namez.record(event)
            massz.record(event)
            colorz.record(event)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            worldo.pick(*event.pos)
            namez.focus(*event.pos)
            massz.focus(*event.pos)
            colorz.focus(*event.pos)
        
        elif event.type==pygame.MOUSEBUTTONUP:
            worldo.release()
        elif event.type==pygame.MOUSEMOTION:
            worldo.set_mouse(*event.pos)
        menu.handle_event(event)
        addb.handle_event(event)
        if addb.clicked:
            if namez.text=="" or massz.text=="" or colorz.text=="":
                error="fill all fields !"
            elif not massz.text.isdigit():
                error="enter right values!"
            elif not colorz.text in pygame.color.THECOLORS:
                error="not a pygame color!"
            else:
                obs=object(100,100,100,100,int(massz.text),0.7,0.7,False,colorz.text,namez.text)
                worldo.addobj(obs)
        if menu.clicked:
            if not popped and not opening and not closing  :
                popped=True
                opening=True
                closing=False
            menu.clicked=False
        if popped:
            x.handle_event(event)
            if x.clicked:
                popped=False
                opening =False
                closing=True
                x.clicked=False
                
    menu.draw(screen)
    worldo.update(dt)
    worldo.render()
    menu.draw(screen)
    if opening or closing :
        xt=animatepop(xt,opening ,closing )
       
    screen.blit(board,(xt,-100))
    if (xt==800):
        opening=False
        x.draw(screen)
        screen.blit(txtadd,(1010,150))
        namez.render(screen,font)
        massz.render(screen,font)
        colorz.render(screen,font)
        screen.blit(txtname,(1000,250))
        screen.blit(txtmass,(1000,300))
        screen.blit(txtcolor,(1000,350))
        addb.draw(screen)
        if error!="":
            s=font.render(error,True,pygame.Color('black'))
            screen.blit(s,(1000,600))

    if (xt==1300):
        closing=False
        popped=False
        opening=False

    
    pygame.display.flip()












