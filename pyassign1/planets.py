import math
import turtle
wn=turtle.Screen()
turtle.clearscreen()
wn.bgcolor('black')

Mercury=turtle.Turtle()
Vernus=turtle.Turtle()
Earth=turtle.Turtle()
Mars=turtle.Turtle()
Jupiter=turtle.Turtle()
Saturn=turtle.Turtle()
Sun=turtle.Turtle()

Sun.pensize(10)
Sun.shape('circle')
Sun.color('yellow')

Mercury.up()
Mercury.fd(40)
Mercury.down()
Vernus.up()
Vernus.fd(80)
Vernus.down()
Earth.up()
Earth.fd(120)
Earth.down()
Mars.up()
Mars.fd(160)
Mars.down()
Jupiter.up()
Jupiter.fd(200)
Jupiter.down()
Saturn.up()
Saturn.fd(240)
Saturn.down()

def planet(name,color):
    name.pencolor(color)
    name.color(color)
    name.shape('circle')
    name.speed(0)

planet(Mercury,'purple')
planet(Vernus,'yellow')
planet(Earth,'blue')
planet(Mars,'red')
planet(Jupiter,'green')
planet(Saturn,'pink')

def ellipse(p,o,a,e):
    r=a*(1-e**2)/(1+e*math.cos(math.radians(o)))
    x=r*math.cos(math.radians(o))+a*e
    y=r*math.sin(math.radians(o))
    p.goto(x,y)          

for o in range(1,3601):                
    ellipse(Mercury,16*o,40,0.65)
    ellipse(Vernus,12*o,80,0.45)
    ellipse(Earth,8*o,120,0.2)
    ellipse(Mars,4*o,160,0.5)
    ellipse(Jupiter,2*o,200,0.35)
    ellipse(Saturn,o,240,0.3)