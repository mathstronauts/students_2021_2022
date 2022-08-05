import turtle
screen = turtle.Screen()
screen.setup(700,400)
pen = turtle.Turtle()

## Draw a triangle!
for i in range(3):
    pen.forward(50)
    pen.right(120)

pen.clear()

## Draw a square!
for i in range(4):
    pen.forward(50)
    pen.right(90)

pen.clear()

## Draw a hexagon!
for i in range(6):
    pen.forward(50)
    pen.right(60)

pen.clear()

## Draw a pattern!
sideLength = 10
while True:
    pen.forward(sideLength)
    pen.left(90)
    sideLength = sideLength + 20
