#Name: Ana Timpano
#Course Code: ICS3UE
#Program Description: This program will print a table that converts ounces to grams from 1 - 15

print("Ounces to Grams") #Title
print("1 ounce = 28.35 grams") #Shows the user that 1 ounce = 28.35 grams
print(" ")
print ("{0:7}\t{1:18}".format("Ounces", "Grams")) #Formats the titles of the table

for i in range (1,16): #Converts ounces to grams until 15
    ounces = i
    grams = float(round(i * 28.35 ,2))#Equation for ounces to grams, rounded to 2 decimal places
    print ("{0:<7}\t{1:<30}".format(ounces,grams)) #Formats the numbers under the titles
