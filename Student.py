#Created by Jonathan Davis. All rights reserved, 2019.
#This class is an object to contain Student info when using them during the program

attributeList = ["",""]
lastName = ""
firstName = ""
rosterID = 0
allergies = []
otherTeachers = [[""],[""]]
contactEmails = ["None"]
contactPhones = ["None"]

class Student(object):

    def __init__(self,last,first):
        lastName = last
        firstName = first

    def __init__(self):
        lastName = "none"
        firstName = "none"

    def addAttrbute(self, skill, score): #Add an attribute to each student
        attributeList.append(skill, score)

    def nameStudent (last,first):
        lastName = last
        firstName = first

    def getRoster(self):
        return rosterID

    def newAllergy(allergy):
        allergies.append(allergy)

    def consoleCreateStudent(self):
        lastName = input("Student's Last Name: ")
        firstName = input("Student's First Name: ")
        tempStudent = Student(lastName, firstName)
        return tempStudent

    def getFullName(self):
        return lastName + ", " + firstName