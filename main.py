from turtle import Turtle, Screen

import random

tim = Turtle()
# tim.shape("arrow")
tim.color("lawn green")

# Challenge 1 *************************************************************

# for vuelta in range(4):
#     tim.right(90)
#     if vuelta < 3:
#         tim.forward(100)
#     else:
#         tim.forward(100)

# Challenge 2 *************************************************************

# for _ in range(30):
#     tim.fd(5)
#     tim.pu()
#     tim.fd(5)
#     tim.pd()


# Challenge 3 *************************************************************

lados_figuras = [3, 4, 5, 6, 7, 8, 9, 10]


for figura in lados_figuras:
    r = lambda: random.randint(0, 255)
    color = '#%02X%02X%02X' % (r(), r(), r())
    tim.pencolor(color)
    for vuelta in range(figura):
        tim.right(360 / figura)
        if vuelta <= figura - 1:
            tim.forward(100)

# # Triángulo
# for lados in range(3):
#     tim.right(120)
#     if lados <= 2:
#         tim.forward(100)
#
# # Cuadrado
# for vuelta in range(4):
#     tim.right(90)
#     if vuelta <= 3:
#         tim.forward(100)
#
# # Pentágono
# for vuelta in range(5):
#     tim.right(72)
#     if vuelta <= 4:
#         tim.forward(100)
#
# # Hexágono
# for vuelta in range(6):
#     tim.right(60)
#     if vuelta <= 5:
#         tim.forward(100)
#
# # Heptágono
# for vuelta in range(7):
#     tim.right(360 / 7)
#     if vuelta <= 6:
#         tim.forward(100)
#
# # Octágono
# for vuelta in range(8):
#     tim.right(45)
#     if vuelta <= 7:
#         tim.forward(100)
#
# # Nonágono
# for vuelta in range(9):
#     tim.right(40)
#     if vuelta <= 8:
#         tim.forward(100)
#
# # Decágono
# for vuelta in range(10):
#     tim.right(36)
#     if vuelta <= 9:
#         tim.forward(100)























pantalla = Screen()
pantalla.exitonclick()
