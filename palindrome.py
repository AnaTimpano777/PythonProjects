#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: February 18, 2020
#Decription: Determines if the word is a palindrome

print("This program determines if a word is a palindrome")
print(" ")

word = str(input("Please enter a word: ")) #Aks user to enter a word
word = word.lower() #Makes letters lowercase

backwardsWord = "" #sets variable to empty string

for i in range(len(word) -1, -1, -1): #loops over each character
    backwardsWord = backwardsWord + word[i] #Updates variable

    
print(" ") #space
print(word, "in reverse is", backwardsWord) #Tells the user their word backwards
print(" ") #space

if word == backwardsWord: #If the word the user entered is equal to the backwards form of their word
    print("The word", word,"is a palindrome") #Display to the user that their word is a palindrome
else: #else / if the word isnt equal to the backwards word
    print("The word", word,"is not a palindrome") #Displays to the user that their word isnt a palindrome


