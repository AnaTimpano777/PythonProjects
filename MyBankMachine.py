#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 10, 2020
#Decription: This program mimics a real life bank machine with the class file ATM.py

from ATM import ATM #From ATM.py import ATM class

print('Welcome to the ATM machine of your very own bank! Lets get started...') #Outputs intro to bank program
print('') #space

bankName = input('Please enter your bank name: ') #Asks user for bank name and inputs it into the variable bankName
balance = float(input('Please enter your starting balance: $')) #Asks user for starting balance and inputs it as a float to the variable balance


myAtm = ATM(bankName, balance) #Instantiates myAtm sending bankName and balance as paramaters
done = False #Sets variable done to False

while not done: #While done = False keep running loop

    print('Please select from the following menu:') #Prints bank menu options
    print('1 - Display Balance')
    print('2 - Deposit Money')
    print('3 - Withdraw Money')
    print('4 - Add Daily Interest')
    print('5 - Exit')
    print(' ')
    choice = int(input('Type in the number associated with your choice: ')) #Asks user to choose an option and store as an integer in variable choice

    if choice == 1: #If choice is equal to 1
        myAtm.displayBalance() #Output balance in myAtm using displayBalance() method
    elif choice == 2: #If choice is equal to 2
        amount = int(input('How much would you like to deposit?: $')) #Asks user deposit amount and stores as an integer in variable amount
        myAtm.deposit(amount) #deposit amount in myAtm using deposit(amount) method
    elif choice == 3: #If choice is equal to 3
        amount = float(input('How much would you like to withdraw?: $')) #Asks user withdraw amount and stores as a float in variable amount
        myAtm.withdraw(amount) #withdraw amount in myAtm using withdraw(amount) method
    elif choice == 4: #If choice is equal to 4
        intRate = float(input('What is the annual interest rate as a percentage?: %')) #Asks user for percentage and stores as float in variable intRate
        numDays = int(input('How many days will you leave the balance invested?: ')) #Asks user for # of days and stores as integer in variable numDays
        myAtm.addDailyInterest(intRate, numDays) #add daily interest in myAtm using addDailyInterest(rate, days) method
    elif choice == 5: #If choice is equal to 5
        done = True #Sets variable done to True
    else: #else
        print('Error: Invalid selection') #Output error message

