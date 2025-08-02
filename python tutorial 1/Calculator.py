from Functions import *

while True:
    print("What do you want to do? ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division.")
    print("4. Multiplication")
    print("press Q to exit")

    choice = input("Enter your choice: ")
    if choice == "q" or choice == "Q":
        break
    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    if choice == "1" :
        addition(num1,num2)
    elif choice == "2" :
        subtraction(num1,num2)
    elif choice == "3" :
        division(num1,num2)
    elif choice == "4" :
        multiplication(num1,num2)
    else :
        print("invalid choice")
    print("\n")

