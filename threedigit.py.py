#Name: Ana Timpano
#Course Code: ICS3U
#Program Description: This program asks the user for a three-digit positive integer and prints the sum of the digits.

#Asks the user for a 3 digit positive integer
number = int(input("Please enter a positive 3 digit number: "))

#space
print (" ")

#variables
digit1 = (number // 100)
digit3 = (number % 10)
digit2 = ((number % 100 - digit3) / 10)
total =  (int(digit1 + digit2 + digit3))

print (digit1,"+",(int(digit2)),"+",digit3,"=",total)

