import pygame 
import numpy as np
import sys

WINDOW_WIDTH=1280
WINDOW_HEIGHT=720






pygame.init()
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("mohamed pyhsics engine")
font=pygame.font.Font(None,36)
green= (0, 255, 0)



while True:
    screen.fill(green)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()






