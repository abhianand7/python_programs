import pygame
from pygame.locals import *

pygame.init()

Obj = pygame.display.Info()           # returns info object about display

screen = pygame.display.set_mode((Obj.current_w, Obj.current_h))


keypress = pygame.KEYDOWN

key_release = pygame.KEYUP

