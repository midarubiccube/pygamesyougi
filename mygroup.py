import pygame
from pygame.locals import *
from koma import Komaclass

class Koma_group:
    def __init__(self):
        self.group_list = []
    
    def sprites(self):
        return list(self.group_list)

    def add(self, sprite):
        self.group_list.append(sprite)

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update(*args, **kwargs)
    
    def top_to(self, sprite):
        index = self.group_list.index(sprite)
        tmp = self.group_list[len(self.group_list)-1]
        self.group_list[len(self.group_list)-1] = self.group_list[index]
        self.group_list[index] = tmp

    def draw(self, screem):
        for sprite in self.sprites():
            screem.blit(sprite.image, sprite.rect)    