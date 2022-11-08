import pygame as pg
import sys
import random
import time

floor_num = 8
floor_x = [0.0] * floor_num
floor_y = [0.0] * floor_num
floor_dx = [0.0] * floor_num
floor_half_w = [0.0] * floor_num

start_t =time.time()


class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg)
        self.bgi_rct = self.bgi_sfc.get_rect()
        pg.draw.line(self.bgi_sfc,(255,0,0),(0,900),(600,900),width=30)

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class chara:
    key_delta = {
        #pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
        pg.K_SPACE: [0, -2]#ジャンプ、跳（ちょう）かとん
    }
    def __init__(self, img, zoom, xy):
            sfc = pg.image.load(img) 
            self.sfc = pg.transform.rotozoom(sfc, 0, zoom) 
            self.rct = self.sfc.get_rect()
            self.rct.center = xy 

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        char_g = 0
        char_g += 1
        self.rct.move_ip(0,char_g)#降下とん
        
        key_states = pg.key.get_pressed()
        for key, delta in chara.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct,scr) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class floor:
    def __init__(self,scr:Screen):
        for i in range(floor_num):
            floor_half_w[i] = random(30,60)
            floor_x[i] = random(floor_half_w[i],scr.width - floor_half_w[i])
            if floor_x[i] < scr.width/2:
                floor_dx[i] = random(0.3,0.8)
            else:
                floor_dx[i] = - random(-0.8,-0.3)
        floor_y[i] = scr.height / (floor_num + 1) * (i+1)

    def move_floor(self,scr:Screen):
        for i in range(floor_num):
            if floor_x[i] <  floor_half_w[i] or scr.width- floor_half_w[i] < floor_x[i]:
                floor_dx[i] *= -1
            floor_x[i] += floor_dx[i]
            pg.draw.line(floor_x[i] - floor_half_w[i],floor_y[i],
                floor_x[i] + floor_half_w[i],floor_y[i])
         

def kouka_die(scr:Screen):#ゲームオーバー画面表示
    fonto =pg.font.Font(None,60)
    tmr = "GAME OVER"
    txt =fonto.render(str(tmr),True,"RED")
    scr.sfc.blit(txt,(100,100))
    

def check_bound(obj_rct, scr_rct,scr:Screen):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top:# or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    if scr_rct.bottom < obj_rct.bottom:
        tate = -1
        kouka_die(scr)
    return yoko, tate


def time_count(scr:Screen):#時間計測
    global start_t
    elapse_t = int(time.time() - start_t)
    el_hour = elapse_t // 3600
    el_minute = (elapse_t % 3600) // 60
    el_second = (elapse_t % 3600 % 60)
    fonto =pg.font.Font(None,60)
    tm = str(el_hour).zfill(2) + ":" + str(el_minute).zfill(2) + ":" + str(el_second).zfill(2)
    txt = fonto.render(str(tm),True,"RED")
    scr.sfc.blit(txt,(100,100))


def main():
    scr = Screen("hopping GAME", (600, 900), "fig/pg_bg.jpg")
    play = chara("fig/6.png", 1.5, (500, 100))
    time_count(scr)
    clock = pg.time.Clock()
    
    while True:
        scr.blit() 
        
        for event in pg.event.get(): 
             if event.type == pg.QUIT:
                 return

        play.update(scr)

    
        pg.display.update() 
        clock.tick(1000)



if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()