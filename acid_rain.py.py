#Name: Ana Timpano
#Course Code: ICS3UE
#Program Description: This program determines the risk of fish based on pH levels that the user inputs.

print("Risk of fish based on pH levels")#Title
print(" ")#space
print("Hello, Acid rain is an environmental problem. The unit that measures acidity (the amount of acid) in water and other substances is pH.")#Intro about acid rain
print(" ")#space
pH_Num = float(input("Enter the pH level: "))#User enters their pH level

if pH_Num >= 6.5 and pH_Num <= 7.5: #If pH level is greater than or equal to 6.5 and less than and equal to 7.5, print the following
    print("NEUTRAL - FISH IN STREAMS, RIVERS AND LAKES WILL SURVIVE.")

if pH_Num < 6.5:
    print("TOO ACIDIC - FISH IN STREAMS, RIVERS AND LAKES WILL NOT SURVIVE.") #If pH level is less than 6.5, print the following

if pH_Num > 7.5:
    print("TOO ALKALINE - FISH IN STREAMS, RIVERS AND LAKES WILL NOT SURVIVE.") #If the pH level is greater than 7.5, print the following
