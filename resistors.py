#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: March 3, 2020
#Decription: Determines the values of the resistors colour code (ohms)

import random #Imports random function

print("This program will determine the value of the resistors based on the colour code") #Displays to the user what the code is about
print(" ")

colours = [] #Creates an append list of all of the colours in order
colours.append("BLACK")
colours.append("BROWN")
colours.append("RED")
colours.append("ORANGE")
colours.append("YELLOW")
colours.append("GREEN")
colours.append("BLUE")
colours.append("VIOLET")
colours.append("GREY")
colours.append("WHITE")

res1 = 0.0 #Sets value of the first colour of the resistor to 0
res2 = 0.0 #Sets value of the first colour of the resistor to 0
res3 = 0.0 #Sets value of the first colour of the resistor to 0

resistorColoursInput = str(input("Please enter the resistors colour code (Seperate each colour by hyphens eg. red-orange-black): ")) #Asks user to enter a phrase

result = resistorColoursInput.upper() #Sets users input to all lowercase characters

resistorColoursList = result.split("-") #Breaks up the colours into seperate strings
print(" ")

for i in range(len(colours)): #Loops through all of the colours
 
    if resistorColoursList[0] == colours[i]: #If the first colour is equal to the colour in the list, set the index number of the colour to the variable res1
        res1 = i
    if resistorColoursList[1] == colours[i]: #If the first colour is equal to the colour in the list, set the index number of the colour to the variable res2
        res2 = i
    if resistorColoursList[2] == colours[i]: #If the first colour is equal to the colour in the list, set the index number of the colour to the variable res3
        res3 = i
        
num1 = int(str(res1) + str(res2)) #Combines the first two numbers into one
resValue = num1*(10**(res3)) #Ohms calculation

print("You entered: ", resistorColoursInput) #Repeats what colour pattern the user entered
print("The value of the resistor is: ", resValue,"ohms") #Displays the value of the resistor in ohms

