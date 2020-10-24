#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 20, 2020
#Decription: This program will read any text file.

myFile = None #Assign value None to myFile
fileName = input('Please enter a file name: ') #Get users input for .txt file name

try: 
    myFile = open(fileName, "r") #Open .txt file with name fileName in read only mode
    for myLine in myFile: # loops through each line in myFile
        print(myLine, end='') #Outputs myLine with end='' to disable new lines

except IOError:
    print('There was an IOError!') #Output error message
    print('')

finally:
    myFile.close() #Close the file
