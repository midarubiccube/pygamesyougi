import pygame
from pygame.locals import *

class Komaclass(pygame.sprite.Sprite):
    def __init__(self, x, y, img, kind, opponent):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load("asset/koma/" + img + ".png")
        if opponent == True:
            self.img = pygame.transform.flip(self.img, 90, 90)
        width = self.img.get_width()
        height = self.img.get_height()
        self.rect = Coordinate_transformation(x, y, Rect(0, 0, width, height))
        self.kind = kind
        self.opponent = opponent
    
    def Coordinate_transformation(self, x, y, rect):
        rect.x = (x-1)*50+190
        rect.y = (y-1)*50+40
        return rect
        
    def draw(self, screen):
        screen.blit(self.img, self.rect)

"""
test = Komaclass("gyoku", "ho", opponent=False)
x = 1
y = 1
rect = Rect(0, 0, 800, 500)
rectreturn =test.Coordinate_transformation(x,y,rect)
print(rectreturn)
"""