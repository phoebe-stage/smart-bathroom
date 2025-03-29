import pygame
import random
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from global_constants import constants

# screenSize = [640,720]
pygame.init()
screen = pygame.display.set_mode(constants.screenSize)
running = True
screen.fill(constants.mid_light)
slider = Slider(screen, 50, 150, 500, 40, min=0, max=99, step=1, initial=0)
output = TextBox(screen, 475, 50, 50, 50, fontSize=30)
humidity_heading = TextBox(screen, 50, 50, 250, 50, fontSize = 30)
humidity_heading.setText("Humidity Level (%)")

poll_slider = Slider(screen, 50, 400, 500, 40, min=0, max=1000, step=1, initial=0)
poll_output = TextBox(screen, 475, 300, 100, 50, fontSize=30)
poll_heading = TextBox(screen, 50, 300, 300, 50, fontSize = 30)
poll_heading.setText("Pollutant Level (ppb)")
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    output.setText(slider.getValue())
    poll_output.setText(poll_slider.getValue())
    constants.humidityLevel = slider.getValue()
    constants.vocLevel = poll_slider.getValue()
    # print(constants.humidityLevel)
    pygame_widgets.update(events)
    pygame.display.update()
pygame.quit()