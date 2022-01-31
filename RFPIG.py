import os
import math
import json
import textwrap

foodPlaces = json.load(open('foodPlaces.json'))
wrapper = textwrap.TextWrapper(width=80)

divider = "=" * 80
subDivider = "-" * 80

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def filterFoodPlaces(tier, priceRange, isDessert):
    filtered = []

    for x in foodPlaces:
        if x['tier'] == tier and x['price_range'] == priceRange and x['is_dessert'] == isDessert:
            filtered.append(x)
    return filtered

def formattedOutput(filtered):
    for x in filtered:
        desc = wrapper.fill(text=x["desc"])

        print("\n" + divider)
        print("Name: " + x['name'])
        print(subDivider)
        print("Tier: " + x['tier'])
        print("Price Range: " + x['price_range'])
        print("Description: \n" + desc)

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
    Hopefully that Name isn't the only mouthful you'll be experiencing today.""")
    print(divider)

    input("\nPlease press ENTER to continue... ")
    page1()

def page1():
    foodChoice = interrogate(
        "The least you could do is choose what Tier food you want:", 
        ["fast food", "mediocre food", "faaaancy food"])
    
    clear()

    if foodChoice == "1":
        print(formattedOutput(foodPlaces))
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
