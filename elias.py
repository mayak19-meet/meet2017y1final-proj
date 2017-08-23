######################################################################elias's code 
import turtle
import random 
import time
turtle.tracer(1,0)
size_x=800
size_y=500
turtle.setup(size_x,size_y)
turtle.penup()
#how far the snake moves 
SQUARE_SIZE=20
pos_list=[]
plane=turtle.clone()
#the shape of the plane
turtle.register_shape("download (2).gif")
plane.shape("download (2).gif")
turtle.hideturtle()


UP_ARROW='Up'
LEFT_ARROW='Left'
RIGHT_ARROW='Right'
DOWN_ARROW='Down'
TIME_STEP=100
SPACEBAR='spacebar'
UP=0
DOWN=1
LEFT=2
RIGHT=3
turn=4
direction=UP
end_time= time.time()+120
############################################################################
def up():
    global direction
    direction=UP
    move_plane()
    print("you pressed up ")

def down():
    global direction
    direction=DOWN
    move_plane()
    print("you pressed DOWN ")

def right():
    global direction
    direction=RIGHT
    move_plane()
    print("you pressed RIGHT ")

def left():
    global direction
    direction=LEFT
    move_plane()
    print("you pressed LEFT ")
def turn():
    global direction
    direction=turn
    turtle.right(90)

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.listen()

turtle.goto(200,0)#this is moing the turtle to 200 to write the timer 

##################
start_time = 120##chpse how much time till the game ends 
##################
 
def timer():#the game timer
    global start_time
    start_time = start_time-1
    print(start_time)
    turtle.clear()
    turtle.write(start_time,font=50)
    if start_time==0:
        quit()
        print("you ran out of time ")
    turtle.ontimer(timer,1000)

def move_plane():#how the plane moves 
    my_pos=plane.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]       
    if direction==RIGHT:
        plane.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moevd right ')
    if direction==DOWN:
        plane.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moevd DOWN ')
    if direction==LEFT:
        plane.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moevd LEFT ')
    if direction==UP:
        plane.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moevd UP ')
        
timer()#this is baisicly activating he timer 
############################################################################################
            
