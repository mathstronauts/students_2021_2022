import turtle

def drawStar(pen, starSideLength, lineColour, fillColour):
  pen.color(lineColour)
  pen.fillcolor(fillColour)
  pen.pendown()
  pen.begin_fill()

  print(pen.pos())
  for i in range(5):
    pen.forward(starSideLength)
    pen.right(144)

  pen.end_fill()
  pen.color("white")
  pen.fillcolor("white")
  pen.penup()
## starting code ## 
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(700,400)

spacePen = turtle.Turtle()
spacePen.color("white") ## white to make pen visible on black background
spacePen.penup()

## students can draw a space scene however they want ##
## Use at least 1 loop(can be while or for loop), the circle function, and the provided drawStar function to complete the assignment ##
