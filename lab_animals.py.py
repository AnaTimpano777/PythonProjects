#Name: Ana Timpano
#Course Code: ISC3UE
#Program Description: this code calculates the annual compound investment based on the users input

print("Lab Animals")#Title
print(" ")#space
print("At present there are X animals in the lab and enough food for Y animals. At the end of every hour the population doubles, and enough food is added to support Z more animals. During any hour the animals will eat enough food for only themselves. This program will determine when the population will outgrow the food supply.")
print(" ")

population = int(input("Enter the initial animal population (X): "))
food = int(input("Enter the initial food supply (Y): "))
amountf = int(input("Enter the amount of food added each hour (Z): "))

Animalend = population #Setting the population to a new variable
Foodend = food #Setting the food to a new variable
print(" ")
print(" ")

print ("{0:14}\t{1:14}\t{2:16}\t{3:15}\t{4:18}".format("Hour", "Animals at Start", "Food at Start", "Food at End", "Animals at End")) #Formats the title of the table

for i in range (1,25): #1-24 for hours(1 day)
    
    hour = i

    Foodend = (round(food + amountf - population ,2)) #Equation for finding the Food at end
    
    Animalend = (round(population *2  ,2))#Equation for the Animals at end

    print ("{0:<14}\t{1:<18}\t{2:<18}\t{3:<15}\t{4:<2}".format(hour,population,food,Foodend,Animalend)) #Formats the numbers under the table

    food = (round(food + amountf - population ,2)) #Equation for finding food at start

    population = (round(population * 2 ,2)) #Equation for incrementing the animals at start

    print(" ")#space
    
    if population > Foodend:
        print("By hour", hour, "the population outgrows the food supply") #If statement that determines when the population outgrows the food supply
        break #Stops the code when if statement is true



    






    

