import turtle


def cir():
    r.color("red")
    r.penup()
    r.right(90)
    r.forward(25)
    r.left(90)
    r.pendown()
    r.circle(25)
    r.penup()

def cross():
    r.color("blue")
    r.pendown()
    r.right(45)
    r.forward(25)
    r.backward(50)
    r.forward(25)
    r.left(90)
    r.forward(25)
    r.back(50)
    r.forward(25)
    r.right(45)
    r.penup() 

def goto():
    r.pensize(3)
    ch = int(input("enter a number 1-9: "))
    if ch == 1:
        r.penup()
        r.goto(-100,100)
        r.pendown()

    elif ch == 2:
        r.penup()
        r.goto(0,100)
        r.pendown()

    elif ch == 3:
        r.penup()
        r.goto(100,100)
        r.pendown()

    elif ch == 4:
        r.penup()
        r.goto(-100,0)
        r.pendown()

    elif ch == 5:
        r.penup()
        r.goto(0,0)
        r.pendown()

    elif ch == 6:
        r.penup()
        r.goto(100,0)
        r.pendown()

    elif ch == 7:
        r.penup()
        r.goto(-100,-100)
        r.pendown()

    elif ch == 8:
        r.penup()
        r.goto(0,-100)
        r.pendown()

    elif ch == 9:
        r.penup()
        r.goto(100,-100)
        r.pendown()
    else:
        print("incorrect input, closing game")      

###Main code
r=turtle.Turtle()
r.shape("turtle")
#grid
r.pensize(10)
r.color("black")
r.penup()
r.goto(-50,-150)
r.left(90)
r.pendown()
r.forward(300)
r.penup()
r.goto(50,-150)
r.pendown()
r.forward(300)
r.penup()
r.goto(-150,-50)
r.right(90)
r.pendown()
r.forward(300)
r.penup()
r.goto(-150,50)
r.pendown()
r.forward(300)
r.penup()

#Logic
print('player one will be circle, player 2 will be cross')
for i in range(1,10):
    if i % 2 == 0:
        print('player 2 turn')
        goto()
        cross()
    else:
        print("player 1 turn")
        goto()
        cir()


