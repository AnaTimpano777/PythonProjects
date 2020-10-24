#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: February 6, 2020
#Decription: Compares the sqaure to the square root of a specified number to determine the rounding error.

import math

def start(): #defines all code as start()

    print("Rounding Error Program") #title
    print(" ") #space
    number = int(input("Enter the number you want to use: ")) #Aks user to enter a number

    root = float(math.sqrt(number)) #Determines the root of the inputed number
    square = float(math.pow(root, 2)) #Determines the square of the root number
    error = abs(square-number) #Deternubes the rounding error

    print(" ") #space
    print("The square of the square = ", square) #Displays the sqaure number to the user

    print(" ") #space
    print("The rounding error of the number you inputed is: ", float(error)) #Displays the rounding error to the user

    print(" ")#space
    playAgain = str(input("Do you want to enter a new number? (Enter a [Y] for yes or [N] for no):")).lower()#Asks user if they want to restart the game

    if playAgain == "n":                #If the user does not want to restart the game (Equals no)
        print("Ok, have a good day!") #Prints have a good day and ends the code
    else:                               #Else (If user wants to enter a new number)
        print(" ") #space
        start()                         #Goes back to the start of the code

start()


