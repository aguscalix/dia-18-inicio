from turtle import Turtle, Screen

tim = Turtle()
# tim.shape("arrow")
tim.color("lawn green")

# Challenge 1

# for vuelta in range(4):
#     tim.right(90)
#     if vuelta < 3:
#         tim.forward(100)
#     else:
#         tim.forward(90)

# Challenge 2

# for _ in range(30):
#     tim.fd(5)
#     tim.pu()
#     tim.fd(5)
#     tim.pd()

# Challenge 3

for lados in range(1, 53):
    if lados <= 3:
        tim.forward(100)
        tim.right(120)
    if lados <= 4:
        tim.forward(100)
        tim.right(90)














pantalla = Screen()
pantalla.exitonclick()
