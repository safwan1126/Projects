from turtle import Turtle, Screen
from random import randint
tim = Turtle()
tim1 = Turtle()
tim2 = Turtle()
tim3 = Turtle()
tim4 = Turtle()

turtles = [tim, tim1, tim2, tim3, tim4]
colours = ['red', 'orange', 'yellow', 'blue', 'green']

screen = Screen()
def move_forward():
    tim.forward(5)
def move_backward():
    tim.backward(5)
def right():
    tim.right(2)
def left():
    tim.left(2)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

# screen.onkeypress(key= 'w', fun = move_forward)
# screen.onkeypress(key= 's', fun = move_backward)
# screen.onkeypress(key= 'a', fun = left)
# screen.onkeypress(key= 'd', fun = right)
# screen.onkeypress(key='c', fun = clear)

screen.setup(width=500, height=400)


verticle = -80
for i in range(5):
    turtles[i].color(colours[i])
for turtle in turtles:
    turtle.penup()
    turtle.goto(-200, verticle)
    verticle += 40

line_turtle = Turtle()
line_turtle.hideturtle()
line_turtle.penup()
line_turtle.goto(220, -100)
line_turtle.pendown()
line_turtle.color('black')
line_length = 200
line_turtle.setheading(90)
line_turtle.forward(line_length)

while True:
    guess = screen.textinput( title= 'Turle Race', prompt='Who will win the race? Pick a colour')
    if guess in colours:
        break

end = False
while not end:
    for turtle in turtles:
        turtle.forward(randint(1,10))
        if turtle.xcor() >= 219:
            end = True
            print(f'Winner is {turtle.color()[1]}')
            if guess == turtle.color()[1]:
                print('You win!')
            else:
                print('You lose!')
            break

screen.exitonclick()
