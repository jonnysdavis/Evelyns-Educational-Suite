#Created by Jonathan Davis. All rights reserved, 2019.
#Named after the passionate educator who inspired this creation, who also suggested the tools. Your students are lucky to have you.

from tkinter import *
from Roster import *
from tkinter import Menu
import webbrowser
import VisualTimer

rosterList = [Roster]
studentList = [Student]

def createMenuBar(window):
    menu = Menu(window)  # Start Menu Bar
    '''
    How to link file menu option to command
    rosterMenu.add_command(label="About...", command=about)
    '''
    fileMenu = Menu(menu,tearoff=False) #Create File Dropdown
    fileMenu.add_command(label='About', command=about)  # Add option to current file-menu column
    fileMenu.add_command(label='Save' , command=save)
    fileMenu.add_command(label='Exit' , command = gracefulExit)
    fileMenu.add_command(label='Check for Updates', command=checkUpdate)
    menu.add_cascade(label='File', menu=fileMenu)  # Creates new file-menu column

    rosterMenu = Menu(menu,tearoff=False) #Create Roster Dropdown
    rosterMenu.add_command(label="New Roster", command=about)
    rosterMenu.add_command(label="Edit Roster", command=about)
    rosterMenu.add_command(label="Display Roster", command=about)
    rosterMenu.add_command(label="Import Roster", command=about)
    rosterMenu.add_command(label="Export Roster", command=about)
    menu.add_cascade(label='Roster', menu=rosterMenu)  # Creates new file-menu column

    studentMenu = Menu(menu,tearoff=False)  # Create student Dropdown
    menu.add_cascade(label='Students', menu=studentMenu)
    studentMenu.add_command(label="Add Pupil", command=about)
    studentMenu.add_command(label="Edit Pupil", command=about)
    studentMenu.add_command(label="Add Pupil Attribute", command=about)
    studentMenu.add_command(label="Import Pupil", command=about)
    studentMenu.add_command(label="Export Pupil", command=about)

    groupMenu = Menu(menu,tearoff=False)  # Create group Dropdown
    menu.add_cascade(label='Groups', menu=groupMenu)
    groupMenu.add_command(label="New Groups", command=about)
    groupMenu.add_command(label="Re-Use Group", command=about)
    groupMenu.add_command(label="Import Group", command=about)
    groupMenu.add_command(label="Export Group", command=about)

    subMenu = Menu(menu,tearoff=False)  # Create sub Dropdown
    menu.add_cascade(label='Substitutes', menu=subMenu)
    subMenu.add_command(label="New Plan", command=about)
    subMenu.add_command(label="Load Plan", command=about)
    subMenu.add_command(label="Edit Info", command=about)

    donateMenu = Menu(menu,tearoff=False)  # Create donate Dropdown
    donateMenu.add_command(label="Donate", command=donate)
    donateMenu.add_command(label="Share", command=share)
    menu.add_cascade(label='Donate', menu=donateMenu)

    moreTool = Menu(menu, tearoff=False)  # Create Other Tools Dropdown
    moreTool.add_command(label="Visual Timer", command=visualTimer)
    moreTool.add_command(label="New Functional Behavioral Assessment", command=newFba)
    moreTool.add_command(label="Book Scheduler", command=readTimeGuess)
    menu.add_cascade(label='More Tools', menu=moreTool)

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

def newFba():
    print("needs to enter a new functional behvarioal assesment for a student and log it")

def visualTimer():
    print("create a visually friendly and kid friendly timer based on hannah's large red circle timer")

def readTimeGuess():
    pass

def newRoster(id):
    newClass = Roster
    newClass.setRosterName(id)
    rosterList.append(newClass)

def addRoster(new):
    rosterList.append(new)

def enrollStudent(newStudent):
    pupil = Student

def gracefulExit():
    exit()

def share():
    url = "https://github.com/jonnysdavis/Evelyns-Educational-Suite"
    webbrowser.open_new(url)

def donate():
    url = "https://supporters.eff.org/donate/join-4"
    webbrowser.open_new(url)

def checkUpdate():
    top = Toplevel()
    top.geometry('150x75')
    top.title("Updates")
    msg = Message(top, text="You have the most up to date version.")
    msg.pack()
    button = Button(top, text="OK", command=top.destroy)
    button.pack()

def getRosterList():
    return rosterList

def setRosterList(newRosterList):
    rosterList = newRosterList

def newYesPopUp(newTitle, message, buttonText):
    top = Toplevel()
    top.title(newTitle)
    msg = Message(top, text=message)
    msg.pack()
    button = Button(top, text=buttonText, command=top.destroy)
    button.pack()
    return top



baseWindow = Tk()
baseWindow.geometry('700x300')
baseWindow.title("Evelyn's Educational Suite")
createMenuBar(baseWindow)
deleteMe = Student()

studentList.append(Student.consoleCreateStudent(Student))
print(studentList[0].getFullName())





baseWindow.mainloop() #Forever loop to keep window open, breaking loop closes program