##Author: Indranil Ghosh, Jadavpur University, Physics Department


import random, pygame, sys
from pygame.locals import *

DISPLAYSURF=pygame.display.set_mode((600, 600),)
pygame.display.set_caption("Barnsley's fern")

GREEN=(0, 255, 0)

X=[0.0]
Y=[0.0]
i=0

while True:
    r=random.random() 
    if r<=0.02:
        X+=[0.0, ]
        Y+=[0.16*Y[i], ]
    elif r<=0.86:
        X+=[0.85*X[i] + 0.04*Y[i], ]
        Y+=[-0.024*X[i] + 0.85*Y[i] + 1.6, ]
    elif r<=0.93:
        X+=[0.20*X[i] - 0.26*Y[i], ]
        Y+=[0.23*X[i] + 0.22*Y[i] + 1.6, ]
    else:
        X+=[-0.15*X[i] + 0.28*Y[i], ]
        Y+=[0.26*X[i] + 0.24*Y[i] + 0.44, ]

    pygame.draw.circle(DISPLAYSURF, GREEN, (int(X[i]*90 + 300), 600 - int(Y[i]*50)), 0, 0) # Plotting the points after required transformations
    i+=1
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

