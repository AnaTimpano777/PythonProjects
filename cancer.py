#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: May 19, 2020
#Decription: Program that simulates a life form of cancer and gets rid of it

def flood_fill(row, col): #Function called flood_fill with paramters row and col
    if grid[row][col] == "-":
        grid[row][col] = " "
        flood_fill(row - 1, col - 1)
        flood_fill(row - 1, col)
        flood_fill(row - 1, col + 1)
        flood_fill(row, col - 1)
        flood_fill(row, col + 1)
        flood_fill(row + 1, col - 1)
        flood_fill(row + 1, col)
        flood_fill(row + 1, col + 1)

def display_grid(): #Function called display_grid
    output = "" #Set var output to empty string
    for row in range(0, 15): #Loops through 0 to 15 rows
        for col in range(0, 15): #Loops through 0 to 15 columns
            output += grid[row][col] #Var output adds var grid with row and col
        output += "\n" #Formats output
    print(output) #Outputs var output

rows = 15 #Set var rows to 15
cols = 15 #Set var cols to 15
tempData = "" #Set var tempData to empty string

grid = [] #Empty list in var grid
for i in range(0, rows): #Loops through rows
    grid.append([]) #Appends to grid list
    for j in range(0, cols): #Loops through cols
        grid[i].append(tempData) #Appends to grid list with tempData

numBlobs = 0 #Sets numBlobs to 0

myFile = open("cancer.txt", "r") #Opens text file cancer.txt for reading in var myFile

for i in range(0, rows): #Loop through rows
        myLine = myFile.readline() #Reads through each line in txt file
        for j in range(0, cols): #Loops through cols
            grid[i][j] = str(myLine[j])

display_grid() #Calls function display_grid

for row in range(1, 14): #search through the list and count blobs of cancer
    for col in range(1, 14):
        if grid[row][col] == "-":
            flood_fill(row, col)
            numBlobs += 1
            
print("") #Space
            
print("The file has", numBlobs, "cancer spots in it.") #Outputs to the user how many numBlobs there are
print("The new grid is:") #Outputs to user indicating what the new grid is
print(" ") #space
display_grid() #Calls function display_grid()
       
