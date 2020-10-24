#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: April 14, 2020
#Decription: This program mimics two dogs meeting and based on their aggression and hunger if they will be friendly or not (Class file = Dog.py)

# Dog.py

from Dog import Dog #Imports class Dog from file Dog.py

import random #Imports random

print('Two dogs will be created') #Explains code to user
inputName = input('Enter the name of the first dog: ') #Asks user for dog1's name
inputBreed = input('Enter the breed of the first dog: ') #Asks user for dog1's breed
print(' ') #space

aggression = random.randint(1, 10) #Picks a random number from 1 to 10 and sets it to the variable aggression
hunger = random.randint(1, 10) #Picks a random number from 1 to 10 and sets it to the variable hunger

dog1 = Dog(inputName, inputBreed, aggression, hunger) #Instantiates dog1 with 4 paramaters

inputName = input('Enter the name of the second dog: ') #Asks user for dog2's name
inputBreed = input('Enter the breed of the second dog: ') #Asks user for dog2's breed
print(' ') #space

aggression = random.randint(1, 10)#Picks a random number from 1 to 10 and sets it to the variable aggression
hunger = random.randint(1, 10) #Picks a random number from 1 to 10 and sets it to the variable hunger

dog2 = Dog(inputName, inputBreed, aggression, hunger) #Instantiates dog2 with 4 paramaters

print(dog1) #Prints dog1
print(' ') #space

print('Is', dog1.name, "'s aggression okay?") #Asks user if dog1's agression is okay
print('1 - Yes')
print('2 - No')
myInput = int(input('Enter number: ')) #Gets user input yes/no and sets it to var myInput
print(' ') #space

if myInput == 2: #If myInput is equal to 2 (No)
    newAgg = input(f'Enter {dog1.name}\'s new aggression level (1-10): ') #Asks user for new aggression number
    print(' ') #space
    dog1.aggression = newAgg #Sets dog1's aggression to new aggression

print('Is', dog1.name, "'s hunger okay?") #Asks user if dog1's hunger is okay
print('1 - Yes')
print('2 - No')
myInput = int(input('Enter number: ')) #Gets user input yes/no and sets it o var myInput
print(' ') #space

if myInput == 2: #If my input is equal to 2 (No)
    newHunger = input(f'Enter {dog1.name}\'s new hunger level (1-10): ')#Asks user for new hunger number
    print(' ') #space
    dog1.hunger = newHunger #Sets dog1's hunger to new hunger

    

print(dog1)#Output dog1
print(' ')
print(dog2) #Output dog2
print(' ')

print('Is', dog2.name, "'s aggression okay?") #Asks user if dog2's aggression is okay
print('1 - Yes')
print('2 - No')
myInput = int(input('Enter number: ')) #Gets user input yes/no and sets it to var myInput
print(' ') #space

if myInput == 2: #If myInput is equal to 2 (No)
    newAgg = input(f'Enter {dog2.name}\'s new aggression level (1-10): ') #Asks user for new aggression number
    print(' ') #Space
    dog2.aggression = newAgg #Sets dog2's aggression to new aggression

print('Is', dog2.name, "'s hunger okay?") #Asks user if dog2's hunger is okay
print('1 - Yes')
print('2 - No')
myInput = int(input('Enter number: ')) #Gets user input yes/no and sets it to var myInput
print(' ') #space

if myInput == 2: #If myinput is equal to 2 (No)
    newHunger = input(f'Enter {dog1.name}\'s new hunger level (1-10): ')#Asks user for new hunger number
    print(' ') #Space
    dog2.hunger = newHunger #Sets dog2's hunger to new hunger

print(dog2) #Outputs dog2
print(' ') 

print(dog1.name + " and " + dog2.name + " meet") #Tells user that both dogs meet

if int(dog1.aggression) > 5 and int(dog2.aggression) < 5: #If dog1's aggression is greater than 5 and dog2's aggression is less than 5
    print(dog1.name,':') #Outputs dog1 name
    dog1.bark_angry() #Calls angry bark function
    print(dog2.name, 'runs away!') #Outputs that dog2 runs away

elif int(dog2.aggression) > 5 and int(dog1.aggression) < 5: #If dog2's aggression is greater than 5 and dog1's aggression is less than 5
    print(dog2.name,':') #Ouputs dog2 name
    dog2.bark_angry() #Calls angry bark function
    print(dog1.name, 'runs away!') #Outputs that dog1 runs away

elif int(dog1.aggression) < 5 and int(dog2.aggression) < 5: #If dog1's aggression is less than 5 and dog2's aggression is less than 5
    print(dog1.name,':') #Outputs dog1's name
    dog1.bark_friendly() #Calls friendly bark function
    print(dog2.name,':') #Outputs dog2's name
    dog2.bark_friendly() #Outputs friendly bark function

else: #Else
    print(dog1.name,':') #outputs dog1's name
    dog1.bark_angry() #Calls angry bark function
    print(dog2.name,':') #Outputs dog2's name
    dog2.bark_angry() #Calls angry bark function

    if dog1.hunger > dog2.hunger: #If dog1's hunger is greater than dog2's hunger
        print(dog1.name, 'bites', dog2.name) #Output that dog1 bites dog2
    if dog2.hunger > dog1.hunger: #If dog2's hunger is greater than dog1's hunger
        print(dog2.name, 'bites', dog1.name) #Output that dog2 bites dog1
        
    else: #Else
        print(" ") #Outputs that both dogs are equally aggressive and want to fight
        print("Both dogs are equally hungry and equally aggressive.")
        print("The dogs circle each other to fight...")
        print(" ")
        print("The owner of the dog shakes a can of treats and the dogs snap out of it") #Outputs that the owner shakes treates
        dog1.aggression = 0 #Sets dogs aggression number to 0
        dog2.aggression = 0
        print("The dogs are enjoying a treat together!") #Output that the dogs enjoy the treats
        dog1.hunger = 0 #Sets dogs hunger number to 0
        dog2.hunger = 0
        
