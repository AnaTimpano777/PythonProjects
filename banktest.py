#This program is written in two different files because my teacher
#is teaching us about classes

#This is the class file where all of the def's are
class ATM:
    def __init__(self, bankName='BMO', balance= 1000):
        self.bankName = bankName
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(' ')
        else:
            print('Error: Please type in a valid number')

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(' ')
        else:
            print('Error: Please type in a valid number')

    def displayBalance(self):
        print('Bank Balance: $', self.balance)
        print(' ')

    def addDailyInterest(self, intRate, numDays):
        self.intRate = intRate
        self.numDays = numDays
        if intRate > 0 and intRate <= 100 and numDays > 0:
            i = (intRate) / 100 / 365
            A = ((self.balance * ((1 + i) ** numDays)))
            print('The interest earned in', numDays, 'days is: $', round(A - self.balance, 2))
            self.balance = A
            print(' ')
        else:
            print('Error: Please type in a valid number')
            
#This is the second file where the instructions and interaction is

from ATM import ATM

print('Welcome to the ATM machine of your very own bank! Lets get started...')
print('')

bankName = input('Please enter your bank name: ')
balance = float(input('Please enter your starting balance: $'))


myAtm = ATM(bankName, balance) #How to INSTANTIATE???????
done = False

while not done:

    print('Please select from the following menu:')
    print('1 - Display Balance')
    print('2 - Deposit Money')
    print('3 - Withdraw Money')
    print('4 - Add Daily Interest')
    print('5 - Exit')
    print(' ')
    choice = int(input('Type in the number associated with your choice: '))

    if choice == 1:
        myAtm.displayBalance() #How do I run functions from 
        #the class file???
    elif choice == 2:
        amount = int(input('How much would you like to deposit?: $'))
        myAtm.deposit(amount)
    elif choice == 3:
        amount = float(input('How much would you like to withdraw?: $'))
        myAtm.withdraw(amount)
    elif choice == 4:
        intRate = float(input('What is the annual interest rate as a percentage?: %'))
        numDays = int(input('How many days will you leave the balance invested?: '))
        myAtm.addDailyInterest(intRate, numDays)
    elif choice == 5:
        done = True
    else:
        print('Error: Invalid selection')

