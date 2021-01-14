import pygame

class Komaclass(pygame.sprite.Sprite):
    def __init__(self, img, kind, opponent):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load("asset/koma/" + img + ".png")
        if opponent == True:
            self.img = pygame.transform.flip(self.img, 90, 90)
        width = self.img.get_width()
        height = self.img.get_height()
        #self.rect = Rect(x, y, width, height)
        self.kind = kind
        self.opponent = opponent