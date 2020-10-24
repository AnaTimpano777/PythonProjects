#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: May 4, 2020
#Decription: This program uses a recursive function to find the value of the nth Fibonacci number

def fib(n): #Define function called fib with paramater n
    if (n == 1) or (n == 2): #If n is equivalent to 1 or 2 then
        return 1 #Return 1
    else: #Else
        return fib(n-1) + fib(n-2) #Return the sum of fib(n-1) and fib(n-2)

print("The first nine Fibonacci numbers are listed as follows:") #Outputs first nine fibonacci numbers
print("1, 1, 2, 3, 5, 8, 13, 21, 34, ...")
fibNum = int(input("What Fibonacci term would you like to see?:")) #Gets user input for n and stores as an int in the varibale fibNum
print("The " + str(fibNum) + "th Fibonacci number is", fib(fibNum)) #Ouptuts the term number n and the calculated value of fib(n)
