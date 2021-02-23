import pygame
from pygame.locals import *

class Button:
    def __init__(self, x, y, w, h, text=''):
       self.rect = pygame.Rect(x, y, w, h)
       self.color = (200,200,200)
       self.text = text
       self.txt_surface = FONT.render(text, True, self.color)
       self.active = False
       
    def update(self):
       width = max(200, self.txt_surface.get_width()+10)
       self.rect.w = width

    def draw(self, screen):
       pygame.draw.rect(screen, self.color, self.rect, 0)
       self.txt_surface = FONT.render(self.text, True, (0,0,0))
       screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

    def onClick(self):
        r = self.active
        self.active = False
        return r