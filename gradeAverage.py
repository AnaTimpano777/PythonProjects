#Program Name: gradeAverage.py
#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: June 15, 2020
#Decription: CCT Assignment. Program that calculates and outputs a students a grade average and their grade letter. and outputs 

print("Grade Average") #Outputs program title to user
print("*************")
print(" ") #space

print("This program will ask you for the grade in each of your four courses.") #Outputs program description to user
print("It will then average them for you and give you your letter grade.")
print("") #space

while True: #Try again loop, as long as the loop is true keep running
    
    name = str(input("Enter your first name:")) #Gets users input for their first name and stores it as string in the variable name
    period1 = float(input("Enter your period 1 percentage grade (Please do not include % symbol):")) #Gets user input for period 1 percentage grade and stores as float in variable period1
    period2 = float(input("Enter your period 2 percentage grade (Please do not include % symbol):")) #Gets user input for period 2 percentage grade and stores as float in variable period2
    period3 = float(input("Enter your period 3 percentage grade (Please do not include % symbol):")) #Gets user input for period 3 percentage grade and stores as float in variable period3
    period4 = float(input("Enter your period 4 percentage grade (Please do not include % symbol):")) #Gets user input for period 4 percentage grade and stores as float in variable period4

    print("") #space
    print("Hello " + name + "!") #Outputs Hello to user with their name

    total = (period1 / 100)+(period2 / 100)+(period3 / 100)+(period4 / 100) #Totals up all the period percentage grades and divides each by 100, stores in variable total
    gradeAverage = round((total / 4) * 100, 1) #Calculates the percentage grade average by dividing the variable total by 4 and then multiplying by 100. Stores in variable gradeAverage
                                               #Rounds gradeAverage to 1 decimal place
    
    print("Your average mark for the semester is: " + str(gradeAverage) + "%") #Ouptuts average mark for the semester to user

    gradeAverage = round(gradeAverage) #Rounds grade average to nearest whole number for letter grade, this way it is more accurate

    if gradeAverage >= 80 and gradeAverage <= 100: #If gradeAverage is greater than or equal to 80 and less than or equal to 100 then
        print("Your Letter Grade for the semester is: A") #Outputs letter grade to user (A)

    elif gradeAverage >= 70 and gradeAverage <= 79: #If gradeAverage is greater than or equal to 70 and less than or equal to 79 then
        print("Your Letter Grade for the semester is: B") #Outputs letter grade to user (B)

    elif gradeAverage >= 60 and gradeAverage <= 69: #If gradeAverage is greater than or equal to 60 and less than or equal to 69 then
        print("Your Letter Grade for the semester is: C") #Outputs letter grade to user (C)

    elif gradeAverage >= 50 and gradeAverage <= 59: #If gradeAverage is greater than or equal to 50 and less than or equal to 59 then
        print("Your Letter Grade for the semester is: D") #Outputs letter grade to user (D)

    elif gradeAverage >= 0 and gradeAverage <= 49: #If gradeAverage is greater than or equal to 0 and less than or equal to 49 then
        print("Your Letter Grade for the semester is: F") #Outputs letter grade to user (F)

    else: #else (error message)
        print("Something went wrong. Your percentage grade average seems to be out of range.") #output to user that something went wrong and that their average is out of range
        print("Please try again.") #Outputs to user to please try again

    print("") #space
    end = str(input("Press 'y' to try again or any other key to quit: ")) #gets user input on if they want to try the program again ("y") or quit program (any other letter) and stores as 
                                                                          #string in variable end
    if end == "y": #if variable end is equal to y then
        print("") #space
        continue  #use continue function. Continues the program from where the while loop starts (while continues to equal True)
    else: #else (if end is equal to anything but y)
        break #use break function. Stops/breaks program

    
