# this intro just tells you to how make a gui window pop up


import pygame
import sys
from pygame.locals import *

pygame.init()

setDisplay = pygame.display.set_mode((400,300))

pygame.display.set_caption('epic game')

while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()