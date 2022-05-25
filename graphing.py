import pygame
screenx = 2560+1920
screen = pygame.display.set_mode((screenx,1000))
running: bool = True
days =[]
lines = 0
lastx = 0
lasty = 0

affile = open("tmax", "r")
for i in affile.readlines():
    days.append(i)

    lines += 1

affile.close()

while running:
    lines = int(lines)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((100,100,100))
    n=0
    lastx = 0
    lasty = 1000
    peaky =0

    for i in days:
        n+=1
        n=int(n)
        pygame.draw.line(screen, (255, 255, 255), ((screenx/lines)*n,1000-(float(i)*20)), (lastx,lasty), 2)
        lastx = (screenx/lines)*n
        lasty = 1000-(float(i)*20)
        if 1000-(float(i)*20) > peaky:
            peaky = 1000-(float(i)*20)
    for i in range(10):
        pygame.draw.line(screen,(255, 255, 255),(0,i*100), (screenx, i*100), 2)


    print(peaky)


    pygame.display.flip()
