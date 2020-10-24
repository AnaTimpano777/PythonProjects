#Name: Ana Timpano
#Course Code: ICS3UE
#Program Description: Prepares a discount for restaurant bill based on price and calculates the sales tax and tip

print("Restaurant Bill Calculator")#Title
print(" ")#Space
bill = float(input("Enter the price of your bill: "))#User enters bill price
twenty = (bill -(bill / 100) * 20) #20% discount formula
ten = (bill -(bill / 100) * 10) #10% discount formula

if bill > 100:
    print("You get a discount of 20%: ", twenty)
    print("Your total price is: ", round(twenty + (twenty / 100) * 13) + (twenty / 100) * 20),1#Adds discounted price with 13% tax and 20% tip, rounds to 2

if bill > 50 and bill < 100:
    print("You get a discount of 10%: ", ten)
    print("Your total price is: ", round(ten + (ten / 100) * 13) + (ten / 100) * 20),1#Adds discounted price with 13% tax and 20% tip, rounds to 2

if bill < 50:
    print("Your bill has no discount: ", bill)
    print("Your total price is: ",round(bill + (bill / 100) * 13) + (bill / 100) * 20),1#Adds discounted price with 13% tax and 20% tip, rounds to 2






































