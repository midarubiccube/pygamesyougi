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

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.Coordinate_transformation(x, y, Rect(0, 0, self.width, self.height))

        self.x = x
        self.y = y
        self.kind = kind
        self.promotionflag = promotionflag
        self.promotion = False
        self.opponent = opponent
        self.mouseclickflag = False
        self.mousetouchflag = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, MOUSE_CLICK_FLAG, mx, my, koma_group):
        if self.opponent == False:
            if MOUSE_CLICK_FLAG == True:
                if self.rect.collidepoint(mx, my) and not self.mousetouchflag == True:
                    koma_list = pygame.sprite.spritecollide(self, koma_group, dokill= False, collided = None)
                    if len(koma_list) > 1:
                        for sprite in koma_list:
                            if not sprite == self:
                                sprite.mousetouchflag = True
                    self.rect.x = mx - self.width / 2
                    self.rect.y = my - self.height / 2
                    self.mouseclickflag = True
            else:
                if self.mouseclickflag == True:
                    self.mouseclickflag = False
                    #ドラック後の処理
                    print("ok")

    def Coordinate_transformation(self, x, y, rect):
        rect.x = x*53.5+171
        rect.y = y*52.5+19
        return rect