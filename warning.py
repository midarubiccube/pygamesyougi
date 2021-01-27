import pygame
from pygame.locals import *

class warning(pygame.sprite.Sprite):
    def __init__(self):
        self.count = 0
        self.showflag = 0
        self.flag = False 

    def show(self, number):
        if number == 1:
            self.count=1
            self.flag = True
            self.image = pygame.image.load("asset/can't.png")
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.rect = Rect(0, 0, self.width, self.height) 
            self.showflag = 1

    def update(self):
        if self.flag == True:
            if not self.count == 1000: 
                print(self.count)
                self.count = self.count + 1
                
            else:
                self.count = 0
                self.showflag = 0
                self.flag = False

    def draw(self, screen): 
        if self.showflag == 1:
            screen.blit(self.image, self.rect)
