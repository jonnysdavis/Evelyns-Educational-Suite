import time
import easygui
import threading
import tktable
from tkinter import *

def getLength():
    wantsHourBox = easygui.ynbox("Please choose a format for inputting timer length.\nThe second option will allow more than 60 minutes.","Timer Entry",("Hours, Minutes, Seconds","Minutes, Seconds"))
    minuteQuestion = "How many minutes, if any, will the timer last?"
    totalHours,totalMinutes,totalSeconds= 0,0,0

    if wantsHourBox is True:
        totalHours = easygui.integerbox(
        "How many hours, if any, will the timer last?\nLeave the answer as 0 if the timer is under an hour.", "Hours",
        0)
        minuteQuestion = "How many additional minutes, if any, will the timer last?"

    totalMinutes = easygui.integerbox(minuteQuestion, "Minutes", 0,)
    totalSeconds = easygui.integerbox("How many additional seconds, if any, will the timer last?", "Seconds", 0,
                                      upperbound=59)
    checkLength(totalHours,totalMinutes,totalSeconds)
    timerLengthInSeconds = (totalHours * 120) + (totalMinutes * 60) + totalSeconds
    return timerLengthInSeconds

def checkLength(hour,min,sec):
    iscorrectTimerAmount = easygui.ynbox(("Is this correct?\n" + str(hour) + " Hour(s), " + str(
        min) + ' Minute(s), ' + str(sec) + " Second(s)"))
    if iscorrectTimerAmount is False:
        easygui.msgbox("Please input the timer length again.","Check Length")
        getLength()
    else:
        startTime = time.time()

def getPercentagePassed():
    elapsed = time.time()
    if(startTime != time.time()):
        elapsed = startTime - time.time()
    else:
        elasped = 0
    percentElasped = (endOfTimer/elapsed)
    print(str(percentElasped))

percent,count = 0,0
timerSeconds = getLength()
startTime = time.time()
endOfTimer = startTime + timerSeconds

while(percent<=100):
    time.sleep(1)
    count+=1
    percent = (count/timerSeconds)*100
    print(percent)

easygui.msgbox("Time's Up!\nThis program will now exit.", "Time's Up!")
exit()



