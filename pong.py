import turtle
import os

##Game UI code

wn = turtle.Screen()
wn.title("Pong by Ari")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) #allows for the program to run faster

##Game backend code

#Paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0) #max possible speed
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() #removes the line 
paddle_a.goto(-350,100)


#Paddel 2
paddle_b = turtle.Turtle()
paddle_b.speed(0) #max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup() #removes the line 
paddle_b.goto(350,0)

#Ball

ball = turtle.Turtle()
ball.speed(0) #max possible speed
ball.shape("square")
ball.color("white")
ball.penup() #removes the line 
ball.goto(0,0)
#everytime ball moves, moves two pixels
ball.dx = 1.5
ball.dy = 1.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Functions
def move_up_paddle_a():
    y= paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def move_up_paddle_b():
    y= paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def move_down_paddle_a():
    y= paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def move_down_paddle_b():
    y= paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#Keyboard
wn.listen()
wn.onkeypress(move_up_paddle_a, "w")
wn.onkeypress(move_down_paddle_a, "s")
wn.onkeypress(move_up_paddle_b, "Up")
wn.onkeypress(move_down_paddle_b, "Down")

score_a = 0
score_b =0
while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dy *= -1
        score_b+=1 
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dy *= -1
        score_a+=1 


    #touch paddle
    paddle_a_top=paddle_a.ycor()+40
    paddle_a_down=paddle_a.ycor()-40

    paddle_b_top=paddle_b.ycor()+40
    paddle_b_down=paddle_b.ycor()-40
    if (ball.xcor() == (paddle_a.xcor()+20)) and (ball.ycor() < paddle_a_top and ball.ycor() > paddle_a_down):
        ball.dx *= -1
        
    if (ball.xcor() == (paddle_b.xcor()-20)) and (ball.ycor() < paddle_b_top and ball.ycor() > paddle_b_down):
        ball.dx *= -1
    pen.clear()
    pen.write("Player A: "+ str(score_b) +"  Player B: "+ str(score_a) +"", align="center", font=("Courier", 24, "normal"))
