import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('paleturquoise')

t = turtle.Turtle()
t.speed(0)

#water
t.penup()
t.goto(-5000,0)
t.pendown()
t.fillcolor('darkblue')
t.begin_fill()
t.goto(5000,0)
t.goto(5000,-150)
t.goto(-5000,-150)
t.goto(-5000,0)
t.end_fill()

#sand
t.penup()
t.goto(-5000,-110)
t.pendown()
t.pencolor('beige')
t.fillcolor('beige')
t.begin_fill()
t.goto(5000,-110)
t.goto(5000,-5000)
t.goto(-5000,-5000)
t.goto(-5000,-110)
t.end_fill()

#sun
t.penup()
t.goto(200,200)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.circle(60)
t.end_fill()

#person 1
t.pencolor('tan')
t.pensize(8)
t.penup()
t.goto(-50,-200)
t.pendown()
t.goto(-50,-160)
t.fillcolor('tan')
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(-50,-200)
t.pendown()
t.right(45)
t.forward(15)
t.penup()
t.goto(-50,-200)
t.pendown()
t.right(90)
t.forward(15)
t.penup()
t.goto(-50,-175)
t.pendown()
t.right(200)
t.forward(20)
t.penup()
t.penup()
t.goto(-50,-175)
t.pendown()
t.right(350)
t.forward(20)
t.penup()

#person 1 eyes
t.pencolor('brown')
t.pensize(2)
t.penup()
t.goto(-45,-135)
t.pendown()
t.circle(2)
t.penup()
t.goto(-53,-135)
t.pendown()
t.circle(2)

#beach ball
t.pencolor('magenta')
t.pensize(4)
t.penup()
t.goto(25,-115)
t.pendown()
t.fillcolor('pink')
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(25,-115)
t.pendown()
t.pencolor('magenta')
t.fillcolor('magenta')
t.begin_fill()
t.circle(17)
t.end_fill()
t.penup()
t.goto(25,-115)
t.pendown()
t.pencolor('white')
t.fillcolor('white')
t.begin_fill()
t.circle(14)
t.end_fill()
t.penup()
t.goto(25,-115)
t.pendown()
t.pencolor('pink')
t.fillcolor('pink')
t.begin_fill()
t.circle(11)
t.end_fill()
t.penup()
t.goto(25,-115)
t.pendown()
t.pencolor('magenta')
t.fillcolor('magenta')
t.begin_fill()
t.circle(8)
t.end_fill()
t.penup()
t.goto(15,-105)
t.pendown()
t.pencolor('black')
t.write("Wilson",font=("Arial",8,"bold italic"),align="center")

#person 2
t.pencolor('tan')
t.pensize(8)
t.penup()
t.goto(90,-200)
t.pendown()
t.goto(90,-160)
t.fillcolor('tan')
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(90,-200)
t.pendown()
t.right(45)
t.forward(15)
t.penup()
t.goto(90,-200)
t.pendown()
t.right(90)
t.forward(15)
t.penup()
t.goto(90,-175)
t.pendown()
t.right(100)
t.forward(20)
t.penup()
t.penup()
t.goto(90,-175)
t.pendown()
t.right(115)
t.forward(20)
t.penup()

#person 2 eyes
t.pencolor('black')
t.pensize(2)
t.penup()
t.goto(85,-140)
t.pendown()
t.circle(2)
t.penup()
t.goto(76,-140)
t.pendown()
t.circle(2)
t.pencolor('green')
t.pensize(2)
t.penup()
t.goto(85,-140)
t.pendown()
t.circle(1)
t.penup()
t.goto(76,-140)
t.pendown()
t.circle(1)
t.pencolor('white')
t.pensize(1)
t.penup()
t.goto(84,-139)
t.pendown()
t.circle(.5)
t.penup()
t.goto(75,-139)
t.pendown()
t.circle(.5)

#person 2 mouth
t.pencolor('red')
t.pensize(2)
t.penup()
t.goto(82,-153)
t.pendown()
t.circle(5)

#boat
t.pencolor('orange')
t.pensize(2)
t.penup()
t.goto(-200,10)
t.pendown()
t.fillcolor('orange')
t.begin_fill()
t.setheading(270)
t.circle(70,180)
t.end_fill()

t.penup()
t.goto(-200,10)
t.pendown()
t.goto(-60,10)

t.pensize(8)
t.penup()
t.goto(-130,10)
t.pendown()
t.fillcolor('lightpink')
t.begin_fill()
t.goto(-130,100)
t.goto(-100,70)
t.goto(-130,50)
t.end_fill()

t.penup()
t.goto(-130,-25)
t.pendown()
t.pencolor("purple")
t.write("Summer Time",font=("Arial",13,"bold"),align="center")

#person 1 mouth
t.pencolor('pink')
t.pensize(3)
t.penup()
t.goto(-56,-143)
t.pendown()
t.setheading(265)
t.circle(6,180)

#fish body
t.penup()
t.goto(150,100)
t.pendown()
t.pensize(3)
t.fillcolor("grey")
t.begin_fill()
t.pencolor('grey')
# t.circle(50,140)
t.penup()
t.goto(150,100)
t.pendown()
t.setheading(45)
t.circle(50,200)

t.end_fill()

#fish eye
t.penup()
t.goto(152,117)
t.pendown()
t.pencolor("black")
t.circle(3)

#fish tail
t.penup()
t.goto(65,155)
t.pendown()
t.pencolor("grey")

t.fillcolor("grey")
t.begin_fill()

t.goto(40,135)
t.goto(90,135)
t.goto(65,155)

t.end_fill()

t.penup()
t.goto(55,105)
t.pendown()
t.pencolor("darkblue")
t.pensize(8)
t.goto(50,80)

t.penup()
t.goto(45,115)
t.pendown()
t.goto(25,60)

#umbrella
t.penup()
t.goto(-115,-150)
t.pendown()
t.setheading(85)
t.fillcolor("red")
t.begin_fill()
t.pencolor("green")
t.circle(80,180)
t.end_fill()
t.penup()
t.goto(-190,-145)
t.pensize(10)
t.pendown()
t.goto(-200,-300)

#towel
t.penup()
t.goto(-300,-275)
t.pendown()
t.pencolor("blue")
t.fillcolor("blue")
t.begin_fill()
t.goto(-250,-275)
t.goto(-175,-350)
t.goto(-225,-350)
t.goto(-300,-275)
t.end_fill()

#clouds
t.penup()
t.goto(-200,350)
t.pencolor("skyblue")
t.fillcolor("skyblue")
t.begin_fill()
t.circle(50)
t.penup()
t.goto(-170,355)
t.pendown()
t.circle(55)
t.penup()
t.goto(-190,335)
t.pendown()
t.circle(60)
t.penup()
t.goto(-155,340)
t.pendown()
t.circle(55)
t.penup()
t.goto(-185,320)
t.pendown()
t.circle(55)
t.penup()
t.goto(-145,300)
t.pendown()
t.circle(55)
t.end_fill()
t.fillcolor("skyblue")
t.begin_fill()
t.penup()
t.goto(-230,320)
t.pendown()
t.circle(60)
t.end_fill()




turtle.done()