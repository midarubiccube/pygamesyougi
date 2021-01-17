import pygame
from pygame.locals import *

def startstage(screen, SCR_RECT):
    press_space = True
    pygame.mixer.music.load("asset/タイトル.wav")
    pygame.mixer.music.play(loops=1, start=0.0)
    while(press_space):
        screen.fill((0, 0, 0, 255))
        title_font = pygame.font.SysFont(None, 80)
        title = title_font.render("Syougi online", False, (255,0,0))
        screen.blit(title, ((SCR_RECT.width-title.get_width())/2, 100))
        # PUSH STARTを描画
        push_font = pygame.font.SysFont(None, 40)
        push_space = push_font.render("PUSH SPACE KEY", False, (255,255,255))
        screen.blit(push_space, ((SCR_RECT.width-push_space.get_width())/2, 300))
        # クレジットを描画
        credit_font = pygame.font.SysFont(None, 20)
        credit = credit_font.render(u"Miyakedaichi", False, (255,255,255))
        screen.blit(credit, ((SCR_RECT.width-credit.get_width())/2, 380))
        pygame.time.wait(30) # 更新間隔。多分ミリ秒
        pygame.display.update()
        for event in pygame.event.get(): # 終了処理
            if  event.type == KEYDOWN and event.key == K_SPACE:
                press_space = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.mixer.music.stop()