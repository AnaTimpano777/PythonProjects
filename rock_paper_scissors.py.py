import random 

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

rounds = int(input("Enter the amount of rounds you want to play: ")) #User inserts value to the variable rounds

print(" ")

for i in range(0,rounds):

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
