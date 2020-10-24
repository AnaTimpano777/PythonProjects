#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: March 13, 2020
#Decription: Determines the amount of money raised from different schools based on donation amount and school population

import random #Imports random function

print("This program will determine the money raised from different schools") #Displays to the user what the code is about
print(" ")

rows = 4 #Sets varibales to int
cols = 10
tempData = 0

values = [] #Makes an empty list called values

for i in range(0, rows):n#Loops through the rows
    values.append([]) #Appends to the list
    for j in range(0, cols):#loops through the columns
        values[i].append(tempData) #Sets list values to tempData(0)

choice = int(-1) #Sets variables to int
population = int(-1)
donation = int(-1)

realAmount = int(0)
totalLine = int(0)
totalDonation = int(0)

endMenu = bool(False) #Boolean false

while not endMenu: #gets user to choose which school is fundraising in a while statement
    print("Which school is doing fundraising?")
    print("0 - St.Joseph's")
    print("1 - St.Peter's")
    print("2 - St.Joan of Arc")
    print("3 - Holy Trinity")
    print("4 - St.Thomas Aquinas")
    print("5 - Patrick Fogarty")
    print("6 - St.Theresa's")
    print("7 - St.Dominics")
    print("8 - Jean Vanier")
    print("9 - Exit")

    choice = int(input("Please enter the number that is associated with your school: "))#Inputs number user selects
    print(" ")
    if choice == 9: break #If choice is equal to 9 break code

    print("What is the donation amount?") #Asks user what the donation amount is
    print("0 - 25 cents")
    print("1 - 50 cents")
    print("2 - 1 dollar")
    print("3 - 2 dollars")

    donation = int(input("Please enter the number that is associated with the amount you want to donate: "))#Inputs number user selects for donation amount
    
    print(" ")

    population = int(input("Please enter the school population: "))#Gets input for school population number

    if donation == 0: #If donation equals 0 
        realAmount = 0.25 * population #Multiply 0.25 by the poluation #

    if donation == 1: #If donation equals 1 
        realAmount = 0.50 * population #Multiply 0.50 by the poluation #
    
    if donation == 2: #If donation equals 2 
        realAmount = 1.00 * population #Multiply 1.00 by the poluation #

    if donation == 3: #If donation equals 3 
        realAmount = 2.00 * population #Multiply 2.00 by the poluation #

    values[donation][choice] = realAmount 
    
    totalDonation = 0 #Sets total donation to 0

    print("AMT\t \t SJO\t PET\t JOA\t HTR\t STS\t PFO\t STH\t DOM\t JVA\t TOTAL\t") #Creates formatted table

    print("$0.25\n $0.50\n $1.00\n $2.00\n", end="") #Formats first column $

    for i in range(0, 4): #Loops 4 times
        totalLine = 0 #totalLine is set to 0

        for j in range(0, 9): #Loops nine times in columns to display proper numbers
            totalDonation += values[i][j] 
            totalLine += values[i][j]
            print(values[i][j], end="")
        print(totalLine)
        print(" ")
    print(totalDonation)

#I got the numbers to work but I wasn't able to format the number properly under each column
