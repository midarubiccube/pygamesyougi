import pygame
from pygame.locals import *
from koma import Komaclass

koma_img_route = ["ginn", "ginnnaru", "gyoku", "hisya", "hisyanaru", "ho", "honaru", "kaku", "kakunaru", "keima", "keimanaru", "kinn", "kyousya", "kyousyanaru", "ou"]

def koma_init():
    koma_group = pygame.sprite.Group()
    for i in range(9):
        koma_group.add(Komaclass(i, 6, koma_img_route[5], "ho", opponent=False))
    return koma_group