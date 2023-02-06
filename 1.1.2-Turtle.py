import turtle as trtl

painter = trtl.Turtle()


index = 0
print("COMPREHENDED, WRITTEN, AND FINALIZED BY DAVID")
painter.speed(200000)
painter.turtlesize(0.1)
while index < 1000:
    painter.pencolor("blue")
    painter.pensize(2.5)
    painter.circle(index + 1)
    painter.left(90)
    painter.circle(index + 1)
    painter.left(90)
    painter.circle(index + 1)
    painter.left(90)
    painter.circle(index + 1)
    painter.left(90)
    painter.pencolor("red")
    painter.pensize(1)
    painter.circle(index * 2)
    painter.left(90)
    painter.circle(index * 2)
    painter.left(90)
    painter.circle(index * 2)
    painter.left(90)
    painter.circle(index * 2)
    painter.left(90)
    index = index + 10
    print(index)

while index < 1011:
    painter.pencolor("blue")
    painter.pensize(2.5)
    painter.circle(index - 2)
    painter.left(90)
    painter.circle(index - 2)
    painter.left(90)
    painter.circle(index - 2)
    painter.left(90)
    painter.circle(index - 2)
    painter.left(90)
    painter.pencolor("red")
    painter.pensize(1)
    painter.circle(index / 3)
    painter.left(90)
    painter.circle(index / 3)
    painter.left(90)
    painter.circle(index / 3)
    painter.left(90)
    painter.circle(index / 3)
    painter.left(90)
    index = index - 10
    print(index)



 
wn = trtl.Screen()
wn.mainloop()
