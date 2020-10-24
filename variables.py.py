#Name: Ana Timpano
#Course Code: ICS3U
#Program Description: This program shows how variables are used in Python

#Declare variable names and assign original values to each variable
firstname = "Ana"
mynum1 = 5
mynum2 = 4
mynum3 = 7
mynum4 = 10
mydecimal = 5.783

# Let’s display some of the information to the screen
print (firstname)
print (mynum1)

# Let’s make some sense of our data and properly display to the user
print ("My name is: " + firstname)
print ("The first number that I entered," + " an integer is: ", mynum1)
print ("The second number that I " + "entered as a double " + "data type is: ", mydecimal)
print ("The third number is: ", mynum3, " and my fourth number is: ", mynum4)
print ("My name is " + firstname + " and my favourite number is: ", mynum3)

# Adding numbers
answer1 = mynum1+mynum2

# Subtracting numbers
answer2 = mynum4 - mynum1

# Multiplying numbers
answer3 = mynum2 * mynum4

# Dividing numbers using the answer3 variable
answer4 = answer3 / mynum2

answer5 = answer3 / mydecimal

# Before printing out our answers, let’s print 2 blank spaces
print (" ")
print (" ")

# Let’s output the information that is stored in each variable 
print ("When I add ", mynum1, " and ", mynum2, "the answer is ", answer1)
print ("Subtracting numbers gave me: ", answer2)
print ("Multiplying my numbers gave me: ", answer3)
print ("Dividing my numbers gave me: ", answer4)
print ("Dividing numbers with a double data type gave me: ", answer5)
