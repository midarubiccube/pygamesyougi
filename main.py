import pygame
from pygame.locals import *
import sys
from koma import Komaclass
from startstage import startstage
from komainit import koma_init

x, y = 800, 800

SCR_RECT = Rect(0, 0, 800, 500)

#初期化する
def init():
    pygame.init() # 初期化
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption("syougionline")
    pygame.display.set_icon(pygame.image.load("asset/icon.png"))
    startstage(screen, SCR_RECT)
    return screen

def syori(screen, koma_group, touch_group, boadimg, rect_boadimg, backimg, rect_backimg, MOUSE_CLICK_FLAG = False, MOUSEDRAGSTART = False, mousestart = True):
    mx, my = 0, 0
    while(True):
        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                MOUSE_CLICK_FLAG = True
                mx, my = event.pos
                koma_group.check(mx, my, koma_group, touch_group)
                """
                if mousestart:
                    MOUSEDRAGSTART = True
                    mousestart = False
                else:
                    MOUSEDRAGSTART = False
                """
            if event.type == MOUSEBUTTONUP:
                mousestart = True 
                MOUSE_CLICK_FLAG = False 
                for koma in koma_group.sprites():
                    koma.mousetouchflag = False

            if event.type == MOUSEMOTION:
                mx, my = event.pos
        screen.fill((0, 20, 0, 0))
        screen.blit(backimg, rect_backimg)
        screen.blit(boadimg, rect_boadimg)
        
        koma_group.update(MOUSE_CLICK_FLAG, mx, my, koma_group, touch_group, MOUSEDRAGSTART)
        touch_group.update()

        touch_group.draw(screen)
        koma_group.draw(screen)
        pygame.display.update()
        pygame.time.wait(30) 
        
def main():
    screen = init()
    koma_group, touch_group = koma_init()

    boadimg = pygame.image.load("asset/boad.jpg").convert_alpha()
    rect_boadimg = boadimg.get_rect()
    rect_boadimg.x = 150
    rect_boadimg.y = 0

    backimg = pygame.image.load("asset/back.jpg").convert_alpha()
    rect_backimg = backimg.get_rect()
    
    syori(screen, koma_group, touch_group, boadimg, rect_boadimg, backimg, rect_backimg)

if __name__ == "__main__":
    main()
