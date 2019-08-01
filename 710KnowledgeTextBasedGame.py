import time
from turtle import *
import random

# globals
userName = ""
directions = ['left', 'right', 'forward', 'back']
noOrYes = ['y','n']
encodedOrEnculturedList = ['encoded','encultured']


# start of the game get user name and their intial knowledge
def start():
    global userName
    print("Enter your name")
    userName = input()
    time.sleep(0.5)
    print("")
    print(userName)
    print("Welcome to Learning about Knowledge")
    time.sleep(0.5) 
    print("An understanding of Frank Blacker’s perspective")
    time.sleep(0.5)
    print("Brought to you by Josh Ryland and Quillan Aherne")
    time.sleep(0.5)
    print("Do you wish to proceed? [Y/N]")
    userYesOrNo = yesOrNo()
    if (userYesOrNo.lower() == 'y'):
        print("Wonderful!")
        time.sleep(0.5)
        print("As Blacker outlines there are many approaches to understanding knowledge within an organisational setting.")
        time.sleep(0.5)
        print("Today "+ userName+", you are going to be exploring two of these: encultured knowledge and encoded knowledge.")
        time.sleep(0.5)
        print("The format you will be interacting with reflects the themes you are going to explore.")
        time.sleep(0.5)
        print("With the decontextual nature of the code itself mirroring encoded knowledge")
        print("And the style of 90’s computing providing cultural nuance to the information about to be displayed.")
        time.sleep(0.5)
        print("So, where you do you want to start?")
        time.sleep(0.5)
        print("[encoded/encultured]")
        encodedOrEncultured = ""
        while encodedOrEncultured not in encodedOrEnculturedList:
            encodedOrEncultured = input()
            if (encodedOrEncultured.lower() == 'encoded'):
                encodedKnowledge()
            elif  (encodedOrEncultured.lower() == 'encultured'):
                enculturedKnowledge()
            else:
                time.sleep(1)
                print("That was never a option.")        
    elif (yesOrNo.lower() == 'n'):
        time.sleep(1)
        print("Umm… [NAME] you seem to have missed the point.")
        time.sleep(0.5)
        print("Please don’t get trapped in an infinite loop.")
        time.sleep(0.5)
        print("Would you like to learn about knowledge? [Y/N]")      

#Direction or YesNo method, simply gets userInput of either left, right, y or n depending on variable direction or yesOrNo
def leftOrRight():
        print("So left or right?")
        userChoice = ""
        while userChoice not in directions:
            userChoice = input()
            if userChoice.lower() == 'left':
                return 'left'
            elif userChoice.lower() == 'right':
                return 'right'
            else:
                print("well that wasn't an option, left or right?")
        

#Y or N
def yesOrNo():
    print("[Y/N]")
    userInput = ""
    while userInput not in noOrYes:
        userInput= input()
        if (userInput.lower() == 'y'):
            return 'y'
        elif (userInput.lower() == 'n'):
            return 'n'
        else:
            print("well that wasn't an option, left or right?")
# encodedKnowledge story

def encodedKnowledge():
    print("Interested in Encoded Knowledge are you "+userName + ". Impressive, beware the tombs.")
    
# embodiedKnowledge story


def enculturedKnowledge():
    print("I currently know nothing about this.")
# the end
def theEnd():
    print("TBC")


# start of the program is called
start()
