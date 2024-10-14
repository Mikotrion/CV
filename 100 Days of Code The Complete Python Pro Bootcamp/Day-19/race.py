from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win hte race? Enter a color: ")
new_turtle = Turtle()
colors = ["red", "orange", "yellow", "green", "purple","blue"]

all_turtle = []

t = 0
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-250, y =-100+t*40)
    all_turtle.append(new_turtle)
    t+=1

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>250:
            is_race_on = False
            winning_color = turtle.color()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost. The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()