import os
import math

divider = "=" * 80
subDivider = "-" * 80

fastL = ["mcD", "kfc", "pepes", "gdk"]
midL = ["franzos", "nandos", "pho"]
fancyL = ["saharaG", "gokyuzu", "hakkasan"]
dessertL = ["creams", "amorino", "bubbleT"]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def interrogate(punchLine, questions):
    clear()
    choiceCounter = 0

    print(divider)
    print(punchLine)
    print(divider)

    for x in questions:
        choiceCounter = choiceCounter + 1
        print("Press " + str(choiceCounter) + " for " + x)

    print(divider)
    choice = input("Please type in your choice here -> ")
    return choice 

def home():
    clear()

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
    foodChoice = interrogate(
        "The least you could do is choose what tier food you want:", 
        ["fast food", "mediocre food", "faaaancy food"])
    
    clear()
    if foodChoice == "1":
        for x in fastL:
            print(x)
    elif foodChoice == "2":
       for x in midL:
            print(x)
    elif foodChoice == "3":
        for x in midL:
            print(x)
    else:
        clear()
        print("\nYou must have misunderstood, excuse you,")
        input("\nPlease press ENTER to continue... ")
        page1()

home()
