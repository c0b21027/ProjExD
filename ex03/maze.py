import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""

def pain():#こうかとんが苦しむ
    global tori
    tori = tk.PhotoImage(file = "fig/8.png")
    canv.create_image(cx,cy,image=tori,tag="tori")

def goal():
    tori = tk.PhotoImage(file = "fig/toririn.gif")
    canv.create_image(cx,cy,image=tori,tag="tori")
    tkm.showinfo("すごい","こうかとん　の　好感度が　あがった！")
    labe = tk.Label(root,text="こうかとん　は　鳥取大学　の　とりりん　に　なった　！",font =20)
    labe.pack()
    root.mainloop()

    

def main_proc():
    global mx, my,tori
    global cx, cy
    tori = tk.PhotoImage(file = "fig/0.png")
    canv.create_image(cx,cy,image=tori,tag="tori")
    if key =="Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_list[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        pain()
        if key =="Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1

    canv.coords("tori", cx, cy)
    if cx == 13*100+50:#メッセージボックスの出現
        if  cy == 1*100+50:
            goal()
    root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk() 
    root.title("迷えるこうかとん")

    canv = tk.Canvas(root,width = 1500,height = 900,bg ="black")
    canv.pack()

    maze_list = mm.make_maze(15,9)
    print(maze_list)#1壁,0床

    mm.show_maze(canv, maze_list)
    canv.create_rectangle(1300,100,1400,200,fill="red")

    tori = tk.PhotoImage(file = "fig/0.png")
    mx,my = 1,1
    cx,cy = mx*300+50,my*400+50
    canv.create_image(cx,cy,image=tori,tag="tori")

    key = ""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    root.mainloop()