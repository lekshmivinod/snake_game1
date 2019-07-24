import os
import turtle
import time
import random


delay=0.1

#score
score = 0
high_score=0


# screen stup

wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("pink")
wn.setup(width=600,height=600)
wn.tracer(0) #terns screen off

# snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(0,0)
head.direction="left"


#fooooodd
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("brown")
food.penup()
food.goto(0,100)


segments=[]#initialy thebody segmenta only head.

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  High Score:0", align="center",font=("Courier", 24, "normal"))



#fns

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction="down"

def go_left():
    if head.direction != "right":
        head.direction="left"

def go_right():
    if head.direction != "left":
        head.direction="right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard bindings

wn.listen()
wn.onkeypress(go_up,"s")
wn.onkeypress(go_down,"x")
wn.onkeypress(go_left,"c")
wn.onkeypress(go_right,"d")




#main gamlolop

while True:
    wn.update()

    #cchk for colsn withborder
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide the segmnts
        for segment in segments:
            segment.goto(1000,1000)

         #clear the segments list
        segments.clear()


     #reset the score
        score=0
        pen.clear()
        pen.write("Score: {}  High Score:{}".format(score, high_score), align="center", font=("Courier", 24, "normal"))





        # check for collision with food.each food posi adds sgment obody

    if head.distance(food) < 20:
        x=random.randint( -290, 290)  #move the foodtorandomplace, total600,600.cordinate system
        y=random.randint( -290, 290)
        food.goto(x,y)

        #add segmnt
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        #increasescore
        score+=10
        if score >high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {}  High Score:{}".format(score, high_score),align="center",font=("Courier", 24, "normal"))



     #move the end segments first
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move 1stsegmnet tohead
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    # check forhea collisions body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

    # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

                # clear the segments list
            segments.clear()



    time.sleep(delay)








wn.mainloop()
