#Name: Ana Timpano
#Course Code: ISC3UE
#Program Description: The user chooses which game they want to play (Rock paper scissors, random number guessing game, or blackjack)

import random
import time

def main():  #Defines all code under this as main()
    print("Welcome!") #Tells the user welcome
    game = int(input("Please enter the number assosiated with which game you want to play (Rock-Paper-Scissors = 1 , Random number guessing game = 2 , Blackjack = 3): ")) #Asks user to pick a game
    print(" ")

    if game > 3 or game == 0:                   #If game is greater than 3 or game is equal to 0
        print("Please enter only 1, 2, or 3")   #Tells user to only pick numbers 1 2 or 3
        main()                                  #Takes user back to the start of the code






        

    if game == 1:       #If game is equal to 1 (User picks rock paper scissors)(plays rock paper scissors)

        Rock = 1
        Paper = 2
        Scissors = 3

        wins = 0
        ties = 0
        loss = 0

        print("Welcome to Rock-Paper-Scissors")#intro
        print(" ")
        print("Rock beats Scissors")#Rules
        print("Scissors beats Paper")
        print("Paper beats Rock")
        print(" ")

        

        print(" ")
        
        playAgain = "y"

        while playAgain == "y": #While play again is equal to yes - continue the loop

            choice = int(input("Pick Rock, Paper, or Scissors. Type the number associated with the option. Rock = 1 Paper = 2 and Scissors = 3 : ")) #The user chooses Rock, Paper, or Scissors

            print(" ") #Print space

            if (choice == 1):
                print("Your option is: Rock") #Displays on the screen what option you choose: Rock
                
            elif (choice == 2):
                print("Your option is: Paper")#Displays on the screen what option you choose: Paper
                
            elif (choice == 3):
                print("Your option is: Scissors")#Displays on the screen what option you choose: Scissors
                
            else:
                print("You can only type in 1, 2, or 3. Try again!")
                choice = int(input("Pick Rock, Paper, or Scissors. Type the number associated with the option. Rock = 1 Paper = 2 and Scissors = 3 : ")) #The user chooses Rock, Paper, or Scissors

            opponent = random.randint(1,3) #The opponent randomly chooses 1, 2 or 3 (Rock, Paper, or Scissors)

            if (opponent == 1):
                print("Your opponent chose: Rock") #Displays on the screen what opponent choose: Rock
                
            elif (opponent == 2):
                print("Your opponent chose: Paper")#Displays on the screen what opponent choose: Paper
                
            elif (opponent == 3):
                print("Your opponent chose: Scissors")#Displays on the screen what opponent choose: Scissors

            print (" ") #Print space


            if (choice == opponent):
                print("You tied") #If your choice is the same / equal to the opponents choice it prints that you tied
                ties = ties+1 #Adds 1 point to ties
                
            elif (choice == 1 and opponent == 2): #If your choice is rock and the opponents choice is paper it prints that you lost
                print("You lost")
                loss = loss+1 #Adds 1 point to losses
                
            elif (choice == 1 and opponent == 3): #If your choice is rock and the opponents choice is scissors it prints that you won
                print("You won!")
                wins = wins+1 #Adds 1 point to wins
                
            elif (choice == 2 and opponent == 1): #If your choice is paper and the opponents choice is rock it prints that you won
                print("You won!")
                wins = wins+1 #Adds 1 point to wins
                
            elif (choice == 3 and opponent == 1): #If your choice is scissors and the opponents choice is rock it prints that you lost
                print("You lost")
                loss = loss+1 #Adds 1 point to losses
                
            elif (choice == 2 and opponent == 3): #If your choice is paper and the opponents choice is scissors it prints that you lost
                print("You lost")
                loss = loss+1 #Adds 1 point to losses
                
            elif (choice == 3 and opponent == 2): #If your choice is scissors and the opponents choice is paper it prints that you won
                print("You won!")
                wins = wins+1 #Adds 1 point to wins

            print(" ")

            print("Ties:", ties)#Print score of ties
            print("Wins:", wins)#Print score of wins
            print("Losses:", loss)#Print score of losses

            print(" ")

            playAgain = str(input("Do you want to play Rock-Paper-Scissors again? ([Y] for yes or [N] for no): ")).lower() #Asks user if they want to play rock paper scissors again

            if playAgain == "n":  #If play again is equal to "n"(No)(The user does not want to play again)
                print(" ")
                main()              #Brings the user to the very start of the code
            else:               #else (If the user does want to play again)
                print(" ")
                print("Have fun!")  #Prints have fun and goes back to the start of the while statement in the game
                print(" ")
                











    elif game == 2: #If game is equal to 2 (User picks the random number guessing game)(plays the game)

        wins = 0
        losses = 0

        print("Welcome to the random number guessing game!") #Intro to game

        print(" ") #Space

        playAgain = "y"

        while playAgain == "y": #Keeps looping if playAgain is equal to y (yes)
            
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

            print(" ")

            playAgain = str(input("Do you want to play the random number guessing game again? ([Y] for yes or [N] for no): ")).lower() #Asks user if they want to play random num guessing game again

            if playAgain == "n":  #If play again is equal to "n"(No)(The user does not want to play again)
                print(" ")
                main()              #Brings the user to the very start of the code
            else:               #else (If the user does want to play again)
                print(" ")
                print("Have fun!")  #Prints have fun and goes back to the start of the while statement in the game
                print(" ")
                






        

    elif game == 3:

        def start():        #Defines all code as start()
            
            print("Welcome to Black Jack!")         #Intro and rules
            print(" ")
            print("Here are the rules. Their are no face cards, an ace holds the value of 1, and you start with a balance of $1000. The dealer has to take a card if they are below 17. Minimum bet is a $1 and Maximum bet is $1000.")
            print(" ")
            name = str(input("Enter your name:  "))             #tells user to enter their name
            print(" ")
            print(" ")
            time.sleep(.5)                                      #Pauses code for half a second
            print("Welcome",name,"please gamble responsibly")   #Tells the user to gamble responsibly
            print(" ")
            newBalance = 1000
            time.sleep(.5)
            print("Your starting balance is: $",newBalance)     #Tells the user what their balance is
            
            betAgain = "y" 

            while newBalance > 1 and betAgain == "y":                #Plays code if the balance is greater than 1 and betAgain equals yes
                bet = int(input("Make a bet from $1 - $1000 :"))     #Asks the user how much they want to bet
                newBalance = newBalance - bet                        #Sets new balance

                if bet > 1000 or bet == 0:                           #If bet is greater than 1000 or equal to 0
                    print("Maximum bet is $1000, bet again.")        #Tells user to bet again
                    betAgain = str(input("Do you want to bet again? (Enter [Y] for yes or [N] for no): ")).lower()#Asks the user if they want to bet again (Goes back to the start of the while loop)
                    
                else:
                    print("Good Luck!")
                    
                
                    card1 = random.randint(1,10)                #Gives user their 2 random cards and card total
                    card2 = random.randint(1,10)
                    cardTotal = card1 + card2

                    print("Your cards are: ",card1,"and", card2)
                    print("Your total is: ", cardTotal)

                    time.sleep(1)                               #Pauses code for 1 second

                    oppCard1 = random.randint(1,10)             #Gives computer(opponent) their 2 random cards and card total
                    oppCard2 = random.randint(1,10)
                    oppTotal = oppCard1 + oppCard2
                    time.sleep(.5)
                    print(" ")

                    print("Your opponents cards are: ", oppCard1,"and", oppCard2)
                    print("Your opponents total is: ", oppTotal)

                    print(" ")
                    choice = str(input("Do you want to [H]it or [S]tand? (Please enter only the first letter of your option): ")).lower() #Asks user if they want to hit or stand

                if choice == "h":                                   #If the user hits

                    while choice == "h" and cardTotal <= 21:        #when the user hits and their card total is less than or equal to 21

                            hitCard = random.randint(1,10)          #Generates a random hitcard 
                            print("Your new card is: ", hitCard)
                            cardTotal = cardTotal + hitCard         #Updates card total (Card total plus the hitcard value)
                            time.sleep(1)
                            print("Your new card total is: ", cardTotal) #Tells user their new cardtotal
                            print(" ")

                            if cardTotal > 21:                                  #If users cardtotal is greater than 21
                                print("You went over 21! You lost!")            #Tells user they lost
                                print("Your new balance is: $",newBalance)      #Tells user their new balance
                                if newBalance == 0:                             #If their balance is equal to 0
                                        print("Sorry you ran out of money! GAME OVER")   #Tell the user game over
                                        playAgain = str(input("Do you want to restart the game? (Enter a [Y] for yes or [N] for no):")).lower()#Asks user if they want to restart the game
                                        if playAgain == "n":                    #If the user doesnt want to play again
                                            print(" ")
                                            print("Better luck next time!")     #Prints better luck next time and stops code
                                            print(" ")
                                            main()
                                        else:
                                            start()                             #Else restart the game(If user wants to play agin)
                                else:                                           #else (If balance is not equal to 0) 
                                    betAgain = str(input("Do you want to bet again? (Enter [Y] for yes or [N] for no): ")).lower() #Asks the user if they want to bet again
                                    if betAgain == "n":                             #If bet again equals n (No)
                                        print("Thank you for playing Black Jack!")  #Tells user thank you for playing black jack and ends code
                                        main()
                                    else:                                           #else(If user wants to bet again)
                                        print("Good Luck!")                         #Prints good luck and goes back to the start of the first while loop
                            else:                               #else (If card total is not greater than 21)
                                choice = str(input("Do you want to [H]it or [S]tand? (Please enter only the first letter of your option): ")).lower() #Asks user if they want to hit or stand

                
                
                if choice == "s":                       #If user stands
                    print("You stand")                  #Tells the user that they stand
                    time.sleep(1)                       #Pauses code for 1 second
                    print("It is your opponents turn")  #Tells user its their opponents turn
                    time.sleep(1)                       #Pauses code for one second
                    print(" ")
                    
                    while oppTotal < 17:                #If opponent total is less than 17
                        print("Your opponents total is less than 17, they have to take another card")   #Tells user that they have to take another card
                        print(" ")
                        time.sleep(1)
                        oppHit = random.randint(1,10)                   #Gives opponent a random hit card
                        print("Your opponents new card is: ",oppHit)    #Tells user their opponents new card
                        time.sleep(1)
                        oppTotal = oppTotal + oppHit                    #Updates opponent total to add their hit card
                        print("Their new total is: ", oppTotal)         #Tells user opponents new total
                        print(" ")
                        time.sleep(1)

                    if oppTotal >= 17:                                  #If opponents total is greater than or equal to 17

                        print("Your card total is: ",cardTotal)         #Tells user their total
                        print("Your opponents total is: ",oppTotal)     #Tells user their opponents total
                        print(" ")

                        if cardTotal > oppTotal and cardTotal <= 21:    #If the users total is greater than the opponents total and the users total is less than or equal to 21
                            print("YOU WON!")                           #Tells the user that they won
                            newBalance = newBalance + (bet * 2)         #Updates new balance to add the money they won
                            print("Your new balance is: $",newBalance)  #Tells user what their new balance is
                            betAgain = str(input("Do you want to bet again? (Enter [Y] for yes or [N] for no): ")).lower() #Asks user if they want to bet again (Goes to function at bottom)

                        elif oppTotal > 21 and cardTotal <= 21 :            #If the opponents total is greater than 21 and the users total is less than or equal to 21
                            print("YOU WON! Your opponent went over 21.")   #Tells the user that they won and their opponent went over 21
                            newBalance = newBalance + (bet * 2)             #Updates new balance to add the money that they won 
                            print("Your new balance is: $",newBalance)      #Tells the user their new balance
                            betAgain = str(input("Do you want to bet again? (Enter [Y] for yes or [N] for no): ")).lower() #Asks user if they want to bet again (Goes to function at bottom)

                        elif oppTotal == cardTotal :                    #If the opponents total is equal to the users total
                            print("You tied")                           #Tells user that they tied
                            newBalance = newBalance + bet               #Updates their balance to add their bet money
                            print("Your new balance is: $",newBalance)  #Tells user what their new balance is
                            betAgain = str(input("Do you want to bet again? (Enter [Y] for yes or [N] for no): ")).lower()#Asks user if they want to bet again (Goes to function at bottom)

                        elif cardTotal <= 21 and oppTotal <= 21 and oppTotal > cardTotal: #If users total is less than or equal to 21 and opponents total is less than or equal to 21 and opponent total is greater than the users total
                            print("You lost!")                                            #Tells the user they lost  
                            print("Your new balance is: $",newBalance)                    #Tells user their new balance (Their balance minus their bet)
                            
                            if newBalance == 0:                                     #If the users balance is equal to 0
                                print("Sorry you ran out of money! GAME OVER")      #Tells user they ran out of money and the game is over
                                playAgain = str(input("Do you want to restart the game? (Enter a [Y] for yes or [N] for no):")).lower()#Asks user if they want to restart the game

                                if playAgain == "n":                #If the user does not want to restart the game (Equals no)
                                    print(" ")
                                    print("Better luck next time!") #Prints better luck next time and ends the code
                                    print(" ")
                                    main()
                                else:                               #Else (If user wants to restart)
                                    start()                         #Goes back to the start of the code
                            else:               #else (If balance does not equal 0)
                                betAgain = str(input("Do you want to bet again? (Enter [Y] for yes or [N] for no): ")).lower()#Asks user if they want to bet again (Goes to function at bottom)

                        if betAgain == "n":         #If betAgain is equal to no (The user does not want to bet again)
                            if newBalance > 1000:   #If the users balance is greater than 1000
                                print(" ")
                                print("Thank you for playing Black Jack!") #Tells the user thank you for paying black jack
                                wins = newBalance - 1000                   #Variable called wins is the users balance subtract 1000 
                                print("You won: $",wins)                   #Tells the user how much money they won
                                time.sleep(1)
                                main()

                            elif newBalance <1000:                          #If the users balace is less than 1000
                                print(" ")
                                print("Thank you for playing Black Jack!") #Tells the user thank you for paying black jack
                                wins = 1000 - newBalance                    #Variable called wins is 1000 subtract the users balance 
                                print("You lost: $",wins)                   #Tells the user how much money they lost
                                time.sleep(1)
                                main()
                            
                        else:                   #Else (If bet again is yes (The user wants to bet again))
                            print("Good Luck!") #Print good luck

        start()     #Continues the code from the start (Finishes the def  start statement)



main()

