### Shelly's code

import turtle, random, time
turtle.bgcolor('dodgerblue')

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
bb = turtle.clone()
bb.goto(100, 100)
#####################################################
#maya's code
SIZE_X=700
SIZE_Y=700

kenya=turtle.clone()
egypt=turtle.clone()
uganda=turtle.clone()
syria=turtle.clone()

kenya.penup()
turtle.register_shape("kenya3.gif")
kenya.shape('kenya3.gif')
kenya.goto(-200,200)

egypt.penup()
turtle.register_shape("EGYPT1.gif")
egypt.shape('EGYPT1.gif')
egypt.goto(-200,10)

uganda.penup()
turtle.register_shape("uganda3.gif")
uganda.shape('uganda3.gif')
uganda.goto(-200,-170)

syria.penup()
turtle.register_shape("syria2.gif")
syria.shape('syria2.gif')
syria.goto(100,-170)

###############################################

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
hamburger.goto(120,290)
print(hamburger.pos())
hamburger.stamp()
hamburger.showturtle()

water.hideturtle()
water.goto(40,290)
print(water.pos())
water.stamp()
water.showturtle()





############################################################################################
#####eliass code
turtle.tracer(1,0)
size_x=800
size_y=500
turtle.setup(size_x,size_y)
turtle.penup()
#how far the snake moves 
SQUARE_SIZE=10
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




new_pos = plane.pos()
new_x_pos = new_pos[0]
new_y_pos = new_pos[1]
############################################################################


    
s_score = turtle.clone()
u_score = turtle.clone()
e_score = turtle.clone()
k_score = turtle.clone()

#carmis code
food_list = ["hamburger", "pizza", "cola", "water"]
def r_food():
    rand_index = random.randint(0, 3)
    return food_list[rand_index]

def up():
    global direction, new_x_pos, new_y_pos, UP_EDGE, DOWN_EDGE, RIGHT_EDGE, LEFT_EDGE
    direction=UP
    if new_y_pos < UP_EDGE and new_y_pos > DOWN_EDGE and new_x_pos < RIGHT_EDGE and new_x_pos > LEFT_EDGE:
        move_plane()
    print("you pressed up ")

def down():
    global direction, new_x_pos, new_y_pos, UP_EDGE, DOWN_EDGE, RIGHT_EDGE, LEFT_EDGE
    direction=DOWN
    if new_y_pos < UP_EDGE and new_y_pos > DOWN_EDGE and new_x_pos < RIGHT_EDGE and new_x_pos > LEFT_EDGE:
        move_plane()
    print("you pressed DOWN ")

def right():
    global direction, new_x_pos, new_y_pos, UP_EDGE, DOWN_EDGE, RIGHT_EDGE, LEFT_EDGE
    direction=RIGHT
    if new_y_pos < UP_EDGE and new_y_pos > DOWN_EDGE and new_x_pos < RIGHT_EDGE and new_x_pos > LEFT_EDGE:
        move_plane()
    print("you pressed RIGHT ")

def left():
    global direction, new_x_pos, new_y_pos, UP_EDGE, DOWN_EDGE, RIGHT_EDGE, LEFT_EDGE
    direction=LEFT
    if new_y_pos < UP_EDGE and new_y_pos > DOWN_EDGE and new_x_pos < RIGHT_EDGE and new_x_pos > LEFT_EDGE:
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

turtle.goto(200,0)#this is moving the turtle to 200 to write the timer 

##################
start_time = 120##choose how much time till the game ends 
##################
 
def timer():#the game timer
    global start_time
    start_time = start_time-1
    print(start_time)
    turtle.clear()
    turtle.write(start_time,font=50)
    if start_time==0:
        quit()
        print("You ran out of time! ")
    turtle.ontimer(timer,1000)
def c_food_s():
        global s_score, syria_food
        syria_food = r_food()
        s_score.goto(173,-145)
        s_score.clear()
        s_score.write('We want ' + syria_food)
        #return syria_food
def c_food_u():
        global u_score, uganda_food
        uganda_food = r_food()
        u_score.goto(-127,-145)
        u_score.clear()
        u_score.write('We want ' + uganda_food)
        #return uganda_food
