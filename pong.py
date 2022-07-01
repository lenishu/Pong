import turtle
  
  #MAKING THE WINDOW FOR THE GAME
wn = turtle.Screen()
wn.title("POng Tutorial")
wn.bgcolor("blue")
wn.setup(width=800, height = 600)
wn.tracer()


#PADDLE A
pad_a = turtle.Turtle()
pad_a.shape("square")
pad_a.color("white")
pad_a.speed(0)
pad_a.shapesize(stretch_wid=7 , stretch_len=1 )
pad_a.penup()
pad_a.goto(-350 , 0)

#PADDLE B
pad_b = turtle.Turtle()
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=7 , stretch_len=1 )
pad_b.speed(0)
pad_b.penup()
pad_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("red")
ball.penup()
ball.goto(0,0)



#Moving Paddle A
def pad_a_up():
  y = pad_a.ycor()
  y += 15
  pad_a.sety(y)

def pad_a_down():
  y = pad_a.ycor()
  y -= 15
  pad_a.sety(y)






#Moving Paddle b
def pad_b_up():
    y = pad_b.ycor()
    y += 15
    pad_b.sety(y)
  
  
  
def pad_b_down():
   y = pad_b.ycor()
   y -= 15
   pad_b.sety(y)


wn.listen()
wn.onkeypress(pad_a_down , "s" )
wn.onkeypress(pad_a_up , "w" )
wn.onkeypress(pad_b_up , "Up" )
wn.onkeypress(pad_b_down , "Down" )

  


  



while True:
 wn.update()


