import sys
import os
import numpy
import time
import random
#====================================================
boardSizeX = 60
boardSizeY = 30
#Run for X number of generations. 
generations = 10
#2D board for holding our little world. 
gameBoard = [[random.choice('0001') for i in range(boardSizeX)] for j in range(boardSizeY)]

clear = lambda: os.system('cls')
#====================================================
#Creates our game board header with a dynamic centering title. Woo!
def printBoardHeader():
    title = "Conway's Game of Life"
    createSoldRow()
    extraWhileSpace =  boardSizeX - len(title)
    
    #Board is too big for our title. 
    if(extraWhileSpace < 0):
        print("Gen:"+str(generations))
    else:
        #This is our title. 
        #Check if odd
        if(extraWhileSpace % 2 != 0):
            sys.stdout.write(" ")
            extraWhileSpace = extraWhileSpace - 1

        halfOfWhiteSpace = extraWhileSpace / 2
        sys.stdout.write(' '*int(halfOfWhiteSpace))
        sys.stdout.write(title)
        sys.stdout.write(' '*int(halfOfWhiteSpace)+"\n")

        #This is our generation title. 
        extraWhileSpace =  boardSizeX - len("generations left:"+str(generations))
        if(extraWhileSpace % 2 != 0):
            sys.stdout.write(" ")
            extraWhileSpace = extraWhileSpace - 1
        #I assume there is a cleaner way to do this but I'm short on time. 
        halfOfWhiteSpace = extraWhileSpace / 2
        sys.stdout.write(' '*int(halfOfWhiteSpace))
        sys.stdout.write("Generations left:"+str(generations))
        sys.stdout.write(' '*int(halfOfWhiteSpace)+"\n")

    


#Create a sold boarder row
def createSoldRow():
    sys.stdout.write("+")
    sys.stdout.write("="*boardSizeX)
    sys.stdout.write("+\n")


        

#Creates a random row of populated/empty cells 
def randomCell(x,y):
    if(random() < 0.3):
        sys.stdout.write("#")
        gameBoard[y][x] = "1" #Living
    else:
        sys.stdout.write(".")
        gameBoard[y][x] = "0" #Dead

#Prints the board. 
def printBoard():
    #Looping through the Y states printing each line as we go. 
    createSoldRow()
    for y in range (0,boardSizeY):
        sys.stdout.write("=")
        for x in range (0,boardSizeX):
            if(int(gameBoard[y][x]) == 1):
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        sys.stdout.write("=\n")
    createSoldRow()

#The bread and butter of our funtion updates our board.
def updateBoardState():
    #Loop through every cell in our board and updates their state.
    for y in range (0,boardSizeY):
        for x in range (0,boardSizeX):
            updateCell(x, y)

#This funtion handles all the edge cases on the board. 
def updateCell(x,y):
    #First, we are going to grab the number of living sells around us
    livingCells = 0

    #We first need to check to see if the cells around us out of bounds.
    # (-x,-y)   (x,-y)   (+x,-y)
    # (-x,y)    (Home)   (+x,y) 
    # (-x,+y)  (x,+y)    (+x,+y)

    negX = x - 1
    negY = y - 1
    posX = x + 1
    posY = y + 1

    if(negX != -1): #This handles our -x cases
        if(negY != -1):
            #This is (-x,-y)
            livingCells = livingCells + int(gameBoard[negY][negX])            

        if(posY != boardSizeY):
            #This is (-x,+y)
            livingCells = livingCells + int(gameBoard[posY][negX])
           
        #This is (-x,y) 
        livingCells = livingCells + int(gameBoard[y][negX])

    if(posX != boardSizeX): #This handles our +x cases
        if(negY != -1):
            #This is (+x,-y)
            livingCells = livingCells + int(gameBoard[negY][posX])         

        if(posY != boardSizeY):
            #This is (+x,+y)
            livingCells = livingCells + int(gameBoard[posY][posX])

        #This is (+x,y) 
        livingCells = livingCells + int(gameBoard[y][posX])

    if(negY != -1): #(x,-y) 
        livingCells = livingCells + int(gameBoard[negY][x])

    if(posY != boardSizeY): #(x,+y)
        livingCells = livingCells + int(gameBoard[posY][x])

    boolAlive = gameBoard[y][x]
    #Checks to see if a cell is living.
    if(isLiving(livingCells,boolAlive) == True):
        gameBoard[y][x] = 1
    else:
        gameBoard[y][x] = 0
    return;
#Handles the check to see if a cell is living or not. 
def isLiving(livingCells, boolAlive):
    #Any live cell...
    if(boolAlive == True):
        #with fewer than two live neighbours dies
        if(livingCells < 2):
            return False;
        #with two or three live neighbours lives
        if((livingCells) == 2 or (livingCells == 3)):
            return True;
        #with more than three live neighbours dies
        else:
            return False;
    #Any dead cell...        
    else:
        #exactly three live neighbours becomes a live cell
        if(livingCells == 3):
            return True;
        else:
            return False;
#====================================================
clear() #Clears the terminal. 
printBoardHeader()
printBoard()

while (generations != 0):
    generations = generations - 1
    time.sleep(2)
    clear() #Clears the terminal.
    updateBoardState()
    printBoardHeader()
    printBoard()