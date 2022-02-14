import turtle

# s = turtle.getscreen()
# t = turtle.Turtle()
# t.circle(60)
# turtle.bgcolor("blue")

star = turtle.Turtle()  # turtle instance creation

for i in range(5):
    star.forward(50)  # turtle instance method
    star.right(144)  # turtle instance method

screen = turtle.Screen()  # access sole screen instance
screen.mainloop()  # screen instance method