import os
import math
import json
from re import X
import textwrap
from tkinter.ttk import Style
import random

global tierChoice
global priceRangeChoice
global isDessert

wrapper = textwrap.TextWrapper(width=80)

foodPlaces = json.load(open('foodPlaces.json'))
divider = "=" * 80
subDivider = "-" * 80

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def niceOutput(x):
    
    desc = wrapper.fill(text=x["desc"])
    print("\n" + divider)
    print("Name: " + x["name"])
    print(subDivider)
    print("Tier: " + x["tier"])
    print("Price range: " + x["priceRange"])
    print("Description: " + desc + "\n")

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

def filterFoodPlaces(tier, priceRange, isDessert):
    filtered = []
    
    for x in foodPlaces:
        if x["tier"] == tier and x["priceRange"] == priceRange and x["isDessert"] == isDessert:
            filtered.append(x)
    
    return filtered

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
    
    global tierChoice
    global priceRangeChoice
    global isDessert

    foodChoice = interrogate(
        "The least you could do is choose what tier food you want:", 
        ["fast food", "mediocre food", "faaaancy food"])
    
    clear()
    if foodChoice == "1":
        tierChoice = "Fast food"
        page2()
    elif foodChoice == "2":
        tierChoice = "Mediocre food"
        page2()
    elif foodChoice == "3":
        tierChoice = "Fancy food"
        page2()
    else:
        clear()
        print("\nYou must have misunderstood, excuse you,")
        input("\nPlease press ENTER to continue... ")
        page1()

def page2():
    
    global tierChoice
    global priceRangeChoice
    global isDessert

    foodChoice = interrogate(
        "How willing are you to split the bill?", 
        ["Very willing", "Kinda...", "Im stingy"])
    
    clear()
    if foodChoice == "1":
        priceRangeChoice = "High"
        page3()
    elif foodChoice == "2":
        priceRangeChoice = "Mid"
        page3()
    elif foodChoice == "3":
        priceRangeChoice = "Low"
        page3()
    else:
        clear()
        print("\nYou must have misunderstood, excuse you,")
        input("\nPlease press ENTER to continue... ")
        page2()

def page3():
    
    global tierChoice
    global priceRangeChoice
    global isDessert

    foodChoice = interrogate(
        "How willing are you to split the bill?", 
        ["Sweet", "Salty"])
    
    clear()
    if foodChoice == "1":
        isDessert = True
        page4()
    elif foodChoice == "2":
        isDessert = False
        page4()

    else:
        clear()
        print("\nYou must have misunderstood, excuse you,")
        input("\nPlease press ENTER to continue... ")
        page3()

def page4():
    finalChoice = filterFoodPlaces(tierChoice, priceRangeChoice, isDessert)
    size = len(finalChoice)
    randomPos = random.randint(0, size) - 1

    
    print("\nYour choice has been made: Bon Appetite!")

    niceOutput(finalChoice[randomPos])

home()
