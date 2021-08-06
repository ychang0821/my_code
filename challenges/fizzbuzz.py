#!/usr/bin/env pyhton3

def getnumbers():
    numberlist = []
    with open("numfile.txt", "r") as numfile:
        for row in numfile:
            numberlist.append(int(row))
    return numberlist

def fizzbuzz(numberlist):
    Fizzes = 0 
    Buzzes = 0 
    FizzBuzzes = 0
    for num in numberlist:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            FizzBuzzes += 1
        elif num % 3 == 0:
            print("Fizz")
            Fizzes += 1
        elif num % 5 == 0:
            print("Buzz")
            Buzzes += 1
        else:
            print(num)
    return {"Fizzes": Fizzes, "Buzzes": Buzzes, "FizzBuzzes": FizzBuzzes}
    
def main():
    print(fizzbuzz(getnumbers()))

if __name__ == "__main__":
    main()