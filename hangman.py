#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: March 13, 2020
#Decription: Hangman Game

import random #Imports random function


print("HANGMAN") #Displays to the user what the code is about
print(" ") #space

sports = ["SPORTS", "LEBRON JAMES", "BASKETBALL", "BADMINTON", "SIDNEY CROSBY"] #Creates a list of sports in the variable sports
movies = ["MOVIES", "TOY STORY", "STAR WARS", "JAWS", "JURASSIC PARK"] #Creates a list of moveis in the variable movies
tvShows = ["TVSHOWS", "GREYS ANATOMY", "BREAKING BAD", "THE OFFICE", "FRIENDS"] #Creates a list of TV Shows in the variable tvShows

hangmanWords = [sports, movies, tvShows] #Creates a list of all 3 categories in the varibale hangmanWords

graphics = ["  O \n/ | \\\n  |\n/   \\", "  O \n/ | \\\n  |\n/", "  O \n/ | \\\n  |", "  O \n/ | \\", "  O \n/ |", "  O \n/", "  O", " "] #Creates the graphics of the person if letter is guessed incorrectly

categoryIndex = random.choice([0, 1, 2])  # Pick a random number between 0 and 2.
wordIndex = random.choice([0, 1, 2, 3, 4]) # Pick a random number between 0 and 4.

category = hangmanWords[categoryIndex][0] #Selects one of the 3 categories and sets it to the variable category
word = hangmanWords[categoryIndex][wordIndex] #Picks a word from one of the 3 categories and sets it to the variable word

blankWord = str("") #Sets variable blankWord to an empty string
numWords = int(1) #Sets variable numWords to the interger 1

for pos in range(0, len(word)): # Convert each letter to dash
    if (ord(word[pos]) >= 65) and (ord(word[pos]) <= 90):
        blankWord += "-"
    else: # if space keep it and increment numWords
        blankWord += word[pos]
        if word[pos] == ' ':
            numWords += 1

lettersUsed = str("") #Sets variable lettersUsed to an empty string
numGuesses = int(7) #Sets numGuesses to the interger 7 (7 guesses total)

while numGuesses > 0: #While the number of gusses is greater than 0
    print("Category: ",category) #Displays to the user what the category is
    print("Number of Words: ",numWords) #Displays to the user the number of words
    print("") #Space
    print(blankWord) #Prints varibale blankWord
    print(graphics[numGuesses]) #Prints the graphics (stickman) based on number of guesses
    print(numGuesses, "guesses remaining") #Displays number of guesses remaining
    myGuess = str(input("Guess a letter: ")) #Tells the user to guess a letter and inputs answer to varibale myGuess
    myGuess = myGuess.upper() #Sets myGuess to uppercase letter
    found = False #Sets found to False

    for pos in range(0, len(word)): # loop through and check letters in word(s)
        if word[pos] == myGuess: # Replace hyphen with the letter
            blankWord = blankWord[0:pos] + myGuess + blankWord[pos + 1:len(blankWord)]
            found = True #Sets found to True
            
    print("") #Space

    if found: #If letter gusses is found in word
        print(myGuess, "is in the word") #Displays that the letter they guessed is in the word
    else:#Else
        print(myGuess, "is not in the word") #Displays that the letter they gusses is not in the word
        numGuesses -= 1 #Subtracts 1 guess from total guesses
        print("")#space
    if blankWord.find("-") == -1: # No dashes left, you guessed it!
        print("Category: ",category) #Displays category to user
        print("Number of Words: ",numWords) #Displays number of words to user
        print(blankWord) #Displays variable blankWord
        print("")#space
        print("Congratulations! You won the game!!!") #Congratulates the user for winning the game
        exit() #exits out of code
        
print("Game Over") #Tells the user the game is over
print(graphics[0]) #Dislays varibale graphics[0]
print("The correct word is", word) #Displays what the correct word is
    
