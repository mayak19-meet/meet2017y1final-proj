import turtle
import random
color=0
turtle.tracer(1,0)
counter=1
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()
SQUARE_SIZE=20
turtle.color("red")
plane=turtle.clone()
plane.shape('circle')
turtle.hideturtle()
plane.color("green")




    
    

    
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR="space"
UP=0
DOWN=1
LEFT=2
RIGHT=3
    
direction=UP

UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400

def up():
    global direction
    if direction !=DOWN:
        direction=UP
    print("you moved up !!")
    
def down():
    global direction
    if direction != UP:
        direction=DOWN
    print("you moved down !!")

def left():
    global direction
    if direction !=RIGHT:
        direction=LEFT
    print("you moved left !! ")

def right():
    global direction
    if direction !=LEFT:
        direction=RIGHT
    print("you moved right !!")

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()



    
    
def move_snake():
    my_pos=plane.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    if direction==RIGHT:
        plane.goto(x_pos+SQUARE_SIZE,y_pos)
        print("you moved right")
    elif direction==LEFT:
        plane.goto(x_pos-SQUARE_SIZE,y_pos)
        print("you moved left !!")
    elif direction==UP:
        plane.goto(x_pos,y_pos+SQUARE_SIZE)
        print("you moved up !!")
    elif direction==DOWN:
        plane.goto(x_pos,y_pos-SQUARE_SIZE)
    
        
    my_pos=plane.pos()
   
    
    
    
           
        



    new_pos=plane.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    
    if new_x_pos>=RIGHT_EDGE:
        print("GAME OVER !!! YOU HIT THE RIGHT EDGE ")
        quit()
    if new_x_pos<=LEFT_EDGE:
        print("GAME OVER !!! YOU HIT THE LEFT EDGE ")
        quit()
    if new_y_pos<=DOWN_EDGE:
        print("GAME OVER !!! YOU HIT THE LOWER EDGE ")
        quit()
    if new_y_pos>=UP_EDGE:
        print("GAME OVER !!! YOU HIT THE UPPER EDGE ")
        quit()
   
    
    
move_snake()

