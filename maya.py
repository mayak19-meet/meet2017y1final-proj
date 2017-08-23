import turtle
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
uganda.goto(-200,-175)

syria.penup()
turtle.register_shape("syria2.gif")
syria.shape('syria2.gif')
syria.goto(100,-175)
