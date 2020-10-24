import random

# This make a 'pool; for the computer to randomly choose
#  ie. the random import

make = ['Alpha', 'Ferrari', 'Mazda', 'Honda', 'Mitsubishi']
comp_make = random.choice(make)
model = None
if comp_make == 'Alpha':
    model = 'Romeo'
elif comp_make == 'Ferrari':
    model = 'Enzo'
elif comp_make =='Mazda':
    model = 'Rx-7'
elif comp_make == 'Honda':
    model = 'S2000'
elif comp_make == 'Mitstubishi':
    model = '3000gt'

comp_year = str(random.randrange(1991, 2003))
comp_price = str(random.randrange(10000, 20000))

class Car:
    # Here we set the requirements for the object to a default
    #  All or none of the arguments can be defined, if not defined
    # The object will have a value
    def __init__(self, make=comp_make, model=model, year=comp_year, price=comp_price, colour='Black', doors='2'):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour
        self.doors = doors

    def honk(self):
        print("HONK!!!")

    def __str__(self):
        output = "Make: " + self.make + "\n"
        output += "Model: " + self.model + "\n"
        output += "Year: " + self.year + "\n"
        output += "Price: $" + self.price + "\n"
        output += "Colour: " + self.colour + "\n"
        output += "Number of Doors: " + self.doors + "\n"
        return output
