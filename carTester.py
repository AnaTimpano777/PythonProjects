#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 8, 2020
#Decription: This program creates 3 different cars with 6 paramaters with the class file car.py

from car import Car #From file car.py import class Car


print('This is Car Creator, lets make a car!') #Displays intro to program to user
print(' ') #Space
print('--- Car 1 (Computer Generated) ---') #Outputs Car 1 title

# INSTANTIATE (create) car1 without sending any parameters

c1 = Car() 
print(c1)

#INSTANTIATE car2 sending only 4 parameters: make, model, year and price
c2 = Car('Alpha Romeo', '4c', '2007', '25000') #Sets car 2 to first 4 default paramaters

print(' ') #space
print('Now its your turn, start to make car 2!') #Outputs message to user to start making car 2
print(' ') #space
make = input('Give me a make: ') #Asks user to input the first 4 paramaters and assigns each one to their designated variable
model = input('Give me a model: ')
year = input('Give me a year: ')
price = input('Give me a price: $')
c2 = Car(make, model, year, price) #Takes the 4 input values that user inputed in the class Car and sets it to the variable c2
print(' ') #space
print('--- Car 2 ---') #Outputs car 2 title
print(c2) #Outputs all 6 car 2 paramters to user (4 input and last 2 default)

#INSTANTIATE car3 sending all 6 parameters
print(' ') #space
print('Now make car 3 all by yourself!') #Outputs message to make car 3
print(' ') #space
make = input('Give me a make: ') #Asks user to input all 6 paramaters and assigns each one to their designated variable
model = input('Give me a model: ')
year = input('Give me a year: ')
price = input('Give me a price: $')
colour = input('Give me a colour: ')
doors = input('Enter the amount of doors the car has: ')
print(" ") #Space

c3 = Car(make, model, year, price, colour, doors) #Takes the 6 input values that user inputed in the class Car and sets it to the variable c3
print('--- Car 3 ---') #Output car 3 title
print(c3) #Outputs all 6 car paramaters to user

print('Car 3 says: ') #Outputs message to user
#CALL method honk() from object car3
c3.honk()




