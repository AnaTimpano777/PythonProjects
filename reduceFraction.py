#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: May 4, 2020
#Decription: This program uses a recursive function to calculate the GCD (Greatest Common Divisor) of two integers

def gcd(a, b): #def gcd function with paramater a and b
    if b == 0: #If b is equal to 0 then 
        return a #return a
    else: #else
        # % is modulus, also known as the remainder function
        return gcd(b, a % b) #Return calc

print("This program simplifies fractions!") #Outputs what the program is to the user
print("")

num = int(input("Please enter the numerator for your fraction: ")) #Gets user input for numerator number and stores as an int in variable num
denom = int(input("Please enter the denominator for your fraction: ")) #Gets user input for denominator number and stores as an int in variable denom

divisor = gcd(num, denom) #Uses gcd function and stores in variable divisor

numR = round(num/divisor) #Calculates the reduced value of num by dividing number by the var divisor and stores result in variable numR (Rounds number)
denomR = round(denom/divisor) #Calculates the reduced value of denom by dividing number by the var divisor and stores result in variable denomR (Rounds number)

print("")
print("The fraction " + str(num) + "/" + str(denom) + " can be reduced to: " + str(numR) + "/" + str(denomR)) #Outputs original input fraction and reduced fraction
