#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: June 2, 2020
#Decription: Program that reads psalms based on each psalms number/order

def binary_search(my_list, left, right, v): #binary_search function with paramaters from the BinarySearchIntro.py in lesson

    if left > right: #If left is greater than right
        return False #Return False

    middle = int((left + right) / 2)
    if my_list[middle] == v: 
        return True

    if v < my_list[middle]:
        return binary_search(my_list, left, middle - 1, v)
    else:
        return binary_search(my_list, middle + 1, right, v)

psalm_numbers = [] #Empty list under variable psalm_numbers
psalm_titles = [] #Empty list under variable psalm_titles


myFile = open("psalms.txt", "r") #Opens text file psalms.txt for reading in var myFile

for i in range(0, 24): #Loop through psalm numbers
    num = int(myFile.readline().replace("\n", "")) #stores the odd numbered lines (psalm #'s) as int in variable num (remove carriage returns)
    psalm_numbers.append(num) #append num to psalm_numbers list
    title = (myFile.readline().replace("\n", "")) # stores even numbered lines as int
    psalm_titles.append(title) #append title to psalm_titles list
    
psalm_num = int(input("What psalm number would you like to see? (1 - 99):")) #Gets user input for what psalm number they would like to see and stores as int in var psalm_num

print("") #space

if binary_search(psalm_numbers, 0, len(psalm_numbers), psalm_num): #if a call to the binary_search() function returns True for psalm_num in list psalm_numbers then:
    print(psalm_num) #Outputs var psalm_num (number user inputed)
    print(psalm_titles[psalm_numbers.index(psalm_num)]) #Outputs psalm_titles[psalm_numbers.index(psalm_num)]

else: #Else
    print(psalm_num) #Output psalm_num (number user inputed)
    print("Not Found") #Output Error message "Not Found"

