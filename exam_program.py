#Ana Timpano
#Course Code: ISC3UE
#Program Description: Creates a reciept for the user who is buying photos / art work

orderAgain = "y" #orderAgain is set equal to y so the while loop can run

mouse = 9.99 #variable mouse is set equal to the price of the product
wall = 34.99 #variable wall is set equal to the price of the product
magnet = 2.99 #variable magnet is set equal to the price of the product

mouseQuantity = 0 #Setting the quantity of all of the products to 0
wallQuantity = 0
magnetQuantity = 0

while orderAgain == "y": #While variable orderAgain is equal to y (yes) keep running the loop
    
    print(" ")
    print("Welcome to the custom photos and artwork store!") #Intro to store
    print(" ")
    print("Today we have three products for sale. We have photos on mouse pads - $9.99 each, photo wall art - $34.99 each, and photo magnets - $2.99 each!") #Selection of products
    print(" ")
    print("If you purchase more than 5 products you will recieve a discount of 10%(before tax)") #Notifies user that they get a 10% discount if above 5 items
    print(" ")

    mouseAmount = int(input("Enter the amount of mouse pads you would like to buy: ")) #Asks the user to enter the amount of mouse pads they want to buy and sets it to the variable mouseAmount
    mouseQuantity = mouseQuantity + mouseAmount #Updates the quantity of the mouse pads plus the mouse Amount
    mouseTotal = mouse * mouseAmount #Sets the mouse pad total to the variable mouse multiplied by the mouse amount
    print(" ")

    wallAmount = int(input("Enter the amount of wall art you would like to buy: ")) #Asks the user to enter the amount of wall art they want to buy and sets it to the variable wallAmount
    wallQuantity = wallQuantity + wallAmount #Updates the quantity of the wall art plus the wall Amount
    wallTotal = wall * wallAmount #Sets the wall art total to the variable wall multiplied by the wall amount
    print(" ")

    magnetAmount = int(input("Enter the amount of magnets you would like to buy: ")) #Asks the user to enter the amount of magnets they want to buy and sets it to the variable magnetAmount
    magnetQuantity = magnetQuantity + magnetAmount #Updates the quantity of the magnets plus the magnet Amount
    magnetTotal = magnet * magnetAmount #Sets the magnets total to the variable magnet multiplied by the magnet amount
    print(" ")

    price = mouseTotal + wallTotal + magnetTotal #Sets variable price to all of the totals added together

    if mouseQuantity + wallQuantity + magnetQuantity > 5:#If all the products quanity is greater than 5
        print(" ")
        print("You get a discount of 10% for ordering more than 5 items!") #Tells user they get a discount
        price = price - (price * 0.10) #Updates the price to the price subtract 10% of the price

        print(" ")
        name = str(input("Please enter your first and last name: ")) #Asks user to enter their name
        print(" ")
        print("Reciept") #Prints reciept
        print(name)
        print(" ")
        print("Mouse pads = ",mouseQuantity, " Price: ",mouseTotal) #Shows user their quantity and price of products
        print("Wall art = ",wallQuantity, "   Price: ",wallTotal)
        print("Magnets = ",magnetQuantity, "    Price: ",magnetTotal)
        print(" ")
        print("10% discount added before tax")
        print(" ")
        print("Subtotal: {0:3,.2f}".format(price)) #Shows user their subtotal and formats it to 2 decimal places
        print(" ")
        print("Tax is 13%")
        print("HST : {0:3,.2f}".format(price * 0.13)) #Shows user their HST / tax and formats it to 2 decimal places
        print(" ")
        totalPrice = price + (price * 0.13) #Creates variable of the total price with tax
        print("Total Price: {0:3,.2f}".format(totalPrice)) #SHows user their total price formated to 2 decimal places
        print(" ")
        orderAgain = str(input("Would you like to place another order? [Y] for yes or [N]for no: ")).lower() #Ass user if they want to order again


    else:
        print(" ")
        name = str(input("Please enter your first and last name: ")) #Asks user to enter their name
        print(" ")
        print("Reciept") #Prints recept
        print(name)#prints name
        print(" ")
        print("Mouse pads = ",mouseQuantity, " Price: ",mouseTotal) #Prints the products quantity and prices
        print("Wall art = ",wallQuantity, "   Price: ",wallTotal)
        print("Magnets = ",magnetQuantity, "    Price: ",magnetTotal)
        print(" ")
        print("Subtotal: {0:3,.2f}".format(price)) #Shows user their subtotal and formats it to 2 decimal places
        print(" ")
        print("Tax is 13%")
        print("HST : {0:3,.2f}".format(price * 0.13)) #Shows user their ax / HST and formats it to 2 decimal places
        print(" ")
        totalPrice = price + (price * 0.13) #Creates variable total price with the price plus the tax
        print("Total Price: {0:3,.2f}".format(totalPrice)) #SHows user their total price and formats it to 2 decimal places
        orderAgain = str(input("Would you like to place another order? [Y] for yes or [N]for no: ")).lower()#Asks user if they would like to place another order

if orderAgain == "y": #If order again is equal to y (The user does want to order again)
    print(" ") #Prints a space and goes back to the start of the while statement

else: #Else if the user does not want to place another order
    print(" ")
    print("Have a good day! Come again!") #Tells user to have a good day and come again
    
