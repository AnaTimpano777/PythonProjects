#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: June 11, 2020
#Decription: program that will sort a list of random numbers using the 4 sorting routines

import random #Imports random function

#Sorts numbers in ascending order using selction_sort function

def asc_selection_sort(data):
    for i in range(0, len(data)):
        smallest = i
        # see if there is a smaller number further in the list
        for index in range(i + 1, len(data)):
            if data[index] < data[smallest]:
                smallest = index
        swap(data, i, smallest)

#Sorts numbers in descending order using selction_sort function
        
def dsc_selection_sort(data):
    for i in range(0, len(data)):
        smallest = i
        # see if there is a smaller number further in the list
        for index in range(i + 1, len(data)):
            if data[index] > data[smallest]:
                smallest = index
        swap(data, i, smallest)

#swap function that helps order numbers for the other functions
def swap(data, first, second):
    hold = data[first]
    data[first] = data[second]
    data[second] = hold

#Sorts numbers in ascending order using bubble_sort function

def asc_bubble_sort(data):
# Loop to control number of passes
    for i in range(1, len(data)):
        # Loop to control number of comparisons for length of list-1
        for element in range(0, len(data) - 1):
            # compare side-by-side elements and swap them if first element is
            # greater than second element
            if data[element] > data[element + 1]:
                swap(data, element, element + 1)  # call swap method

#Sorts numbers in descending order using bubble_sort function

def dsc_bubble_sort(data):
# Loop to control number of passes
    for i in range(1, len(data)):
        # Loop to control number of comparisons for length of list-1
        for element in range(0, len(data) - 1):
            # compare side-by-side elements and swap them if first element is
            # greater than second element
            if data[element] < data[element + 1]:
                swap(data, element, element + 1)  # call swap method

#Sorts numbers in ascending order using insertion_sort function
                
def asc_insertion_sort(data):
    for next_item in range(1, len(data)):
        insert = data[next_item]
        move_item = next_item

        while (move_item > 0) and (data[move_item - 1] > insert):
            data[move_item] = data[move_item - 1]
            move_item -= 1
        data[move_item] = insert

#Sorts numbers in descending order using insertion_sort function
        
def dsc_insertion_sort(data):
    for next_item in range(1, len(data)):
        insert = data[next_item]
        move_item = next_item

        while (move_item > 0) and (data[move_item - 1] < insert):
            data[move_item] = data[move_item - 1]
            move_item -= 1
        data[move_item] = insert

#Sorts numbers in ascending order using quick_sort function
        
def asc_quick_sort(data, low, high):
    if low < high:
        partition_loc = asc_partition(data, low, high)
        asc_quick_sort(data, low, partition_loc - 1)
        asc_quick_sort(data, partition_loc + 1, high)

#Sorts numbers in descending order using quick_sort function
        
def dsc_quick_sort(data, low, high):
    if low < high:
        partition_loc = dsc_partition(data, low, high)
        dsc_quick_sort(data, low, partition_loc - 1)
        dsc_quick_sort(data, partition_loc + 1, high)

#Sorts numbers in ascending order using asc_partiton function through asc_quick_sort function
        
def asc_partition(data2, left, right):
    move_left = True
    separator = data2[left]

    while left < right:
        if move_left == True:
            while (data2[right] >= separator) and (left < right):
                right -= 1
            data2[left] = data2[right]
            move_left = False
        else:
            while (data2[left] <= separator) and (left < right):
                left += 1
            data2[right] = data2[left]
            move_left = True
    data2[left] = separator
    return left

#Sorts numbers in descending order using dsc_partiton function through dsc_quick_sort function

def dsc_partition(data2, left, right):
    move_left = True
    separator = data2[left]

    while left < right:
        if move_left == True:
            while (data2[right] <= separator) and (left < right):
                right -= 1
            data2[left] = data2[right]
            move_left = False
        else:
            while (data2[left] >= separator) and (left < right):
                left += 1
            data2[right] = data2[left]
            move_left = True
    data2[left] = separator
    return left

list_size = int(input("How many random numbers do you wish to generate?:")) #Gets user input for how many numbers they want to generate and stores as int in variable list_size

nums = [] #create empty list called nums

for i in range(0, list_size):#For loop from 0 to the amount of numbers the user inputed (list_size)
    nums.append(random.randint(0, 1000)) #generates list_size amount of random numbers form 0 to 1000

#Outputs the unsorted list, nums, with no brackets and spaces instead of commas
print("")
print("The unsorted list is:") 
print(*nums, sep =' ') 

#Outputs to user what type of sort they want to perform
print(" ")
print("What type of sort would you like to perform?")
print("1 - Selection Sort")
print("2 - Bubble Sort")
print("3 - Insertion Sort")
print("4 - Quick Sort")
print("")

sort_method = int(input("Enter Sort Number: ")) #Gets user input for the sort method and stores as int in variable sort_method

#Outputs to user what order they want the numbers sorted (asc or dsc)
print("")
print("In what order do you want the numbers sorted?")
print("1 - Ascending")
print("2 - Descending")
print("")

sort_order = int(input("Enter Order Number:")) #Gets user input for the order method and stores as int in variable sort_order
print("")

if sort_method == 1: #If sort method is equal to 1 (selction sort method)
    if sort_order == 1: #If sort order is equal to 1 (ascending)
        print("Performing Ascending Selection Sort") #Output to user that list is undergoing ascending selection
        asc_selection_sort(nums)#Calls function and applies to nums list
    elif sort_order == 2: #If sort order is equal to 2 (descending)
        print("Performing Descending Selection Sort") #Output to user that list is undergoing descending selection
        dsc_selection_sort(nums) #Calls function and applies to nums list
        
if sort_method == 2: #If sort method is equal to 2 (bubble sort method)
    if sort_order == 1: #If sort order is equal to 1 (ascending)
        print("Performing Ascending Selection Sort") #Output to user that list is undergoing ascending selection
        asc_bubble_sort(nums) #Calls function and applies to nums list
    elif sort_order == 2: #If sort order is equal to 2 (descending)
        print("Performing Descending Selection Sort") #Output to user that list is undergoing descending selection
        dsc_bubble_sort(nums) #Calls function and applies to nums list

if sort_method == 3: #If sort method is equal to 3 (insertion sort method)
    if sort_order == 1: #If sort order is equal to 1 (ascending)
        print("Performing Ascending Selection Sort") #Output to user that list is undergoing ascending selection
        asc_insertion_sort(nums) #Calls function and applies to nums list
    elif sort_order == 2: #If sort order is equal to 2 (descending)
        print("Performing Descending Selection Sort") #Output to user that list is undergoing descending selection
        dsc_insertion_sort(nums) #Calls function and applies to nums list

if sort_method == 4: #If sort method is equal to 4 (quick sort method)
    if sort_order == 1: #If sort order is equal to 1 (ascending)
        print("Performing Ascending Selection Sort") #Output to user that list is undergoing ascending selection
        asc_quick_sort(nums, 0, len(nums)-1) #Calls function and applies to nums list
    elif sort_order == 2: #If sort order is equal to 2 (descending)
        print("Performing Descending Selection Sort") #Output to user that list is undergoing descending selection
        dsc_quick_sort(nums, 0, len(nums)-1) #Calls function and applies to nums list

print(*nums, sep=" ") #Print ordered list nums with no brackets and spaces instead of commas