def c_food_e():
        global e_score, egypt_food
        egypt_food = r_food()
        e_score.goto(-127,10)
        e_score.clear()
        e_score.write('We want ' + egypt_food)
        #return egypt_food
def c_food_k():
        global k_score, kenya_food 
        kenya_food = r_food()
        k_score.goto(-127,230)
        k_score.clear()
        k_score.write('We want ' + kenya_food)
        #return kenya_food

c_food_s()
c_food_u()
c_food_e()
c_food_k()
score = 0
plane_food = 'aa'
score_1 = turtle.clone()
score_1.goto(300,0)
score_1.pencolor("white")

def move_plane():#how the plane moves 
    global plane_food, score
    my_pos=plane.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]       
    if direction==RIGHT:
        plane.goto(x_pos+SQUARE_SIZE,y_pos)
        
    if direction==DOWN:
        plane.goto(x_pos,y_pos-SQUARE_SIZE)
        
    if direction==LEFT:
        plane.goto(x_pos-SQUARE_SIZE,y_pos)
    if direction==UP:
        plane.goto(x_pos,y_pos+SQUARE_SIZE)

    
    if plane.pos() == hamburger.pos():
        bb.clear()
        plane_food = 'hamburger'
        bb.write('you picked up hamburger',font = ("Ariel",20,"normal"))
    if plane.pos()== cola.pos():
        bb.clear()
        plane_food = 'cola'
        bb.write('you picked up cola',font = ("Ariel",20,"normal"))
    if plane.pos() == pizza.pos():
        bb.clear()
        plane_food = 'pizza'
        bb.write('you picked up pizza',font = ("Ariel",20,"normal"))
    if plane.pos() == water.pos():
        bb.clear()
        plane_food = 'water'
        bb.write('you picked up water',font = ("Ariel",20,"normal"))
    
    print("syria food: " + syria_food)
    print("plane_food: " + plane_food)
    print("plane_pos: " + str(plane.pos()))
    
    #if plane.pos() == syria.pos() and plane_food == syria_food:
    if (plane.pos()[0] - syria.pos()[0])**2 + (plane.pos()[1] - syria.pos()[1])**2 < 50 and plane_food == syria_food:
        score = score+1
        score_1.clear()
        score_1.write('score is: ' + str(score),font = ("Ariel",20,"normal"))
        c_food_s()
    #if plane.pos() == uganda.pos() and plane_food == uganda_food:
    if (plane.pos()[0] - uganda.pos()[0])**2 + (plane.pos()[1] - uganda.pos()[1])**2 < 50 and plane_food == uganda_food:
        score = score+1
        score_1.clear()
        score_1.write('score is: ' + str(score),font = ("Ariel",20,"normal"))
        c_food_u()
        
    #if plane.pos() == egypt.pos() and plane_food == egypt_food:
    if (plane.pos()[0] - egypt.pos()[0])**2 + (plane.pos()[1] - egypt.pos()[1])**2 < 50 and plane_food == egypt_food:
        score = score+1
        score_1.clear()
        score_1.write('score is: ' + str(score),font = ("Ariel",20,"normal"))
        c_food_e()
    #if plane.pos() == kenya.pos() and plane_food == kenya_food:
    if (plane.pos()[0] - kenya.pos()[0])**2 + (plane.pos()[1] - kenya.pos()[1])**2 < 50 and plane_food == kenya_food:
        score = score+1
        score_1.clear()
        score_1.write('score is: ' + str(score),font = ("Ariel",20,"normal"))
        c_food_k()
            
        
timer()#this is basicly activating he timer 




clear_list = []
turtle.goto(0, 0)

UP_EDGE = SIZE_Y/2
DOWN_EDGE = -SIZE_Y/2
RIGHT_EDGE = SIZE_X/2
LEFT_EDGE = -SIZE_X/2



##
##turtle.ontimer(c_food_u ,1200)
##turtle.ontimer(c_food_s, 900)
##turtle.ontimer(c_food_e ,1500)
##turtle.ontimer(c_food_k ,1700)



