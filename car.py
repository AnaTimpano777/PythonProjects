#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 8, 2020
#Decription: is the class file for carTester.py (Creates 3 different cars with 6 paramaters)

import random #Import random

# This make a 'pool; for the computer to randomly choose
#  ie. the random import

make = ['Alpha', 'Ferrari', 'Mazda', 'Honda', 'Mitsubishi'] #List under the variable make for the computer to randomly choose
comp_make = random.choice(make) #Random choice from list make
if comp_make == 'Alpha Romeo': #If the vairiable comp_make (random computer choice) is equal to a car name pair it with its designated model
    model = '4C'
elif comp_make == 'Ferrari':
    model = 'Enzo'
elif comp_make =='Mazda':
    model = 'Rx-7'
elif comp_make == 'Honda':
    model = 'S2000'
elif comp_make == 'Mitstubishi':
    model = '3000gt'

comp_year = str(random.randrange(1991, 2003)) #Chooses random year from 1991 to 2003 in variable comp_year
comp_price = str(random.randrange(10000, 20000)) #Chooses random price number from 10000 to 20000 in variable comp_price

class Car: #Class car
    def __init__(self, make=comp_make, model=model, year=comp_year, price=comp_price, colour='Black', doors='2'): #Defines the contructor with 6 properties and provides them each with a default value
        self.make = make #Assigns paramaters to instance properties
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour
        self.doors = doors

    def honk(self): #Defines honk method
        print("HONK!!!") #Outputs string 

    def __str__(self): #Defines string method
        output = "Make: " + self.make + "\n" #Outputs the 6 paramaters to the user (formatted)
        output += "Model: " + self.model + "\n"
        output += "Year: " + self.year + "\n"
        output += "Price: $" + self.price + "\n"
        output += "Colour: " + self.colour + "\n"
        output += "Number of Doors: " + self.doors + "\n"
        return output #return output
