import os

fastL = ["mcD","kfc","pepes", "gdk"]

midL = ["franzos", "nandos", "pho"]

fancyL = ["saharaG", "gokyuzu", "hakkasan"]

dessertL = ["creams", "amorino", "bubbleT"]

def home():
    os.system("cls")

    print("""
 ___         ___        ___         ___          ___ 
| _ \       | __|      | _ \       |_ _|        / __|
|   /  _    | _|       |  _/  _     | |   _    | (_ |
|_|_\ (_)   |_|        |_|   (_)   |___| (_)    \___|
© Created by ShmuelIndustries

Welcome to the Random Food Place Idea Generator,
Hopefully that name isn't the only mouthful you'll be experiencing today.
    """)

    input("Please press ENTER to continue... ")
    page1()

def page1():
    os.system("cls")

    print("""

The least you could do is choose what tier food you want:
\nPress 1 for fast food
\nPress 2 for mediocre food
\nPress 3 for faaaancy food
        """)
    foodChoice = input("Please type in your choice here -> ")

    if foodChoice == "1":
        fastF()

    elif foodChoice == "2":
        midF()

    elif foodChoice == "3":
        fancyF()
    
    else:
        os.system("cls")
        print("\nYou must have misunderstood, excuse you,")
        input("\nPlease press ENTER to continue... ")
        page1()

home()
