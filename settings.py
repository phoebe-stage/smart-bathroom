import pygame
import random
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from global_constants import constants


pygame.init()
screen = pygame.display.set_mode(constants.screenSize)
running = True
screen.fill(constants.blue)
slider = Slider(screen, 50, 100, 500, 40, min=0, max=99, step=1)
output = TextBox(screen, 475, 200, 50, 50, fontSize=30)

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    output.setText(slider.getValue())
    constants.humidityLevel = slider.getValue()
    print(constants.humidityLevel)
    pygame_widgets.update(events)
    pygame.display.update()
pygame.quit()