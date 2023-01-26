Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
import random
import time
bored = True
while bored:
    # draw gallows
    turtle.home()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(74)
    turtle.left(90)
    turtle.forward(35)
    turtle.penup()
    turtle.goto(-135,-35)

    word = random.choice(wordbank)

    for i in word:
        turtle.write('_ ', True, font=("Courier", 14, "normal"))
