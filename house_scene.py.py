#Name: Ana Timpano
#Program Description: Using turtles this program will draw a house scene with trees, mountains, hills, and a house
#Course Code: ICS3UE

import turtle

wn = turtle.Screen() #Creates graphics window for turtle
wn.bgcolor("lightblue") #Sets background colour to light blue

joe = turtle.Turtle() #Imports turtle named joe
joe.color("lightgreen") #Makes joe light green
joe.pensize(200) #Sets the width of the pen/line

joe.up()         #Moves joe to a new position without drawing a line
joe.left(180)
joe.forward(377)
joe.left(90)
joe.forward(250)
joe.down()

joe.left(90)      #Draws straight line  
joe.forward(740)



jeff = turtle.Turtle() #Imports turtle named Jeff
jeff.color("grey") #Makes turtle grey colour
jeff.pensize(5) #Sets width of pen/line

jeff.up()         #Moves jeff to a new position without drawing a line
jeff.left(180)
jeff.forward(470)
jeff.left(90)
jeff.forward(150)
jeff.down()

jeff.right(200) #Changes the angle of jeff before the loop

jeff.begin_fill()   #Fills mountains in with colour
for i in [0,1,2]:       #Repeats 3 times, creates 3 mountains
    jeff.forward(460)
    jeff.right(140)
    jeff.forward(460)
    jeff.right(110)
    jeff.forward(315)
    jeff.right(180)
    jeff.forward(315)
    jeff.left(70)
jeff.end_fill()     #Fills mountains in with colour



dan = turtle.Turtle()#Imports turtle named dan
dan.color("white")#Makes dan white colour
dan.pensize(10)#Sets width of pen/line

dan.up()        #Changes position of dan without drawing a line
dan.left(90)
dan.forward(220)
dan.left(90)
dan.forward(335)
dan.right(110)
dan.down()

dan.begin_fill()    #Fills in drawing with same colour
for i in [0,1,2]:   #Repeats loop 3 times
    dan.forward(65) #Draws snow on mountains
    dan.right(140)
    dan.forward(65)
    dan.right(110)
    dan.forward(45)
    dan.up()
    dan.right(180)
    dan.forward(315)
    dan.left(70)
    dan.down()
dan.end_fill()



alex = turtle.Turtle() #Imports turtle named alex
alex.color("lightyellow")#Makes alex a lightbrown colour
alex.pensize(45) #Sets the width of the pen/line

alex.up()       #Moves alex to a new position without drawing a line
alex.right(90)
alex.forward(150)
alex.right(90)
alex.forward(50)
alex.down()

alex.begin_fill() #Fills in space with same colour
for i in [0,1,2,3]: #Repeat four times
    alex.right(90)      #Creates a square
    alex.forward(100)
alex.end_fill()



bob = turtle.Turtle() #Imports turtle named bob
bob.color("brown")#Makes bob brown
bob.pensize(10)#Sets width of the pen/line

bob.up()        #Moves bob to a new position
bob.right(90)
bob.forward(35)
bob.right(90)
bob.forward(100)
bob.down()

bob.begin_fill()    #Creates triangle on top of house and fills it in with brown colour
bob.right(135)  #Could not use loop structure due to shape of the roof
bob.forward(135)
bob.right(90)
bob.forward(135)
bob.right(135)
bob.forward(185)
bob.end_fill()



amy = turtle.Turtle() #Imports turtle named amy
amy.color("brown")      #Sets colour to brown
amy.pensize(35)     #Sets pen/line width

amy.up()        #Draws door for house
amy.right(90)
amy.forward(125)
amy.left(90)
amy.forward(30)
amy.right(90)
amy.down()
amy.forward(30)



eve = turtle.Turtle() #Imports turtle named eve
eve.color("#AD6422") #Changed color to a light brown
eve.pensize(40) #Width of pen/line

eve.up()    #Changed position of eve without drawing
eve.right(90)
eve.forward(200)
eve.right(90)
eve.forward(230)
eve.right(90)
eve.down()

eve.forward(50) #Draws a simple line

eve.up()#Changes position of line without drawing
eve.forward(20)
eve.right(90)
eve.forward(6)
eve.down()

eve.color("green")#Changes colour to green
eve.begin_fill() #Fills in shape with colour
eve.circle(30)#Draws a circle
eve.end_fill()




kim = turtle.Turtle() #Imports turtle named kim
kim.color("#AD6422") #Changed color to a light brown
kim.pensize(40) #Width of pen/line

kim.up()    #Changed position of kim without drawing
kim.right(90)
kim.forward(200)
kim.left(90)
kim.forward(230)
kim.left(90)
kim.down()

kim.forward(50) #Draws a simple line

kim.up()#Changes position of line without drawing
kim.forward(20)
kim.right(90)
kim.forward(6)
kim.down()

kim.color("green")#Changes colour to green
kim.begin_fill() #Fills in shape with colour
kim.circle(30)#Draws a circle
kim.end_fill()



zoe = turtle.Turtle() #Imports turtle named zoe
zoe.color("lightgrey")      #Sets colour to lightgrey
zoe.pensize(45)     #Sets pen/line width

zoe.up()        #changes position of line without drawing
zoe.right(90)
zoe.forward(195)
zoe.down()
zoe.forward(100) #Draws line



