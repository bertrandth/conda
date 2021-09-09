from turtle import *
from random import randint

def carre():
    left(90)
    for i in range(4):
        forward(5)
        right(90)
        forward(5)
    penup()
    setheading(0)
    forward(10)
    pendown()

def tiret():
    forward(10)

goto(-230,0)
setheading(0)
clear()
pendown()
for i in range(46):
    if randint(1, 2) == 1:
        carre()
    else:
        tiret()