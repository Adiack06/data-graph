import pygame
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600, 600))
xm =0
ym =0
xc = 100
yc = 100
r = 40
running: bool = True
background = 100, 100, 100


def collision_circle(xm,ym,xc,yc,r):
    if ((xm - xc)*(xm - xc)+((ym - yc)*(ym - 100))) <= r*r:
        return True



while running:
    screen.fill((background))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    xm, ym = pygame.mouse.get_pos()#
    c = collision_circle(xm,ym,xc,yc,r)
    if c == True:
        background = 255,255,255
    else:
        background = 100, 100, 100


    #if ((xm -centrex)*(xm - centrex)) <= xsize*xsize
        #if ((ym - centrey) * (ym - centrey)) <= ysize * ysize
    pygame.draw.circle(screen,(30,30,30),(100,100),40) #render circle

    pygame.display.flip()

