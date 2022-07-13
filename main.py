import os.path
import time
import webbrowser
import os
import pync
import subprocess

#print("Hello! This your new note taker, reminder, or whatever you want to call it! =)\nWhen asked to put an input, it won't matter if you put it in captial leltters or not, but please don't spell it wrong.")
def fileExistence():
    if os.path.exists("/Users/shubsharma/Desktop/Logger.txt"):
        pass
    else:
        file = open("/Users/shubsharma/Desktop/Logger.txt", "w")
        file.close()
fileExistence()

def addNotes():
    appendin = open("/Users/shubsharma/Desktop/Logger.txt", "a+")
    addingNotes = input("Would you like to add a note/reminder.\nType yes or no. ")
    if addingNotes.upper() == "YES":
        print("Please answer the further more questions to add a note/reminder.")
        inputDT = input("Please set the notifier as in the order of '(Year)-(Month)-(Date) (Hours):(Minutes):(Seconds)'\nPlease put your time in 24 hours and put numbers for the month.\n")
        notTitle = input("What would you like to name your notification? ")
        notSubitle = input("What is your subtitle/message? ")
        notOpenweb = input("Would you like to open a webpage?\nDirectly put the link if yes or else type no. ")
        def main2():
            Actual_DT = time.strftime("%Y-%m-%d %H:%M:%S")
            while (Actual_DT != inputDT):
                print("It is " + Actual_DT)
                Actual_DT = time.strftime("%Y-%m-%d %H:%M:%S")
                time.sleep(1)
            if (Actual_DT == inputDT):
                print("You should see your notification now. =)")
                subprocess.call(["afplay", "/Users/shubsharma/Desktop/Bruh.wav"])
        if notOpenweb.upper() == "NO":
           main2()
           pync.notify('', title=notTitle, subtitle=notSubitle)
        else:
            main2()
            pync.notify('',title=notTitle, subtitle=notSubitle, open=notOpenweb)
            webbrowser.open(notOpenweb)
    elif addingNotes.upper() == "NO":
        print("Quitting application.")
        quit()
    else:
        print("Wrong input. Try again.")
        addNotes()
    appendin.write("\n\n---------------------------\n\n" + "Date: "+ inputDT+"\nTitle- "+notTitle+"\nSubtitle/Message- "+notSubitle+"\nWebpage- "+notOpenweb)
    appendin.close()
addNotes()
