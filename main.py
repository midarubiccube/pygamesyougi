import pygame
from pygame.locals import *
import sys
from koma import Komaclass
from startstage import startstage
from wxtest import login
import threading
from komainit import koma_init

x, y = 800, 800

koma_img_route = ["ginn", "ginnnaru", "gyoku", "hisya", "hisyanaru", "ho", "honaru", "kaku", "kakunaru", "keima", "keimanaru", "kinn", "kyousya", "kyousyanaru", "ou"]
SCR_RECT = Rect(0, 0, 800, 500)

#初期化する
def init():
    pygame.init() # 初期化
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption("Pygame Test")
    pygame.display.set_icon(pygame.transform.flip(pygame.image.load("asset/icon.png"), 90, 90))
    startstage(screen, SCR_RECT)
    koma_group = koma_init()
    return screen, koma_group

def syori(screen, koma_group, bg, rect_bg):
    while(True):
        screen.fill((255, 255, 255, 0)) # 背景色の指定。RGBのはず
        screen.blit(bg, rect_bg) # 背景画像の描画
        koma_group.draw(screen)
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
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                print(pygame.mouse.get_pos())

def main():
    screen, koma_group = init()
    bg = pygame.image.load("asset/back.jpg").convert_alpha()
    rect_bg = bg.get_rect()
    rect_bg.x = 150
    rect_bg.y = 0
    syori(screen, koma_group, bg, rect_bg)

if __name__ == "__main__":
    main()
