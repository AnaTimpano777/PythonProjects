#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: February 18, 2020
#Decription: Determines if a phrase contains palindromes

print("This program determines if a phrase is a palindrome")
print(" ")

originalPhrase = str(input("Please enter a phrase(do not include a punctuation mark): ")) #Aks user to enter a word

phrase = originalPhrase.replace(" ", "").lower() #Converts original phrase to lowercase and removes all spaces

backwardsPhrase = "" #sets variable to an empty string

for i in range(len(phrase) -1, -1, -1): #loops through characters in phrase backwards and builds a reverse string
    backwardsPhrase += phrase[i]

if phrase == backwardsPhrase: #If the phrase is equal to the backwards phrase
    print("The phrase that you entered is a palindrome") #Display that the phrase is a palindrome
else: #else
    print("The phrase that you entered is not a palindrome")#Display that the phrase is not a palindrome


