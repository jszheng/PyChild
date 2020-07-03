import turtle

myturtle = turtle.Turtle()
mywin = turtle.Screen()

def drawsqiral(myturtle, linelenth):
    if linelenth > 0:
        myturtle.forward(linelenth)
        myturtle.right(90)
        drawsqiral(myturtle, linelenth - 5)


drawsqiral(myturtle, 100)
mywin.exitonclick()
