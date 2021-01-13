import pygame

def draw_startstage(screen):
    screen.fill((0, 0, 0))
    title_font = pygame.font.SysFont(None, 80)
    title = title_font.render("SyouGi online", False, (255,0,0))
    screen.blit(title, ((SCR_RECT.width-title.get_width())/2, 100))
    # PUSH STARTを描画
    push_font = pygame.font.SysFont(None, 40)
    push_space = push_font.render("PUSH SPACE KEY", False, (255,255,255))
    screen.blit(push_space, ((SCR_RECT.width-push_space.get_width())/2, 300))
    # クレジットを描画
    credit_font = pygame.font.SysFont(None, 20)
    credit = credit_font.render(u"2008 http://pygame.skr.jp", False, (255,255,255))
    screen.blit(credit, ((SCR_RECT.width-credit.get_width())/2, 380))