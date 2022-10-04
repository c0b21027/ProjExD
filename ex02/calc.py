import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import ttk


b_t_n = [
    ['χ2', '16', 'p', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['-', '0', 'C', '='],
] 
ope = ["÷", "×", "-", "+", "="]

def main():
    root = tk.Tk()
    root.title("calc")
    root.geometry("350x400")

def click_num(tap):#いらんかもな
    btn = tap.widget
    n = btn["text"]
    #tkm.showinfo("info",f"{n}のボタンがクリックされました")
    entry.insert(tk.END,n) #0でえーえんとく

class click_ev():#条件分岐をする
    def __init__(self):
        self.cal = tk.StringVar()
        self.var = tk.StringVar()
        def cl_bn(self,event):
            check = event.widget['text']
            if check == '=':
                if self.cal[-1:] in ope:
                    self.cal = self.cal[:-1]

                res = '=' + str(eval(self.cal)) 
                self.var.set(res)

            elif check == 'C':
                self.cal = ''
                self.var.set('')
            
            elif check == 'χ2':
                self.cal *= self.cal
                entry.delete(0, tk.END)
                entry.insert(tk.END, res)

            elif check == '16':
                self.cal = hex(self.cal)
            
            #elif check == 'P':
                #えらとすてねすがはいる


            elif check in ope: 
                if self.cal[-1:] not in ope and self.cal[-1:] != '':
                    self.cal += check
                elif self.cal[-1:] in ope:
                    self.cal = self.cal[:-1] + check 
    
"""  
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)
"""

entry = tk.Entry(root, width = 10, font = ("Times New Roman", 40), justify = "right")
entry.grid(row = 0, column = 0, columnspan = 3)


#r , c = 1, 0

for i, num in enumerate(b_t_n, 1):
    for j, nn in enumerate(num):
        button = tk.Button(root, text =f"{nn}",font = ("Times New Roman", 25),
                        width= 3, height= 1)
        if  nn.isdigit() == True :
            button.bind("<1>", click_num)
            button.grid(row = i, column = j, padx = 0, pady = 0)
        else :
            button.bind("<1>", click_ev)
            button.grid(row = i, column = j, padx = 0, pady = 0)

"""
#ほしゅ
nums = list(range(9, -1, -1))
enzan = ["+", "-", "*", "/"]
for i,num in enumerate(nums+enzan, 1):
    button = tk.Button(root, text =f"{num}",font = ("Times New Roman", 20),
                      width= 3, height= 1)
    button.bind("<1>", click_num)
    button.grid(row = r, column = c, padx = 0, pady = 0, columnspan = 1)
    c += 1 
    if i%3 == 0:
        r += 1
        c = 0

button = tk.Button(root, text = "=", font = ("Times New Roman", 27),
                   width= 4, height= 2)
button.bind("<1>", click_eq)
button.grid(row = r, column = c)

"""

root.mainloop()