#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 20, 2020
#Decription: "Quote of the day" program. Provides a random quote.

import random #Import random

quotes = [] #Initialize variable quotes as empty list
myFile = None #Set myFile variable to the value None

try:
    myFile = open("quotes.txt") #Open .txt file and store in variable myFile
    for i in myFile: #Loop through each line of myFile
        quotes.append(i) #Append each line in myFile to the list quotes

except IOError:
    print('There was an IOError!') #Output error message
    print('')

finally:
    myFile.close() #Close the file

num = random.randint(0,len(quotes)-1) #Generates random number and stores in variable num (From 0 to 1 less than the len of the list quotes)
print(quotes[num]) #Output the quote stores at index num
