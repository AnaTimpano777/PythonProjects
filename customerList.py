#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 27, 2020
#Decription: This program allows the user to add customers names and information to a text file (customerList.txt)

myFile = None #Set myFile variable to the value None
postalCode = "" #set postalCode variable to empty string
numCustomers = int(0) #set numCustomers to 0 int

print("Welcome to the Discount Fly customer information storage!") #Outputs program intro 
print("") 

try:
    myFile = open("customerList.txt", "r") #open the text file with name "customerList.txt" in read mode and store the file object in variable myFile
    for myLine in myFile: # loops through each line in myFile
        print(myLine, end='') #Output myLine with end='' to disable new lines
    isError = bool(True) #INITIALIZE variable isError by ASSIGNING it the Boolean value of True
    
    while isError: #While isError is set to boolean value True
        try: 
            numCustomers = int(input("How many customers would you like to input?:")) #get user input for number of customers to be input as an int and store in variable numCustomers
            isError = bool(False) #Sets variable is Error to boolean value False
        except ValueError: 
            print("Error: You can only input a numerical value")#Output error message

    for i in range(0, numCustomers): #Loop in the range of 0 to numCustomers
        name = input("Enter the name of customer #" + str(i + 1) + ":") #User inputs information for customer(s)
        address = input("Enter the address of customer #" + str(i + 1) + ":")
        city = input("Enter the city of customer #" + str(i + 1) +":")
        province = input("Enter the province of customer #" + str(i + 1) + ":")
        isError = bool(True) #Set variable isError to boolean value True

        while isError: #While isError is set to boolean value True
            postalCode = input("Enter the postal code of the customer without spaces:") #User inputs postal code for customer(s)
            postalCode = postalCode.upper() #Uppercases all letters
            if postalCode[0].isalpha() and postalCode[1].isdigit() and postalCode[2].isalpha() and postalCode[3].isdigit() and postalCode[4].isalpha() and postalCode[5].isdigit(): #If postal code is valid
                print("")
                print("That is a correct postal code, your information has now been saved to customerList.txt") #Output that the postal code is correct
                print("A preview of your personal information will be displayed below:")#Outputs that personal info will be displayed below
                print("")
                isError = bool(False) #Set variable isError to boolean value False
            else: #Else, if postal code is not valid
                print("The postal code you entered is invalid, please try again") #Output that postal code is invalid and to try again
                
        info = ["Name: " + name , "\nAddress: "+ address, "\nCity: "+city, "\nProvince: "+province, "\nPostalcode: "+ postalCode] #ASSIGN all customer data (name, address, city, province and postalCode) to variable info with formatting 
        myFile = open("customerList.txt", "a+") #open the text file with name "customerList.txt" in append mode and store the file object in variable myFile
        myFile.writelines(info) #writelines() the contents of variable info to myFile
        myFile.write("\n------------------------------------------\n") #write() the customer seperate to var myFile
        
        for i in range(len(info)): #Loops through length of variable info
            print(info[i], end = '') #Outputs info contents with end='' to start each one on a new line
        print("\n------------------------------------------\n") #Output customer seperator
        
except IOError: 
    print('There was an IOError!') #Output error message
    print('')

finally:
    myFile.close() #Close the file
                
        
