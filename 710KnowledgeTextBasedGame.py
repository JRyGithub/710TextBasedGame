import time
import sys

# globals
userName = ""
directions = ['left', 'right', 'forward', 'back']
noOrYes = ['y', 'n']
encodedOrEnculturedList = ['encoded', 'encultured']
hadBeenToEncoded = ""
hadBeenToEncultured = ""


# start of the game get user name and their intial knowledge
def start():
    global userName
    print("Enter your name")
    userName = input()
    time.sleep(2)
    print("")
    print(userName)
    print("Welcome to Learning about Knowledge")
    time.sleep(2)
    print("An understanding of Frank Blacker’s perspective")
    time.sleep(2)
    print("Brought to you by Josh Ryland and Quillan Aherne")
    time.sleep(2)
    print("Do you wish to proceed? [Y/N]")
    userYesOrNo = yesOrNo()
    if (userYesOrNo.lower() == 'y'):
        print("Wonderful!")
        time.sleep(2)
        print("As Blacker outlines there are many approaches to understanding knowledge within an organisational setting.")
        time.sleep(2)
        print("Today " + userName +
              ", you are going to be exploring two of these: encultured knowledge and encoded knowledge.")
        time.sleep(2)
        print("The format you will be interacting with reflects the themes you are going to explore.")
        time.sleep(2)
        print("With the decontextual nature of the code itself mirroring encoded knowledge")
        print("And the style of 90’s computing providing cultural nuance to the information about to be displayed.")
        time.sleep(2)
        print("So, where you do you want to start?")
        time.sleep(2)
        print("[encoded/encultured]")
        encodedOrEncultured = ""
        while encodedOrEncultured not in encodedOrEnculturedList:
            encodedOrEncultured = input()
            if (encodedOrEncultured.lower() == 'encoded'):
                encodedKnowledge()
            elif (encodedOrEncultured.lower() == 'encultured'):
                enculturedKnowledge()
            else:
                time.sleep(3)
                print("That was never a option.")
    elif (userYesOrNo.lower() == 'n'):
        time.sleep(3)
        print("Umm… "+userName+" you seem to have missed the point.")
        time.sleep(2)
        print("Please don’t get trapped in an infinite loop.")
        time.sleep(2)
        print("Would you like to learn about knowledge?")
        theySaidNo = ""
        while theySaidNo != 'y':
            theySaidNo = yesOrNo()
            time.sleep(3)
            print("That was never a option.")
        print("So, where you do you want to start?")
        time.sleep(2)
        print("[encoded/encultured]")
        encodedOrEncultured = ""
        while encodedOrEncultured not in encodedOrEnculturedList:
            encodedOrEncultured = input()
            if (encodedOrEncultured.lower() == 'encoded'):
                encodedKnowledge()
            elif (encodedOrEncultured.lower() == 'encultured'):
                enculturedKnowledge()
            else:
                time.sleep(3)
                print("That was never a option.")

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
    global hadBeenToEncoded
    hadBeenToEncoded = "y"
    time.sleep(3)
    print(userName+" you are on a small prop plane flying over the Florida Everglades when you hear the engine on one of the wings sputter and stall.")
    time.sleep(3)
    print("You don’t need the frantic yelling of the pilot to alert you that there is a problem.")
    time.sleep(3)
    print("One of the Colombian smugglers hands you a backpack and a small leaflet, not being able to speak Spanish isn’t much of a burden right now as what")
    time.sleep(3)
    print("you assume to be a parachute and its manual is probably Soviet surplus as the cover is written in an alphabet you don’t recognise.")
    time.sleep(3)
    print("Do you:")
    time.sleep(3)
    print("")
    time.sleep(3)
    print("[A] drop the leaflet to the floor and decide to wing it (literally)")
    print("")
    time.sleep(3)
    print("OR")
    time.sleep(3)
    print("")
    print("[B] open the leaflet to see if there’s anything you can understand")
    userChoiceEncoded3 = aOrB()
    # option a choice 3
    if (userChoiceEncoded3 == 'a'):
        print("As you’re free falling you start to panic, maybe you should have asked someone or glanced at the booklets content.")
        time.sleep(3)
        print("A few seconds after jumping out of the plane you pull what you assume to be the rip cord.")
        time.sleep(2)
        print("Nothing happens.")
        time.sleep(3)
        print("You tug harder and harder.")
        time.sleep(2)
        print("Is the parachute defunct? Are you pulling the wrong thing? Panic begins to override your consciousness.")
        time.sleep(3)
        print("A few more seconds go by in a blur and the ominous darkness of the land below rapidly approaches.")
        time.sleep(3)
        print("You hadn’t realised how low you were actually flying. You thrash to look around you and cannot see any of the smugglers.")
        time.sleep(3)
        print("You think you hear yelling but the wind is rushing by so quickly you can’t be sure.")
        time.sleep(3)
        print("As you hit the ground, everything turns to black.")
        time.sleep(2)
        print("Oops, doesn’t look like that went well for you "+userName)
        print("Do you want to try again?")
        userYesOrNo=yesOrNo()
        if(userYesOrNo == 'n'):
            time.sleep(3)
            print("GAME OVER")
            time.sleep(3)
            sys.exit
        elif(userYesOrNo == 'y'):
            encodedKnowledge()
        # option B choice 3
    elif(userChoiceEncoded3 == 'b'):
        print("You quickly flick open the leaflet and are relieved to see diagram pictures of house to use the parachute.")
        time.sleep(3)
        print("You realise that what you had assumed to be the rip cord..")
        time.sleep(3)
        print(
            "Was merely a tightening mechanism to keep the parachute firmly on your back.")
        time.sleep(3)
        print("The actual rip cord is on the bottom of the backpack. You look up to see the smugglers doing the same.")
        time.sleep(3)
        print("Looks like none of them have used these before either.")
        time.sleep(3)
        print(
            "You put the backpack on and continue to look at the pictograms. There are images of")
        time.sleep(3)
        print("an analogue clock dial that show you should wait for 5 seconds before pulling the cord. You check ")
        time.sleep(3)
        print("that you can reach the cord and focus on remembering to count 5 ‘Mississippis’ before pulling.")
        time.sleep(3)
        print(
            "You exit the plane and let out a little yelp and then begin the harrowing count to 5.")
        time.sleep(3)
        print("3")
        time.sleep(3)
        print("2")
        time.sleep(3)
        print("3")
        time.sleep(3)
        print("4")
        time.sleep(3)
        print("5")
        print(
            "Once you’ve thought the final Mississippi you reach behind you and tug at the rip cord.")
        time.sleep(3)
        print(
            "The immediate sense of deceleration hauls you back from your previously rapid descent. ")
        time.sleep(3)
        print("You look around you to see the majority of the crew doing the same at varying degrees of proximity to you.")
        time.sleep(2)
        print(userName + " do you want to understand how the theory of encoded knowledge worked in this scenario?")
        userChoiceEncoded2=yesOrNo()
        if (userChoiceEncoded2 == 'y'):
            print(
                "In the scenario the use of pictograms exemplified encoded knowledge as by")
            time.sleep(3)
            print("using images of people and the related tangible items there was no need for domain expertise in order to understand.")
            time.sleep(3)
            print("This is particularly true of the time delay provided. As analogue clocks are almost universally understood this information was presented")
            time.sleep(2)
            print(
                "In a way that was more practical than if a subject specific metric, like altitude had been used.")
            time.sleep(3)
            print("This form of knowledge transfer is regularly employed by traditional airlines as it allows for speakers of different")
            time.sleep(3)
            print(
                "Languages to understand what is expected of them during the flight and emergencies.")
            time.sleep(2)
            print(
                "Encoded knowledge is focused on this transference through symbols and signs and acts as a format")
            time.sleep(3)
            print("To convey other information easily. Foundational to this is this idea of collective understanding as if the symbols")
            time.sleep(3)
            print("Are specific to a field of study or group of people then they have limited ability to provide a vehicle through which to transfer knowledge.")
            time.sleep(3)
            if (hadBeenToEncultured == ''):
                print(userName+" are you ready to look at encultured knowledge?")
                yesOrNo2=yesOrNo()
                if(yesOrNo2 == 'y'):
                    time.sleep(3)
                    enculturedKnowledge()
                else:
                    time.sleep(3)
                    print("Your here to learn buddy.")
                    enculturedKnowledge()
            else:
                theEnd()
                
        else:
            time.sleep(3)
            print("Oh... well. Next up is Encultured Knowledge")
            time.sleep(3) 
            hadBeenToOtherKnowledgeType == "y"
            enculturedKnowledge()
