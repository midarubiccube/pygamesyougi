import pygame
from pygame.locals import *

class touch_class(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.Noneimg = pygame.image.load("asset/None.png")
        self.ableimg = pygame.image.load("asset/able.png")
        self.image = self.Noneimg
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = Rect(0, 0, self.width, self.height)
        self.Coordinate_transformation(x, y)
        self.onkoma = False
        self.komakind = None
        self.able = False
        self.x = x
        self.y = y
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.able == True:
            self.image = self.ableimg
        else:
            self.image = self.Noneimg

    def Coordinate_transformation(self, x, y):
        self.rect.x = x*53.5+172
        self.rect.y = y*52.5+27
