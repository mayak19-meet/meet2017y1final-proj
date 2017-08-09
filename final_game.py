### Shelly's code

import turtle

turtle.bgcolor("blue")

turtle.pencolor("yellow")
turtle.pensize(4)
turtle.penup()
turtle.goto(350,350)
turtle.pendown()
turtle.goto(-350,350)
turtle.goto(-350,-350)
turtle.goto(350,-350)
turtle.goto(350,350)
turtle.penup()
turtle.goto(0,0)
turtle.hideturtle()

pizza = turtle.clone()
pizza.hideturtle()
turtle.register_shape("Pizza.gif")
pizza.shape("Pizza.gif")

hamburger = turtle.clone()
hamburger.hideturtle()
turtle.register_shape("burger_sandwich2.gif")
hamburger.shape("burger_sandwich2.gif")

water = turtle.clone()
water.hideturtle()
turtle.register_shape("water4.gif")
water.shape("water4.gif")

cola = turtle.clone()
cola.hideturtle()
turtle.register_shape("cocacola7.gif")
cola.shape("cocacola7.gif")
##
##hamburger = "burger_sandwich.gif"
##
##turtle.register_shape(hamburger)
##turtle.shape(hamburger)
##
##water = "water.gif"
##
##turtle.register_shape(water)
##turtle.shape(water)
##
##cola = "cocacola.gif"
##
##turtle.register_shape(cola)
##turtle.shape(cola)

pizza.hideturtle()
pizza.goto(290,290)
pizza.stamp()
pizza.showturtle()

cola.hideturtle()
cola.goto(210,290)
cola.stamp()
cola.showturtle()

hamburger.hideturtle()
hamburger.goto(123,290)
hamburger.stamp()
hamburger.showturtle()

water.hideturtle()
water.goto(40,290)
water.stamp()
water.showturtle()

#maya's code
SIZE_X=800
SIZE_Y=800

kenya=turtle.clone()
EGYPT=turtle.clone()
uganda=turtle.clone()
syria=turtle.clone()

kenya.penup()
turtle.register_shape("kenya3.gif")
kenya.shape('kenya3.gif')
kenya.goto(-200,200)

EGYPT.penup()
turtle.register_shape("EGYPT1.gif")
EGYPT.shape('EGYPT1.gif')
EGYPT.goto(-200,10)

uganda.penup()
turtle.register_shape("uganda3.gif")
uganda.shape('uganda3.gif')



