#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 14, 2020
#Decription: This program mimics a combination lock and has a lock guessing game

import random #Import random
from comboLock import ComboLock #From file comboLock.py import class ComboLock

#creating combination lock from user input

print("Creating combination lock") #Outputs user to create combination lock
num1 = int(input("Enter the first number of the combination: ")) #Gets user input for 3 number combinations
num2 = int(input("Enter the second number of the combination: "))
num3 = int(input("Enter the third number of the combination: "))

c11 = ComboLock(num1, num2, num3) #Instantiates ComboLock with the 3 user input values

print(" ")
print("Your lock has been created") #Outputs that lock has been created
num1 = int(input("Please guess the first number of the lock: ")) #Gets user to guess their lock numbers in inputs
num2 = int(input("Please guess the second number of the lock: "))
num3 = int(input("Please guess the third number of the lock: "))

print(" ")
if c11.check_combo(num1, num2, num3): #Calls check_combo to check if the input numbers are equal to the combination numbers, if it is then...
    print("\nCongratulations! You got the combination right!\nThe lock is now open") #Output congratulation message

else: #Else
    print("\nYour guess was incorrect. The lock is still locked.") #Outputs incorrect message, lock is still locked
    
c12 = ComboLock(random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)) # creating a combination lock with random values between 1 and 3

print(" ")
print("A new random lock has been created") #Outputs that a new lock has been created
print("You have three guesses to open the lock!") #User has 3 guesses to open the lock
print(" ")
guess = 0 #Sets variable guess to 0

while guess < 3: #While var guess is less than 3 keep loop running
    num1 = int(input("Please guess the first number of the lock (1-3): ")) #Gets user to guess the lock combination numbers
    num2 = int(input("Please guess the second number of the lock (1-3): "))
    num3 = int(input("Please guess the third number of the lock (1-3): "))
    print(" ")

    if c12.check_combo(num1, num2, num3): #Calls check_combo to check if the input numbers are equal to the combination numbers, if it is then...
        print("Congratulations! You got the combination right!") #Output congratulation message
        print("The lock is now open!")
        guess = 4 #Sets var guess to 4 to stop loop
        
    else: #Else
        guess += 1 #Increment var guess by 1
        print("Your guess was incorrect. The lock is still locked") #Output guess was inncorrect, lock is still locked
        print("You have", 3 - guess, "guesses left") #Outputs number of guesses left

if guess == 3: #if var guess is equal to 3
    print(" ")
    print("Sorry you are out of guesses. You did not open the lock") #Outputs to user that they are out of guesses and that they did not open the lock
    print("The correct combination was:") #Displays the correct combination to the user
    print(c12)
    
