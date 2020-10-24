#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: February 6, 2020
#Decription: Determines the area of a traingle using either Heron's formula or triginometry

import math

def start(): #defines all code as start()

    print("Area of Triangle") #title
    print(" ") #space
    choice = float(input("Enter 1 if you want to use Heron's formula or 2 if you want to use triginometry to find the triangle's area: ")) #Aks user to choose Heron's formula or Trig
    print(" ") #space

    if choice == 1: #If user inputs 1

        print("You are using Heron's formula") #Tells the user that they choose Heron's Formula
        print(" ") #space
        
        a = float(input("What is the length of side 'a'? : ")) #Asks user what the length of side a is 
        b = float(input("What is the length of side 'b'? : ")) #Asks user what the length of side b is 
        c = float(input("What is the length of side 'c'? : ")) #Asks user what the length of side c is

        s = (a + b + c) / 2 #Calculates semi-perimeter of triangle

        area = math.sqrt(s*(s-a)*(s-b)*(s-c)) #Calculates area

        print(" ") #space
        print("The area of the triangle with side lengths", a,",", b,", and", c, "is: ", area) #Displays the area to the user

        print(" ")#space
        playAgain = str(input("Do you want to calculate the area of a new triangle? (Enter a [Y] for yes or [N] for no):")).lower()#Asks user if they want to restart

        if playAgain == "n":                #If the user does not want to restart the game (Equals no)
            print("Ok, have a good day!") #Prints have a good day and ends code
        else:                               #Else (If user wants to enter a new number)
            print(" ") #space
            start()                         #Goes back to the start of the code
        

    if choice == 2: #If user inputs 2

        print("You are using Triginometry") #Tells the user that they chose triginometry
        print(" ") #space

        a = float(input("What is the length of side 'a'? : ")) #Asks user what the length of side a is
        b = float(input("What is the length of side 'b'? : ")) #Asks user what the length of side b is
        C = float(input("What is the measurement of angle 'C' in degrees? : ")) #Asks user what the angle of C is

        area = (a * b * math.sin(C * math.pi / 180)) / 2 #Calculates area

        print(" ") #space
        print("The area of the triangle with side lengths", a,",", b,", and angle", C, "is: ", area) #Displays the area to the user

        print(" ")#space
        playAgain = str(input("Do you want to calculate the area of a new triangle? (Enter a [Y] for yes or [N] for no):")).lower()#Asks user if they want to restart

        if playAgain == "n":                #If the user does not want to restart the game (Equals no)
            print("Ok, have a good day!") #Prints have a good day and ends code
        else:                               #Else (If user wants to enter a new number)
            print(" ") #space
            start()                         #Goes back to the start of the code

start()













