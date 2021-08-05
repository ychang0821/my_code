#!/usr/bin/env python3

def calculate(x, y, operation):
    if(operation == "add"):
        print(x + y)
    elif(operation == "subtract"):
        print(x-y)
    elif(operation == "divide"):
        if y != 0:
                print(x / y)
        else:
            print("You can't divide by zero!")
    elif(operation == "multiply"):
            print(x*y)

    else:
        print("use a valid OPTION")

def main():
    while True:
        try:
            x = float(input("Enter in a number: "))
            y= float(input("Enter ANOTHER  number: "))
            break
        except:
            print("Invalid input, try again.")

    operation = ""
    while(operation != "add" and operation != "subtract" and operation != "divide" and operation != "multiply"):
        operation = input("What operation would like to perform? OPTIONS: 'add', 'subtract','divide','multiply': ").lower()

    calculate(x, y, operation)

if __name__ == "__main__":
    main()
