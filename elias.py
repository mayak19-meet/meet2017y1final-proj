import turtle
import random 
import time
turtle.tracer(1,0)
size_x=800
size_y=500
turtle.setup(size_x,size_y)
turtle.penup()
SQUARE_SIZE=20
pos_list=[]
plane=turtle.clone()
plane.shape('square')
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
direction=UP
end_time= time.time()+120

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
s_l_s = []
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.listen()
clear_score = turtle.clone()
clear_score.speed(10)
clear_score.color('white')
turtle.goto(400, 0)
def move_plane():
    my_pos=plane.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    while end_time-time.time()>0:
        print(int(end_time-time.time()))
        clear_score.goto(400, 0)
        ax = clear_score.stamp()
        s_l_s.append(ax)
        clear_score.goto(800, 0)
        turtle.write(int(end_time-time.time()),font=50)
        


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
        
            
