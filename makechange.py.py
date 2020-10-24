#Name: Ana Timpano
#Course Code: ICS3U
#Program Description: This program calclates the number of coins necessary to make the smallest amount of change for an given dollar amount that the user types in.

#Print to the user what the code is
print ("Welcome to the make change machine!")

#Space
print (" ")

#Variables
totalMoney = float(input("Please enter the amount of dollars and cents you have: "))

#Print the total money back to the user
print ("Your amount is:", totalMoney)

#Print space
print (" ")

#variables
toonies = int(2)
loonies = int(1)
quarters = float(0.25)
dimes = float(0.10)
nickles = float(0.05)

amountToonies = (totalMoney // toonies)
#I changed the value of the toonies so each toonie is equal to 2 dollars
valueToonies = (amountToonies * 2)
totalMoney = round(totalMoney - valueToonies, 2)
amountLoonies = (totalMoney // loonies)
totalMoney1 = round(totalMoney - amountLoonies, 2)
amountQuarters = (totalMoney1 // quarters)
#I changed the value of the quarters so each quarter is equal to 25 cents
valueQuarters = (amountQuarters * 0.25)
totalMoney2 = round(totalMoney1 - valueQuarters, 2)
amountDimes = (totalMoney2 // dimes)
#I changed the value of the dimes so each dime is equal to 10 cents
valueDimes = (amountDimes * 0.10)
totalMoney3 = round(totalMoney2 - valueDimes,2)
amountNickles = (totalMoney3 // nickles)
#I changed the value of the nickles so each nickle is equal to 5 cents
valueNickles = (amountNickles * 0.05)


print ("Toonies =", int(amountToonies))
print ("Loonies =", int(amountLoonies))
print ("Quarters =",int(amountQuarters))
print ("Dimes =", int(amountDimes))
print ("Nickles =", int(amountNickles))
