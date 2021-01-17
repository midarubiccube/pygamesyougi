import pygame
from pygame.locals import *

class Komaclass(pygame.sprite.Sprite):
    def __init__(self, x, y, image, promotionflag, promotionimage, kind, opponent):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("asset/koma/" + image + ".png")
        if opponent == True:
            self.image = pygame.transform.flip(self.image, 90, 90)
    
        if promotionflag == False:
            self.promotionimage = pygame.image.load("asset/koma/" + image + ".png")
            if opponent == True:
                self.promotionimage = pygame.transform.flip(self.image, 90, 90)

        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = self.Coordinate_transformation(x, y, Rect(0, 0, width, height))

        self.kind = kind
        self.promotionflag = promotionflag
        self.promotion = False
        self.opponent = opponent
    
    def Coordinate_transformation(self, x, y, rect):
        rect.x = x*53.5+171
        rect.y = y*52.5+19
        return rect
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)