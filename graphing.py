
numvar=5





import functions
import pygame
screenx = 2560
screeny = 1000
screen = pygame.display.set_mode((screenx,screeny))
running: bool = True
days =[]
lines = 0
lastx = 0
lasty = 0
verticlescale = 40
horizontalscale = 4
xlocation = 0
ylocation = 0
affile = open("tmax", "r")
cbuttons =[]
shown =0

for i in range(numvar):
    xc = (screenx / numvar) * (i + 0.5)
    yc = 100
    cbuttons.append((xc, yc))

while running:
    keys = pygame.key.get_pressed()
    keymod = pygame.key.get_mods
    lines = int(lines)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    n=0
    lastx = 0+xlocation
    lasty = screeny+ylocation
    peaky =0
    for i in range(1000):
        pygame.draw.line(screen, (50, 50, 50), (0, ylocation+(screeny - (5 * (i*80))/4)),(screenx, ylocation+(screeny - (5 * (i*80))/4)), 2)
    for i in range(1000):
        pygame.draw.line(screen, (50, 50, 50),(50 * (i*2)+xlocation,0 ),(50 * (i*2)+xlocation, screeny), 2)

    for i in days:
        n+=1
        n=int(n)
        pygame.draw.line(screen, (70, 70, 70), ((n*horizontalscale)+xlocation,(screeny-(float(i)*verticlescale))+ylocation), (lastx,lasty), 4)
        lastx = (n*horizontalscale)+xlocation
        lasty = (screeny-(float(i)*verticlescale))+ylocation


    if pygame.mouse.get_pressed(5)[2]:
        if pygame.mouse.get_pressed(5)[3]:
            horizontalscale+= 0.025
        if pygame.mouse.get_pressed(5)[4]:
            horizontalscale -= 0.025


    if pygame.mouse.get_pressed(5)[0]:
        if pygame.mouse.get_pressed(5)[3]:
            verticlescale += 0.25
        if pygame.mouse.get_pressed(5)[4]:
            verticlescale -= 0.25
    if keys[pygame.K_d]:
        xlocation -= 5
    if keys[pygame.K_a]:
        xlocation += 5
    if keys[pygame.K_s]:
        ylocation -= 5
    if keys[pygame.K_w]:
        ylocation += 5
    xm, ym = pygame.mouse.get_pos()

    n=0
    r=40
    for i in cbuttons:
        n = n+1
        xc, yc = i
        a = functions.collision_circle(xm, ym, xc, yc, r)
        if a == True:
           shown = n
    n=0
    for i in cbuttons:
        pygame.draw.circle(screen,(40,40,40),(i),40)
    print(shown)
    days=[]
    lines =0

    if shown == 1:
        affile = open("tmax", "r")
        for i in affile.readlines():
            days.append(i)
            lines += 1
        affile.close()
    if shown == 2:
        affile = open("af.txt", "r")
        for i in affile.readlines():
            days.append(i)
            lines += 1
        affile.close()
    print(verticlescale)
    print(horizontalscale)
    pygame.display.flip()
