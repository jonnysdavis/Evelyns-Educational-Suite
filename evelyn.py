from tkinter import *

from tkinter import Menu


window = Tk()
window.title("Evelyn's Educational Suite")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='About')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()
