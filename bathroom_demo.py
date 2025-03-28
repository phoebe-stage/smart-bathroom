import pygame
import random
from global_constants import constants


pygame.init()
screen = pygame.display.set_mode(constants.screenSize)
running = True
screen.fill(constants.normal)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print(constants.humidityLevel)  # Debugging
    if constants.humidityLevel >=55:
        screen.fill(constants.alert)
    else:
        screen.fill(constants.normal)
    pygame.display.flip()

pygame.quit()