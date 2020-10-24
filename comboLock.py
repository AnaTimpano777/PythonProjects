#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 14, 2020
#Decription: is the class file for comboLockDriver.py (This program mimics a combination lock and has a lock guessing game)

class ComboLock: #Creates class ComboLock
    def __init__(self, num1=0, num2=0, num3=0):#Contructor with 3 properties
        self.num1 = num1 #Assigns paramaters to instance properties
        self.num2 = num2
        self.num3 = num3

    def check_combo(self, num1, num2, num3): #Creates check_combo function for 3 paramaters
        if self.num1 == num1 and self.num2 == num2 and self.num3 == num3: #If all the self.num's are equivalent to num's
            return True #Return True
        else: #Else
            return False #Return False

    def __str__(self): #String method outputs correct comboLock
        output = "Combo: " + str(self.num1) + "," + str(self.num2) + "," + str(self.num3) + "\n"
        return output #Return output
