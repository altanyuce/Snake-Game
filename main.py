from turtle import Turtle, Screen
import time
from snake import Snake, wall
from food import Food
from score import Score

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

wall()

should_stop = False
while not should_stop:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.newscore()
        snake.create_snake()

    if snake.head.xcor() > 259 or snake.head.xcor() < -259 or snake.head.ycor() > 259 or snake.head.ycor() < -259:
        should_stop = True
        score.gameover()


    for segment in snake.segments[1:len(snake.segments) - 1]:
        if snake.head.distance(segment) < 10:
            should_stop = True
            score.gameover()

screen.exitonclick()