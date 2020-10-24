#Name: Ana Timpano
#Course Code: ICS3U
#Program Description: This program finds the area and perimiter of a rectangle

#Assigning variables
length = int(input("Enter the Length of the rectangle: "))
width = int(input("Enter the Width of the rectangle: "))

#Output of the equation for the perimiter of a rectangle
print ("The perimiter of the rectangle is", length, "multiplied by 2 plus", width, "multiplied by 2")
print ("Therefore the perimiter is:", length * 2 + width * 2 )

#Print spaces to make the outcome look nice
print (" ")

#Output of the equation for the area of a rectangle
print ("The area of the rectangle is", length, "multiplied by", width)
print ("Therefore the area is:", length * width )

#Print spaces to make it look nice
print (" ")

#Equation to find the circumference of a circle
radius = int(input("Enter the Radius of the circle: "))
print ("The circumference of a circle is: {0:2,.2f}".format(2 * 3.14 * radius))