#encultured knowledge story
def enculturedKnowledge():
    global hadBeenToEncultured
    hadBeenToEncultured = 'y'
    print(userName+" it is your first day as a surgical nurse at a new hospital and you are rostered to assist in a common surgery.")
    time.sleep(3)
    print("You have performed this surgery before at your previous job.")
    time.sleep(3) 
    print("When you enter the Operation Room and look at the set up while waiting for the patient and surgeon to enter.")
    time.sleep(3)
    print("As another nurse enters to set up you watched how they laid out the surgical instruments.")
    time.sleep(3)
    print("The lay out the instruments in a different order from what you are used to,")
    time.sleep(3)
    print("in this instance it doesn’t matter as you are not directly assisting, but you worry about when you have to take the lead in a future surgery.")
    time.sleep(3)
    print("")
    time.sleep(3)
    print("In your second surgery of the day, you are assisting a different set of nurses and doctors.")
    time.sleep(3)
    print("Again you watch the assisting nurse lay out the surgical instruments, and again it is different from what you are used to,")
    time.sleep(3)
    print("But more so, its different from last time. You begin to worry…")
    time.sleep(3)
    print("What do you do?")
    print("")
    time.sleep(3)
    print("Talk to you charge nurse about the tray layouts? [A]")
    print("")
    time.sleep(3)
    print("Or")
    print("")
    time.sleep(3)
    print("Ignore the layout and just ‘go with the flow’ [B]")
    enculturedKnowledgeFirstOption = aOrB()
    if (enculturedKnowledgeFirstOption == 'a'):
        print("At the end of your first shift your charge nurse catches up with you to see how you found your first day.")
        time.sleep(3)
        print("The first thing you ask is about the changing instrument layout. They nod in understanding and say")
        time.sleep(3)
        print("")
        print("Yeah, each surgeon and most assisting nurses have their own way of setting things up that makes sense for them. You’ll learn them as you go, just chat to the other nurses and they will help you figure them out.")
        time.sleep(3)
        print("")
        print("But what if the current layout is inefficient?” you ask.")
        time.sleep(3)
        print("")
        print("Then change it! Most people will be happy to try something new. And the rest, send to me if you must” they reply.")
        time.sleep(3)
        print(userName+ " shall we explore how encultured knowledge worked in this scenario?")
        enculturedResponse3 = yesOrNo()
        if (enculturedResponse3 == 'y' ):
            print("Encultured knowledge is the process of sharing information by engaging with a culture, in this case the hospitals organisational culture.")
            time.sleep(3)
            print("By seeing the routines and rituals performed by your new colleagues you noticed anomalies with previous cultures you had interacted with.")
            time.sleep(3) 
            print("This opened the opportunity to discuss and negotiate understanding, a hallmark of encultured knowledge.") 
            time.sleep(3)
            print("")
            print("A common language and heavy discourse are necessary components of this type of knowledge transfer.")
            time.sleep(3)
            print("As such, this type of knowledge relies on the collective nature of knowledge as it is the combination of individuals within a culture that allows for this form of knowledge transfer.")
            if(hadBeenToEncoded == 'y'):
                theEnd()
            else:
                time.sleep(2)
                print("Time to learn about encoded knowledge.")
                time.sleep(3)
                encodedKnowledge()
        elif(enculturedResponse3 == 'n'):
            time.sleep(3)
            print("Come on now, thats not the spirit of the game.")
            time.sleep(3)
            print("But if you insist")
            time.sleep(3)
            if(hadBeenToEncoded == 'y'):
                print("Game Over")
                sys.exit
            else:
                print("You can at least learn about encoded knowledge.")
                encodedKnowledge()
    elif (enculturedKnowledgeFirstOption == 'b'):
        time.sleep(3)
        print("")
        print("A few days later, you are the assisting nurse in an appendectomy.")
        time.sleep(3)
        print("You set up the instrument tray as you would normally do for this surgery.")
        time.sleep(3) 
        print("You don’t think there’ll be an issue until the surgeon asks for a scalpel and reaches to their left and bumps the instrument tray table.")
        time.sleep(3) 
        print("You had assumed they were right handed and placed everything in the logical order for you, not them.")
        time.sleep(3)
        print("You fumble as you pick up the scalpel, it drops to the floor.")
        time.sleep(3)
        print("The withering look from the surgeon does nothing to stop your hands sweating in your gloves.")
        time.sleep(3)
        print("")
        print("Luckily the other assisting nurse swoops in and presses a fresh scalpel into the surgeon’s hand.")
        time.sleep(3)
        print("You shoot her a grateful look and duck to retrieve the fallen instrument.")
        time.sleep(3)
        print("Retreating to the medical waste disposal unit while the other nurse takes your place next to the surgeon.")
        print("")
        time.sleep(3)
        print("That didn’t go well. Do you want to try again?")
        enculturedKnowledgeSecondOption = yesOrNo()
        if (enculturedKnowledgeSecondOption == 'y'):
            enculturedKnowledge()
        elif (enculturedKnowledgeSecondOption == 'n'):
            time.sleep(3)
            print("Game Over")
            time.sleep(3)
