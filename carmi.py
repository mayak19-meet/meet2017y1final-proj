food_list = ["hamburger", "pizza", "cola", "water"]

score = 0
clear_list = []
clear_s = turtle.clone()
clear_s.color('white')
turtle.goto(0, 0)
clear_s.speed(100)

UP_EDGE = SIZE_Y/2
DOWN_EDGE = -SIZE_Y/2
RIGHT_EDGE = SIZE_X/2
LEFT_EDGE = -SIZE_X/2

def r_food():
    rand_index = random.randint(0, 3)
    return food_list[rand_index]
    
s_score = turtle.clone()
u_score = turtle.clone()
e_score = turtle.clone()
k_score = turtle.clone()

def c_food_s():
        global s_score
        syria_food = r_food()
        s_score.goto(100,-145)
        s_score.clear()
        s_score.write('syria: we want ' + syria_food) 
def c_food_u():
        global u_score
        uganda_food = r_food()
        u_score.goto(-200,-145)
        u_score.clear()
        u_score.write('uganda: we want ' + uganda_food)
def c_food_e():
        global e_score
        egypt_food = r_food()
        e_food.goto(-150,10)
        e_score.clear()
        turtle.write('egypt: we want ' + egypt_food)
def c_food_k():
        global k_score
        kenya_food = r_food()
        k_score.goto(-200,230)
        k_score.clear()
        turtle.write('kenya: we want ' + kenya_food)

turtle.ontimer(c_food_u ,1200)
turtle.ontimer(c_food_s, 900)
turtle.ontimer(c_food_e ,1500)
turtle.ontimer(c_food_k ,1700)

plane_food = 'aa'
if plane.pos() == hamburger.pos():
    plane_food = 'hamborger'
    print('you picked up hamborger') 
if plane.pos()== cola.pos():
    plane_food = 'cola'
    print('you picked up cola') 
if plane.pos() == pizza.pos():
    plane_food = 'pizza'
    print('you picked up pizza') 
if plane.pos() == water.pos():
    plane_food = 'water'
    print('you picked up water')

if plane.pos() == syria.pos() and plane_food == syria_food:
    score = score+1
    turtle.cleanr()
    turtle.write(score)
if plane.pos() == uganda.pos() and plane_food == uganda_food:
    score = score+1
    turtle.clear()
    turtle.write(score)
    
if plane.pos() == egypt.pos() and plane_food == egypt_food:
    score = score+1
    clear_s.goto(0, 0)
    turtle.clear()
    turtle.write(score)
if plane.pos() == kenya.pos() and plane_food == kenya_food:
    score = score+1
    turtle.clear()
    turtle.write(score)

 ##########move_plane!!!!!!!!!!!!!!!!!!!!!!!   
new_pos = plane.pos()
new_x_pos = new_pos[0]
new_y_pos = new_pos[1]
if new_y_pos < UP_EDGE and new_y_pos > DOWN_EDGE and new_x_pos < RIGHT_EDGE and new_x_pos > LEFT_EDGE:
    move_plane()
