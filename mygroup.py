import pygame
from pygame.locals import *
from koma import Komaclass
import os

class Koma_group:
    def __init__(self):
        self.group_list = []
        self.komano = pygame.mixer.Sound(os.path.join(os.getcwd(), "asset\\sound\\"+"komano.mp3"))
        self.komaon = pygame.mixer.Sound(os.path.join(os.getcwd(), "asset\\sound\\"+"komaon.wav"))
        self.komaget = pygame.mixer.Sound(os.path.join(os.getcwd(), "asset\\sound\\"+"komaget.mp3"))
    
    def sprites(self):
        return list(self.group_list)

    def add(self, sprite):
        self.group_list.append(sprite)

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update(*args, **kwargs)

    def check(self, *arg, **kwargs):
        for sprite in self.sprites():
            sprite.check(*arg, **kwargs)

    def top_to(self, sprite):
        index = self.group_list.index(sprite)
        tmp = self.group_list[len(self.group_list)-1]
        self.group_list[len(self.group_list)-1] = self.group_list[index]
        self.group_list[index] = tmp

    def draw(self, screem):
        for sprite in self.sprites():
            screem.blit(sprite.image, sprite.rect)

    def komaon_play(self):
        self.komaon.play()

    def komano_play(self):
        self.komano.play()
        
    def komaget_play(self):
        self.komaget.play()

