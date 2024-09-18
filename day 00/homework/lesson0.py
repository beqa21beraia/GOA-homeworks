from turtle import *

speed(10)
shape('turtle')

#step 1: drawing a square in center
width(8)
color('green')
penup()
goto(-125, -200)
pendown()
forward(250)

left(90)
forward(250)

left(90)
forward(250)

left(90)
forward(250)

#step 2: drawing a door
left(90)
forward(85)

color('brown')
begin_fill()
left(90)
forward(150)

right(90)
forward(80)

right(90)
forward(150)
end_fill()

#step 3: drawing a roof
penup()
goto(125, 50)
pendown()
color('red')
begin_fill()
right(150)
forward(250)

left(120)
forward(250)
end_fill()

#step 4: drawing a window
penup()
goto(125, -70)
pendown()
color('purple')
begin_fill()
right(60)
forward(60)

right(90)
forward(60)

right(90)
forward(60)
end_fill()

penup()
goto(-125, -70)
pendown()
color('purple')
begin_fill()
forward(60)

left(90)
forward(60)

left(90)
forward(60)

end_fill()
exitonclick()