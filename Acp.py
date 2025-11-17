import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill((255,255,255))
color=(54,255,124)
pygame.draw.circle(screen,color,(300,300),50)
pygame.draw.circle(screen,color,(100,100),50,3)
pygame.display.update()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()