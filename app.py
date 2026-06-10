import pygame 
import numpy as np
import sys
from source import Button

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720








pygame.init()
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("mohamed pyhsics engine")
font=pygame.font.Font(None,36)
beige=(245, 240, 225)
green= (0, 255, 0)
menu=Button(1150,50,100,50,"menu",beige,beige,)


while True:
    screen.fill(beige)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    menu.draw(screen)
    pygame.display.flip()






