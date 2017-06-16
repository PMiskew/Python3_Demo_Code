import turtle


bob = turtle.Turtle()


angle1 = 79
angle2 = 60
angle3 = 180 - angle1 - angle2

side = 100

bob.forward(side)
bob.right(180 - angle1)


bob.forward(side)
bob.right(180 - angle2)



bob.forward(side)
bob.right(180 - angle3)






turtle.done()