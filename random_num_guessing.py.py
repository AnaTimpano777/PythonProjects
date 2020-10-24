#Name:Ana Timpano
#Course Code: ISC3UE
#Program Description: Random number guessing game!  

import random

wins = 0
losses = 0

print("Welcome to the random number guessing game!") #Intro to game

print(" ") #Space

rounds = int(input("Enter the amount of rounds you want to play: ")) #Asks user to enter the amount of rounds they want to play, sets it to the variable

for i in range(0,rounds): #Loop for the amount of rounds the user inputed, determines how long the loop repeats
    
    Range = int(input("Enter the number you want to set the range to from 1: ")) #Asks user to enter the range from 1 to guess between, sets it to the variable

    randomNum = random.randint(1,Range) #The computer generates a random number from 1 to the inputed range

    if Range <= 10:                                         #If range is less than or equal to 10
        RemainGuesses = 3                                   #Sets  the variable remaining guesses to 3
        print("You have", RemainGuesses, "guesses left")    #Prints the amount of guesses you have left

    elif Range <= 30 and Range > 10:                        #If range is less than or equal to 30 and greater than 10
        RemainGuesses = 5                                   #Sets  the variable remaining guesses to 5
        print("You have", RemainGuesses, "guesses left")    #Prints the amount of guesses you have left

    elif Range <= 50 and Range > 30:                        #If range is less than or equal to 50 and greater than 30
        RemainGuesses = 7                                   #Sets  the variable remaining guesses to 7
        print("You have", RemainGuesses, "guesses left")    #Prints the amount of guesses you have left

    elif Range <= 70 and Range > 50:                        #If range is less than or equal to 70 and greater than 50
        RemainGuesses = 8                                   #Sets  the variable remaining guesses to 8
        print("You have", RemainGuesses, "guesses left")    #Prints the amount of guesses you have left

    elif Range <= 100 and Range > 70:                       #If range is less than or equal to 100 and greater than 70
        RemainGuesses = 10                                  #Sets  the variable remaining guesses to 10
        print("You have", RemainGuesses, "guesses left")    #Prints the amount of guesses you have left

    elif Range > 100:                                       #If range is greater than 100
        RemainGuesses = 15                                  #Sets  the variable remaining guesses to 15
        print("You have", RemainGuesses, "guesses left")    #Prints the amount of guesses you have left

    print(" ")

    for i in range(1,Range): #Loop for the 1 to range, determines how many times the loop repeats
        
        guess = int(input("Enter your guess, your guess can only be one number: ")) #Asks the user to enter their guess, sets guess to variable

        if guess > Range:                                                               #If the guess is greater than the range
            print("Your guess is out of range, try again!")                             #Tells the user that their guess is out of range and to try again
            guess = int(input("Enter your guess, your guess can only be one number: ")) #Allows user to input another guess
            print(" ")
            
        elif guess > randomNum:                             #If the guess is greater than the random number
            print("Too High!")                              #Prints that your guess is too high
            RemainGuesses=RemainGuesses-1                   #Subtracts your remaining guesses by 1
            print("You have",RemainGuesses," guess left")   #Tells the user how many guess they have left
            print(" ")
            
        elif guess < randomNum:                             #If the guess is less than the random number
            print("Too Low!")                               #Prints that your guess is too low
            RemainGuesses=RemainGuesses-1                   #Subtracts your remaining guesses by 1
            print("You have",RemainGuesses," guess left")   #Tells the user how many guesses they have left
            print(" ")
            
        elif guess == randomNum:     #If the guess is equal to the random number
            print("YAY! You won!")   #Prints that you have won
            wins = wins + 1          #Increases wins by 1
            print(" ")
            break

        if RemainGuesses == 0:                              #If remaining guesses is equal to 0
            print("Sorry you ran out of guesses!GAME OVER") #Prints that you ran out of guesses and the game is over
            losses = losses + 1                             #Increases losses by 1
            print(" ")
            break

    print("Wins: ",wins)     #Prints the amount of wins you have
    print("Losses: ",losses) #Prints the amount of losses you have



