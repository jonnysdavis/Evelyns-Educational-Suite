#Created by Jonathan Davis. All rights reserved, 2019.

#A roster is a collection of students, as well as the attributes of of that class.
#The same student can be in multiple rosters because a teacher may have the student in different classes throughout the day

from Student import *

studentList = [Student]
attributeList = []
rosterID = "0"

class Roster(object):
    def __init__(last,first,class_period_arg):
        lastName = last
        firstName = first
        class_period = class_period_arg

    def addAttrbuteAll(attribute,roster): #Add an attribute to each student
        for Student in roster:
            tempStudent = Student

    def addBan(Student):
        banList.append(Student)

    def setRosterName(name):
        rosterID = name

    def addStudent(pupil):
        studentList.append(pupil)

