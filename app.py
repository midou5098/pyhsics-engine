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
beige=(200, 150, 120)
essp=(80, 65, 55)
esp_h=(10, 55, 80)
green= (0, 255, 0)
black= (0, 0, 0)
xbox=pygame.Rect((50,320),(200,420))
menu=Button(1150,50,100,50,"menu",essp,esp_h)


while True:
    screen.fill(beige)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        menu.handle_event(event)

    menu.draw(screen)
    pygame.draw.rect(screen,black,xbox)
    
    pygame.display.flip()






