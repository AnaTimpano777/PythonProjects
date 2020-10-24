#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: February 18, 2020
#Decription: Determines if the words in a sentence are palindromes

print("This program determines if a sentence is a palindrome")
print(" ")

sentence = str(input("Please enter a sentence (do not include punctuation mark): ")) #Aks user to enter a sentence
sentence = sentence.lower() #Makes all letters lowercase

words = sentence.split() #Sets the sentence into a list of all the seperate words

palindromes = [] #creates an empty list
palindromeCounter = 0

for i in range(0, len(words)): #loops through words
    reverseWord = words[i][::-1] #Reverses string
    if words[i] == reverseWord: #Tests to see if it's a palindrome
        palindromeCounter += 1
        palindromes.append(words[i])

    
print(" ")
print("There are", palindromeCounter,"in the sentence") #displays the amount of palindroms in the sentence
print(palindromes)


