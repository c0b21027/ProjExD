import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("300x500")

def click_num(tap):
    btn = tap.widget
    n = btn["text"]
    #tkm.showinfo("info",f"{n}のボタンがクリックされました")
    entry.insert(tk.END,n) #0でえーえんとく

def click_eq(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)


entry = tk.Entry(root, width = 10, font = ("Times New Roman", 40), justify = "right")
entry.grid(row = 0, column = 0, columnspan = 3)


r , c = 1, 0
nums = list(range(9, -1, -1))
enzan = ["+"]
for i,num in enumerate(nums+enzan, 1):
    button = tk.Button(root, text =f"{num}",font = ("Times New Roman", 27),
                      width= 4, height= 2)
    button.bind("<1>", click_num)
    button.grid(row = r, column = c,)
    c += 1 
    if i%3 == 0:
        r += 1
        c = 0

button = tk.Button(root, text = "=", font = ("Times New Roman", 27),
                   width= 4, height= 2)
button.bind("<1>", click_eq)
button.grid(row = r, column = c)


root.mainloop()