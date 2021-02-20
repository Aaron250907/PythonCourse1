import turtle

wn = turtle.Screen()
wn.bgcolor('#427AA1');
wn.title("My Rectangle")

rectangle = turtle.Turtle()

for i in range(2):
    rectangle.forward(300)
    rectangle.right(90)
    rectangle.forward(150)
    rectangle.right(90)

turtle.done()

