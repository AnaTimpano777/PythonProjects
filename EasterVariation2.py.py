#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: February 6, 2020
#Decription: Determines the exact date of Easter Sunday based on the year

import math

def start(): #Defines all code as start()

    print("Easter Date Calendar") #title
    print(" ") #space
    year = int(input("Please enter a year: ")) #Aks user to choose a year
    print(" ") #space

    a = int(year / 100) #Calculations
    b = year % 100
    c = int((3*(a+25)) / 4)
    d = (3*(a+25)) % 4
    q = int((8*(a+11)) / 25)
    f = (5*a+b) % 19
    g = (19*f+c-q) % 30
    h = int((f+11*g) / 319)
    j = int((60*(5-d)+b) / 4)
    k = (60*(5-d)+b) % 4
    n = (2*j-k-g+h) % 7
    month = int((g-h+n+114) / 31)
    p = (g-h+n+114) % 31
    day = int(p+1)

    if month == 3: #Determines the month
        monthStr = "March"

    else:
        monthStr = "April"

    print("Easter will fall on Sunday, ", monthStr," ", day, ", ",year) #Displays Easter Sunday date to user

    print(" ")#space
    playAgain = str(input("Do you want to enter a different year? (Enter a [Y] for yes or [N] for no):")).lower()#Asks user if they want to restart

    if playAgain == "n":                #If the user does not want to restart the game (Equals no)
        print("Ok, have a good day!") #Prints have a good day and ends code
    else:                               #Else (If user wants to enter a new number)
        print(" ") #space
        start()                         #Goes back to the start of the code

start()