# the end
def theEnd():
    print("Congratulations "+userName+", you’ve successfully navigated both scenarios.") 
    time.sleep(3)
    print("But before we let you go, we have a little quiz for you:")
    time.sleep(3)
    print("")
    question3()
    question2()
    question3()

def question3():
    print("Question 3: Based on the understanding of tacit being knowledge that cannot be codified (written down) do you think that encultured knowledge is inherently tacit?")
    time.sleep(3)
    question3 == yesOrNo()
    if (question3 == 'y'):
        print("That’s correct: as encultured knowledge relies understanding information and cues that are difficult to codify.")
        time.sleep(3)
        print("In the scenario of the operating room nurse, having a knowledge management system outlining how every surgeon and doctor liked their instruments to be set up would not have worked.")
        time.sleep(3)
        print("as these preferences could and would change with different interactions.")
    else:
        print("That’s incorrect: as encultured knowledge relies understanding information and cues that are difficult to codify.")
        time.sleep(3) 
        print("In the scenario of the operating room nurse, having a knowledge management system outlining how every surgeon and doctor liked their instruments to be set up would not have worked")
        time.sleep(3)
        print("As these preferences could and would change with different interactions.")
        time.sleep(3)

def question2():
    print("Question 2: Do you think encoded knowledge and encultured knowledge are?")
    time.sleep(3)
    print("")
    print("[A] More similar to each other")
    print("")
    time.sleep(3)
    print("[B] Or more different from each other")
    question2Result = aOrB()
    time.sleep(3)
    print("It’s a bit of a trick question.")
    time.sleep(3)
    print("There are some ways in which they are similar: both being part of a collective understanding of knowledge.")
    time.sleep(3)
    print("And other ways in which they are different: one relies on context and shared language.")
    time.sleep(3)
    print("While the other is independent of these constraints.")
def question3():
    print("Question 3: An easy one for you, would you consider encoded knowledge to be explicit (able to be written down/codified)?")
    question3Response = yesOrNo()
    if (question3Response == 'y'):
        print("Bingo! The basis of encoded knowledge is the idea that information can be written in symbols in physical or digital means.")
        time.sleep(3)
        print("")
        print("And with that final success we bid you adieu!")
        print("")
        time.sleep(3)
        print("Thank you "+userName+" for playing along!")
        print("We hope you go away from this knowing more about knowledge!")

    else:
        print("In all honesty, a little disappointed you’re on this screen, we expected more from you!")
        print("")
        time.sleep(3)
        print("Ah well, we have come to the end.")
        time.sleep(3)
        print("")
        print("Thank you "+userName+" for playing along!")
        time.sleep(3)
        print("We hope you go away from this knowing more about knowledge!")


# start of the program is called
start()
