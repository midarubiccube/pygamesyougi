import pygame

class Komaclass(pygame.sprite.Sprite):
    def __init__(self, img, kind):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load("asset/koma/" + img + ".png")
        width = self.img.get_width()
        height = self.img.get_height()
        #self.rect = Rect(x, y, width, height)
        self.kind = kind