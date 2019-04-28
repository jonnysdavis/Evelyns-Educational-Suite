#Created by Jonathan Davis. All rights reservered, 2019.
#Named after the passionate educator who inspired this creation, who also suggested the tools. Your students are lucky to have you.

from tkinter import *
from Student import *
from tkinter import Menu

def createMenuBar():
    menu = Menu(window)  # Start Menu Bar
    new_item = Menu(menu)
    new_item.add_command(label='About', command=about)  # Add option to current file-menu column
    new_item.add_command(label='Save')
    new_item.add_command(label='Exit')
    menu.add_cascade(label='File', menu=new_item)  # Creates new file-menu column
    window.config(menu=menu)  # End Menu Bar

#Information about the program
def about():
    top = Toplevel()
    top.title("About")
    msg = Message(top, text="Thank you for downloading Evelyn's Educational Suite."
                            "\nThis program was inspired by, and created for, a passionate educator whose students are lucky to have her."
                            "\nCreated by Jonathan Davis."
                            "\nAll Rights Reserved, 2019.")
    msg.pack()

    button = Button(top, text="Thank You Evelyn!", command=top.destroy)
    button.pack()

#Code to run program
window = Tk()
window.title("Evelyn's Educational Suite")
createMenuBar()
window.mainloop()