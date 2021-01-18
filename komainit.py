import pygame
from pygame.locals import *
from koma import Komaclass
from mygroup import Koma_group

koma_img_route = ["ho", "honaru", "kyousya", "kyousyanaru", "keima", "keimanaru", "ginn", "ginnnaru", "kinn", "ou", "gyoku", "hisya", "hisyanaru", "kaku", "kakunaru"]

def koma_init():
    koma_group = Koma_group()
    #歩インスタント化
    for i in range(9):
        koma_group.add(Komaclass(x=i, y=6, image=koma_img_route[0], promotionflag=True, promotionimage=koma_img_route[1], kind="ho", opponent=False))      
    #香車インスタント化
    koma_group.add(Komaclass(x=0, y=8, image=koma_img_route[2], promotionflag=True, promotionimage=koma_img_route[3], kind="kyousya", opponent=False))
    koma_group.add(Komaclass(x=8, y=8, image=koma_img_route[2], promotionflag=True, promotionimage=koma_img_route[3], kind="kyousya", opponent=False))
    #桂馬インスタント化
    koma_group.add(Komaclass(x=1, y=8, image=koma_img_route[4], promotionflag=True, promotionimage=koma_img_route[5], kind="keima", opponent=False))
    koma_group.add(Komaclass(x=7, y=8, image=koma_img_route[4], promotionflag=True, promotionimage=koma_img_route[5], kind="keima", opponent=False))
    #銀インスタント化    
    koma_group.add(Komaclass(x=2, y=8, image=koma_img_route[6], promotionflag=True, promotionimage=koma_img_route[7], kind="ginn", opponent=False))
    koma_group.add(Komaclass(x=6, y=8, image=koma_img_route[6], promotionflag=True, promotionimage=koma_img_route[7], kind="ginn", opponent=False))
    #金インスタント化
    koma_group.add(Komaclass(x=3, y=8, image=koma_img_route[8], promotionflag=False, promotionimage=None, kind="kinn", opponent=False))
    koma_group.add(Komaclass(x=5, y=8, image=koma_img_route[8], promotionflag=False, promotionimage=None, kind="kinn", opponent=False))
    #王インスタント化
    koma_group.add(Komaclass(x=4, y=8, image=koma_img_route[9], promotionflag=False, promotionimage=None, kind="ou", opponent=False))
    #飛車インスタント化
    koma_group.add(Komaclass(x=7, y=7, image=koma_img_route[11], promotionflag=True, promotionimage=koma_img_route[12], kind="hisya", opponent=False))
    #角インスタント化
    koma_group.add(Komaclass(x=1, y=7, image=koma_img_route[13], promotionflag=True, promotionimage=koma_img_route[14], kind="kaku", opponent=False))
    #対戦相手側
    #歩インスタント化
    for i in range(9):
        koma_group.add(Komaclass(x=i, y=2, image=koma_img_route[0], promotionflag=True, promotionimage=koma_img_route[1], kind="ho", opponent=True))      
    #香車インスタント化
    koma_group.add(Komaclass(x=0, y=0, image=koma_img_route[2], promotionflag=True, promotionimage=koma_img_route[3], kind="kyousya", opponent=True))
    koma_group.add(Komaclass(x=8, y=0, image=koma_img_route[2], promotionflag=True, promotionimage=koma_img_route[3], kind="kyousya", opponent=True))
    #桂馬インスタント化
    koma_group.add(Komaclass(x=1, y=0, image=koma_img_route[4], promotionflag=True, promotionimage=koma_img_route[5], kind="keima", opponent=True))
    koma_group.add(Komaclass(x=7, y=0, image=koma_img_route[4], promotionflag=True, promotionimage=koma_img_route[5], kind="keima", opponent=True))
    #銀インスタント化    
    koma_group.add(Komaclass(x=2, y=0, image=koma_img_route[6], promotionflag=True, promotionimage=koma_img_route[7], kind="ginn", opponent=True))
    koma_group.add(Komaclass(x=6, y=0, image=koma_img_route[6], promotionflag=True, promotionimage=koma_img_route[7], kind="ginn", opponent=True))
    #金インスタント化
    koma_group.add(Komaclass(x=3, y=0, image=koma_img_route[8], promotionflag=False, promotionimage=None, kind="kinn", opponent=True))
    koma_group.add(Komaclass(x=5, y=0, image=koma_img_route[8], promotionflag=False, promotionimage=None, kind="kinn", opponent=True))
    #王インスタント化
    koma_group.add(Komaclass(x=4, y=0, image=koma_img_route[9], promotionflag=False, promotionimage=None, kind="ou", opponent=True))
    #飛車インスタント化
    koma_group.add(Komaclass(x=1, y=1, image=koma_img_route[11], promotionflag=True, promotionimage=koma_img_route[12], kind="hisya", opponent=True))
    koma_group.add(Komaclass(x=7, y=1, image=koma_img_route[13], promotionflag=True, promotionimage=koma_img_route[14], kind="kaku", opponent=True))
    return koma_group