import pygame
import random

from global_constants import constants


pygame.init()
screen = pygame.display.set_mode(constants.screenSize)
running = True
screen.fill(constants.red)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()