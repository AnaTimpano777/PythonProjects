import random
import time


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
                                    print("Better luck next time!")     #Prints better luck next time and stops code
                                else:
                                    start()                             #Else restart the game(If user wants to play agin)
                        else:                                           #else (If balance is not equal to 0) 
                            betAgain = str(input("Do you want to bet again? (Enter [Y] for yes or [N] for no): ")).lower() #Asks the user if they want to bet again
                            if betAgain == "n":                             #If bet again equals n (No)
                                print("Thank you for playing Black Jack!")  #Tells user thank you for playing black jack and ends code
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
                            print("Better luck next time!") #Prints better luck next time and ends the code
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

                    elif newBalance <1000:                          #If the users balace is less than 1000
                        print(" ")
                        print("Thank you for playing Black Jack!") #Tells the user thank you for paying black jack
                        wins = 1000 - newBalance                    #Variable called wins is 1000 subtract the users balance 
                        print("You lost: $",wins)                   #Tells the user how much money they lost
                    
                else:                   #Else (If bet again is yes (The user wants to bet again))
                    print("Good Luck!") #Print good luck

start()     #Continues the code from the start (Finishes the def  start statement)

