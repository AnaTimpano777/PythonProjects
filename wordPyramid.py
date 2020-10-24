#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: May 19, 2020
#Decription: Program that uses a recursive algorithm to make a word pyramid from user input

def pyramid(word): #Function called pyramid that has paramter word
    print(word) #Outputs word
 
word = input("Please enter a word with more than 2 letters: ") #Gets user input and stores it in the variable word
print("") #space

if len(word) > 2: #If the length of the variable word is greater than 2 then...
    for i in range(len(word)//2+1): #Loops through the length of the word until the middle letter(s) is left
        pyramid(word) #Call function pyramid (Outputs word)
        word = word[1:-1] #Gets rid of the first and last letters of the word

else: #Else
    pyramid(word) #Call function pyramid (Outputs word)
    print("Error: Word is too short to make a pyramid. Please type in a word with more than 2 letters!") #Outputs error to user
 
                    
        
