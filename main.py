from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

while True:
    snake.move()
    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        snake.create_snake(snake.position)
        scoreboard.score += 1
        scoreboard.update_score()
    
    if snake.snakes[0].ycor() >= 290 or snake.snakes[0].ycor() <= -290 or snake.snakes[0].xcor() >= 290 or snake.snakes[0].xcor() <= -290:
        scoreboard.reset()
        snake.reset()
    
    for body in snake.snakes[1:-1]:
        if snake.snakes[0].distance(body) < 10:
            scoreboard.reset()
            snake.reset()
    else:
        continue

screen.exitonclick()