import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Rectangles")

pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1

while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT,pygame.KEYDOWN):
            print(event.type )
            sys.exit()
    screen.fill((0,0,200))

    pos_x += vel_x
    pos_y += vel_y

    if pos_x >500 or pos_x <0:
        vel_x = -vel_x
    if pos_y >400 or pos_y <0:
        vel_y = -vel_y

    yellow = 255,255,0
    position = pos_x,pos_y,100,100
    width = 0

    pygame.draw.rect(screen,yellow,position,width)
    pygame.display.update()