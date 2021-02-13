import pygame
from pygame.locals import *

class Get_koma:
    def __init__(self):
        self.next = [9, 0]
        self.nextopponent = []
    
    def put(self, komaself):
        komaself.x = self.next[0]
        komaself.y = self.next[1]
        if self.next[1] == 8:
            self.next[0] += 1
            self.next[1] = 0
        else:
            self.next[1] += 1