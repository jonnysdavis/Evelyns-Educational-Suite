#test.py
try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import pygubu


class addStudent:
    def __init__(self, master):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file("addstudent.ui")

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('addStudentBox', master)

        entry = self.builder.get_object('lastNameEntry')
        value = entry.get()
        print('Entry_1:', value)

if __name__ == '__main__':
    root = tk.Tk()
    app = addStudent(root)

    root.mainloop()