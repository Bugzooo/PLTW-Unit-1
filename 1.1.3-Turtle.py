import turtle as trtl

painter = trtl.Turtle()



print("COMPREHENDED, WRITTEN, AND FINALIZED BY DAVID")
painter.speed(100)
painter.turtlesize(0.1)

painter.penup()
painter.pensize(10)
painter.color("green")
painter.right(180)
painter.forward(50)
painter.left(90)
painter.pendown()
painter.forward(200)
painter.penup()

painter.pensize(25)
painter.color("blue")
painter.goto(0,0)

for petal in range(20):
    painter.pendown()
    painter.stamp()
    painter.color("blue")
    painter.circle(20)
    painter.penup()
    painter.right(20)
    painter.forward(20)

painter.pensize(10)
for petal in range(20):
    painter.pendown()
    painter.stamp()
    painter.color("red")
    painter.circle(15)
    painter.penup()
    painter.right(20)
    painter.forward(20)

    """ painter.color("red")
    painter.pendown()
    painter.circle(20)
    painter.right(20)
    painter.forward(20)
    """

 
wn = trtl.Screen()
wn.mainloop()
