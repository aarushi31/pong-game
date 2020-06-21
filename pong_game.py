import turtle
wn = turtle.Screen()
wn.title("pong by Aarushi")
wn.bgcolor("black")
wn.setup(width=800 , height=600)
wn.tracer(0)
#paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)
#paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("pink")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = -0.3

#function
def paddle1_up():
	y = paddle1.ycor()
	y+=20
	paddle1.sety(y)
def paddle1_down():
    y = paddle1.ycor()
    y-=20
    paddle1.sety(y)	
def paddle2_up():
	y = paddle2.ycor()
	y+=20
	paddle2.sety(y)
def paddle2_down():
    y = paddle2.ycor()
    y-=20
    paddle2.sety(y)	

#keyboard binding
wn.listen()
wn.onkeypress(paddle1_up,"w")  
wn.onkeypress(paddle1_down,"s")
wn.onkeypress(paddle2_up,"e")  
wn.onkeypress(paddle2_down,"d")

#main game loop
while True:
    wn.update()
    #movement of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border checking
    if ball.ycor() > 290:
    	ball.sety(290)
    	ball.dy*=-1
    if ball.xcor() > 390:
        ball.setx(390)
        ball.goto(0,0)
        ball.dx*=-1	
    if ball.xcor() <-390:
        ball.setx(-390)
        ball.goto(0,0)
        ball.dx*=-1
    if ball.ycor() < -290:
    	ball.sety(-290)
    	ball.dy*=-1
    #paddle and ball working
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40) :
    	ball.setx(340)
    	ball.dx*=-1
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40) :
    	ball.setx(-340)
    	ball.dx*=-1

    	


