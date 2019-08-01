import time
import sys

# globals
userName = ""
directions = ['left', 'right', 'forward', 'back']
noOrYes = ['y', 'n']
encodedOrEnculturedList = ['encoded', 'encultured']


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
        print("Today " + userName +
              ", you are going to be exploring two of these: encultured knowledge and encoded knowledge.")
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
            elif (encodedOrEncultured.lower() == 'encultured'):
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

# Direction or YesNo method, simply gets userInput of either left, right, y or n depending on variable direction or yesOrNo


def aOrB():
        userChoice = ""
        while userChoice not in directions:
            userChoice = input()
            if userChoice.lower() == 'a':
                return 'a'
            elif userChoice.lower() == 'b':
                return 'b'
            else:
                print("well that wasn't an option, [A] or [B]?")


# Y or N
def yesOrNo():
    print("[Y/N]")
    userInput = ""
    while userInput not in noOrYes:
        userInput = input()
        if (userInput.lower() == 'y'):
            return 'y'
        elif (userInput.lower() == 'n'):
            return 'n'
        else:
            print("well that wasn't an option, [Y] or [N]")
# encodedKnowledge story


def encodedKnowledge():
    time.sleep(1)
    print(userName+" you are on a small prop plane flying over the Florida Everglades when you hear the")
    time.sleep(1)
    print("engine on one of the wings sputter and stall.")
    time.sleep(1)
    print("You don’t need the frantic yelling of the pilot to")
    time.sleep(1)
    print("alert you that there is a problem.")
    time.sleep(1)
    print("One of the Colombian smugglers hands you a backpack and a small leaflet, not being able to speak Spanish isn’t much of a burden right now as what")
    time.sleep(1)
    print("you assume to be a parachute and its manual is probably Soviet surplus as the cover is")
    time.sleep(1)
    print("written in an alphabet you don’t recognise.")
    time.sleep(1)
    print("Do you:")
    time.sleep(1)
    print("")
    time.sleep(1)
    print("[A] drop the leaflet to the floor and decide to wing it (literally)")
    print("")
    time.sleep(1)
    print("OR")
    time.sleep(1)
    print("")
    print("[B] open the leaflet to see if there’s anything you can understand")
    userChoiceEncoded1 = aOrB()
    # option a choice 1
    if (userChoiceEncoded1 == 'a'):
        print("As you’re free falling you start to panic, maybe you should have asked someone or glanced at the booklets content.")
        time.sleep(1)
        print("A few seconds after jumping out of the plane you pull what you assume to be the rip cord.")
        time.sleep(2)
        print("Nothing happens.")
        time.sleep(1)
        print("You tug harder and harder.")
        time.sleep(2)
        print("Is the parachute defunct? Are you pulling the wrong thing? Panic begins to override your consciousness.")
        time.sleep(1)
        print("A few more seconds go by in a blur and the ominous darkness of the land below rapidly approaches.")
        time.sleep(1)
        print("You hadn’t realised how low you were actually flying. You thrash to look around you and cannot see any of the smugglers.")
        time.sleep(1)
        print("You think you hear yelling but the wind is rushing by so quickly you can’t be sure.")
        time.sleep(1)
        print("As you hit the ground, everything turns to black.")
        time.sleep(2)
        print("Oops, doesn’t look like that went well for you "+userName)
        print("Do you want to try again?")
        userYesOrNo=yesOrNo()
        if(userYesOrNo == 'n'):
            time.sleep(1)
            print("GAME OVER")
            time.sleep(1)
            sys.exit
        elif(userYesOrNo == 'y'):
            encodedKnowledge()
        # option B choice 1
    elif(userChoiceEncoded1 == 'b'):
        print("You quickly flick open the leaflet and are relieved to see diagram pictures of house to use the parachute.")
        time.sleep(1)
        print("You quickly realise that what you had assumed to be the rip cord was")
        time.sleep(1)
        print(
            "merely a tightening mechanism to keep the parachute firmly on your back.")
        time.sleep(1)
        print("The actual rip cord is on the bottom of the backpack. You look up to see the smugglers doing the same.")
        time.sleep(1)
        print("Looks like none of them have used these before either.")
        time.sleep(1)
        print(
            "You put the backpack on and continue to look at the pictograms. There are images of")
        time.sleep(1)
        print("an analogue clock dial that show you should wait for 5 seconds before pulling the cord. You check ")
        time.sleep(1)
        print("that you can reach the cord and focus on remembering to count 5 ‘Mississippis’ before pulling.")
        time.sleep(1)
        print(
            "You exit the plane and let out a little yelp and then begin the harrowing count to 5.")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("5")
        print(
            "Once you’ve thought the final Mississippi you reach behind you and tug at the rip cord.")
        time.sleep(1)
        print(
            "The immediate sense of deceleration hauls you back from your previously rapid descent. ")
        time.sleep(1)
        print("You look around you to see the majority of the crew doing the same at varying degrees of proximity to you.")
        time.sleep(2)
        print(userName + "do you want to understand how the theory of encoded knowledge worked in this scenario?")
        userChoiceEncoded2=yesOrNo()
        if (userChoiceEncoded2 == 'y'):
            print(
                "In the scenario the use of pictograms exemplified encoded knowledge as by")
            print("using images of people and the related tangible items there was no need for domain expertise in order to understand.")
            print("This is particularly true of the time delay provided. As analogue clocks are almost universally understood this information was presented")
            print(
                "in a was that was more practical than if a subject specific metric, like altitude had been used.")
            print("This form of knowledge transfer is regularly employed by traditional airlines as it allows for speakers of different")
            print(
                "languages to understand what is expected of them during the flight and emergencies.")
            time.sleep(2)
            print(
                "Encoded knowledge is focused on this transference through symbols and signs and acts as a format")
            print("to convey other information easily. Foundational to this is this idea of collective understanding as if the symbols")
            print("are specific to a field of study or group of people then they have limited ability to provide a vehicle through which to transfer knowledge.")
            print(userName+"are you ready to look at encultured knowledge?")
            yesOrNo2=yesOrNo()
            if(yesOrNo2 == 'y'):
                enculturedKnowledge()
            else:
                print("Your here to learn buddy.")
                enculturedKnowledge()
# embodiedKnowledge story


def enculturedKnowledge():
    print("I currently know nothing about this.")
# the end
def theEnd():
    print("TBC")


# start of the program is called
start()
