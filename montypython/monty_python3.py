#!/usr/bin/python3
round = 0
answer = " "

while round < 3 and answer not in [ "Brian", "Shrubbery"]:
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ').capitalize().strip()
    if answer == "Brian": # logic to check if user gave correct answer
        print("Correct!")
        break
    elif answer == "Shrubbery":
        print("You gave the super secret answer")
        break
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
        break
    else:                 # if answer was wrong
        print("Sorry. Try again!")

