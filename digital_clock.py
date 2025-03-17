import turtle
import datetime
import time
screen=turtle.Screen()
screen.tracer(0)
s=turtle.Turtle()
t=turtle.Turtle()   

s.shape("turtle")       
# turtle.bgcolor("black")
# s.color("white")
s.hideturtle()
t.hideturtle()
s.speed(0)
t.speed(0)
# for i in range(100):
#     for i in range(4):
#         s.forward(100)
#         s.left(90)
#     s.right(2)
# 
# 
# 
# s.goto(100,100)
# s.write()
s.pensize(3)
s.penup()
s.goto(-100,-100)
s.pendown()
for i in range(12):
    s.forward(100)
    s.left(30)
t.penup()
t.goto(-200,50)
t.pendown()
s=datetime.datetime.now().second
m=datetime.datetime.now().minute
h=datetime.datetime.now().hour
while(True):
# t.color("")
    t.write(str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2),font=(("Arial",60,"normal")))
    s+=1
    if s==60:
        s=0
        m+=1
    if m==60:
        m=0
        h+=1
    if h==13:
        h=1
    time.sleep(1)
    screen.update()
    t.undo()
    # turtle.mainloop()