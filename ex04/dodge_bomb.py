import pygame as pg
import sys
from random import randint
import time



def check_bound(obj_rct,scrn_rct):#obj_rctこうかとんor爆弾rect
    yoko,tate = +1,+1
    if obj_rct.left < scrn_rct.left or scrn_rct.right <obj_rct.right:
        yoko = -1
    if obj_rct.top < scrn_rct.top or scrn_rct.bottom < obj_rct.bottom: 
        tate = -1

    return yoko, tate


def koukaton_attack():
    global scr_sfc,toriki_zoku
    bakushi = pg.image.load("fig/8.png")
    bakushi = pg.transform.rotozoom(bakushi,0,2.0)
    j = 0
    bakushi_rct = bakushi.get_rect()
    #pg.Rect.move_ip(600,600)
    scr_sfc.blit(bakushi,bakushi_rct)
    # pg.display.update()
    # for i in range(5):#こうかとんがのたうちまわる
    #      while(1):
    #          bakushi= pg.transform.rotate(bakushi,j)
    #          j += 90
    #          if j == 360:
    #              j = 0
    #              i += 1


    # bakushi= pg.transform.rotate(bakushi,180)


    

def count_k():
    global  time_sta
    fonto =pg.font.Font(None,80)
    tmr = "GAME OVER"
    txt =fonto.render(str(tmr),True,"RED")
    scr_sfc.blit(txt,(300,200))
    time.sleep(1)
    time_end = time.time()
    tim = time_end- time_sta
    tk =fonto.render(str(tim),True,"BLACK")
    scr_sfc.blit(tk,(1000,600))
    koukaton_attack()
    


def main():
    global scr_sfc,toriki
    pg.display.set_caption("逃げろ！こうかとん")
    scr_sfc = pg.display.set_mode((1600,900))
    scr_rct =scr_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    toriki = pg.image.load("fig/6.png")
    toriki = pg.transform.rotozoom(toriki,0,2.0)
    toriki_zoku = toriki.get_rect()
    toriki_zoku.center = 900,400

    bomb = pg.Surface((50,50))
    bomb.set_colorkey((0,0,0))
    pg.draw.circle(bomb, (255, 0, 0), (25,25),20)
    bomb_rct = bomb.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(0,scr_rct.width),randint(0,scr_rct.height)
    vx,vy = 5,5
    clock = pg.time.Clock()
    while 1:
        scr_sfc.blit(bg_sfc,bg_rct)

        key_states =pg.key.get_pressed()
        if key_states[pg.K_UP]: toriki_zoku.centery -= 1 #こうかとん-1
        if key_states[pg.K_DOWN]: toriki_zoku.centery += 1#こうかとん+1
        if key_states[pg.K_LEFT]: toriki_zoku.centerx -= 1#こうかとん横-1
        if key_states[pg.K_RIGHT]: toriki_zoku.centerx += 1 #こうかとん横+1
        yoko, tate = check_bound(toriki_zoku, scr_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                toriki_zoku.centerx += 1
            if  key_states[pg.K_RIGHT]:
                toriki_zoku.centerx -= 1

        if tate == -1:
            if key_states[pg.K_UP]:
                toriki_zoku.centery += 1
            if  key_states[pg.K_DOWN]:
                toriki_zoku.centery -= 1

        scr_sfc.blit(toriki,toriki_zoku)

        yoko, tate = check_bound(bomb_rct, scr_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx,vy)
        scr_sfc.blit(bomb,bomb_rct)

        if toriki_zoku.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
            count_k()

        pg.display.update()


        for event in pg.event.get():
            if event.type == pg.QUIT: return

        clock.tick(1000)

    


if __name__ == "__main__":
    pg.init()
    scr_sfc = pg.display.set_mode((1600,900))
    toriki = pg.image.load("fig/6.png")
    toriki_zoku = toriki.get_rect()
    time_sta = time.time()
    main()
    pg.quit()
    sys.exit()