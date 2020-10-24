#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: March 13, 2020
#Decription: Game that simulates a life form

import random #Imports random function

print("This program will simulate a simple life form") #Displays to the user what the code is about
print(" ") #space

rows = 20 #Sets variable rows to 20
cols = 20 #sets variable cols to 20
dot = "." #Sets variable dot to the string .

board = [] #Creates a list called board

for i in range(0, rows): #Loops through the rows
    board.append([]) #Appends to list
    for j in range(0, cols): #Loops through the columns
        board[i].append(dot) #appends to index and sets dots



cells = int(input("Enter the number of cells you want to start with:")) #Asks the user the number of cells they want to start with

for i in range(0, cells): #place random cells on board 
    randCol = random.randint(0, 19) 
    randRow = random.randint(0, 19)
    board[randCol][randRow] = "O"

generation = int(0) #Sets variabe generation to 0
continueGame = str("") #Sets variable continueGame to empty string

while continueGame != "2": #While the varibale continueGame is not equal to 2
    board2 = [] #Set variable board2 to an empty list
    print("Generation:", generation) #Displays the generation number
    generation += 1 #Increments generation by 1
    for i in range(0, 20): #Loops through again
        for j in range(0, 20):
            print(board[i][j], end="") #Prints the life cycle again
        print('')
    continueGame = input("\n1 - Advance one generation.\n2 - exit game\n:") # Menu
    if continueGame == "1": # Propagate neighbours
        for i in range(0, 20):
            board2.append([])
            for j in range(0, 20):
                neighbours = int(0)
                board2[i].append(".")
                # count the number of neighbours the cell has
                # Note : check i and j to prevent IndexOutOfBounds Exceptions
                if i > 0 and j > 0:
                    if board[i - 1][j - 1] == "O": # upper left
                        neighbours = neighbours + 1
                if i > 0:
                    if board[i - 1][j] == "O": # upper center
                        neighbours = neighbours + 1
                if i > 0 and j < 19:
                    if board[i - 1][j + 1] == "O": # upper right
                        neighbours = neighbours + 1
                if j > 0:
                    if board[i][j - 1] == "O": # left
                        neighbours = neighbours + 1
                if j < 19:
                    if board[i][j + 1] == "O": # right
                        neighbours = neighbours + 1
                if i < 19 and j > 0:
                    if board[i + 1][j - 1] == "O": # lower left
                        neighbours = neighbours + 1
                if i < 19:
                    if board[i + 1][j] == "O": # lower center
                        neighbours = neighbours + 1
                if i < 19 and j < 19:
                    if board[i + 1][j + 1] == "O": # lower right
                        neighbours = neighbours + 1
                # Determine if the cell in the next generation is alive
                if board[i][j] == "O" and (neighbours == 2 or neighbours == 3):
                    board2[i][j] = "O"
                if board[i][j] == "." and neighbours == 3:
                    board2[i][j] = "O"
        board = board2 # Replace board with the new board
