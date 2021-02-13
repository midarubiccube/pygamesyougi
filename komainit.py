import pygame
from pygame.locals import *
from koma import Komaclass
from mygroup import Koma_group
from touch import touch_class

koma_img_route = ["ho", "honaru", "kyousya", "kyousyanaru", "keima", "keimanaru", "ginn", "ginnnaru", "kinn", "ou", "gyoku", "hisya", "hisyanaru", "kaku", "kakunaru"]

def koma_init():
    touch_group = pygame.sprite.Group()
    for i in range(9):
        for j in range(9):
            touch_group.add(touch_class(i, j))
    koma_group = Koma_group()
    #歩インスタント化
    for i in range(9):
        koma_group.add(Komaclass(x=i, y=6, image=koma_img_route[0], promotionflag=True, promotionimagepath=koma_img_route[1], kind="ho", opponent=False, touch_group=touch_group))      
    #香車インスタント化
    koma_group.add(Komaclass(x=0, y=8, image=koma_img_route[2], promotionflag=True, promotionimagepath=koma_img_route[3], kind="kyousya", opponent=False, touch_group=touch_group))
    koma_group.add(Komaclass(x=8, y=8, image=koma_img_route[2], promotionflag=True, promotionimagepath=koma_img_route[3], kind="kyousya", opponent=False, touch_group=touch_group))
    #桂馬インスタント化
    koma_group.add(Komaclass(x=1, y=8, image=koma_img_route[4], promotionflag=True, promotionimagepath=koma_img_route[5], kind="keima", opponent=False, touch_group=touch_group))
    koma_group.add(Komaclass(x=7, y=8, image=koma_img_route[4], promotionflag=True, promotionimagepath=koma_img_route[5], kind="keima", opponent=False, touch_group=touch_group))
    #銀インスタント化    
    koma_group.add(Komaclass(x=2, y=8, image=koma_img_route[6], promotionflag=True, promotionimagepath=koma_img_route[7], kind="ginn", opponent=False, touch_group=touch_group))
    koma_group.add(Komaclass(x=6, y=8, image=koma_img_route[6], promotionflag=True, promotionimagepath=koma_img_route[7], kind="ginn", opponent=False, touch_group=touch_group))
    #金インスタント化
    koma_group.add(Komaclass(x=3, y=8, image=koma_img_route[8], promotionflag=False, promotionimagepath=None, kind="kinn", opponent=False, touch_group=touch_group))
    koma_group.add(Komaclass(x=5, y=8, image=koma_img_route[8], promotionflag=False, promotionimagepath=None, kind="kinn", opponent=False, touch_group=touch_group))
    #王インスタント化
    koma_group.add(Komaclass(x=4, y=8, image=koma_img_route[9], promotionflag=False, promotionimagepath=None, kind="ou", opponent=False, touch_group=touch_group))
    #飛車インスタント化
    koma_group.add(Komaclass(x=7, y=7, image=koma_img_route[11], promotionflag=True, promotionimagepath=koma_img_route[12], kind="hisya", opponent=False, touch_group=touch_group))
    #角インスタント化
    koma_group.add(Komaclass(x=1, y=7, image=koma_img_route[13], promotionflag=True, promotionimagepath=koma_img_route[14], kind="kaku", opponent=False, touch_group=touch_group))
    #対戦相手側
    #歩インスタント化
    for i in range(9):
        koma_group.add(Komaclass(x=i, y=2, image=koma_img_route[0], promotionflag=True, promotionimagepath=koma_img_route[1], kind="ho", opponent=True, touch_group=touch_group))      
    #香車インスタント化
    koma_group.add(Komaclass(x=0, y=0, image=koma_img_route[2], promotionflag=True, promotionimagepath=koma_img_route[3], kind="kyousya", opponent=True, touch_group=touch_group))
    koma_group.add(Komaclass(x=8, y=0, image=koma_img_route[2], promotionflag=True, promotionimagepath=koma_img_route[3], kind="kyousya", opponent=True, touch_group=touch_group))
    #桂馬インスタント化
    koma_group.add(Komaclass(x=1, y=0, image=koma_img_route[4], promotionflag=True, promotionimagepath=koma_img_route[5], kind="keima", opponent=True, touch_group=touch_group))
    koma_group.add(Komaclass(x=7, y=0, image=koma_img_route[4], promotionflag=True, promotionimagepath=koma_img_route[5], kind="keima", opponent=True, touch_group=touch_group))
    #銀インスタント化    
    koma_group.add(Komaclass(x=2, y=0, image=koma_img_route[6], promotionflag=True, promotionimagepath=koma_img_route[7], kind="ginn", opponent=True, touch_group=touch_group))
    koma_group.add(Komaclass(x=6, y=0, image=koma_img_route[6], promotionflag=True, promotionimagepath=koma_img_route[7], kind="ginn", opponent=True, touch_group=touch_group))
    #金インスタント化
    koma_group.add(Komaclass(x=3, y=0, image=koma_img_route[8], promotionflag=False, promotionimagepath=None, kind="kinn", opponent=True, touch_group=touch_group))
    koma_group.add(Komaclass(x=5, y=0, image=koma_img_route[8], promotionflag=False, promotionimagepath=None, kind="kinn", opponent=True, touch_group=touch_group))
    #王インスタント化
    koma_group.add(Komaclass(x=4, y=0, image=koma_img_route[9], promotionflag=False, promotionimagepath=None, kind="ou", opponent=True, touch_group=touch_group))
    #飛車インスタント化
    koma_group.add(Komaclass(x=1, y=1, image=koma_img_route[11], promotionflag=True, promotionimagepath=koma_img_route[12], kind="hisya", opponent=True, touch_group=touch_group))
    koma_group.add(Komaclass(x=7, y=1, image=koma_img_route[13], promotionflag=True, promotionimagepath=koma_img_route[14], kind="kaku", opponent=True, touch_group=touch_group))
    return koma_group, touch_group