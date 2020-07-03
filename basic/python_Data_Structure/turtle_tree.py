import turtle


def tree(brenchlenth, t):
    if brenchlenth > 5:
        t.forward(brenchlenth)
        t.right(20)
        tree(brenchlenth - 15, t)
        t.left(40)
        tree(brenchlenth - 15, t)
        t.right(20)
        t.backward(brenchlenth)


def main():
    t = turtle.Turtle()
    mywin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t)
    mywin.exitonclick()


main()
