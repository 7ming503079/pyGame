import pygame,sys,math

pygame.init()
screen = pygame.display.set_mode((600,500))

pygame.display.set_caption("drawing Lines")

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
    pygame.draw.line(screen,color,(100,100),(500,100),width)
    pygame.draw.arc(screen,color,position,start_angle , end_angle ,width)
    pygame.display.update()