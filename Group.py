#Created by Jonathan Davis. All rights reserved, 2019.

#A roster is a collection of students, of which have no over-lapping bans.

from Student import *

students = [Student]
groupBans = []
groupName = "?"
sizeMax = 999
sizeMin = 0
size = 0


class Group(object):
    def __init__(self):
        print()