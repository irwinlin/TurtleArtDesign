import turtle
import random
from projectstuffs import*
turtle.tracer(0)
turtle.bgcolor("black")
bob=turtle.Turtle()
turtle.colormode(255)
for pos in range(150):
    bob.color(255,0,0)#red
    bob.circle(pos)
    bob.left(130)
for x in range(120):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    myColor=(r,g,b)
    mySize=(x*0.2)
    mySide=random.randint(5,10)
    polygon(bob,mySide,mySize,myColor)
    bob.forward(x*0.8)
    bob.left(30)
jump(bob,500,0)
for pos in range(150):
    bob.color(0,0,255)#blue
    bob.circle(pos)
    bob.left(130)
jump(bob,500,0)
for x in range(120):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    myColor=(r,g,b)
    mySize=(x*0.2)
    mySide=random.randint(5,10)
    polygon(bob,mySide,mySize,myColor)
    bob.forward(x*0.8)
    bob.left(30)
jump(bob,-500,0)
for pos in range(150):
    bob.color(0,255,0)#green
    bob.circle(pos)
    bob.left(130)
jump(bob,-500,0)
for x in range(120):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    myColor=(r,g,b)
    mySize=(x*0.2)
    mySide=random.randint(5,10)
    polygon(bob,mySide,mySize,myColor)
    bob.forward(x*0.8)
    bob.left(30)
