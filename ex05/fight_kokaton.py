import pygame as pg
import sys
import random


SCREENRECT = pg.Rect(0, 0, 640, 480)
SCORE = 0

class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)

    def attack(self):
        return Shot()


class Bomb:
    def __init__(self,color,radius, vxy,scr:Screen):
        sfc = pg.image.load("fig/fire.png") # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, 0.1) # 2.0
        self.rct = self.sfc.get_rect()
        # self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        # self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        # pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        #self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Alien(pg.sprite.Sprite):
    """An alien space ship. That slowly moves down the screen."""
    #こうかとんを焼きたがる
    speed = 13
    animcycle = 12
    images = []

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Alien.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 3]

class Shot():
    #戦うこうかとん、放火とん
    def __init__(self,image,chr:Bird,key):
        self.sfc=pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self,0,0.1)
        self.rct=self.sfc.get_rect()
        if key == pg.K_2:
            self.rct.midleft=chr.rct.center
            self.key = 'right'
        if key == pg.K_1:
            self.rct.midright=chr.rct.center
            self.key = 'left'
    def blit(selff,scr:Screen):
        scr.sfc.blit(scr.sfc,scr.rct)
    def update(self,scr:Screen):
        if self.key == 'right':
            self.rct.centerx += 10
        else:
            self.rct.centerx -= 10
        scr.sfc.blit(self.sfc,self.rct)
        self.blit(scr) 

        



def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

beams=[]
beam =None
def main():
    # 練習1
    scr = Screen("戦え！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習3
    kkt = Bird("fig/7.png", 2.0, (900, 400))

    # 練習5
    bkd = Bomb((255,0,0),10,(+1, +1), scr)

    
    #Shot.images = [load_image("shot.gif")]
    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    print(type(event.type))
                    print(type(pg.QUIT))
                    return
                if event.type ==pg.KEYDOWN and event.key == pg.K_1:
                    beam=Shot("fig/junsui.png",kkt,event.key)
                    beams.append(beam)
                if event.type ==pg.KEYDOWN and event.key == pg.K_2:
                    beam=Shot("fig/junsui.png",kkt,event.key)
                    beams.append(beam)
                if event.type ==pg.KEYDOWN and event.key == pg.K_RIGHT:
                    kx,ky = kkt.rct.center
                    kkt.Bird("fig/6.png",2.0,(kx,ky))
                if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                    kx,ky =kkt.rct.centerkkt=Bird("fig/8.png",2.0,(kx,ky))

        kkt.update(scr)
        if beams != None:
            for i in beams:
                i.update(scr)
        # 練習4
        #kkt.update(scr)

        # 練習7
        bkd.update(scr)

        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()