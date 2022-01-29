import os
import math

divider = "=" * 80
subDivider = "-" * 80

fastL = ["mcD","kfc","pepes", "gdk"]
midL = ["franzos", "nandos", "pho"]
fancyL = ["saharaG", "gokyuzu", "hakkasan"]
dessertL = ["creams", "amorino", "bubbleT"]

def question(punchLine, questions):
    os.system("clear")
    choiceCounter = 0

    print(divider)
    print(punchLine)
    print(divider)

    for x in questions:
        choiceCounter = choiceCounter + 1
        print("Press " + str(choiceCounter) + " for " + x)

    print(divider)
    choice = input("Please type in your choice here ->")
    return choice 

def home():
    os.system("clear")

    print("""
 ___         ___        ___         ___          ___ 
| _ \       | __|      | _ \       |_ _|        / __|
|   /  _    | _|       |  _/  _     | |   _    | (_ |
|_|_\ (_)   |_|        |_|   (_)   |___| (_)    \___|
© Created by ShmuelIndustries
    
    """)
    
    print(divider)
    print("""Welcome to the Random Food Place Idea Generator,
    Hopefully that name isn't the only mouthful you'll be experiencing today.""")
    print(divider)

    input("\nPlease press ENTER to continue... ")
    page1()

def page1():
    os.system("clear")

    # print(subDivider)
    # print("""The least you could do is choose what tier food you want:
    # \nPress 1 for fast food
    # \nPress 2 for mediocre food
    # \nPress 3 for faaaancy food""")
    # print(subDivider)

    # foodChoice = input("\nPlease type in your choice here -> ")

    question("The least you could do is choose what tier food you want:", ["test", "test2"])

    if foodChoice == "1":
        fastF()

    elif foodChoice == "2":
        midF()

    elif foodChoice == "3":
        fancyF()
    
    else:
        os.system("clear")
        print("\nYou must have misunderstood, excuse you,")
        input("\nPlease press ENTER to continue... ")
        page1()

home()
