import pygame
import functions

pygame.init()
pygame.font.init()
screenx =600
screeny =600
screen = pygame.display.set_mode((screenx, screeny))
running: bool = True
background = 100, 100, 100
xc = 0
yc = 0
cbuttons =[]
while running:
    screen.fill((background))
    background = 100, 100, 100
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    xm, ym = pygame.mouse.get_pos()
    for i in range(6):
            xc = (screenx/6)*(i+0.5)
            yc = 100
            r = 40
            cbuttons.append((xc,yc))

    for i in cbuttons:
        xc, yc = i
        a = functions.collision_circle(xm, ym, xc, yc, r)
        if a == True:
            background = 200, 200, 200

    for i in cbuttons:
        pygame.draw.circle(screen,(40,40,40),(i),40)




    pygame.display.flip()
