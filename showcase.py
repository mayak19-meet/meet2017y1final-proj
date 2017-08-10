### Shelly's code

import turtle
import random
import time

SIZE_X=1300
SIZE_Y=750
turtle.setup(SIZE_X,SIZE_Y)
UP_EDGE = SIZE_Y/2
DOWN_EDGE = -SIZE_Y/2
RIGHT_EDGE = SIZE_X/2
LEFT_EDGE = -SIZE_X/2

#how far the snake moves 
SQUARE_SIZE=40
pos_list=[]

turtle.tracer(1,0)

#def first_screen():
w = turtle.clone()
turtle.bgcolor("dodgerblue")

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
bb = turtle.clone()
bb.goto(100,100)
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

turtle.pencolor("black")
turtle.ht()

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
w.write("the game will start in 5 seconds", font = ("Ariel",25,"normal","bold"))

s_score = turtle.clone()
s_score.pencolor('yellow')
u_score = turtle.clone()
u_score.pencolor('yellow')
e_score = turtle.clone()
e_score.pencolor('yellow')
k_score = turtle.clone()
k_score.pencolor('yellow')
##################
start_time = 60##chpse how much time till the game ends 
##################
kenya=turtle.clone()
egypt=turtle.clone()
uganda=turtle.clone()
syria=turtle.clone()
kenya.penup()
turtle.register_shape("kenya3.gif")
kenya.shape('kenya3.gif')

egypt.penup()
turtle.register_shape("EGYPT1.gif")
egypt.shape('EGYPT1.gif')

uganda.penup()
turtle.register_shape("uganda3.gif")
uganda.shape('uganda3.gif')

syria.penup()
turtle.register_shape("syria2.gif")
syria.shape('syria2.gif')

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


plane=turtle.clone()
#the shape of the plane
turtle.register_shape("photoplane1.gif")
plane.shape("photoplane1.gif")
turtle.hideturtle()


new_pos = plane.pos()
new_x_pos = new_pos[0]
new_y_pos = new_pos[1]
    
pizza = turtle.clone()
hamburger = turtle.clone()
water = turtle.clone()
cola = turtle.clone()

def game():
    global new_x_pos, new_y_pos, UP_EDGE, DOWN_EDGE, LEFT_EDGE, RIGHT_EDGE, SIZE_X, SIZE_Y, start_time

    ##################################
    #to Carmi

    ############

        
    #first_screen()

    turtle.bgcolor('dodgerblue')


    time.sleep(5)
    w.clear()
    up_gif.clear()
    down_gif.clear()
    right_gif.clear()
    left_gif.clear()

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

    #####################################################
    #maya's code




    kenya.showturtle()
    kenya.goto(-200,200)

    egypt.showturtle()
    egypt.goto(-200,00)

    uganda.showturtle()
    uganda.goto(-200,-160)

    syria.showturtle()
    syria.goto(100,-160)

    ###############################################

    
    pizza.hideturtle()
    turtle.register_shape("Pizza.gif")
    pizza.shape("Pizza.gif")

    
    hamburger.hideturtle()
    turtle.register_shape("burger_sandwich2.gif")
    hamburger.shape("burger_sandwich2.gif")

    
    water.hideturtle()
    turtle.register_shape("water4.gif")
    water.shape("water4.gif")

    
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
    pizza.goto(280,280)
    a = pizza.stamp()
    pizza.showturtle()

    cola.hideturtle()
    cola.goto(200,280)
    cola.stamp()
    cola.showturtle()

    hamburger.hideturtle()
    hamburger.goto(120,280)
    print(hamburger.pos())
    hamburger.stamp()
    hamburger.showturtle()

    water.hideturtle()
    water.goto(40,280)
    print(water.pos())
    water.stamp()
    water.showturtle()

    turtle.penup()


    plane.showturtle()




    timer()#this is basicly activating he timer
    c_food_s()
    c_food_u()
    c_food_e()
    c_food_k()
    ############################################################################
turtle.onkeypress(game, "space")
turtle.listen()



############################################################################################
#####eliass code

#carmis code
food_list = ["hamburger", "pizza", "cola", "water"]
def r_food():
    rand_index = random.randint(0, 3)
    return food_list[rand_index]

def up():
    global direction, new_x_pos, new_y_pos, UP_EDGE, DOWN_EDGE, RIGHT_EDGE, LEFT_EDGE
    direction=UP
    new_x_pos = plane.pos()[0]
    new_y_pos = plane.pos()[1]
    if new_y_pos < UP_EDGE: #and new_y_pos > DOWN_EDGE and new_x_pos < RIGHT_EDGE and new_x_pos > LEFT_EDGE:
        move_plane()
    print("you pressed up ")

def down():
    global direction, new_x_pos, new_y_pos, UP_EDGE, DOWN_EDGE, RIGHT_EDGE, LEFT_EDGE
    direction=DOWN
    new_x_pos = plane.pos()[0]
    new_y_pos = plane.pos()[1]
    if  new_y_pos > DOWN_EDGE: #and new_y_pos < UP_EDGEand new_x_pos < RIGHT_EDGE and new_x_pos > LEFT_EDGE:
        move_plane()
    print("you pressed DOWN ")

def right():
    global direction, new_x_pos, new_y_pos, UP_EDGE, DOWN_EDGE, RIGHT_EDGE, LEFT_EDGE
    direction=RIGHT
    new_x_pos = plane.pos()[0]
    new_y_pos = plane.pos()[1]
    if new_x_pos < RIGHT_EDGE: # and new_y_pos < UP_EDGE and new_y_pos > DOWN_EDGE and new_x_pos > LEFT_EDGE:
        move_plane()
    print("you pressed RIGHT ")

