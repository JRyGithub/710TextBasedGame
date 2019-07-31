import time
from turtle import *
import random

# globals
userName = ""
directions = ['left', 'right', 'forward', 'back']


# start of the game get user name and their intial knowledge
def start():
    global userName
    print("Hi there, welcome to Quillan's and Josh's 710 program. I am Knowledgebot 5000! What's your name?")
    userName = input()
    print("So "+userName+" heard of Frank Blacker's theories on knowledge?")
    yesOrNo = input()
    if (yesOrNo == 'yes'):
        print("Awesome! Time for an adventure to explore Blacker's theories of knowledge, see if you add a few things to that knowledge base.")
        time.sleep(1)
        print("Would you like to go left to explore the Jungle of Embodied Knowledge?")
        time.sleep(1)
        print("Or you can go right to enter the Tombs of Encoded Knowledge?")
        time.sleep(1)
        directionOfChoice =  leftOrRight()
        if(directionOfChoice == 'left'):
            embodiedKnowledge()
        else:
            encodedKnowledge()           
    elif (yesOrNo == 'no'):
        print("Your being sent on a adventure to learn then! Welcome to the Tombs of Encoded Knowledge.")
        time.sleep(2)
        encodedKnowledge()

#Direction method, returns users input of either left or right, will be reused so put into simple method
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
# encodedKnowledge story

def encodedKnowledge():
    print("Interested in Encoded Knowledge are you "+userName + ". Impressive, beware the tombs.")
    
# embodiedKnowledge story


def embodiedKnowledge():
    print("I currently know nothing about this.")
# the end
def theEnd():
    print("TBC")


# start of the program is called
start()
