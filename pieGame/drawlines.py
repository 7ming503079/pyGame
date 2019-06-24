import pygame,sys,math,random

pygame.init()
screen = pygame.display.set_mode((600,500))

pygame.display.set_caption("drawing Lines")

print(  )
while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT,pygame.KEYDOWN):
            sys.exit()

    screen.fill((0,80,0))

    color = 100,255, 200
    color1 = 255,0,255
    position  = 200,150,200,200
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    width = 8
    for i in range(100):
        pygame.draw.line(screen,color,(random.randint(1,600),random.randint(1,500)),(random.randint(1,600),random.randint(1,500)),width)
    pygame.draw.arc(screen,color,position,start_angle , end_angle ,width)
    pygame.display.update()