
import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)       #defining colour in RGB
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purpule = (255,0,255)

setDisplay = pygame.display.set_mode((400,300))

singlePixel = pygame.PixelArray(setDisplay)         # you can draw each pixel seperately
singlePixel[5][5] = yellow


pygame.display.set_caption('PyGame Tutorial')

while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

