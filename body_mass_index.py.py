#Name: Ana Timpano
#Course Code: ICS3UE
#Program Description: Finds the BMI of an individual and determines their risk of health

print("BMI and health risk calculator")#title
print(" ")#space
formula = input("Type in imperial or metric for which formula you would like:") #Asks the user if they want the imperial or metric formula

if formula == "imperial": 
    weight = int(input("Type in your weight in lbs: "))
    height = float(input("Type in your height in inches: "))
    print(" ")
    BMI = (round((weight*703 / height) / height, 1)) #Calculation of BMI
    print(BMI)

    if BMI < 18.5:
        print("Classification: Under weight     Risk of developing health problems: Increased") # All of the if statements determine the classification and risk of health
    if BMI >= 18.5 and BMI <=24.9:
        print("Classification: Normal weight     Risk of developing health problems: Least")
    if BMI >= 25.0 and BMI <= 29.9:
        print("Classification: Over weight     Risk of developing health problems: Increased")
    if BMI >= 30.0 and BMI <= 34.9:
        print("Classification: Obese class 1     Risk of developing health problems: High")
    if BMI >= 35.0 and BMI <=39.9:
        print("Classification: Obese class 2     Risk of developing health problems: Very high")
    if BMI >= 40.0:
        print("Classification: Obese class 3     Risk of developing health problems: Extermely high")

if formula == "metric":

    weightM = int(input("Type in your weight in kg: "))
    heightM = float(input("Type in your height in meters: "))
    print(" ")
    BMIM = (round((weightM / heightM) / heightM, 1))#Calculation of BMI
    print(BMIM)

    if BMIM < 18.5:
        print("Classification: Under weight     Risk of developing health problems: Increased")# All of the if statements determine the classification and risk of health
    if BMIM >= 18.5 and BMIM <=24.9:
        print("Classification: Normal weight     Risk of developing health problems: Least")
    if BMIM >= 25.0 and BMIM <= 29.9:
        print("Classification: Over weight     Risk of developing health problems: Increased")
    if BMIM >= 30.0 and BMIM <= 34.9:
        print("Classification: Obese class 1     Risk of developing health problems: High")
    if BMIM >= 35.0 and BMIM <=39.9:
        print("Classification: Obese class 2     Risk of developing health problems: Very high")
    if BMIM >= 40.0:
        print("Classification: Obese class 3     Risk of developing health problems: Extermely high")







