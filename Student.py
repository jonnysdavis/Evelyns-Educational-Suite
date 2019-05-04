#Created by Jonathan Davis. All rights reserved, 2019.
#This class is an object to contain Student info when using them during the program

attributeList = ["",""]
lastName = ""
firstName = ""
rosterID = 0

class Student(object):

    def __init__(last,first,class_period_arg):
        lastName = last
        firstName = first
        class_period = class_period_arg

    def addAttrbute(self, skill, score): #Add an attribute to each student
        attributeList.append(skill, score)

    def nameStudent (last,first):
        lastName = last
        firstName = first

    def getRoster(self):
        return rosterID