def left():
    global direction, new_x_pos, new_y_pos, UP_EDGE, DOWN_EDGE, RIGHT_EDGE, LEFT_EDGE
    direction=LEFT
    new_x_pos = plane.pos()[0]
    new_y_pos = plane.pos()[1]
    if new_x_pos > LEFT_EDGE: #and new_y_pos < UP_EDGE and new_y_pos > DOWN_EDGE and new_x_pos < RIGHT_EDGE:
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


def timer():#the game timer
    global start_time
    turtle.goto(-330,310)
    turtle.pencolor("navy")
    start_time = start_time-1
    print(start_time)
    turtle.clear()
    turtle.write(start_time,font = ("Ariel",23,"normal","bold"))
    if start_time==0:
        plane.clear()
        hamburger.clear()
        pizza.clear()
        water.clear()
        cola.clear()
        uganda.clear()
        kenya.clear()
        egypt.clear()
        syria.clear()
        score_1.clear()
        bb.clear()
        u_score.clear()
        s_score.clear()
        k_score.clear()
        e_score.clear()
        pizza.clearstamps()
        pizza.hideturtle()
        cola.clearstamps()
        cola.hideturtle()
        hamburger.clearstamps()
        hamburger.hideturtle()
        water.clearstamps()
        water.hideturtle()
        syria.clearstamps()
        syria.hideturtle()
        uganda.clearstamps()
        uganda.hideturtle()
        kenya.clearstamps()
        kenya.hideturtle()
        egypt.clearstamps()
        egypt.hideturtle()
        plane.clearstamps()
        plane.hideturtle()
        turtle.clear()

        turtle.bgcolor("dodgerblue")
        turtle.pencolor("yellow")
        turtle.hideturtle()
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

        turtle.goto(-235,170)
        turtle.pencolor("navy")
        turtle.write("You ran out of time!", font = ("Ariel",35,"normal"))
        turtle.goto(-150,50)
        turtle.pencolor("floralwhite")
        turtle.write("Your score was: " + str(score), font = ("Ariel",25,"normal")) 
        turtle.goto(-320,-162)
        turtle.pencolor("darkslategray")
        turtle.write("GAME OVER :(" , font = ("Ariel",62,"normal","bold"))
        time.sleep(5)
        quit()
        print("you run out of time ")
    turtle.ontimer(timer,1000)
def c_food_s():
        global s_score, syria_food
        syria_food = r_food()
        s_score.goto(173,-145)
        s_score.clear()
        s_score.write('We want ' + syria_food, font = ("Ariel",11,"normal"))
        #return syria_food
def c_food_u():
        global u_score, uganda_food
        uganda_food = r_food()
        u_score.goto(-135,-145)
        u_score.clear()
        u_score.write('We want ' + uganda_food, font = ("Ariel",11,"normal"))
        #return uganda_food
def c_food_e():
        global e_score, egypt_food
        egypt_food = r_food()
        e_score.goto(-135,10)
        e_score.clear()
        e_score.write('We want ' + egypt_food, font = ("Ariel",11,"normal"))
        #return egypt_food
def c_food_k():
        global k_score, kenya_food 
        kenya_food = r_food()
        k_score.goto(-135,230)
        k_score.clear()
        k_score.write('We want ' + kenya_food, font = ("Ariel",11,"normal"))
        #return kenya_food


score = 0
plane_food = 'aa'
score_1 = turtle.clone()
score_1.color('white')
score_1.goto(300,0)
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
    if ((plane.pos()[0] - syria.pos()[0])**2 + (plane.pos()[1] - syria.pos()[1])**2)**0.5 < 50 and plane_food == syria_food:
        score = score+1
        score_1.clear()
        score_1.write('score: ' + str(score),font = ("Ariel",20,"normal", 'bold'))
        c_food_s()
    #if plane.pos() == uganda.pos() and plane_food == uganda_food:
    if ((plane.pos()[0] - uganda.pos()[0])**2 + (plane.pos()[1] - uganda.pos()[1])**2)**0.5 < 50 and plane_food == uganda_food:
        score = score+1
        score_1.clear()
        score_1.write('score: ' + str(score),font = ("Ariel",20,"normal", 'bold'))
        c_food_u()
        
    #if plane.pos() == egypt.pos() and plane_food == egypt_food:
    if ((plane.pos()[0] - egypt.pos()[0])**2 + (plane.pos()[1] - egypt.pos()[1])**2)**0.5 < 50 and plane_food == egypt_food:
        score = score+1
        score_1.clear()
        score_1.write('score: ' + str(score),font = ("Ariel",20,"normal", 'bold'))
        c_food_e()
    #if plane.pos() == kenya.pos() and plane_food == kenya_food:
    if ((plane.pos()[0] - kenya.pos()[0])**2 + (plane.pos()[1] - kenya.pos()[1])**2)**0.5 < 50 and plane_food == kenya_food:
        score = score+1
        score_1.clear()
        score_1.write('score: ' + str(score),font = ("Ariel",20,"normal", 'bold'))
        c_food_k()
            
        




game()
clear_list = []
turtle.goto(0, 0)





##
##turtle.ontimer(c_food_u ,1200)
##turtle.ontimer(c_food_s, 900)
##turtle.ontimer(c_food_e ,1500)
##turtle.ontimer(c_food_k ,1700)

        



        



