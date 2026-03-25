                                                   #Make screen#
import turtle 
display = turtle.Screen() #بتعمل شاشة
display.title("pong game") #بتحدد اسم الشاشة
display.bgcolor("black") #بتحدد لون الشاشة
display.setup(width=800, height=600) #بتحدد حجم الشاشة
display.tracer(0) #بتوقف التحديث التلقائي للشاشة
                                                    #madrab#

madrab1 = turtle.Turtle() #بتعمل شكل للمضرب 
madrab1.shape("square") #بتحدد شكل المضرب
madrab1.color("blue") #بتحدد لون المضرب                                    
madrab1.shapesize(stretch_wid=5 , stretch_len=1) #بتكبر شكل المضرب
madrab1.penup() #بتمنع المضرب من الرسم                                     
madrab1.goto(-350,0) #بتحدد مكان المضرب                                                               
madrab1.speed(2) #بتحدد سرعة المضرب                                      

madrab2 = turtle.Turtle()  
madrab2.shape("square") 
madrab2.color("red")                                    
madrab2.shapesize(stretch_wid=5 , stretch_len=1)
madrab2.penup()                                      
madrab2.goto(350,0)                                                            
madrab2.speed(2)                                     
                                                    #ball#
ball = turtle.Turtle()      
ball.shape("circle")  
ball.shapesize(stretch_wid= 1 , stretch_len= 1)  
ball.color("white")
ball.speed(5)
ball.goto(0,0)
ball.penup()                                          
ball.dx = 0.20  #بتحدد سرعة الكرة في   المحور    x
ball.dy = 0.20  #بتحدد سرعة الكرة في المحور y   


                                                    #score#
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1: 0 player 2: 0", align="center", font=("courier",24,"normal"))
score1 = 0
score2 = 0
                                         
                                                           #functions#

def madrab1_up():
    y= madrab1.ycor()# بتجيب مكان المضرب على محور y
    y+=20 #بتزود 20 على مكان المضرب
    madrab1.sety(y)  #بتحدد مكان المضرب الجديد على محور y                               

def madrab1_down():
    y = madrab1.ycor()
    y-=20 
    madrab1.sety(y)

display.listen() #بتخلي الشاشة تستمع للأوامر                               
display.onkeypress(madrab1_up , "w") #بتحدد ان لما اضغط w المضرب يتحرك لفوق
display.onkeypress(madrab1_down,"s") #بتحدد ان لما اضغط s المضرب يتحرك لتحت   

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

display.listen()
display.onkeypress(madrab2_up, "Up")
display.onkeypress(madrab2_down, "Down")
                                         
                                         
                                                   #Game loop#
while True:
    display.update()
  

    ball.setx(ball.xcor() + ball.dx) #بتحرك الكرة في المحور x     
    ball.sety(ball.ycor() + ball.dy)   #بتحرك الكرة في المحور y
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1  #بتغير اتجاه الكرة في المحور y
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score1 += 1
        score.clear()
        score.write("player 1: {} player 2: {}" .format(score1 , score2), align="center", font=("courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0) 
        ball.dx*=-1   
        score2 += 1
        score.clear()
        score.write("player 1: {} player 2: {}" .format(score1 , score2), align="center", font=("courier",24,"normal"))

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<madrab2.ycor()+50 and ball.ycor()>madrab2.ycor()-50):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<madrab1.ycor()+50 and ball.ycor()>madrab1.ycor()-50):
        ball.setx(-340)
        ball.dx*=-1 