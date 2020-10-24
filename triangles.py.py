#Name: Ana
#Course Code: ICS3UE
#Program Description: Asks the user for 3 values and will tell the user if the 3 values make a triangle.
#Program Description(2): If the 3 sides are a triangle, the program then determines whether the triangle is a right-angled triangle or not.


print("Triangle?")#title
print(" ")#space
sideA = int(input("Enter the value of side A: "))
sideB = int(input("Enter the value of side B: "))
sideC = int(input("Enter the value of side C: "))

if sideA + sideB > sideC and sideB + sideC > sideA and sideA + sideC > sideB:
    print("Congrats, you made a triangle")
else:
    print("Sorry, your 3 values don't make a triangle")

#Code that determines if the tringle is a right triangle

if sideA**2 + sideB**2 == sideC**2 or sideA**2 + sideC**2 == sideB**2 or sideC**2 + sideB**2 == sideA**2:
    print("The triangle is a right triangle")
else:
    print("This triangle is not a right triangle")
