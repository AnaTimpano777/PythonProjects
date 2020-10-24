#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: February 21, 2020
#Decription: Converts a string into morse code

print("This program will  convert your message into morse code")
print(" ")

message = str(input("Please enter the message you want to turn into morse code: ")).upper() #Aks user to enter a message

morseMessage = "" #Sets variable to an empty string

for i in range(0, len(message)): #loops through all the characters in the message and if character is present add morsecode to variable
    if message[i] == 'A':
        morseMessage += ".- "
    if message[i] == 'B':
        morseMessage += "-... "
    if message[i] == 'C':
        morseMessage += "-.-. "
    if message[i] == 'D':
        morseMessage += "-.. "
    if message[i] == 'E':
        morseMessage += ". "
    if message[i] == 'F':
        morseMessage += "..-. "
    if message[i] == 'G':
        morseMessage += "--. "
    if message[i] == 'H':
        morseMessage += ".... "
    if message[i] == 'I':
        morseMessage += ".. "
    if message[i] == 'J':
        morseMessage += ".--- "
    if message[i] == 'K':
        morseMessage += "-.- "
    if message[i] == 'L':
        morseMessage += ".-.. "
    if message[i] == 'M':
        morseMessage += "-- "
    if message[i] == 'N':
        morseMessage += "-. "
    if message[i] == 'O':
        morseMessage += "--- "
    if message[i] == 'P':
        morseMessage += ".--. "
    if message[i] == 'Q':
        morseMessage += "--.- "
    if message[i] == 'R':
        morseMessage += ".-. "
    if message[i] == 'S':
        morseMessage += "... "
    if message[i] == 'T':
        morseMessage += "- "
    if message[i] == 'U':
        morseMessage += "..- "
    if message[i] == 'V':
        morseMessage += "...- "
    if message[i] == 'W':
        morseMessage += ".-- "
    if message[i] == 'X':
        morseMessage += "-..- "
    if message[i] == 'Y':
        morseMessage += "-.-- "
    if message[i] == 'Z':
        morseMessage += "--.. "
    if message[i] == '1':
        morseMessage += ".---- "
    if message[i] == '2':
        morseMessage += "..--- "
    if message[i] == '3':
        morseMessage += "...-- "
    if message[i] == '4':
        morseMessage += "....- "
    if message[i] == '5':
        morseMessage += "..... "
    if message[i] == '6':
        morseMessage += "-.... "
    if message[i] == '7':
        morseMessage += "--... "
    if message[i] == '8':
        morseMessage += "---.. "
    if message[i] == '9':
        morseMessage += "----. "
    if message[i] == '0':
        morseMessage += "----- "
        


print("Morse Message: ", morseMessage) #Display the morse message to user
