#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 14, 2020
#Decription: is the class file for TwoDogsMeet.py (This program mimics two dogs meeting and based on their aggression and hunger if they will be friendly or not)

class Dog:
    # constructor
    def __init__(self, name="Charlie", breed="Unknown", aggression=0, hunger=0): #Sets default values for paramaters
        self.name = name
        self.breed = breed
        self.aggression = aggression
        self.hunger = hunger

    def bark_friendly(self): #Creates friendly bark function
        print("Arf! Arf!")

    def bark_angry(self): #Creates angry bark function
        print("GRR! RRRFFF!")

    # method to display all info of the Dog
    def __str__(self):
        output = "Name: " + self.name + "\n"
        output += "Breed: " + self.breed + "\n"
        output += "Aggression: " + str(self.aggression) + "\n"
        output += "Hunger: " + str(self.hunger)
        # output string is complete, return it
        return output
