#Name: Ana Timpano
#Course Code: ISC3UE
#Program Description: this code calculates the annual compound investment based on the users input

print("Welcome to the Compound Interest Calculator!")#Title
print(" ")#space
print("This program will print out a table that will display the amount of yearly investment over a period of 15 years") #Program description
print(" ")

amount = int(input("Enter the yearly investment amount($): "))
rate = int(input("Enter the interest rate in percent (%): "))
years = int(input("Enter the number of years for this investment: "))

total = 0 #Set total equal to 0 
account = amount #Sets variable amount to a new variable called account
print(" ")
print(" ")

print ("{0:14}\t{1:14}\t{2:14}\t{3:18}".format("Year", "Account", "Interest", "Total")) #Formats the titles of the table
    
for i in range(1, years + 1): #Increments years by 1 each time until it reaches the value inputed
    year = i
    
    account = (round(amount + total ,2)) #Equation for the amount, Set to a new variable to display the first number inputed (150), rounded to 2 decimal places
    
    interest = (round(rate/100 * account ,2)) #Equation for the interest, rounded to 2 decimal places
    
    total = (round(interest + account ,2)) #Equation for the total, total was set = to 0 so only the interest and amount was added. Rounded to 2 decimal places
    
    print ("{0:<14}\t${1:<14}\t${2:<14}\t${3:<18}".format(year,account,interest,total)) #Formats the numbers under the titles in the table



    
