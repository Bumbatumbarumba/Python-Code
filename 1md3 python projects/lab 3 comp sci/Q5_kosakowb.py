#Bartosz Kosakowski
#400028494
#Lab 3 Question 5
####################
from turtle import *

def nestedSquares():
    reset()
    hideturtle()
    penup()
    setx(-350)
    sety(300)
    pendown()
    speed(0)
    numSides = 16
    i = 0
    color('blue')
    while i < numSides:
        for g in range(4):
            forward(300-16*i)
            right(90)
        if (g+1)%4 == 0:
            penup()
            home()
            setx(-350+4*i)
            sety(300-4*i)
            pendown()
        i = i+1
