print("screen width")
screenx =int(input())
print("screen hight")
screeny =int(input())
print("number of variable")
numvar=int(input())



import pygame
import functions

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screenx,screeny))
running: bool = True
background = 100, 100, 100
cbuttons =[]
shown = 0
for i in range(numvar):
    xc = (screenx / numvar) * (i + 0.5)
    yc = 100
    r = 40
    cbuttons.append((xc, yc))
while running:
    screen.fill((background))
    background = 100, 100, 100
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    xm, ym = pygame.mouse.get_pos()

    n=0
    for i in cbuttons:
        n = n+1
        xc, yc = i
        a = functions.collision_circle(xm, ym, xc, yc, r)
        if a == True:
            background = 10*int(n), 10*n, 10*n
            shown = n
    n=0
    for i in cbuttons:
        pygame.draw.circle(screen,(40,40,40),(i),40)

    if pygame.mouse.get_pressed(5)[4]:
        print("up")
    if pygame.mouse.get_pressed(5)[3]:
        print("down")



    pygame.display.flip()
