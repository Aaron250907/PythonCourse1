import turtle

polygon = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor('#D495F4')
wn.title('My Square')

number_of_sides = 4
side_lenght = 70
angle = 360.0 / number_of_sides

for i in range(number_of_sides):
  polygon.forward(side_lenght)
  polygon.right(angle)

turtle.done()
