# Author : Mariam Elwa
# Date : 22 October 2022

#This program creates a drawing of an optical illusion using the turtle module.

#The moveTurtle procedure moves the turtle forward by xPos pixels on the
#x-axis and up by yPos pixels on the y axis, from its current position.
def moveTurtle(xPos,yPos):
    pu(); fd(xPos); lt(90); fd(yPos); rt(90); pd()
    
#The drawLines procedure draws the lines that will help us represent the rows.
def drawLines(nbOfRows,squaresPerRow, squareSize):
    lineSize=1 #size of line in pixels
    pensize(lineSize)
    pencolor(0.4,0.4,0.4) #set the color of the square
    width=squareSize* squaresPerRow*2
    height=squareSize*(nbOfRows+1) #because we have nbOfRows+1 lines
    
    for _ in range(nbOfRows+1): # draw nbOfRows+1 lines
        fd(width) #draw line of length width
        
        #go back to the start of the line then go down to draw the next line
        moveTurtle(-width, -squareSize)
        
    moveTurtle(0,height) #set back to initial position
    
#The drawSquares procedure draws the squares in each row.

def drawSquares(nbOfRows,squaresPerRow, squareSize):
    pencolor(0,0,0) #the squares are black
    pensize(squareSize) #fill the square
    
    for i in range(nbOfRows): # for each row
        
        #Get the starting coefficient given the number of the row
        if (i%2==0):
            startingCoeff= 1/2
        if (i%4==1):
            startingCoeff= 3/4
        if (i%4==3):
            startingCoeff= 1/4
                    
        #get respective gap for each row
        startingSquare=squareSize*startingCoeff
        
        #position of the turtle in the middle of the corresponding row
        YPos=-(i+1/2)*squareSize
        
        #move turtle to the middle of the left side of the first square of/
        #the corresponding row
        moveTurtle(startingSquare,YPos)
        
        for j in range(squaresPerRow): # for each square per row
            fd(squareSize) #draw black square
            moveTurtle(squareSize,0) #leave an empty space
        
        #turtle position on the x-axis once all squares of the row are drawn
        finalXPos=-2*squaresPerRow*squareSize-startingSquare
        
        #move turtle to the top left corner of the drawing
        moveTurtle(finalXPos,-YPos)
        
#The illusion procedure creates a drawing of an optical illusion.
#The drawing's top left corner is located at the initial position of the turtle
#The function takes as input nbOfRows, squaresPerRow, squareSize
def illusion(nbOfRows, squaresPerRow, squareSize):
    
    #draw lines to represent the rows
    drawLines(nbOfRows, squaresPerRow, squareSize)
    #draw squares with different starting points to give an illusion effect
    drawSquares(nbOfRows, squaresPerRow, squareSize)