##Author: Indranil Ghosh, Jadavpur University, Physics Department

import random, pygame, sys
from pygame.locals import *

#set up the window
DISPLAYSURF=pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('Sierpinski Triangle')

#set up the colors
BLACK=(0, 0, 0)
RED=(255, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)

#set up the points for sierpinski's Triangle 
A  =  (305, 50)
B  =  (600, 640)
C  =  (10, 640)
St =  (1, 1)

while True:
    #for Sierpinski's triangle 
    x=random.randint(1, 6)
    if x==1 or x==2: St=((St[0] + A[0])/2, (St[1] + A[1])/2)
    elif x==3 or x==4: St=((St[0] + B[0])/2, (St[1] + B[1])/2)
    else: St=((St[0] + C[0])/2, (St[1] + C[1])/2)	
    pygame.draw.circle(DISPLAYSURF, RED, St, 0, 0)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
