import pygame
from pygame.locals import *

class Komaclass(pygame.sprite.Sprite):
    def __init__(self, x, y, image, promotionflag, promotionimage, kind, opponent, touch_group):
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
        self.rect = Rect(0, 0, self.width, self.height)
        self.x = x
        self.y = y
        self.Coordinate_transformation()

        self.kind = kind

        lists = pygame.sprite.spritecollide(self, touch_group, dokill=False, collided = None)
        self.touchplace = lists[0]
        self.touchplace.onkoma = True
        self.touchplace.komakind = kind
        #成る時の処理設定

        self.promotionflag = promotionflag
        self.promotion = False

        self.opponent = opponent
        
        self.mouseclickflag = False
        self.mousetouchflag = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, MOUSE_CLICK_FLAG, mx, my, koma_group, touch_group, MOUSEDRAGSTART):
        if self.opponent == False:
            if MOUSE_CLICK_FLAG == True:
                if self.rect.collidepoint(mx, my) and not self.mousetouchflag == True:
                    self.search()
                    if MOUSEDRAGSTART == True:
                        koma_group.top_to(self)
                        koma_list = koma_group.group_list
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
                    if len(pygame.sprite.spritecollide(self, touch_group, dokill=False, collided = None)) > 0:
                        lists = pygame.sprite.spritecollide(self, touch_group, dokill=False, collided = None)
                        if lists[0].able == True:
                            self.touchplace.onkoma = False
                            self.touchplace = lists[0]
                            self.touchplace.onkoma = True
                            self.touchplace.komakind = self.kind
                            self.x, self.y = self.touchplace.x, self.touchplace.y
                            self.Coordinate_transformation()

    def search(self, touch_group):
        for i in touch_group.sprites():
            lists = []
            lists.append(i
        if self.kind = "ho":


    def Coordinate_transformation(self):
        self.rect.x = self.x*53.5+171.9
        self.rect.y = self.y*52.5+19