import pygame, sys
# from pygame.locals import *       # if the above import does not work for you uncomment this line as well

# Initialisation

pygame.init()

# initialise font

pygame.font.init()

sys_font = pygame.font.SysFont(None, 20)            # use system font

# set display

obj = pygame.display.Info()         # fetches the info about your display

screen = pygame.display.set_mode((obj.current_w, obj.current_h))    # set the display resolution to that of your screen
screen_rect = screen.get_rect()
pygame.display.set_caption('Fireball')

clock = pygame.time.Clock()


# initial image rect position
x = 20
y = 20

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)         # initialise sprite
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location


canvas = Background('canvas.jpg',[0,0])
fireball = Background('fireball.png',[20,20])

while True:
    clock.tick(60)
    if pygame.event.peek():                 # see if any events are waiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    if pygame.key.get_focused():            # check if monitor is receiving input from keyboard
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] :
            y -= 2
        elif pressed[pygame.K_DOWN]:
            y += 2
        if pressed[pygame.K_LEFT]:
            x -= 2
        elif pressed[pygame.K_RIGHT]:
            x += 2
        elif pressed[pygame.K_ESCAPE]:
            pygame.QUIT
            sys.exit()
    fireball.rect.clamp_ip(screen_rect)                     # keep the object on the screen
    label = sys_font.render('X = ' +str(x) + " and Y = " + str(y),1,(255,255,0))
    screen.fill((255,255,255))
    screen.blit(canvas.image,canvas.rect)
    screen.blit(fireball.image,fireball.rect.move(x,y))
    screen.blit(label,(20,20))
    pygame.display.flip()