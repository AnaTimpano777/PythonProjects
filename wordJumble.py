#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: May 19, 2020
#Decription: Program that uses a recursive algorithm to jumble words

# input parameters
# word - the remaining letters in the word still to jumble
# jumb_let - the letters already used to create the jumbled word

def jumble_words(word, jumb_let): #Function called jumble_words with 2 paramaters
    orig_word = word #Sets variables
    orig_jumbled_letters = jumb_let
    if len(word) == 1: #If the length of the word is equal to 1
        print(jumb_let + word) #Print vairbale jumb_let plus variable word
    else: #else
        for pos in range(0, len(orig_word)): #For range loop that loops through the original word
            remaining_letters = orig_word[0:pos] + orig_word[pos + 1:len(orig_word)] #Scrammbles the letters into new forms
            # recursive call to jumble_words()
            jumble_words(remaining_letters, orig_jumbled_letters + orig_word[pos])

print("This program will show you all of the different ways your word can be scrammbled!") #Outputs what the program is about to user

letters = str(input("Please enter a word:")) #Gets users input to enter a word and stores in variable letters
print("") #space
jumble_words(letters, "") #Calls function with paramters 
