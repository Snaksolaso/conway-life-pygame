import pygame
import math


class conway:

    def __init__(self, width, height):
        self.pixArray = [[False for i in range(height)]for j in range(width)] 
        self.width = width
        self.height = height

    def displayScale(self, screen, scaleFactor):
        for x in range(screen.get_width()):
            for y in range(screen.get_height()):
                if(x % scaleFactor == 0.0 or y % scaleFactor == 0.0):
                    screen.set_at((x, y), (125, 125, 125))
                else:
                    screen.set_at((x, y), (0, 0, 0))
                if(self.pixArray[math.floor(x/scaleFactor)][math.floor(y/scaleFactor)]):
                    screen.set_at((x, y), (255, 255, 255))
        pygame.display.flip()

    def toggleSquare(self, x, y, scaleFactor, screen, to):
        self.pixArray[x][y] = to
        screenx = int(x*scaleFactor)
        screeny = int(y*scaleFactor)
        for i in range(screenx, int(screenx+scaleFactor) + 1):
            for j in range(screeny, int(screeny + scaleFactor) + 1):
                if(to):
                    screen.set_at((i, j), (255, 255, 255))
                else:
                    screen.set_at((i, j), (0, 0, 0))
                
        pygame.display.flip()

    def displayGrid(self, screen, scaleFactor):
        for x in range(screen.get_width()):
            for y in range(screen.get_height()):
                if(x % scaleFactor == 0.0 or y % scaleFactor == 0.0):
                    screen.set_at((x, y), (125, 125, 125))
                else:
                    screen.set_at((x, y), (0, 0, 0))
        pygame.display.flip()

    def isAlive(self, x, y):
        numAdj = 0
        if(x < self.width-1 and self.pixArray[x + 1][y]):
            numAdj += 1
        if(x < self.width-1 and y < self.height-1 and self.pixArray[x + 1][y + 1]):
            numAdj += 1
        if(x > 0 and y < self.height - 1 and self.pixArray[x - 1][y + 1]):
            numAdj += 1
        if(y > 0 and x < self.width-1 and self.pixArray[x + 1][y - 1]):
            numAdj += 1
        if(x > 0 and y > 0 and self.pixArray[x - 1][y - 1]):
            numAdj += 1
        if(y > 0 and self.pixArray[x][y - 1]):
            numAdj += 1
        if(x > 0 and self.pixArray[x - 1][y]):
            numAdj += 1
        if(y < self.height - 1 and self.pixArray[x][y + 1]):
            numAdj += 1
        if(numAdj == 3):
            return True
        elif(numAdj == 2):
            if (self.pixArray[x][y]):
                return True
            return False
        else:
            return False

    def update(self):
        new = [[False for i in range(self.height)]for j in range(self.width)] 
        for x in range(0, self.width):
            for y in range(0, self.height):
                if(self.isAlive(x, y)):
                    new[x][y] = True
        self.pixArray = new
