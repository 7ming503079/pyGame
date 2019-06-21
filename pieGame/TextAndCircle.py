import pygame
import sys
white = 255,255,255
blue = 0,0,255
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))


myfont = pygame.font.Font(None,60)
textImage = myfont.render("Hello world",True,white)
print(pygame.QUIT)
print(pygame.KEYDOWN)

while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT,pygame.KEYDOWN):
            print(event.type )
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    # pygame.display.update()
    # screen.fill((0,0,200))
    yellow = 255,255,0
    position = 300,200
    radius = 100
    width = 10
    pygame.draw.circle(screen,color,position,radius,width)
    pygame.display.update()