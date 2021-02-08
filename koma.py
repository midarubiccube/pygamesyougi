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
        self.touchplace.komaself = self

        #成る時の処理設定
        self.promotionflag = promotionflag
        self.promotion = False

        self.opponent = opponent
        
        self.mouseclickflag = False
        self.mousetouchflag = False

        self.list = None
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check(self, mx, my, koma_group, touch_group):
        if self.rect.collidepoint(mx, my) and self.opponent == False:
            self.search(touch_group)
            koma_group.top_to(self)
            if len(koma_group.group_list) > 1:
                for sprite in koma_group.group_list:
                    if not sprite == self:
                        sprite.mousetouchflag = True

    def update(self, MOUSE_CLICK_FLAG, mx, my, koma_group, touch_group, MOUSEDRAGSTART):
        if self.opponent == False:
            if MOUSE_CLICK_FLAG == True:
                if self.rect.collidepoint(mx, my) and not self.mousetouchflag == True:
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
                            beforekomaself = None
                            if self.touchplace.komaself == None:
                                beforekomaself = self.touchplace.komaself
                            self.touchplace.komaself = None
                            self.touchplace = lists[0]
                            
                            self.touchplace.komaself = self
                            if self.touchplace.onkoma == True:
                                print("touch") 
                            self.touchplace.onkoma = True
                            self.x, self.y = self.touchplace.x, self.touchplace.y
                            self.Coordinate_transformation()
                            for touch in touch_group.sprites():
                                    touch.able = False
                        else:
                            self.Coordinate_transformation()
                            for touch in touch_group.sprites():
                                touch.able = False
                    else:
                        self.Coordinate_transformation()
                        for touch in touch_group.sprites():
                                touch.able = False

    def search(self, touch_group):
        touchlist = []
        self.list = touch_group.sprites()
        if self.kind == "ho":
            touchlist.append(self.get(self.x, self.y-1))
            #print("predict" + str(touch.x) + " " + str(touch.y))
            
        if self.kind == "ou" or self.kind == "gyoku":
            touchlist.append(self.get(self.x+1, self.y-1))
            touchlist.append(self.get(self.x, self.y-1))
            touchlist.append(self.get(self.x-1, self.y-1))
            touchlist.append(self.get(self.x-1, self.y))
            touchlist.append(self.get(self.x+1, self.y))
            touchlist.append(self.get(self.x+1, self.y+1))
            touchlist.append(self.get(self.x, self.y+1))
            touchlist.append(self.get(self.x-1, self.y+1))
        """
        if touch.y < 2:
            #成るときの処理
            pass
        """
        for touch in touchlist:
            if not touch == None:
                touch.able = True
                if touch.onkoma == True:
                    if touch.komaself.opponent == True:
                        touch.able = True
                    else:
                        touch.able = False 
            else:
                print("You can't put here")

    def get(self, x, y):
        if x < 9 and y < 9 and x > -1 and y > -1:
            return self.list[x*9+y]

    def Coordinate_transformation(self):
        self.rect.x = self.x*53.5+171.9
        self.rect.y = self.y*52.5+19