from time import sleep
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = True
while game_running:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increment_score()

    # Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_running = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_running = False
            scoreboard.game_over()
            break

screen.exitonclick()
