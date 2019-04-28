#Created by Jonathan Davis. All rights reserved, 2019.
#Named after the passionate educator who inspired this creation, who also suggested the tools. Your students are lucky to have you.

from tkinter import *
from Student import *
from Roster import *
from tkinter import Menu

rosterList = [Roster]
studentList = [Student]

def createMenuBar():
    menu = Menu(window)  # Start Menu Bar
    '''
    How to link file menu option to command
    rosterMenu.add_command(label="About...", command=about)
    '''
    fileMenu = Menu(menu) #Create File Dropdown
    fileMenu.add_command(label='About', command=about)  # Add option to current file-menu column
    fileMenu.add_command(label='Save' , command=save)
    fileMenu.add_command(label='Exit' , command = gracefulExit)
    menu.add_cascade(label='File', menu=fileMenu)  # Creates new file-menu column

    rosterMenu = Menu(menu) #Create Roster Dropdown
    rosterMenu.add_command(label="New Roster", command=about)
    rosterMenu.add_command(label="Edit Roster", command=about)
    rosterMenu.add_command(label="Display Roster", command=about)
    rosterMenu.add_command(label="Import Roster", command=about)
    rosterMenu.add_command(label="Export Roster", command=about)
    menu.add_cascade(label='Roster', menu=rosterMenu)  # Creates new file-menu column

    studentMenu = Menu(menu)  # Create student Dropdown
    menu.add_cascade(label='Students', menu=studentMenu)
    studentMenu.add_command(label="Add Pupil", command=about)
    studentMenu.add_command(label="Edit Pupil", command=about)
    studentMenu.add_command(label="Add Pupil Attribute", command=about)
    studentMenu.add_command(label="Import Pupil", command=about)
    studentMenu.add_command(label="Export Pupil", command=about)

    groupMenu = Menu(menu)  # Create group Dropdown
    menu.add_cascade(label='Groups', menu=groupMenu)
    groupMenu.add_command(label="New Groups", command=about)
    groupMenu.add_command(label="Re-Use Group", command=about)
    groupMenu.add_command(label="Import Group", command=about)
    groupMenu.add_command(label="Export Group", command=about)

    subMenu = Menu(menu)  # Create sub Dropdown
    menu.add_cascade(label='Substitutes', menu=subMenu)
    subMenu.add_command(label="New Plan", command=about)
    subMenu.add_command(label="Load Plan", command=about)
    subMenu.add_command(label="Edit Info", command=about)

    donateMenu = Menu(menu)  # Create donate Dropdown
    donateMenu.add_command(label="Donate", command=about)
    donateMenu.add_command(label="Share", command=about)
    menu.add_cascade(label='Donate', menu=donateMenu)

    window.config(menu=menu)  # End and Display Menu Bar


#Information about the program and its inspiration
def about():
    top = Toplevel()
    top.title("About")
    msg = Message(top, text="Thank you for downloading Evelyn's Educational Suite."
                            "\n\nThis program was inspired by, and created for, a passionate educator whose students are lucky to have her."
                            "\n\nCreated by Jonathan Davis."
                            "\n\nAll Rights Reserved, 2019.")
    msg.pack()
    button = Button(top, text="Thank You Evelyn!", command=top.destroy)
    button.pack()

#Currently does nothing as program has no database yet
def save():
    top = Toplevel() #Create pop-up
    top.title("Save")
    msg = Message(top, text="Your changes have been saved.")
    msg.pack()
    button = Button(top, text="OK", command=top.destroy)
    button.pack()

def addStudent():
    newStudent = Student("last","first","roster ID")
    rosterList[0].addStudent(newStudent) #0 needs to eb replaced with finding the students roster
    print()

def gracefulExit():
    exit()



window = Tk()
window.title("Evelyn's Educational Suite")
createMenuBar()


window.mainloop() #Forever loop to keep window open, breaking loop closes program