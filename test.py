import pygame
from pygame.locals import *
import math
import sys
import pygame.mixer

# 画面サイズを設定
SCREEN = Rect(0, 0, 540, 540)

# 跳ね返しバーのクラス
class HanekaeshiBar(pygame.sprite.Sprite):
    # コンストラクタ（初期化メソッド）
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN.bottom - 20  # パドルのy座標

    def update(self):
        # マウスのx座標を跳ね返しバーのx座標に設定
        self.rect.centerx = pygame.mouse.get_pos()[0]
        # ゲーム画面内のみで移動に限定
        self.rect.clamp_ip(SCREEN)

# ボールのクラス
class Ball(pygame.sprite.Sprite):
    # コンストラクタ（初期化メソッド）
    def __init__(self, filename, hanekaeshiBar, blocks, score, speed, angle_left, angle_right):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        # ボールの速度
        self.dx = self.dy = 0
        # 跳ね返しバーへの参照
        self.hanekaeshiBar = hanekaeshiBar
        # ブロックグループへの参照
        self.blocks = blocks
        # ゲーム開始状態に更新
        self.update = self.start
        self.score = score
        # 連続でブロックを壊した回数
        self.hit = 0
        # ボールの初期速度
        self.speed = speed
        # 跳ね返しバーの反射方向(左端:135度）
        self.angle_left = angle_left
        # 跳ね返しバーの反射方向(右端:45度）
        self.angle_right = angle_right

    # ゲーム開始状態
    # 　マウスを左クリックでボールが発射される
    def start(self):
        # ボールの初期位置
        # 　跳ね返しバーの上、センタリング
        self.rect.centerx = self.hanekaeshiBar.rect.centerx
        self.rect.bottom = self.hanekaeshiBar.rect.top

        # 左クリックでボール発射
        if pygame.mouse.get_pressed()[0] == 1:
            self.dx = 0
            self.dy = -self.speed
            self.update = self.move

    # ボールの動き
    def move(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        # 壁に対して反射させる
        #   左側に衝突時
        if self.rect.left < SCREEN.left:
            self.rect.left = SCREEN.left
            # 速度を反転
            self.dx = -self.dx
        # 壁に対して反射させる
        #   右側に衝突時
        if self.rect.right > SCREEN.right:
            self.rect.right = SCREEN.right
            self.dx = -self.dx
        # 壁に対して反射させる
        #   上側に衝突時
        if self.rect.top < SCREEN.top:
            self.rect.top = SCREEN.top
            self.dy = -self.dy

        # 跳ね返りバーとの反射
        # 　左端:135度方向, 右端:45度方向, それ以外:線形補間をする
        #   2つのspriteが接触しているかどうかの判定
        if self.rect.colliderect(self.hanekaeshiBar.rect) and self.dy > 0:
            # 連続ヒットを0に戻す
            self.hit = 0
            (x1, y1) = (self.hanekaeshiBar.rect.left - self.rect.width, self.angle_left)
            (x2, y2) = (self.hanekaeshiBar.rect.right, self.angle_right)
            # ボールが当たった位置
            x = self.rect.left
            # 線形補間する
            y = (float(y2 - y1) / (x2 - x1)) * (x - x1) + y1
            # 反射角度
            angle = math.radians(y)
            self.dx = self.speed * math.cos(angle)
            self.dy = -self.speed * math.sin(angle)
            # 反射音
            self.hanekaeshiBar_sound.play()

        # ボールを落とした場合
        if self.rect.top > SCREEN.bottom:
            # ボールを初期状態に戻す
            self.update = self.start
            self.gameover_sound.play()
            self.hit = 0
            # スコア減点-100点
            self.score.add_score(-100)

        # ボールと衝突したブロックリストを取得
        #   Groupが格納しているSprite中から、指定したSpriteと接触しているものを探索
        blocks_collided = pygame.sprite.spritecollide(self, self.blocks, True)
        # 衝突ブロックがある場合
        if blocks_collided:
            oldrect = self.rect
            for block in blocks_collided:
                # ボールが左からブロックへ衝突した場合
                if oldrect.left < block.rect.left and oldrect.right < block.rect.right:
                    self.rect.right = block.rect.left
                    self.dx = -self.dx

                # ボールが右からブロックへ衝突した場合
                if block.rect.left < oldrect.left and block.rect.right < oldrect.right:
                    self.rect.left = block.rect.right
                    # x軸方向へ増加量を反転
                    self.dx = -self.dx

                # ボールが上からブロックへ衝突した場合
                if oldrect.top < block.rect.top and oldrect.bottom < block.rect.bottom:
                    self.rect.bottom = block.rect.top
                    # ｙ軸方向へ増加量を反転
                    self.dy = -self.dy

                # ボールが下からブロックへ衝突した場合
                if block.rect.top < oldrect.top and block.rect.bottom < oldrect.bottom:
                    self.rect.top = block.rect.bottom
                    # ｙ軸方向へ増加量を反転
                    self.dy = -self.dy
                # 効果音を鳴らす
                self.block_sound.play()
                # 衝突回数カウント
                self.hit += 1
                # 衝突回数に応じてスコア加算
                self.score.add_score(self.hit * 10)

# ブロックのクラス
class Block(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        # ブロックの左上座標
        self.rect.left = SCREEN.left + x * self.rect.width
        self.rect.top = SCREEN.top + y * self.rect.height

# スコアのクラス
class Score():
    def __init__(self, x, y):
        self.sysfont = pygame.font.SysFont(None, 20)
        self.score = 0
        (self.x, self.y) = (x, y)

    def draw(self, screen):
        img = self.sysfont.render("SCORE:" + str(self.score), True, (255, 255, 250))
        screen.blit(img, (self.x, self.y))

    def add_score(self, x):
        self.score += x

# メイン　ここからスタート
def main():
    # 初期化
    pygame.init()
    # スクリーン設定
    screen = pygame.display.set_mode(SCREEN.size)
    # サウンド設定1
    #   パドルにボールが衝突した時の効果音取得
    Ball.hanekaeshiBar_sound = pygame.mixer.Sound("/Users/.../省略/.../songs/catch.wav")
    # サウンド設定2
    #   ブロックにボールが衝突した時の効果音取得
    Ball.block_sound = pygame.mixer.Sound("/Users/.../省略/.../songs/bang.wav")
    # サウンド設定3
    #   ゲームオーバー時の効果音取
    Ball.gameover_sound=pygame.mixer.Sound("/Users/.../省略/.../songs/falling.wav")  
    # 描画用のスプライトグループ
    gp = pygame.sprite.RenderUpdates()

    # 衝突判定用のスプライトグループ
    blocks = pygame.sprite.Group()

    # スプライトグループに追加
    HanekaeshiBar.containers = gp
    Ball.containers = gp
    Block.containers = gp, blocks

    # パドルの作成
    hanekaeshiBar = HanekaeshiBar("/Users/.../省略/.../pngs/haneBar.png")

    # ブロックの作成(20*20)
    for x in range(1, 20):
        for y in range(1, 21):
            # 中間のブロックを抜いておく
            if y < 8 or 14 < y:
                Block("/Users/.../省略/.../pngs/block.png", x, y)

    # スコアを画面(10, 10)に表示
    score = Score(10, 10)

    # ボールを作成
    Ball("/Users/.../省略/.../pngs/ball.png",
         hanekaeshiBar, blocks, score, 5, 135, 45)

    clock = pygame.time.Clock()

    while (1):
        # フレームレート(60fps)
        clock.tick(60)
        screen.fill((0, 20, 0))
        # 全てのスプライトグループを更新
        gp.update()
        # 全てのスプライトグループを描画
        gp.draw(screen)
        # スコアを描画
        score.draw(screen)
        # 画面更新
        pygame.display.update()

        # キーイベント（終了）
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

# これはPythonの特殊な書き方ですが頻繁に出てきます。
# スクリプトをpythonコマンドで実行したりダブルクリックで実行すると
# __name__に__main__という文字列が代入されます。
# if文がTrueになり、main()が自動的に始まります。
if __name__ == "__main__":
    main()
