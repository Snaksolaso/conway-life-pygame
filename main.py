import pygame
import conway
realwidth = 600
realheight = 600
width = 50
height = 50

screen = pygame.display.set_mode((realwidth, realheight))
running = True

scaleFactor = float(realwidth/width)
conway = conway.conway(width, height)

conway.displayGrid(screen, scaleFactor)
pix2set = [[False for i in range(height)]for j in range(width)] 
clock = pygame.time.Clock()
while(pygame.mouse.get_pressed()[1] != True):
    if(pygame.mouse.get_pressed()[0] == True):
        mousepos = pygame.mouse.get_pos()
        val1 = int(mousepos[0]/scaleFactor)
        val2 = int(mousepos[1]/scaleFactor)
        conway.toggleSquare(val1, val2, scaleFactor, screen, True)
        pygame.display.flip()
    elif(pygame.mouse.get_pressed()[2] == True):
        mousepos = pygame.mouse.get_pos()
        val1 = int(mousepos[0]/scaleFactor)
        val2 = int(mousepos[1]/scaleFactor)
        conway.toggleSquare(val1, val2, scaleFactor, screen, False)
        conway.displayGrid(screen, scaleFactor)
        pygame.display.flip()
    pygame.event.get()

conway.displayScale(screen, scaleFactor)

while(running):
    clock.tick(1000)
    conway.update()
    conway.displayScale(screen, scaleFactor)
    pygame.event.get()
