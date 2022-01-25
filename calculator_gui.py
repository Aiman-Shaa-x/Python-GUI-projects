from tkinter import *

window = Tk()
window.title('Basic Calculator')
window.geometry('400x350')


def solve(**num):
    expr = editor.get('1.0', END)
    print(eval(expr, num))


menu_bar = Menu(window)

calc_bar = Menu(menu_bar, tearoff=0)
calc_bar.add_command(label='Solve', command=solve)
menu_bar.add_cascade(label='Calculate', menu=calc_bar)
window.config(menu=menu_bar)

editor = Text(width=50, height=20, font=(5, 15))
editor.pack()

window.mainloop()
