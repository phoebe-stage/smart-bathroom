import pygame
import random

##------VARIABLES------
screenSize = [1280,720]

##------COLOURS------
red = (255,0,0)



pygame.init()
screen = pygame.display.set_mode(screenSize)
running = True
screen.fill(red)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()