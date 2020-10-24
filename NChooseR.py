#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: May 4, 2020
#Decription: This program uses a recursive function to calculate n! (n factorial)

print("This program will calculate the number of ways to choose r different objects from a set of n objects.") #Output what the program is to the user

def fact(n): #Def fact function with paramater n
    if (n == 0) or (n == 1): #If n is equivalent to 0 or 1 then
        return 1 #return 1
    else: #else
        return n * fact(n - 1) #return calculation

def choose(n,r): #def choose function with paramaters n and r
    return int(fact(n)/(fact(r)*fact(n-r))) #return the result of (n)!/((r)!*(n-r)!) as an integer (using a fact function call for each of the 3 factorials in the equation)

r = int(input("How many objects would you like to choose?:")) #get user input for the number of objects to choose and store as an int in variable r
n = int(input("How many objects are there to choose from?:")) #get user input for the total number of objects to choose from and store as an int in variable n

c = choose(n,r)#use the choose function to calculate C(n,r) and store in variable c

print("There are " + str(c) + " ways to choose " + str(r) + " objects from a set of " + str(n) + " objects.") #Output final product to user

