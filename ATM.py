#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 10, 2020
#Decription: is the class file for MyBankMachine.py (This program mimics a real life bank machine)

class ATM: #Creates class called ATM
    def __init__(self, bankName='BMO', balance= 1000): #Defines the contructor with properties that have default values
        self.bankName = bankName #Assigns paramaters to instance properties
        self.balance = balance

    def deposit(self, amount): #Defines deposit method which takes an amount paramater
        if amount > 0: #If amount is greater than 0
            self.balance += amount #Adds desposit amount to balance
            print(' ') #space
        else: #else
            print('Error: Please type in a valid number') #Output error message

    def withdraw(self, amount): #Defines withdraw method which takes an amount paramater
        if amount <= self.balance and amount > 0: #If amount is less than or equal to the balance and the amount is greater than 0
            self.balance -= amount #Subtracts withdraw amount from balance
            print(' ') #space
        else: #else
            print('Error: Please type in a valid number') #Output error message

    def displayBalance(self): #Defines displayBalance method with no paramaters
        print('Bank Balance: $', self.balance) #Displays bank balance to user
        print(' ') #spaces

    def addDailyInterest(self, intRate, numDays): #Defines addDailyInterest method with paramaters intRate and numDays 
        if intRate > 0 and intRate <= 100 and numDays > 0: #If intRate is greater than 0 and intRate is less than or equal to 100 and numdays is greater than 0
            i = (intRate) / 100 / 365 #Intrate calculations set to variable i
            A = ((self.balance * ((1 + i) ** numDays))) #Compound interest calculation set to variable 1
            print('The interest earned in', numDays, 'days is: $', round(A - self.balance, 2)) #Displays interest earned to user
            self.balance = A #Sets A to self.balance variable
            print(' ') #space
        else: #else
            print('Error: Please type in a valid number') #Outputs error message
