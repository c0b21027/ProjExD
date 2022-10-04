import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("300x500")

def click_num(tap):
    btn = tap.widget
    n = int(btn["text"])
    #tkm.showinfo("info",f"{n}のボタンがクリックされました")
    entry.insert(tk.END,n)


entry = tk.Entry(root, width = 10, font = ("Times New Roman", 40), justify = "right")
entry.grid(row = 0, column = 0, columnspan = 3)


r = 1;c = 0


for i,num in enumerate(range(9,-1,-1),1):
    button = tk.Button(root, text =f"{num}",font = ("Times New Roman", 27),
                      width= 4, height= 2)
    button.bind("<1>", click_num)
    button.grid(row = r, column = c, ipadx = 3)
    c += 1 
    if i%3 == 0:
        r += 1
        c = 0

root.mainloop()