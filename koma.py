import pygame
from pygame.locals import *

class Komaclass(pygame.sprite.Sprite):
    def __init__(self, x, y, image, kind, opponent):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("asset/koma/" + image + ".png")
        if opponent == True:
            self.image = pygame.transform.flip(self.image, 90, 90)
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = self.Coordinate_transformation(x, y, Rect(0, 0, width, height))
        self.kind = kind
        self.opponent = opponent
    
    def Coordinate_transformation(self, x, y, rect):
        rect.x = (x-1)*50+190
        rect.y = (y-1)*50+40
        return rect
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

"""
test = Komaclass("gyoku", "ho", opponent=False)
x = 1
y = 1
rect = Rect(0, 0, 800, 500)
rectreturn =test.Coordinate_transformation(x,y,rect)
print(rectreturn)
"""