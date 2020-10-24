#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: February 20, 2020
#Decription: Encrypts or Decrypts a message inputed by the user

print("This program will encrypt or decrypt a phrase using the simple encyption method of roatating the letters.")
print(" ")

phrase = str(input("Please enter a phrase(do not include a punctuation mark): ")) #Aks user to enter a phrase

rotationAmount = int(input("Enter the rotation amount (1 - 25): ")) #Asks user to enter rotation amount from 1 - 25

encOrDecStr = int(input("Enter '1' for encryption or '2' for decryption: ")) #User enters 1 for encyption or 2 for decryption

phrase = phrase.upper() #makes all letters of phrase uppercase

if encOrDecStr == 1: #if user chooses to encrypt phrase
    encryptedPhrase = "" #sets variable to an empty string
    for i in range(0, len(phrase)): #loops through all characters in the phrase
        charValue = ord(phrase[i]) #updates variable
        if charValue != 32: #If variable is equal to the character 32 (space)
            charValue += rotationAmount #Add a rotation amount so it goes to the next character
            if charValue > 90: #If the character is greater than the 90 character
                charValue -= 26 #Subtract 26 roatations (restarts characters)
        encryptedPhrase += chr(charValue) #Sets new phrase to the variable encryptedPhrase

    print(" ") #space
    print("The original phrase is: ", phrase) #Displays the original phrase
    print("The encrypted phrase is: ", encryptedPhrase) #displays the encrypted phrase

if encOrDecStr == 2: #If user chooses to decrypt phrase
    decryptedPhrase = "" #Sets variable to an empty string
    for i in range(0, len(phrase)):
        charValue = ord(phrase[i])
        if charValue != 32:
            charValue -= rotationAmount
            if charValue < 65:
                charValue += 26
        decryptedPhrase += chr(charValue)

    print(" ")
    print("The original phrase is: ", phrase) #displays the original phrase
    print("The decrypted phrase is: ", decryptedPhrase) #Displays decrypted phrase
