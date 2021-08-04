#!usr/bin/env python3
from data import * 
from colorama import Fore, Back, Style

def introduction():
    print(Fore.GREEN + "\nCan You Waste $1 Million In A Week?\n")
    print("OKAY, HERE'S THE DEAL: You receive a letter from an estate lawyer, who tells you that your distant Uncle Gerald has died. As his only heir, you're entitled to the $100 MILLION DOLLARS he left behind.\n")
    print("However, THERE IS A CATCH: In order to receive your inheritance, you have to spend $1 million dollars in only ONE WEEK, but you can't spend it on anything you get to keep. That means you have to waste every single dollar on temporary fun.\n")
    print("Oh, and one more thing: You won't be shown any of the prices of the things you're buying. Oh, Uncle Gerald, you mischievous scamp.\n")
    print("If you succeed, you'll get $100 million. If you fail, you get nothing (no, not even the money you have left over). Think you can waste a million bucks in just seven days? Let's give it a shot!\n")

def makechoice():
    num = 0

    total_waste = 0
    while num < 7:
        if num == 0:
            day1_response = False
            while day1_response == False:
                user_choice = input("Day 1: CHOOSE A HOTEL SUITE TO STAY IN ALL WEEK: \n 1: Royal Suite at Burj AI Arab\n 2: Royal Suite at Plaza Hotel\n 3: Hilltop Estate at Laucala Resort\n 4: Presidential Suite at Grand Hyatt Martinez Cannes\n 5: Shahil Mahal Suite at Raj Palace\n 6: Royal Villa at Grand Resort Lagonissi\n Your choice(enter number between 1 - 6): ")
                if user_choice.isdigit():
                    int_choice = int(user_choice)
                    if int_choice >= 1 and int_choice <= 6:
                        hotel_cost = hotels.get(int_choice).get("price")
                        total_waste += hotel_cost
                        day1_response = True
            

        elif num == 1:
            day2_response = False
            while day2_response == False:
                user_choice = input("Day 2: CHOOSE A CAR TO RENT FOR THE REST OF THE WEEK: \n 1: Ferrari 458 Italia\n 2: Maserati GranCabrio\n 3: Rolls Royce Phantom\n 4: Maybach 57S\n 5: McLaren MP4-12C\n 6: Lamborghini Gallardo Spyder\n Your choice(enter number between 1 - 6): ")
                if user_choice.isdigit():
                    int_choice = int(user_choice)
                    if int_choice >= 1 and int_choice <= 6:
                        car_cost = cars.get(int_choice).get("price")
                        total_waste += car_cost
                        day2_response = True
            
        elif num == 2:
            day3_response = False
            while day3_response == False:
                user_choice = input("Day 3: CHOOSE A VENUE TO THROW A KICK-ASS PARTY: \n 1: Madision Square Garden, New York\n 2: Little Palm Island, Florida\n 3: The Biltmore Estate, North Carolina\n 4: Pelican Hill, California\n 5: Odescalchi Castle, Italy\n 6: Chateaux Vaux-le-Vicomte, France\n Your choice(enter number between 1 - 6): ")
                if user_choice.isdigit():
                    int_choice = int(user_choice)
                    if int_choice >= 1 and int_choice <= 6:
                        venue_cost = venues.get(int_choice).get("price")
                        total_waste += venue_cost
                        day3_response = True
            
        elif num == 3:
            day4_response = False
            while day4_response == False:
                user_choice = input("Day 4: HIRE A CELEBRITY TO PERFORM A PRIVATE CONCERT: \n 1: Avril Lavigne\n 2: Selena Gomez\n 3: Kendrick Lamar\n 4: Carly Rae Jepsen\n 5: Jason Derulo\n 6: Avicii\n Your choice(enter number between 1 - 6): ")
                if user_choice.isdigit():
                    int_choice = int(user_choice)
                    if int_choice >= 1 and int_choice <= 6:
                        celebrity_cost = celebrities.get(int_choice).get("price")
                        total_waste += celebrity_cost
                        day4_response = True

        elif num == 4:
            day5_response = False
            while day5_response == False:
                user_choice = input("Day 5: CHOOSE A PRICEY RESTAURANT TO TAKE 11 OF YOUR PALS FOR DINNER: \n 1: Sublimotion, Ibiza\n 2: Plaza Athenee, Paris\n 3: Ithaa Undersea Restaurant, Maldives\n 4: Aragawa, Tokyo\n 5: Restaurant Crissier, Switzerland\n 6: Masa, New York City\n Your choice(enter number between 1 - 6): ")
                if user_choice.isdigit():
                    int_choice = int(user_choice)
                    if int_choice >= 1 and int_choice <= 6:
                        restaurant_cost = restaurants.get(int_choice).get("price")
                        total_waste += restaurant_cost
                        day5_response = True

        elif num == 5:
            day6_response = False
            while day6_response == False:
                user_choice = input("Day 6: CHOOSE AN EXPENSIVE BOTTLE OF WINE TO DRINK IN ONE SITTING: \n 1: Chateau Margaux 1er cru classé 1900\n 2: Domaine de la Romanee-Conti 1990\n 3: Chateau Lafite 1865\n 4: Heidsieck 1907\n 5: Chateau Mouton-Rothschild 1945\n 6: Cheval Blanc 1947\n Your choice(enter number between 1 - 6): ")
                if user_choice.isdigit():
                    int_choice = int(user_choice)
                    if int_choice >= 1 and int_choice <= 6:
                        wine_cost = wine.get(int_choice).get("price")
                        total_waste += wine_cost
                        day6_response = True
            
        else:
            day7_response = False
            while day7_response == False:
                user_choice = input("Day 7: FIANLLY, CHOOSE A LUXURY SPA TREATMENT SO YOU CAN RELAX AFTER A HARD WEEK OF SPENDING: \n 1: Evian bath\n 2: Gold facial\n 3: Diamond massage\n 4: Clay body treatment\n 5: Turkish bath\n 6: Fish pedicure\n Your choice(enter number between 1 - 6):")
                if user_choice.isdigit():
                    int_choice = int(user_choice)
                    if int_choice >= 1 and int_choice <= 6:
                        spa_cost = spa.get(int_choice).get("price")
                        total_waste += spa_cost
                        day7_response = True
            
        num += 1

    if total_waste >= 1000000:
        print(f"Congratulation! You wasted ${total_waste} in one week. That means you will be inheriting $100 million from your dead uncle.")
    else :
        print(f"You only wasted ${total_waste} in one week! You tried your best to spend a million bucks without accumulating any assets, but in the end, you didn't quite spend enough. That means you WON'T be inheriting $100 million from your dead uncle after all. But hey, on the bright side, you had one pretty awesome week!")

def main():
    replay = True
    while replay:
        introduction()

        makechoice()

        user_replay = input("DO you want to try again? (Type \"yes\" to try again or type anything else to quit)").lower().strip()

        if user_replay == "yes":
            replay = True
        else:
            replay = False
    print("Thanks for playing! Enjoy everyday of your life!")

if __name__ == "__main__":
    main()
