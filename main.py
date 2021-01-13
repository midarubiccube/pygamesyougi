import pygame
from pygame.locals import *
import sys
from koma import Komaclass
from startstage import startstage

x, y = 800, 800

koma_route = ["ginn", "ginnnaru", "gyoku", "hisya", "hisyanaru", "ho", "honaru", "kaku", "kakunaru", "keima", "keimanaru", "kinn", "kyousya", "kyousyanaru", "ou"]
SCR_RECT = Rect(0, 0, 600, 400)

#初期化する
def init():
    pygame.init() # 初期化
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption("Pygame Test")
    pygame.display.set_icon(pygame.image.load("asset/icon.png"))
    startstage(screen, SCR_RECT)
    return screen

def main():
    screen = init()
    bg = pygame.image.load("asset/back.jpg").convert_alpha()
    rect_bg = bg.get_rect()
    koma_group = pygame.sprite.Group()
    for i in range(10):
        koma_group.add(Komaclass(koma_route[5], "ho"))
    while(True):
        screen.fill((255, 255, 255, 0)) # 背景色の指定。RGBのはず
        screen.blit(bg, rect_bg) # 背景画像の描画
        pygame.time.wait(30) # 更新間隔。多分ミリ秒
        pygame.display.update() # 画面更新

        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()

def koma_img_load():
    y

print(koma_img_load())

def Coordinate_transformation(x, y, rect):
    return  rect

