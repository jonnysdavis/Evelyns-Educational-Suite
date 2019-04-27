#This class is an object to contain Student info when using them during the program


lastName = ""
firstName = ""
class_period = 0
grade = 0
other = [[""][""]]
banList = []  # A List of all the students the student in question should not work with

class Student(object):

    def __init__(last,first,class_period_arg,grade_arg):
        lastName = last
        firstName = first
        class_period = class_period_arg
        grade = grade_arg

    def addAttrbuteAll(attribute,roster): #Add an attribute to each student
        for Student in roster:
            tempStudent = Student
            tempStudent.

    def addBan(Student):
        banList.append(Student)

    def addAttribute(attribute):
        other.append([attribute]["?"])




