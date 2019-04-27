from tkinter import *
from Student import *
from tkinter import Menu

attributeList = [""] #Student attributes to help with organzation, such as reading level or math level
roster = [Student]

window = Tk()
window.title("Evelyn's Educational Suite")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='About')
new_item.add_command(label='Save')
new_item.add_command(label='Exit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()

def addStudent(last, first):
    temp = Student("doe","john",1)
    roster.append(temp)

