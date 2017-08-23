import turtle

def first_screen():

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

    up_gif = turtle.clone()
    up_gif.hideturtle()
    turtle.register_shape("arrowup.gif")
    up_gif.shape("arrowup.gif")

    down_gif = turtle.clone()
    down_gif.hideturtle()
    turtle.register_shape("arrowdown.gif")
    down_gif.shape("arrowdown.gif")

    left_gif = turtle.clone()
    left_gif.hideturtle()
    turtle.register_shape("arrowleft.gif")
    left_gif.shape("arrowleft.gif")

    right_gif = turtle.clone()
    right_gif.hideturtle()
    turtle.register_shape("arrowright.gif")
    right_gif.shape("arrowright.gif")

    turtle.pencolor("red")
    turtle.ht()
    w = turtle.clone()
    w.ht()
    w.pu()
    w.goto(-115, 300)
    w.write("To go UP Press: ", font = ("Ariel",20,"normal"))
    w.goto(-120,-210)
    w.write("To go DOWN Press: ", font = ("Ariel",20,"normal"))
    w.goto(-325,63)
    w.write("To go LEFT Press: ", font = ("Ariel",20,"normal"))
    w.goto(80,63)
    w.write("To go RIGHT Press: ", font = ("Ariel",20,"normal"))

    up_gif.hideturtle()
    up_gif.goto(0,238)
    up_gif.stamp()

    down_gif.hideturtle()
    down_gif.goto(0,-275)
    down_gif.stamp()

    left_gif.hideturtle()
    left_gif.goto(-275,0)
    left_gif.stamp()

    right_gif.hideturtle()
    right_gif.goto(275,0)
    right_gif.stamp()

    w.pencolor("aliceblue")
    w.goto(-290,-130)
    w.write("Press SPACE to continue", font = ("Ariel",35,"normal"))

#to Carmi
w.clear()
up_gif.clear
down_gif.clear()
right_gif.clear()
left_gif.clear()
############

    
first_screen()
turtle.onkeypress(game, "space")
turtle.listen()




