from functions import *

while True:
    print("what do u want to do")
    print("1 addition")
    print("2 substraction")
    print("3 multiplication")
    print("4 division")
    print("enter q to exit")

    choice=input("enter your choice ")
    if choice=='q' or choice=='Q':
        break
    num1=float(input("enter number1: "))
    num2=float(input("enter number2: "))

    if choice=='1':
        addition(num1,num2)
    elif choice=='2':
        substraction(num1,num2)
    elif choice=='3':
        multiplication(num1,num2)
    elif choice=='4':
        division(num1,num2)
    else:
        print("invalid choice")
    print("\n")