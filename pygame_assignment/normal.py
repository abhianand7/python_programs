import pygame, sys
from pygame.locals import *

# Initialisation

pygame.init()

# set display

screen = pygame.display.set_mode((1024, 768))    # set the display resolution to that of your screen

clock = pygame.time.Clock()

img_obj = pygame.image.load("fireball.png")
img_rect = img_obj.get_rect()

canvas = pygame.image.load('canvas.jpg')        # load the background image
canvas_rect = canvas.get_rect()
# initial image rect position
x = 100
y = 100





while True:
    clock.tick(60)                          # limit the speed at which the program should execute
    for event in pygame.event.get():        #get the events and do proper operation
        if event.type == pygame.QUIT:
            sys.exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] :           # move image up
        y -= 2
    if pressed[pygame.K_DOWN]:          # move image down
        y += 2
    if pressed[pygame.K_LEFT]:          # move image left
        x -= 2
    if pressed[pygame.K_RIGHT]:         # move image right
        x += 2
    screen.fill((255,255,255))              # fill the screen white
    screen.blit(canvas,canvas_rect)               # on top of white fill the background
    screen.blit(img_obj,img_rect.move(x,y))         # fireball imgage
    pygame.display.flip()