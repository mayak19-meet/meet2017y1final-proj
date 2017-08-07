import random
food_list = ["hamburger", "pizza", "cola", "water"]
def r_food():
    rand_index = random.randint(0, 3)
    food_list[rand_index]

def c_food_s():
        syria_food = r_food()
def c_food_u():
        uganda_food = r_food()
def c_food_e():
        egypt_food = r_food()
def c_food_k():
        kenya_food = r_food()

turtle.ontimer(c_food_u ,1200)
turtle.ontimer(c_food_s, 900)
turtle.ontimer(c_food_e ,1500)
turtle.ontimer(c_food_k ,1700)



score = 0
clear_list()
clear_s = turtle.clone()
clear_s.color('white')
turtle.goto(0, 0)
clear_s.speed(100)

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
    clear_s.goto(0, 0)
    a = clear_s.stamp() #might need change later (stamp also in other places)
    clear_list.append(a)
    turtle.write(score)
    clear_s.goto(0, 200)
if plane.pos() == uganda.pos() and plane_food == uganda_food:
    score = score+1
    clear_s.goto(0, 0)
    a = clear_s.stamp() #might need change later (stamp also in other places)
    clear_list.append(a)
    clear_s.goto(0, 200)
    turtle.write(score)
if plane.pos() == egypt.pos() and plane_food == egypt_food:
    score = score+1
    clear_s.goto(0, 0)
    a = clear_s.stamp() #might need change later (stamp also in other places)
    clear_list.append(a)
    clear_s.goto(0, 200)
    turtle.write(score)
if plane.pos() == kenya.pos() and plane_food == kenya_food:
    score = score+1
    clear_s.goto(0, 0)
    a = clear_s.stamp() #might need change later (stamp also in other places)
    clear_list.append(a)
    clear_s.goto(0, 200)
    turtle.write(score)
