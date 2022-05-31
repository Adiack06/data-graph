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
affile = open("tmax", "r")
for i in affile.readlines():
    days.append(i)

    lines += 1

affile.close()

while running:
    keys = pygame.key.get_pressed()
    keymod = pygame.key.get_mods
    lines = int(lines)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    n=0
    lastx = 0
    lasty = 1000
    peaky =0
    for i in range(1000):
        pygame.draw.line(screen, (50, 50, 50), (0, (screeny - (5 * (i * verticlescale))/4)),(screenx, (screeny - (5 * (i * verticlescale))/4)), 2)
    for i in range(1000):
        pygame.draw.line(screen, (50, 50, 50),(50 * (i * horizontalscale)+xlocation,0 ),(50 * (i * horizontalscale)+xlocation, screeny), 2)

    for i in days:
        n+=1
        n=int(n)
        pygame.draw.line(screen, (70, 70, 70), ((n*horizontalscale)+xlocation,1000-(float(i)*verticlescale)), (lastx,lasty), 4)
        lastx = (n*horizontalscale)+xlocation
        lasty = 1000-(float(i)*verticlescale)


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
    pygame.display.flip()
