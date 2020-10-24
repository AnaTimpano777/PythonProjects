#Name: Ana Timpano
#Course Code: ICS3U
#Program Description: This program finds Canada's debt burden 2008, 2009, and 2010

#Assigning the variable for 2007
debt2007 = 481.5

#Sentence that says the numbers are in billion
print ("The numbers that are going to be displayed below have the value of billion")

#Print spaces to make it look nice
print (" ")

#Print Canada's debt in 2007
print ("Canada's debt in 2007 is:", debt2007)

#Print spaces to make it look nice
print (" ")

#Output of the equaion for the debt in 2008
print ("Canada's debt in 2007 is:", debt2007, "If you multiplied it by 0.03 to get 3% of", debt2007, "you would get: {0:3,.1f}".format(debt2007 * 0.03))
print ("To find Canada's debt in 2008, you need to subtract 3% of", debt2007, "from itself. When we do that the answer is: {0:3,.1f}".format(debt2007-debt2007 * 0.03))

#Print spaces to make it look nice
print (" ")

#Assigning the variable for 2008
debt2008 = debt2007-debt2007 * 0.03

#Print Canada's debt in 2008
print ("Canada's debt in 2008 rounded is: {0:3,.1f}".format(debt2008))

#Print spaces to make it look nice
print (" ")

#Output of the equaion for the debt in 2009
print ("Canada's debt in 2008 is: {0:3,.1f}".format(debt2008), "If you multiplied it by 0.03 to get 3% of {0:3,.1f}".format(debt2008), ",the answer would be: {0:3,.1f}".format(debt2008 * 0.03))
print ("To find Canada's debt in 2009, you need to subtract 3% of {0:3,.1f}".format(debt2008), "from itself. When we do that the answer is: {0:3,.1f}".format(debt2008-debt2008 * 0.03))

#Print spaces to make it look nice
print (" ")

#Assigning the variables for 2009
debt2009 = debt2008-debt2008 * 0.03

#Print Canada's debt in 2009
print ("Canada's debt in 2009 rounded is: {0:3,.1f}".format(debt2009))
       
#Print spaces to make it look nice
print (" ")

#Output of the equaion for the debt in 2010
print ("Canada's debt in 2009 is: {0:3,.1f}".format(debt2009), "If you multiplied it by 0.03 to get 3% of {0:3,.1f}".format(debt2009), "you would get: {0:3,.1f}".format(debt2009 * 0.03))
print ("To find Canada's debt in 2010, you need to subtract 3% of {0:3,.1f}".format(debt2009), "from itself. When we do that the answer is: {0:3,.1f}".format(debt2009-debt2009 * 0.03))

#Print spaces to make it look nice
print (" ")

#Assigning the variables for 2010
debt2010 = debt2009-debt2009 * 0.03

#Print Canada's debt in 2010
print ("Canada's debt in 2010 rounded is: {0:3,.1f}".format(debt2010))
